# blog_spider.py
# By Michael Morales

import scrapy

class BlogSpider(scrapy.Spider):
    name = "blog"
    start_urls = [
        "https://example-blog.com"  # Replace with the target website
    ]

    def parse(self, response):
        """
        Parses the main page of the blog and extracts article titles and links.
        """
        self.log("Scraping the blog's homepage...")

        # Loop through each article element (modify selectors based on the website's structure)
        for article in response.css("article"):
            yield {
                "title": article.css("h2 a::text").get(),
                "link": article.css("h2 a::attr(href)").get()
            }

        # Follow the pagination link to scrape the next page
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
