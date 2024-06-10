import requests
from bs4 import BeautifulSoup

url="https://github.com/Zymiva/hangman_file/blob/6ce478c19d4f4d919b58f6720ced88bd04c22f85/Github_hangman.html"

response = requests.get(url)
response = response.content 
soup=BeautifulSoup(response,"html.parser")


ol = soup.find('ol')
words = ol.find_all('li')
wordList = []

for tag in words:
    #tagContent = tag.find('value')
    #word= tag.attrs['value']
    word = tag.text.strip()
    wordList.append(word)
             

print(wordList)
input()