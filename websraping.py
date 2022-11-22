import requests
from bs4 import BeautifulSoup

url = "https://www.facebook.com/profile.php?id=100012381131101"
# get the html
r = requests.get(url)
htmlContent = r.content

# parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

# tree traversal
title = soup.title

# get all the paragraphs from the page
paras = soup.find('script')
print(paras)
