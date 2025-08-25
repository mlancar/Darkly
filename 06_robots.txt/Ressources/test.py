#!/bin/python3
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def getAllLinks(url) :
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for a_tag in soup.find_all("a"):
        href = a_tag.get("href")
        if href and href != "../":
            full_url = urljoin(url, href)
            links.append(full_url)
    return links

def is_file(url):
    response = requests.head(url, allow_redirects=True)
    content_type = response.headers.get("Content-Type", "")
    return not content_type.startswith("text/html")

baseURL = "http://localhost:4200/.hidden/"
output_dir = "files"
os.makedirs(output_dir, exist_ok=True)

L = getAllLinks(baseURL)

i = 0
while len(L) != 0 :
    #print(L)
    link = L.pop()
    if is_file(link):
        filename = "README_" + str(i)
        response = requests.get(link)
        if response.status_code == 200:
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "wb") as f:
                f.write(response.content)
            print(f"[+] Fichier téléchargé : {filepath}")
            i += 1
        else:
            print(f"[-] Erreur HTTP {response.status_code}")
    else :
        L.extend(getAllLinks(link))

print(i)