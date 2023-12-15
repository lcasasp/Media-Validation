import os
import json
import constants
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY", None)

#Note, these News API keys are subject to change, used only for testing
keys = "Energy 'climate'"

def scrape_google_scholar_metadata(self):
    base_url = "https://scholar.google.com"
    metadata = []

    for page in range(constants.GOOGLE_SCHOLAR_PAGE_DEPTH):
        query_url = f"{base_url}/scholar?q=energy 'climate change'&start={page*10}&scisbd=1"
        response = requests.get(query_url)
        print(response.content)
        soup = BeautifulSoup(response.content, "html.parser")

        results = soup.find_all("div", class_="gs_r")
        print(results)

        for result in results:
            # Extract URL
            url_element = result.find("div", class_="gs_ggsd")
            url = url_element.find("a")["href"] if url_element else ""

            # Create metadata dictionary
            if (url != ""):
                metadata.append({
                    "url": url,
                })
        print(metadata)

    for url in metadata:
        # check if an article with the same URL already exists
        if db.session.query(Urls).filter_by(url=url['url']).first():
            print(f"Article with URL {url['url']} already exists in database.")
            continue

        # Create new article if it doesn't exist in the database
        url = Urls(
            url=url['url'],
        )
        db.session.add(url)
    db.session.commit()

def addNewsUrl(self):
    data = newsapi.get_everything(q=keys,
                            language='en',
                            sort_by='popularity')

    # Loop through articles and add/update them in the database
    pages = data['totalResults'] // 100 + 1
    if pages > constants.NEWS_API_PAGE_DEPTH:
        pages = constants.NEWS_API_PAGE_DEPTH
    for page in range(5, pages+3):
        data = newsapi.get_everything(q=keys,
                                language='en',
                                sort_by='popularity',
                                page=page)
        for article_data in data['articles']:
            # Check if an URL with the same URL already exists in the Urls table
            if db.session.query(Urls).filter_by(url=article_data['url']).first():
                print(f"URL {article_data['url']} already exists in database.")
                continue

            # Create new Url object if it doesn't exist in the database
            url = Urls(url=article_data['url'])
            db.session.add(url)
        db.session.commit()