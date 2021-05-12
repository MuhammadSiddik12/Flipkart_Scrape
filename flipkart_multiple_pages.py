from requests import get            
from bs4 import BeautifulSoup as beauty
from pprint import pprint
import json
final_list=[]
for s in range(0,30):
    print(f'{s+1} is scaping')
    page=get("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DMi&page="+str(s)) 
    soup=beauty(page.text,"html.parser")
    name=soup.findAll('div',class_='_4rR01T')
    info=soup.findAll('ul',class_='_1xgFaf')
    a={}
    final_info=[]
    for i in info:
        b=[]
        f=i.findAll('li')
        for j in f:
            b.append(j.text)
        final_info.append(b)
    price=soup.findAll('div',class_="_30jeq3 _1_WHN1")
    for i,j,k in zip(name,final_info,price):
        a['Brand']=i.text
        a['Full Info']=j
        a['Price']=k.text.replace('\u20b9','Rs ')
        final_list.append(a.copy())
with open('final.json','w') as k:
    k.write(json.dumps(final_list,indent=4))
    k.close()