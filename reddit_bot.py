# Reddit Bot
# By Michael Morales

import praw
import time
import random

# Set up the Reddit client with your credentials
def create_reddit_instance():
    """
    Create and return a Reddit instance for interacting with the API.
    """
    reddit = praw.Reddit(
        username="YOUR_REDDIT_USERNAME",
        password="YOUR_REDDIT_PASSWORD",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        user_agent="YOUR_USER_AGENT"
    )
    return reddit

def post_to_subreddit(reddit, subreddit, title, message):
    """
    Post a message to a specific subreddit.
    """
    try:
        print(f"Posting to /r/{subreddit}...")
        reddit.subreddit(subreddit).submit(title, selftext=message)
        print("Post submitted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def comment_on_posts(reddit, subreddit, comment_text, limit=5):
    """
    Comment on the latest posts in a specific subreddit.
    """
    print(f"Looking for posts in /r/{subreddit} to comment on...")
    for submission in reddit.subreddit(subreddit).new(limit=limit):
        try:
            print(f"Commenting on: {submission.title}")
            submission.reply(comment_text)
            print("Comment posted!")
        except Exception as e:
            print(f"An error occurred: {e}")

def run_bot():
    """
    Run the bot to post and comment on Reddit.
    """
    reddit = create_reddit_instance()

    # Example: Post a message to a subreddit
    post_to_subreddit(reddit, "YOUR_TARGET_SUBREDDIT", "Hello, Reddit!", "This is an automated post from my Reddit bot!")

    # Example: Comment on the latest 5 posts in a subreddit
    comment_text = "This is an automated comment from my Reddit bot!"
    comment_on_posts(reddit, "YOUR_TARGET_SUBREDDIT", comment_text)

if __name__ == "__main__":
    run_bot()
