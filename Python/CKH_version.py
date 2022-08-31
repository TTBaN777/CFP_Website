import requests
from bs4 import BeautifulSoup


url = "https://icsoc2022.spilab.es/"
response1 = requests.get(url).text
print(response1)
soup = BeautifulSoup(response1, 'html.parser')
divs = soup.find_all('td')
print(divs[0])
print('\n----------\n')
