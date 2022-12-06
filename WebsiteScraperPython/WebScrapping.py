import requests
from bs4 import BeautifulSoup

# Making a GET request
print("Enter the URL of the webiste for scarpping: ")

given_url=input()

r = requests.get(given_url)
var159 = BeautifulSoup(r.content, 'html.parser') #Parsing the HTML


# check status code for response received
# success code - 200
print("The Status code for the Given url is :",r)

print("Enter tags like p,a etc to find in content or press enter to contuine  :")
fnd1=input()

s = var159.find('div', class_='entry-content')
content = s.find_all(fnd1)
lines = s.find_all('p')

images_list = []

images = var159.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})


# print content of request
## print(r.content)

print("Passed url is :",r.url)
print("The status code for website :", r.status_code)

## print(var159.prettify())

print("####### Content of title are ##########")
print("The title of the website is :",var159.title)
print("The  name of the tag is :",var159.title.name)
print("name of parent tag:",var159.title.parent.name)
print("The result of find:",content)
print("###################################################################")
print("main content of site:")
for line in lines:
    print(line.text)

print("##################################################################")
print("list of all url in site")
for link in var159.find_all('a'):
    print(link.get('href'))

print("##################################################################")
print("list of all images in site :")

for image in images_list:
    print(image)

outofthe=var159.title

################################################################################################################3

