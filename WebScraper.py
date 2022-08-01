from selenium import webdriver
#from BeautifulSoup import BeautifulSoup
import pandas as pd
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.daf-yomi.com/Dafyomi_Page.aspx?vt=2&massechet=283&amud=3&fs=0")

for i in range(3630):
    content = driver.page_source
    par = driver.find_element("id", "ContentPlaceHolderMain_divTextWrapper")
    print()
    print()
    print(par.text)
    nextButton = driver.find_element("id", "ContentPlaceHolderMain_ancNext")
    nextButton.click()
# soup = BeautifulSoup(content)
# for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
# name=a.find('div', attrs={'class':'_3wU53n'})
# price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
# rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
# products.append(name.text)
# prices.append(price.text)
# ratings.append(rating.text) 