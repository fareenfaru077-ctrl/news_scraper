# Hacker News Headlines Scraper

A simple Python web scraper that fetches the latest headlines from **Hacker News** and saves them to a text file.

---

# Features

* Sends HTTP request to Hacker News
* Parses HTML using BeautifulSoup
* Extracts latest headlines
* Displays headlines in terminal
* Saves headlines to `headlines.txt`

---

# Requirements

Make sure you have Python installed (Python 3.7+ recommended).

Install dependencies:

```bash
pip install requests beautifulsoup4
```

---

# Usage

Run the script:

```bash
python script.py
```

---

# Output

* Headlines are printed in the console
* Headlines are saved in a file:

```
headlines.txt
```

Example output:

```
1. Example Headline One
2. Example Headline Two
3. Example Headline Three
```

---

#Code Overview

| Section        | Purpose           |
| -------------- | ----------------- |
| requests.get() | Fetch webpage     |
| BeautifulSoup  | Parse HTML        |
| find_all()     | Extract headlines |
| open()         | Save to file      |

---

# Error Handling

The script handles:

* Connection failures
* Invalid responses
* Unexpected errors

---


