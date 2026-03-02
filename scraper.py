import requests
import sys
from bs4 import BeautifulSoup

# check if user gave a url
if len(sys.argv) < 2:
    print("Please give a URL to run this program.")
    sys.exit(0)

site_re = sys.argv[1]
print("Working on:", site_re)

# add https if missing example: "univ.sitare.org"
if not site_re.startswith("http"):
    site_re = "https://" + site_re

# download page that user needed 
response = requests.get(site_re)
parts_of_website = BeautifulSoup(response.text, "html.parser")

# extracting the tittle of the website 
print("\n TITLE")
title = parts_of_website.find("title")
if title is not None and title.string:
    print(title.string.strip())
else:
    print("website do not have the tittle")

# extracting the body of the website 
print("\nBODY")
body = parts_of_website.find("body")
if body is not None:
    text = body.get_text()
    lines = text.split("\n")
    req_cleaned= []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line != "":
            req_cleaned.append(line)
        i += 1
    print(" ".join(req_cleaned))
else:
    print("there is no body present in the website.")

# extracting the links in the website 
print("\n LINKS")
all_links = parts_of_website.find_all("a")
count = 0
j = 0
while j < len(all_links):
    link = all_links[j].get("href")
    if link is not None and link.startswith("http"):
        count += 1
        print(str(count) + ") " + link)
    j += 1

if count == 0:
    print("No links found.")
