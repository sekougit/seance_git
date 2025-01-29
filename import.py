
import os
print(os.getcwd())

import sys
sys.path.append("C:/Users/Sekou Drame/moncodepython")
import mymodule as mo
mo.greeting("Sekou Drame") 

from mymodule import  liste
print(liste)

from mymodule import  greeting
print(greeting("Kossa Fall"))

from monmodule import table_mult
#print(afficher_parite(4))
print (table_mult(4))

import platform
print(platform.system())    
print(dir(platform))


from math import pi,cos,sin,exp,degrees,radians,pow,tan
#print(platform.system())    
#print(dir(math))
print(degrees(pi/6))
print(math.cos(radians(45)))

print(pow(2,0.5)/2)
print(pi)

import json
#print(dir(json))
x={"name":"john","age":30,"city":"New York"}
y=json.dumps(x)
print(y)

import json
print(dir(json))
import pandas as pd
x={"name":"john","age":30,"city":"New York"}
df=pd.DataFrame(x)
print(x)

nup=np.array([2,4,56,7,8,9,1,7,6])
print(nup.reshape(3,3))
print(nup[3])

import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import numpy as np

mon_url="https://fr.wikipedia.org/wiki/Liste_des_pays_par_population"
mon_reponse=requests.get(mon_url)
print(mon_reponse)
mon_soup=mon_reponse.content
#print(mon_soup.prettify,"\n")
mon_soup1=BeautifulSoup(mon_soup,"html.parser")
#print(mon_soup1.pretitify,"\n")
#td1=mon_soup1.find(class_="wikitable sortable alternance jquery-tablesorter")
td=mon_soup1.find("table",attrs={"class","wikitable sortable alternance"}).findAll("td")
print(td[2].text)
print(len(td))
pays=[]
#for i in td[2].find_all("td"):
for j in range(0,len(td)):
    pays.append(td[j].text)
    
    
print(pays)
print(len(pays))
rang=[]
nom_pays=[]
population_2021=[]
population_2023=[]
for i in range(0,952,4):
    rang.append(pays[i])
    nom_pays.append(pays[i+1])
    population_2021.append(pays[i+2])
    population_2023.append(pays[i+3])
    
print(rang)
print(nom_pays)
print(population_2021)
print(population_2021[0])
print(population_2023[2])
import re
for i in range(0,952):
    population_2023[i]=re.sub("\xa0","",population_2023[i])
    
print(population_2023)



mon_dict={"rangs":rang,"nom_pays":nom_pays,"population_2021":population_2021,"population_2023":population_2023}
df=pd.DataFrame(mon_dict)
#df1=df["population_2023"]-df["population_2021"]
print(df.info())
df["population_2021"]=df["population_2021"].astype(str).astype(float)
df["population_2023"]=df["population_2023"].astype(str).astype(float)
df["evolution population"]=df["population_2023"]-df["population_2021"]
print(df.info())
print(df.to_string())
print(df.describe())
df.to_excel("C:/Users/Sekou Drame/Desktop/web_scrapping_2.xlsx")
pays_2=pays[1:]
print(pays_2)
pays_1=np.ones((1,952))
for i in range(0,952):
    pays_1[i]=pays_2[i]
    
print(pays_1)




import requests 
from bs4 import BeautifulSoup 
import pandas as pd

mon_url="http://feeds.bbci.co.uk/news/rss.xml"
mon_reponse=requests.get(mon_url)
print(mon_reponse)
mon_soup1=BeautifulSoup(mon_reponse.text,"html.parser")
#print(mon_soup1.prettify)
mon_items=mon_soup1.findAll("item")
#print(mon_items,"\n")
item=mon_items[0]
print(item.title)
mon_news_item=[]
for i in mon_items:
    mon_news_i={}
    mon_news_i["title"]=i.title.text
    mon_news_i["description"]=i.description.text
    mon_news_i["pubdate"]=i.pubdate.text
    mon_news_item.append(mon_news_i)
    
print(mon_news_item)
df=pd.DataFrame(mon_news_item,columns=["tilte","description","pubdate"])
print(df)
df.to_excel("C:/Users/Sekou Drame/Desktop/web_scrqpping.xlsx")
import os
os.rename("C:/Users/Sekou Drame/Desktop/web_scrqpping.xlsx","C:/Users/Sekou Drame/Desktop/web_scrapping.xlsx")



import re
txt ="The rain in Spain"
x=re.sub("W","9",txt)
print(x)











