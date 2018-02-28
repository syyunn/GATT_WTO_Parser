
# coding: utf-8

# In[144]:


import re
import pandas as pd
import pdftotext


# In[145]:


#"/Users/zachary/Downloads/wto.csv"


# In[146]:


class WTO_parser():
    def __init__(self,filepath):
        self.df = pd.read_csv(filepath, header= 0, index_col=0)
    
    def panel_exist(self):
        panel_index = []
        for i in range(0,len(self.df['maker_pr'])):
            binar = self.df['maker_pr'][i]
            if binar == 1:
                panel_index.append(i+1)
        self.panel_exist = panel_index
        return panel_index

    def gatt_III(self):
        #check whether the GATT ArtIII cited
        GATT_III = []
        #make the list which GATT_III cited and also has panel report 
        for i in range(0, len(self.df['cited'])):
            if re.search(r"(?<=)(GATT 1994:)(.*)(, III|Art. III)(.*)(?=')", self.df['cited'][i]): #parenthesis in Regex refers to the (grouped expression) 
                if self.df['maker_pr'][i] == 1 :
                    GATT_III.append(i+1) 
        return GATT_III


# In[147]:


trial = WTO_parser("/Users/zachary/Downloads/wto.csv")


# In[148]:


#"/Users/zachary/Downloads/{}R.pdf"


# In[149]:


class Panel_parser():
    def __init__(self, filepath, ds_numb):
        with open(filepath.format(ds_numb), "rb") as f:
            pdf = pdftotext.PDF(f)
        self.pdf = pdf
        
    def toc_locator(self):
        for i in range(0, len(self.pdf)):
            if "Table of Contents" in self.pdf[i]:
                self.table = i
                print("At page {}, Table of Contents located\n".format(self.table))
                print("Call your value with the variable \"table\"\n")
                print("If you hit self.table, it returns the toc page: {}".format(self.table))
                break
            else:
                print("At page {}, can't locate Table of Contents\n".format(i))
                
    def toc_parser(self):
        self.toc_locator()
        toc_s = self.pdf[self.table]
        self.contents = re.findall('(.*?)[\W]+(\d+)(?=\n|$)', toc_s, flags=re.M)
        return self.contents
    
    def toc_parser_all(self):
        self.pdf_all = "\n\n".join(self.pdf)
        self.contents = re.findall('(.*?)[\W]+(\d+)(?=\n|$)', self.pdf_all, flags=re.M)
        self.romans = ["I.", "II.", "III.", "IV.", "V.", "VI.", "VII.", "VIII.", "IX.", "X."]
        self.charger = []

        for i in range(0,len(self.contents)):
            checkee = self.contents[i][0].split()[0]
            if checkee in self.romans:
                print(i)
                print(self.contents[i][0].split()[0], self.contents[i][0].split()[1])
                self.charger.append((self.contents[i][0].split()[0], self.contents[i][0].split()[1]))
                
        return self.charger
    
    def cont_indexr(self, input_):
        self.toc_parser_all()
        self.indexr_main = []
        for i in range(0, len(self.charger)):
            if self.charger[i][1] == input_:
                self.indexr_main.append(self.romans[i])
                self.indexr_main.append(self.romans[i+1])
        return self.indexr_main
    
    def cited_parser(self,str_):
        cont_index = self.cont_indexr(str_)
        self.cited = [] #cited articles depeding on findings or main

        for i in range(0, len(self.contents)):
            if self.contents[i][0].split()[0] == cont_index[0]:
                indexr_cited = i
                #cited.append(contents[indexr_cited+1][0].split()[1:3])
        for i in range(indexr_cited+1, len(self.contents)):
            if self.contents[i][0].split()[0] != cont_index[1]:
                self.cited.append(self.contents[i][0])#.split()[1:])
            else:
                break
        return self.cited
    
    def cited_III(self, str_):
        self.cited_parser(str_)
        self.cited_III = [] #crawls every III cited in findings list 

        for i in range(0, len(self.cited)):
            if re.search(r".*\sIII.*",self.cited[i]):
                self.cited_III.append(self.cited[i])
        return self.cited_III
    
    def list2pattern(self, lst):
            return r'\s+'.join(lst)
        
    def con_op_locer(self, target):
        self.pdf_all = "\n\n".join(self.pdf)
        reference = re.search(r"[^\s]+.*",target).group()
        lst = reference.split()
        pattern = self.list2pattern(lst)
        self.cands = re.findall(pattern, self.pdf_all)
        #print(len(self.cands))
        self.loca = self.pdf_all.rfind(self.cands[1])
        print("op that corresponds to the target [{}] located at {}   ".format(target, self.loca))
        return self.loca
        
    def entire(self):
        print("Hi, I am your GATT_WTO panel_report parser.")
        print("You can retrieve any part you want in this pdf")
       
        self.toc_parser_all() #list the options of toc chapter 
        
        want = input("What do you want? Choose one among contents: Then type-in")
        print("You have sub-field of {} : {}".format(want, self.cited_parser(want)))
        
        if want == 'FINDINGS':
            agreer = input("Do you want only see GATT:III related?")
            if agreer == 'yes':
                print(self.cited_III("FINDINGS"))
            else:
                pass
        
        want = input("What do you want? Choose one among contents: Then type-in")
        
        start = self.con_op_locer(want)
        for i in range(0, len(self.cited)):
            if self.cited[i] == want:
                indexr = i
            else:
                pass
            
        end = self.con_op_locer(self.cited[indexr+1])
        return self.pdf_all[start:end]
