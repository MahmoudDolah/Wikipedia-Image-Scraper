#! /usr/bin/env python3
import requests
import urllib.parse 
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from lxml import html 

def get_images(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, "lxml")
  for img in soup.select('img'):
    img_url = urllib.parse.urljoin(url, img['src'])
    file_name = img['src'].split('/')[-1]
    urlretrieve(img_url, file_name)
    
def main():
  url = 'https://en.wikipedia.org/wiki/Flatiron_District'
  get_images(url)

if __name__ == "__main__":
  main()