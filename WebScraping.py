from bs4 import BeautifulSoup
import requests

url = "https://wuzzuf.net/search/jobs/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(page.text)
results = soup.find(id="app")
jobs = results.find_all("div", class_ = "css-1gatmva e1v1l3u10")
for job in jobs: 
    title = job.find("a", class_="css-o171kl")
    company = job.find("a", class_="css-17s97q8")
    location = job.find("span", class_="css-5wys0k")
    time = job.find("div", class_="css-4c4ojb")
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print(time.text.strip())
    print()

