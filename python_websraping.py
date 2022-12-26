# import  libraries
import requests
from bs4 import BeautifulSoup

url = 'https://wuzzuf.net/search/jobs/?q=python&a=navbl'
response = requests.get(url)

# print(response.text)
# use bs4 to parser
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

#listing = []

job_title1 = soup.find_all("div", {'class': 'css-1gatmva e1v1l3u10'})
job_title2 = soup.find_all("div", {'class': 'css-pkv5jc'})
jod_title3 = soup.find_all("div", {'class': 'css-1gatmva e1v1l3u10'})

#data_job1 = job_title1.contents[0].find('h2').text
data_job1 = job_title1[0].div.h2.text
data_job2 = job_title2[1].div.h2.a.text
data_job3 = jod_title3[2].div.h2.a.text

print(data_job1+'\n', data_job2+'\n', data_job3)
print('thanks the project has ended', 'ghada mohammed')
#print(job_title1,job_title2)
