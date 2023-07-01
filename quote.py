import requests
from bs4 import BeautifulSoup
url="https://www.kdnuggets.com/2017/05/42-essential-quotes-data-science-thought-leaders.html"

r=requests.get(url)
htmlContent=r.content
print(htmlContent)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

# Getting the title tag
print(soup.title)
 
# Getting the name of the tag
print(soup.title.name)
 
# Getting the name of parent tag
print(soup.title.parent.name)


# filename="quote.csv"
# f=open(filename,"w")
# headers="Author,Quote\n"
# f.write(headers)


# for data in soup.find_all("div",{id:"post"},'p','ol'):
#     print(data.get_text())

for data in soup.find_all("ol"):
    l2=data.get_text()
    print(l2)

for data in soup.find_all("p"):
    l1=data.get_text()
    print(l1)
    



# titles = soup.find_all('div', attrs={'p', 'ol'})
# titles_list = []

# count = 1
# for title in titles:
# 	d = {}
# 	d['Author'] = f'Title {count}'
# 	d['Quote'] = title.text
# 	count += 1
# 	titles_list.append(d)

# filename = "titles.csv"
# with open(filename, 'w', newline='') as f:
# 	w = csv.DictWriter(f,['Author','Quote'])
# 	w.writeheader()
# 	w.writerows(titles_list)



