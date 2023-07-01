import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.kdnuggets.com/2017/05/42-essential-quotes-data-science-thought-leaders.html"

r=requests.get(url)
htmlContent=r.content

soup = BeautifulSoup(r.content, 'html.parser')

quotes=[]
authors=[]
def get_data(soup):
    dic={}

    try:
        print("NEECHE IS ALL THE QUOTES")
        content_div = soup.find('div', {'id': 'post-'})

        for something in content_div.findAll("li"):
            if(something.parent.name == "ol"):
                quotes.append(something.text)

        print("NEECHE IS ALL THE AUTHORS")
        for something in content_div.findAll("em"):
            if(something.parent.name == "a"):
                authors.append(something.text)

    except:
        print(soup.find("li").text)
        dic['IMP DATA']=None
        print("None")


get_data(soup)

print (len(quotes))
print(len (authors))

dict2={'quote':quotes,'author':authors,'category':'datasci'}
df_ds=pd.DataFrame(dict2)

print(df_ds.head())
