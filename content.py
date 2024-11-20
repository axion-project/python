# Content Aggregator
# By Michael Morales

import feedparser

def fetch_rss_feed(url):
    """
    Fetches and parses an RSS feed from a given URL.
    
    Parameters:
        url (str): The URL of the RSS feed to fetch.
        
    Returns:
        list: A list of dictionaries containing the titles and links of the articles.
    """
    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        }
        articles.append(article)

    return articles

def display_articles(articles):
    """
    Displays the aggregated articles in a user-friendly format.
    
    Parameters:
        articles (list): A list of articles with title, link, and publication date.
    """
    if not articles:
        print("No articles found.")
        return

    for idx, article in enumerate(articles, start=1):
        print(f"\n{idx}. {article['title']}")
        print(f"   Published on: {article['published']}")
        print(f"   Link: {article['link']}")

def main():
    """
    Main function to run the content aggregator.
    """
    print("Welcome to the Content Aggregator!")
    rss_urls = [
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",  # Example: The New York Times homepage feed
        "https://feeds.bbci.co.uk/news/rss.xml",  # Example: BBC News feed
        "https://www.theverge.com/rss/index.xml"  # Example: The Verge feed
    ]
    
    aggregated_articles = []

    # Fetch and aggregate articles from each RSS feed URL
    for url in rss_urls:
        print(f"\nFetching content from {url}...")
        articles = fetch_rss_feed(url)
        aggregated_articles.extend(articles)

    # Display all aggregated articles
    print("\nAggregated Articles:")
    display_articles(aggregated_articles)

# Run the Content Aggregator
if __name__ == "__main__":
    main()
