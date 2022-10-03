import time
from bs4 import BeautifulSoup
import requests
import re

def main():
    link = 'https://www.google.com/maps/place/Doppio+Zero/@37.3944871,-122.0812506,17z/data=!4m5!3m4!1s0x808fb7343b0c99fd:0x7a48a445df767cac!8m2!3d37.3944829!4d-122.0790619'
    resp = requests.get(
                link,
                allow_redirects=True
            )

    bsObj = BeautifulSoup(resp.content, 'lxml')
    elements = bsObj.findAll('button', jsaction=re.compile('pane.rating.category'))
    for link in elements:
        print(link)
if __name__ == "__main__":
    main()