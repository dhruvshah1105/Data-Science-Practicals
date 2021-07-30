import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

html = requests.get('https://www.tripadvisor.com/Hotels-g297608-Ahmedabad_Ahmedabad_District_Gujarat-Hotels.html')
print(html.status_code)

bs_object = soup(html.content,'lxml')

hotel = []
for name in bs_object.findAll('div',{'class':'listing_title'}):
  hotel.append(name.text.strip())
print(hotel)

ratings = []
for rating in bs_object.findAll('a',{'class':'ui_bubble_rating'}):
  ratings.append(rating['alt'])
print(ratings)

reviews = []
for review in bs_object.findAll('a',{'class':'review_count'}):
  reviews.append(review.text.strip())
print(reviews)

price = []
for p in bs_object.findAll('div',{'class':'price-wrap'}):
  price.append(p.text.replace('₹','').strip())
print(price)

d1 = {'Hotel':hotel,'Ratings':ratings,'No_of_Reviews':reviews,'Price':price}
df = pd.DataFrame.from_dict(d1)
print(df)
