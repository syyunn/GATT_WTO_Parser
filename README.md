
   ## Import WTO_parser and Panel_parser from parser.py


```python
from parser import WTO_parser, Panel_parser
```

## Instantiation of WTO_parser


```python
trial = WTO_parser("/Users/zachary/Downloads/wto.csv")
```

### print dataframe


```python
#trial.df
```

### DS number that GATT:III has been cited


```python
#trial.gatt_III()
```

### DS number that Panel_report exists


```python
#trial.panel_exist()
```

## Instantiation of Panel_parser


```python
trial = Panel_parser("/Users/zachary/Downloads/{}R.pdf", 2)
```

### Panel_parser provides event-loop driven approach


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



### type-in any chapter you want to get : such as FACTUAL

  
    You have sub-field of FACTUAL : ['     A.   The Clean Air Act', "     B.   EPA's Gasoline Rule", '          1.     Establishment of Baselines', '          2.     Reformulated Gasoline', '          3.     Conventional Gasoline (or "Anti-Dumping Rules', '     C.   The May 1994 Proposal']


### Then type-in element of subfield you want to get: such as  A.   The Clean Air Act

    'A.       The Clean Air Act\n2.1       The Clean Air Act ("CAA"), originally enacted in 1963, aims at preventing and\ncontrolling air pollution in the United States. In a 1990 amendment to the CAA1, Congress\ndirected the Environmental Protection Agency ("EPA") to promulgate new regulations on the\ncomposition and emissions effects of gasoline in order to improve air quality in the most polluted\nareas of the country by reducing vehicle emissions of toxic air pollutants and ozone-forming\nvolatile organic compounds. These new regulations apply to US refiners, blenders and importers.\n2.2       Section 211(k) of the CAA divides the market for sale of gasoline in the United States into\ntwo parts. The first part, which covers approximately 30 percent of gasoline marketed in the\nUnited States, consists of the nine large metropolitan areas that experienced the worst summertime\nozone pollution during the period 1987-1989, plus any areas that do not meet national ozone\nrequirements and are added at the request of the governor of the state. These areas are referred to\nas ozone "nonattainment areas", and in this part of the United States only "reformulated gasoline"\nmay be sold to consumers. In the rest of the United States, "conventional gasoline" may be sold\nto consumers.\n2.3       Section 211(k)(2)-(3) of the CAA established certain compositional and performance\nspecifications for reformulated gasoline. The oxygen content must not be less than 2.0 percent by\nweight, the benzene content must not exceed 1.0 percent by volume and the gasoline must be free\nof heavy metals, including lead or manganese. The performance specifications of the CAA\nrequire a 15 percent reduction in the emissions of both volatile organic compounds ("VOCs") and\ntoxic air pollutants ("toxics") and no increase in emissions of nitrogen oxides ("NOx"). These\nrequirements are measured by comparing the performance of reformulated gasoline in baseline\nvehicles (representative model year 1990 vehicles) against the performance of "baseline gasoline"\nin such vehicles. Section 211(k)(10) of the CAA defines the specifications of baseline gasoline\nsold in the summer, which is the high ozone season, and leaves the specifications of winter\nbaseline gasoline to be determined by EPA. It provides, however, that the specifications for\nwinter gasoline shall be those of the industry average gasoline sold in 1990. For the year 2000\nand beyond, the CAA requires that new reformulated gasoline requirements be developed that\nrequire a 20-25 percent reduction in emissions of VOCs and toxics, depending on EPA\'s\nconsiderations of feasibility and cost.\n    1\n      42 U.S.C. §7545(k).\n\n\n                                                                                  WT/DS2/R\n                                                                                  Page 3\n2.4        The CAA also sets requirements for conventional gasoline, which ensure that each\nrefiner\'s, blender\'s or importer\'s conventional gasoline sold in the rest of the country remains as\nclean as it was in 1990. This programme is known as "anti-dumping rules" because it is designed\nto prevent refiners, blenders or importers from dumping into conventional gasoline fuel\ncomponents that are restricted in reformulated gasoline and that cause environmentally harmful\nemissions. To accomplish this, section 211(k)(8) of the CAA provides that no refiner, blender or\nimporter of gasoline may sell conventional gasoline that emits VOCs, toxics, NOx or carbon\nmonoxide ("pollutants") in greater amounts than the gasoline sold in the United States by that\nrefiner, blender or importer in 1990. In order to implement this provision, separate individual\nbaselines must be established for refiners, blenders or importers based on the gasoline they sold in\n1990. That permits determination of whether the emissions from a refiner\'s, blender\'s and\nimporter\'s conventional gasoline (post-1994 gasoline) are greater than the emissions from its 1990\ngasoline. If, however, EPA determines that no adequate and reliable data exist regarding the\ncomposition of such 1990 gasoline sold by a refiner, blender or importer, the statutory baseline\ngasoline is applied. The statutory annual baseline values are calculated using a seasonal weighting\nof the statutory summer baseline, as defined in the CAA, and the statutory winter baseline, as\ndetermined by EPA.\n           '


### Then you get the corresponding part in the pdf
