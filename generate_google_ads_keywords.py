# Generating Keywords for Google Ads in Python
# By Michael Morales

import requests
from PyDictionary import PyDictionary
import nltk
from nltk.corpus import wordnet
from collections import Counter

# Download wordnet data for synonym extraction
nltk.download('wordnet')
nltk.download('omw-1.4')

# Function to fetch synonyms of a given seed keyword
def get_synonyms(seed_keyword):
    """
    Fetches synonyms for the given seed keyword using WordNet.
    """
    synonyms = set()
    for syn in wordnet.synsets(seed_keyword):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    
    return list(synonyms)

# Function to generate Google Ads related keywords
def generate_keywords(seed_keywords):
    """
    Generates a list of keywords by finding synonyms and related terms.
    """
    all_keywords = set()

    # Loop through each seed keyword and find related keywords
    for keyword in seed_keywords:
        print(f"Generating keywords for: {keyword}")
        synonyms = get_synonyms(keyword)

        # Add the original seed keyword and its synonyms to the keyword set
        all_keywords.update(synonyms)
        all_keywords.add(keyword)
    
    # Remove any unwanted symbols or single-letter words from the list
    all_keywords = {k.lower() for k in all_keywords if len(k) > 1 and k.isalnum()}

    # Return the generated list of keywords
    return list(all_keywords)

# Function to expand the keywords using PyDictionary (related terms)
def expand_keywords_with_related_terms(keywords):
    """
    Expands keywords using PyDictionary to get related terms.
    """
    dictionary = PyDictionary()
    expanded_keywords = set()

    for keyword in keywords:
        print(f"Expanding keyword: {keyword}")
        related_terms = dictionary.synonym(keyword)
        
        if related_terms:
            expanded_keywords.update(related_terms)
    
    return list(expanded_keywords)

# Function to display the most common keywords
def display_top_keywords(keywords):
    """
    Display the top 10 most frequent keywords.
    """
    keyword_counts = Counter(keywords)
    print("\nTop 10 Keywords (by frequency):")
    for keyword, count in keyword_counts.most_common(10):
        print(f"{keyword}: {count}")

# Main function to execute the script
def main():
    # Example seed keywords for your Google Ads campaign
    seed_keywords = ["laptop", "smartphone", "headphones", "tablet", "keyboard"]

    # Step 1: Generate initial list of related keywords
    generated_keywords = generate_keywords(seed_keywords)

    # Step 2: Expand the list with related terms using PyDictionary
    expanded_keywords = expand_keywords_with_related_terms(generated_keywords)

    # Step 3: Display the top keywords by frequency
    display_top_keywords(expanded_keywords)

    # Save the generated keywords to a file
    with open("google_ads_keywords.txt", "w") as f:
        for keyword in expanded_keywords:
            f.write(f"{keyword}\n")
    print("\nKeywords have been saved to 'google_ads_keywords.txt'")

if __name__ == "__main__":
    main()
