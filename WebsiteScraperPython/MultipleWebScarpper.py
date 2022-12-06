import requests
from bs4 import BeautifulSoup as bs
import csv

print("Enter the url of the site:")
URL = input()

req = requests.get(URL)
soup = bs(req.text, 'html.parser')

titles = soup.find_all('div', attrs={'class', 'head'})

for page in range(1, 10):

    req = requests.get(URL + str(page) + '/')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('div', attrs={'class', 'head'})

    for i in range(4, 19):
        if page > 1:
            print(f"{(i - 3) + page * 15}" + titles[i].text)
        else:
            print(f"{i - 3}" + titles[i].text)

soup = bs(req.text, 'html.parser')

titles = soup.find_all('div', attrs={'class', 'head'})
titles_list = []
count = 1
for title in titles:
    d = {}
    d['Title Number'] = f'Title {count}'
    d['Title Name'] = title.text
    count += 1
    titles_list.append(d)

filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['Title Number', 'Title Name'])
    w.writeheader()

    w.writerows(titles_list)


print(titles[4].text)
