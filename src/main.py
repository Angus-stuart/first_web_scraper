from bs4 import BeautifulSoup
import requests
from datetime import date

todays_date = date.today()
todays_date_str = todays_date.strftime("%d/%m/%Y")

# Retrieves the number one news story from hacker news
def get_headline(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.text, 'html.parser')

    first_title = soup.select_one('.titleline a')
    return first_title
    
# Stores relevant information into the text file
def store_headline(top_story):
    with open('data/headlines.txt', 'a', encoding='utf-8') as f:
        f.write(f"{todays_date_str}\n")
        f.write("Today's Top Hacker News Headline:\n")
        f.write(f"Title: {top_story.text.strip()}\n")
        f.write(f"Link: {top_story['href']}\n\n")

def main(): 
    URL = "https://news.ycombinator.com/"
    top_story = get_headline(URL)
    store_headline(top_story)
    

main()