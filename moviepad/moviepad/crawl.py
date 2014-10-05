import requests
from bs4 import BeautifulSoup

url = "http://dout.jp/"
r = requests.get(url)
soup = BeautifulSoup(r.text.encode(r.encoding))
movie_link = soup.find_all("a", {"class":"featured-image"})
print(movie_link)
