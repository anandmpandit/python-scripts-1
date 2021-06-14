import random
import requests # pip install requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')
    movetag0 = movietags[0]
    moviesplit = movetag0.split()
    print(moviesplit)


if __name__ == '__main__':
    main()