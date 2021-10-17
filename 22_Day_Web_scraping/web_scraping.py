import requests
from bs4 import BeautifulSoup

url1 = "https://www.bu.edu/president/boston-university-facts-stats/"
response1 = requests.get(url1)
content1 = response1.content
soup1 = BeautifulSoup(content1, 'html.parser')
print(response1.json())