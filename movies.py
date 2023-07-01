import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url="https://www.rottentomatoes.com/browse/movies_at_home/sort:popular"
r=requests.get(url)
htmlContent=r.content

soup = BeautifulSoup(r.content, 'html.parser')

MovieName=[]
ReleaseDate=[]
WebsiteRatings=[]
AudienceRatings=[]

for i in soup.find_all('span',{'class':'p--small','data-qa':'discovery-media-list-item-title'}):
        # print(i.get_text())
        MovieName.append(i.text.replace('\n','').replace('\r','').replace(' ',''))
for j in soup.find_all('span',{'class':'smaller'}):
    # print(j.get_text().replace("Streaming",""))  
    ReleaseDate.append(j.get_text().replace("Streaming","").replace('\n','').replace('\r','').replace(' ',''))

for k in soup.find_all('div',{'slot':'caption','data-track':'scores', 'data-qa':'discovery-media-list-item-caption'}):
    score = k.find_all('score-pairs', {'criticsscore':True})
    for s in score:
        # print(s.get('criticsscore'))
        WebsiteRatings.append(s.get('criticsscore'))

for k in soup.find_all('div',{'slot':'caption','data-track':'scores', 'data-qa':'discovery-media-list-item-caption'}):
    score = k.find_all('score-pairs', {'audiencescore':True})
    for s in score:
        # print(s.get('audiencescore')) 
        AudienceRatings.append(s.get('audiencescore'))    

print (len(MovieName))
print(len (ReleaseDate))  
print(len(WebsiteRatings))   
print(len(AudienceRatings))

dict1={'MOVIE NAME':MovieName,'RELEASE DATE':ReleaseDate}
# del dict1[0]
df=pd.DataFrame(dict1)
df=df.drop(0)

# print(df.head())        
# df.to_csv("movies.csv")

dict2={'WEBSITE RATINGS':WebsiteRatings,'AUDIENCE RATINGS':AudienceRatings}
# del dict1[0]
df1=pd.DataFrame(dict2)

# merged_df=pd.merge(df,df1,on='index')
# print(merged_df.head())   










