import requests
import sys
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Please give one URL to run this program.")
    sys.exit(0)

site_re = sys.argv[1]  
print("Working on:", site_re)

# add https if missing example: "univ.sitare.org"
if not site_re.startswith("http"):
    site_re = "https://" + site_re

# added to avoid the blocked by the websites 
head = {
    "User-Agent": "Mozilla/5.0"
}
# download page that user needed 
response = requests.get(site_re, headers=head)
parts_of_website = BeautifulSoup(response.text, "html.parser")

# extracting the title of the website 
print("tittle of the website :")
title = parts_of_website.find("title")
if title is not None:  
    print(title.string.strip())
else:
    print("website does not have a title")

# extracting the body of the website 
print("content of the website: ")
body = parts_of_website.find("body")
if body is not None:
    text = body.get_text().strip()
    # check if body is empty or requires JavaScript
    lines = text.split("\n")
    req_cleaned = []
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
print("links in website")
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
    print("No links found in this website.")
