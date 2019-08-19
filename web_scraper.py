from bs4 import BeautifulSoup
from requests import get
import pandas as pd

### web scraping ###

name = []
gender = []
breed = []
colour = []
age = []
for i in range(1,8):
    web = 'http://www.spca.org.sg/services.asp?Page=' +str(i) +'&cat=2&view=&senior=&sColorCode='
    res = get(web)
    html_soup = BeautifulSoup(res.text, 'html.parser')
    bucket = html_soup.find_all('td', width="18%")
    
    num_cats = len(bucket)
    for j in range(0,num_cats):
        temp = bucket[j]
        # name 
        cat_name = str(temp.find_all('td')[0].text)
        cat_name = cat_name.replace(' ','')
        name.append(cat_name)
        
        # gender #
        cat_gender = str(temp.find_all('td')[1].text)
        cat_gender = cat_gender.replace('Gender: ', '')
        gender.append(cat_gender)
        
        # breed 
        cat_breed = str(temp.find_all('td')[2].text)
        cat_breed = cat_breed.replace('Breed: ','').replace(' ','')
        breed.append(cat_breed)
        
        # colour
        cat_colour = str(temp.find_all('td')[3].text)
        cat_colour = cat_colour.replace('Colour: ','').replace(' ','')
        colour.append(cat_colour)
        
        # age
        cat_age = str(temp.find_all('td')[4].text)
        cat_age = cat_age.replace('\r\n\t\t\t\t\t\t\t\tAge:','').replace('\t\t\t\t\t\t\t\t','').replace(' ','')
        age.append(cat_age)

# combining all lists into a dataframe #
cols = ['name', 'gender', 'breed', 'colour', 'age']
adoptcats = pd.DataFrame({'name':name,
              'gender':gender,
              'breed':breed,
              'colour':colour,
              'age':age})[cols]
