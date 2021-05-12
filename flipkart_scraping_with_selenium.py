
from selenium import webdriver
import os,requests,json
import time
from bs4 import BeautifulSoup as bs
driver_path=('/home/muhammad_siddik_akbar/Desktop/chromedriver')
link_list=[]
driver = webdriver.Chrome(driver_path)
driver.get('https://www.flipkart.com/')
cancel=driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
search_bar=driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search_data=search_bar.send_keys('mobiles'+'\n')
time.sleep(4)
brand_fltr=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[5]/div[2]/div[1]/div[1]/input')
brand_list=['poco','redmi']
counter=0
for i in brand_list:
    brand_fltr.send_keys(i)
    time.sleep(3)
    if counter==0:
        (driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[5]/div[2]/div[1]/div[2]/div/label/div[2]')).click()
    else:
        driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[5]/div[2]/div[1]/div[3]/div/label/div[2]').click()
        time.sleep(3)
    brand_fltr.clear()
    counter+=1

def lis_of_product_url_in_page(url):
    url_list=[]
    b=(requests.get(url)).text
    soup1=bs(b,'html.parser')
    url_div=soup1.find_all('a',class_='_1fQZEK')
    for i in url_div:
        url_list.append((i)['href'])
    main_link='https://www.flipkart.com'
      
    def prod_detail():
        prod_details={}
        prod_name=[]
        prod_rating=[]
        prod_price=[]
        prod_discription=[]

        for i in url_list:
            re=(requests.get(main_link+i)).text
            soup2=bs(re,'html.parser')
            try:
                name_div=soup2.find('span',class_='B_NuCI').get_text(strip=True)
            except:
                name_div='NA'
            try:
                rating_div=soup2.find('div',class_='_3LWZlK').text
            except:
                rating_div="NA"
            try:
                price_div=((soup2.find('div',class_="_30jeq3 _16Jk6d"))).get_text(strip=True)
                price_div=price_div.replace('\u20b9','Rs.')
            except:
                price_div="NA"
            try:
                discri_div=soup2.find("div",class_="_1mXcCf RmoJUa").text
            except:
                discri_div='NA'
            prod_name.append(name_div)
            prod_rating.append(rating_div)
            prod_price.append(price_div)
            prod_discription.append(discri_div)  
        details={}
        for data in range(len(prod_name)):
            details[(prod_name[data])]={'price':(prod_price[data]),'ratings':(prod_rating[data]),'discription':(prod_discription[data])}
        return(details)
    return(prod_detail())
b=[]
user=int(input('how much page you want to scrape'))
for bn in range(1,user+1):
    page_url=(driver.current_url)+(f"&page={bn}")
    ln=lis_of_product_url_in_page(page_url)
    b.append(ln)
with open('flipkart.json','w') as data:
    json.dump(b,data,indent=4)
print ("you scraped succesfully")
