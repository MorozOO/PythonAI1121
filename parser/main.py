
import requests
from bs4 import BeautifulSoup

url = "https://uaserials.pro/films/"
r = requests.get(url)
soup = BeautifulSoup(r.text,features="html.parser")
soup_list_name = soup.find_all('div',{'class':'th-title-oname'})

listName= []
listYear = []
# for i in soup_list_name:
#     listName.append(i.text)
# print(listName)
f = open('1.txt','a')
soup_list_href = soup.find_all('a',{'class':'short-img img-fit'})
for a in soup.find_all('a', href=True):
    u = a['href']
    if u.startswith("http"):
        print(u)

        request = requests.get(u)
        soup1 = BeautifulSoup(request.text, features="html.parser")
        soup_list_name = soup1.find_all('div', {'class': 'th-title truncate'})
        soup_list_year = soup1.find_all('ul',{"class":"short-list fx-1"} )

        print(soup_list_year)
        break
        # for i in soup_list_href:
        #     listName.append(i.text)
        #     print(i.text)
        #     f.write(f"{i.text}\n")
f.close()




