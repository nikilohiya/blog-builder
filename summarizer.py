import requests
from dotenv import load_dotenv
import os

load_dotenv()

def google_search(query, api_key, cse_id, num_results=5):
    search_url = "https://customsearch.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id,
        'num': num_results
    }

    try:
        response = requests.get(search_url, params=params)
        print(f"Response Status Code: {response.status_code}")
        
        response.raise_for_status()
        search_results = response.json()

        # Extract and return the URLs from the search results
        urls = [item['link'] for item in search_results.get('items', [])]
        return urls

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return []
    except Exception as err:
        print(f"An error occurred: {err}")
        return []

# Replace these with your own values
API_KEY = os.environ["GOOGLE_API_KEY"]
CSE_ID = os.environ["GOOGLE_SEARCH_ENGINE_ID"]

# Example usage
if __name__ == "__main__":
    query = "latest AI trends 2024"
    top_urls = google_search(query, API_KEY, CSE_ID, num_results=5)

    # Print the URLs
    print("Top search results:")
    for idx, url in enumerate(top_urls, 1):
        print(f"{idx}. {url}")