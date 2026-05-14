# 🕷️ Web Scraper — Python CLI Tool

A command-line Python web scraper that extracts key information from any website — including the page title, body text, and all outbound links.

---

## ✨ Features

- 📌 **Title Extraction** — Grabs the webpage title
- 📄 **Body Text Extraction** — Cleans and prints readable body content
- 🔗 **Outlink Detection** — Lists all external links found on the page
- 🕵️ **Bot Detection Bypass** — Uses a fake User-Agent to avoid being blocked
- ⚡ **JavaScript Detection** — Alerts when a site needs an API instead of scraping

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Libraries | BeautifulSoup4, Requests |
| Interface | Command Line (CLI) |

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Rakshita-0206/SEIR_Projects.git
cd SEIR_Projects
```

**2. Install dependencies**
```bash
pip install requests beautifulsoup4
```

**3. Run the scraper**
```bash
python scraper.py https://example.com
```

---

## 📌 Sample Output

```
Title:
Example Domain

Body Text:
Example Domain This domain is for use in illustrative examples...

Outlinks:
https://www.iana.org/domains/reserved
```

---

## 🧠 How it Works

1. Takes a URL as a command-line argument
2. Sends a GET request with a fake browser User-Agent
3. Parses the HTML using BeautifulSoup
4. Extracts and prints title, cleaned body text, and all outbound links

---

## 🙋‍♀️ Author

**Rakshita K Biradar**
B.Tech Computer Science, Sitare University, Lucknow
📧 su-24110@sitare.org | [GitHub](https://github.com/Rakshita-0206) | [LinkedIn](www.linkedin.com/in/rakshita-k-biradar-a218ab324)

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
