from requests import get
from bs4 import BeautifulSoup as beauty
from pprint import pprint
import json
name=[]
page_=[]
full_d=[]
price_=[]
img_links=[]
inp=int(input('Enter how many pages you want to scrape:'))
a=input('Enter brand name that you want to scrape:')
def page_info(inp,a):
    for i in range(1,inp+1):
        page=get('https://www.flipkart.com/search?q='+a+'&page='+str(i))
        soup=beauty(page.text,'html.parser')
        brand=soup.findAll("div",class_="_4rR01T")
        page_link=soup.findAll('div',class_='_13oc-S')
        full_details=soup.findAll('ul',class_='_1xgFaf')
        price=soup.findAll("div",class_="_30jeq3 _1_WHN1")
        for  i,j,k,l in zip(brand,page_link,full_details,price):
            name.append((i.text))
            page_.append(('https://www.flipkart.com'+j.find('a').get('href')))
            full_d.append((k.text))
            price_.append((l.text))
page_info(inp,a)

def link_of_img(a):
    for i in a:
        page=get(i)
        soup=beauty(page.text,'html.parser')
        link=soup.find('div',class_='_2c7YLP UtUXW0 _6t1WkM _3HqJxg')
        img=link.find('img').get('src')
        img_links.append(img)
link_of_img(page_)

def web_page(a):
    with open ('flipkart.html','w') as l:
        l.write('''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>
    <center>Welcome To Shopping Cart</center>
    </h1>
</body>''')
        for i in range(len(a)):
            l.write(f"""
    <body>
        <a href={page_[i]}></a>
        <img src={img_links[i]}
        width=145" height="310">
        <h2>{'Brand --> '}
            {name[i]}
            {price_[i]}
        </h2><h3>{'full information -->'}{full_d[i]}
        </h3>
    </body>
                """)
            l.write('</html>')
web_page(name)