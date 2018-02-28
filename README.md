

```python
import re
import pandas as pd
import pdftotext
```


```python
#"/Users/zachary/Downloads/wto.csv"
```


```python
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
```


```python
trial = WTO_parser("/Users/zachary/Downloads/wto.csv")
```


```python
#"/Users/zachary/Downloads/{}R.pdf"
```


```python
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
```


```python
trial = Panel_parser("/Users/zachary/Downloads/{}R.pdf", 2)
```


```python
trial.pdf
```




    <pdftotext.PDF at 0x10d51bf30>




```python
trial.entire() #only works for FACTUAL and MAIN as of NOW
```

    Hi, I am your GATT_WTO panel_report parser.
    You can retrieve any part you want in this pdf
    1
    I. INTRODUCTION
    2
    II. FACTUAL
    9
    III. MAIN
    32
    IV. SUBMISSIONS
    35
    V. INTERIM
    36
    VI. FINDINGS
    53
    VII. CONCLUDING
    54
    VIII. CONCLUSIONS


### then type in FACUTAL or FINDINGS


```python
trial.entire()
```

    Hi, I am your GATT_WTO panel_report parser.
    You can retrieve any part you want in this pdf
    1
    I. INTRODUCTION
    2
    II. FACTUAL
    9
    III. MAIN
    32
    IV. SUBMISSIONS
    35
    V. INTERIM
    36
    VI. FINDINGS
    53
    VII. CONCLUDING
    54
    VIII. CONCLUSIONS
    What do you want? Choose one among contents: Then type-inFACTUAL
    1
    I. INTRODUCTION
    2
    II. FACTUAL
    9
    III. MAIN
    32
    IV. SUBMISSIONS
    35
    V. INTERIM
    36
    VI. FINDINGS
    53
    VII. CONCLUDING
    54
    VIII. CONCLUSIONS
    You have sub-field of FACTUAL : ['     A.   The Clean Air Act', "     B.   EPA's Gasoline Rule", '          1.     Establishment of Baselines', '          2.     Reformulated Gasoline', '          3.     Conventional Gasoline (or "Anti-Dumping Rules', '     C.   The May 1994 Proposal']



### COPY and PASTE among the sub-field elements. For example, try     A.   The Clean Air Act


```python
trial.entire()
```

    Hi, I am your GATT_WTO panel_report parser.
    You can retrieve any part you want in this pdf
    1
    I. INTRODUCTION
    2
    II. FACTUAL
    9
    III. MAIN
    32
    IV. SUBMISSIONS
    35
    V. INTERIM
    36
    VI. FINDINGS
    53
    VII. CONCLUDING
    54
    VIII. CONCLUSIONS
    What do you want? Choose one among contents: Then type-inFINDINGS
    1
    I. INTRODUCTION
    2
    II. FACTUAL
    9
    III. MAIN
    32
    IV. SUBMISSIONS
    35
    V. INTERIM
    36
    VI. FINDINGS
    53
    VII. CONCLUDING
    54
    VIII. CONCLUSIONS
    You have sub-field of FINDINGS : ['    A.    Introduction', '    B.    Article III', '          1.      Article III:4', '          2.      Article III:1', '    C.    Article I:1', '    D.    Article XX(b', '          1.      Policy goal of protecting human, animal or plant life or health', '          2.      Necessity of the inconsistent measure', '    E.    Article XX(d', '          1.      Securing compliance with consistent laws or regulations', '          2.      Other conditions', '    F.    Article XX(g', '          1.      Policy goal of conserving an exhaustible natural resource', '                   on domestic production or consumption', '      G.   Article XXIII:1(b', '      H.   Applicability of the Agreement on Technical Barriers to Trade']
    Do you want only see GATT:III related?    A.    Introduction
    What do you want? Choose one among contents: Then type-in    A.    Introduction
    op that corresponds to the target [    A.    Introduction] located at 138699   
    op that corresponds to the target [    B.    Article III] located at 142511   





    'A.      Introduction\n6.1      The Panel noted that the dispute arose from the following facts. The Clean Air Act aims\nto control and reduce air pollution in the United States. The Act and certain of its regulations (the\n“Gasoline Rule”) set standards for gasoline quality intended to reduce air pollution, including\nozone, caused by motor vehicle emissions. From 1 January 1995, the Gasoline Rule permits only\ngasoline of a specified cleanliness (“reformulated gasoline”) to be sold in areas of high air\npollution. In other areas, only gasoline no dirtier than that sold in the base year of 1990\n(“conventional gasoline”) can be sold.\n6.2      The Gasoline Rule applies to refiners, blenders and importers of gasoline. It requires that\ncertain chemical characteristics of the gasoline in which they deal respect, on an annual average\nbasis, defined levels. In the Gasoline Rule some of these levels are fixed; others are expressed as\n“non-degradation” requirements. Under the non-degradation requirements, each domestic refiner\nmust maintain, on an annual average basis, the relevant gasoline characteristics at levels no worse\nthan its “individual baseline” — that is, the annual average levels achieved by that refiner in 1990.\nTo establish an individual baseline, a refiner must show evidence of the quality of gasoline\nproduced or shipped in 1990 (“Method 1"). If that evidence is not complete, then it must use data\non the quality of blendstock produced in 1990 (“Method 2"). If these two methods do not result\nin sufficient evidence, the refiner must also use data on the quality of post-1990 gasoline\nblendstock or gasoline (“Method 3").\n6.3      Importers are also required to use an individual baseline, but only in the case (unlikely,\naccording to the parties to the dispute) that they are able to establish it using Method 1 data.\nUnlike domestic refiners, they are not allowed to establish an individual baseline by using the\nsecondary or tertiary data specified in Methods 2 and 3. If an importer cannot produce Method 1\ndata, then it must use a “statutory baseline” which the United States claims is derived from the\naverage characteristics of all gasoline consumed in the United States in 1990. Some other\ndomestic entities (such as refiners with only partial or no 1990 operations, and blenders with\ninsufficient Method 1 data) are also assigned the statutory baseline. Exceptionally, importers that\nimported in 1990 at least 75 percent of the production of an affiliated foreign refinery are treated\nas domestic refiners for the purpose of establishing baselines. Since this dispute concerns only the\n\n\n                                                                                   WT/DS2/R\n                                                                                   Page 33\nGasoline Rule’s non-degradation requirements, and not reformulated and conventional gasoline as\nsuch, the Panel will refer generally to “gasoline” in the course of its findings.\n6.4      Venezuela and Brazil claim that the Gasoline Rule violates the national treatment\nprovisions of Article III:1 and 4 of the General Agreement and the most-favoured-nation provision\nof Article I. Venezuela claims in the alternative that the Gasoline Rule has nullified and impaired\nbenefits under the non-violation provisions of Article XXIII:1(b). Venezuela and Brazil also claim\nthat the Gasoline Rule violates Article 2 of the Agreement on Technical Barriers to Trade (the\n“TBT Agreement”). The United States rejects these claims and argues that the Gasoline Rule can\nbe justified under the exceptions contained in Article XX, paragraphs (b), (d) and (g), which\nargument is rejected by Venezuela and Brazil. It also argues that the Gasoline Rule does not\ncome within the scope of Article 2 of the TBT Agreement.\n         '



### You get the part of the pdf where is only specific to    A.    Introduction
