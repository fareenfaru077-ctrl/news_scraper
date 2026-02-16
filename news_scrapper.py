import requests
from bs4 import BeautifulSoup

# URL of news website
url = "https://news.ycombinator.com/"

try:
    # Send GET request
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        print("Successfully fetched the webpage!")

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all headline links
        headlines = soup.find_all("span", class_="titleline")

        # Open file to save headlines
        with open("headlines.txt", "w", encoding="utf-8") as file:
            for index, headline in enumerate(headlines, start=1):
                title = headline.get_text()
                print(f"{index}. {title}")
                file.write(f"{index}. {title}\n")

        print("\nHeadlines saved to headlines.txt")

    else:
        print("Failed to retrieve webpage. Status code:", response.status_code)

except Exception as e:
    print("An error occurred:", e)