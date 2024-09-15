from googlesearch import search
import csv



def google_search(query, num_results):
    try:
        # Perform Google search and get the top `num_results` links
        search_results = search(query, num_results=num_results, lang="en")
        
        # Store the results in a list
        results = []
        for result in search_results:
            results.append(result)
        return results
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
# if __name__ == "__main__":
#     query = "latest developments in AI 2024"
#     top_results = google_search(query)
    
#     # Print the top 5 links
#     for idx, link in enumerate(top_results, 1):
#         print(f"{link}")
    
from bs4 import BeautifulSoup
import requests

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all text within <p> tags
    paragraphs = soup.find_all('p')
    page_text = ' '.join([para.get_text() for para in paragraphs])
    
    return page_text


from dotenv import load_dotenv
import openai
import os

load_dotenv()

client = openai.OpenAI(
    # This is the default and can be omitted
    api_key = os.getenv("OPENAI_API_KEY")
)

def summarize_text(text):
    response = openai.completions.create(
        model="tts-1-1106",
        prompt=f"Summarize the following content into a short blog using markdown langugage that is ready to push using Jykell:\n{text}"
    )
    return response.choices[0].text.strip()


def main():
    # 1. Search the web
    query = "latest developments in AI 2024"
    top_5_links = google_search(query, 5)
    
    # 2. Scrape the links
    scraped_contents = [scrape_page(link) for link in top_5_links]
    
    # 3. Store scraped content locally
    with open('scraped_data.txt', 'w', encoding='utf-8') as f:
        for content in scraped_contents:
            f.write(content + "\n\n")
    
    # 4. Summarize the content into a blog
    with open('scraped_data.txt', 'r', encoding='utf-8') as f:
        all_text = f.read()
    
    summary = summarize_text(all_text)
    
    # Save the blog summary
    with open('blog_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)

    print("Blog summary created successfully!")

if __name__ == "__main__":
    main()







