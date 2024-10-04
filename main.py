import site_scraper as sc
import summarizer as sum
import os
import google_search as gs 

def main():
    # Replace these with your own values
    API_KEY = os.environ["GOOGLE_API_KEY"]
    CSE_ID = os.environ["GOOGLE_SEARCH_ENGINE_ID"]
    # 1. Search the web
    query = "Build a Bedrock Chatbot using only Boto3 and no langchain"
    top_10_links = gs.google_search(query, API_KEY, CSE_ID, num_results=10)
    
    # 2. Scrape the links
    scraped_contents = [sc.scrape_page(link) for link in top_10_links]

    link = top_10_links[0]
    print(scraped_contents)
    # 3. Store scraped content locally
    with open("_temp_files\scraped_data.txt", 'w', encoding='utf-8') as f:
        for content in scraped_contents:
            f.write(link + "\n" + content + "\n\n")
    
    # 4. Summarize the content into a blog
    with open("_temp_files\scraped_data.txt", 'r', encoding='utf-8') as f:
        all_text = f.read()
    
    summary = sum.summarize_text(all_text)
    
    # Save the blog summary
    with open("_final_blog\Blog_summary.txt", 'w', encoding='utf-8') as f:
        f.write(summary)

    print("Blog summary created successfully!")

if __name__ == "__main__":
    main()
