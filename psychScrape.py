import bs4 as bs
import urllib.request as req

source = req.urlopen(
    "https://docs.google.com/document/d/16FiNwOLQw8dU--uW7dhGrudwdL-WrB0S4f5c9zuFY60/edit")

soup = bs.BeautifulSoup(source, 'html.parser')

print(soup.title)
