import requests
from bs4 import BeautifulSoup

page=requests.get("https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F")

print(page.status_code)
# f= open("all.txt","w+")

soup=BeautifulSoup(page.content,"html.parser")
info=list(soup.find_all('td', style='border-left:solid 2px #AAA;border-right:solid 1px #AAA;font-family:monospace;'))

arr=[]
for i in info:
    arr.append(i.get_text())
ar=[]
# print(arr)
for i in arr:
    ar.append(str(i).replace('\n',''))
print(ar)