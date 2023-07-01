import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

r=requests.get(url)
htmlContent=r.content

soup = BeautifulSoup(r.content, 'html.parser')

Jobs=[]
SkillsReq=[]
Location=[]

element = soup.find('ul', {'class': 'new-joblist'})
for i in element.findAll("h2"):
    Jobs.append(i.get_text().replace('\n','').replace('\r','').replace(' ',''))
    # print(i.get_text())

for i in soup.find_all('ul',{'class':'top-jd-dtl clearfix'}):
    span = i.find_all('span', {'title':True})
    for s in span:
        # print(s.get_text())
        Location.append(s.get_text().replace('\n','').replace('\r','').replace(' ',''))

for li in soup.find_all('li'):
    span = li.find('span', {'class': 'srp-skills'})
    if span:
        SkillsReq.append(span.get_text().replace('\n','').replace('\r','').replace(' ',''))

lis1 = SkillsReq[::2]        
print (len(Jobs))
print(len (lis1))  
print(len(Location))
# print(SkillsReq[3])      

dict1={'JOBS':Jobs,'Skills':lis1,'LOCATION':Location}
df=pd.DataFrame(dict1)

print(df.head())        
df.to_csv("jobs.csv")



