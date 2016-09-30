#! /usr/bin/env python3

import os
import wikipedia
import requests
import urllib.parse 
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

def get_images(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, "html.parser")
  for img in soup.select('img'):
    img_url = urllib.parse.urljoin(url, img['src'])
    file_name = img['src'].split('/')[-1]
    urlretrieve(img_url, file_name)
    
def search_wikipedia(lookup):
  page = wikipedia.page(lookup)
  url = page.url
  return url

def main():
  lookup = input("What would you like to look up? ")
  url = search_wikipedia(lookup)
  get_images(url)
  
if __name__ == "__main__":
  main()
  
