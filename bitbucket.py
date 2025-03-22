import requests
from datetime import datetime, timedelta

def get_repositories(username, api_token):
    """
    Retrieves a list of repositories for a given user, including their creation dates and last commit timestamps.
    
    Args:
        username (str): The Bitbucket username.
        api_token (str): The Bitbucket API token.
    
    Returns:
        list: A list of Repository dictionaries.
    """
    url = f"https://api.bitbucket.org/2.0/repositories/{username}"
    headers = {"Authorization": f"Bearer {api_token}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return []
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        return []
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return []
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
        return []

    repositories = response.json()["values"]
    repository_list = []
    for repo in repositories:
        repository = {
            "name": repo["name"],
            "created_on": repo["created_on"],
            "last_commit": None
        }
        repository_list.append(repository)

    return repository_list

def filter_repositories(repositories):
    """
    Filters the repositories to only include those created within the last 30 days.
    
    Args:
        repositories (list): A list of Repository dictionaries.
    
    Returns:
        list: A list of filtered Repository dictionaries.
    """
    filtered_repositories = []
    for repository in repositories:
        created_on = datetime.strptime(repository["created_on"], "%Y-%m-%dT%H:%M:%S+00:00")
        if created_on > datetime.now() - timedelta(days=30):
            filtered_repositories.append(repository)
    return filtered_repositories

def get_last_committer(username, api_token, repository):
    """
    Retrieves the commit history for a repository and identifies the user who made the most recent commit.
    
    Args:
        username (str): The Bitbucket username.
        api_token (str): The Bitbucket API token.
        repository (dict): A Repository dictionary.
    
    Returns:
        str: The username of the last committer.
    """
    repo_slug = repository["name"].lower().replace(" ", "-")
    url = f"https://api.bitbucket.org/2.0/repositories/{username}/{repo_slug}/commits"
    headers = {"Authorization": f"Bearer {api_token}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return None
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        return None
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
        return None

    commits = response.json()["values"]
    if commits:
        return commits[0]["target"]["author"]["username"]
    else:
        return None

def generate_report(repositories, username, api_token):
    """
    Generates a report that includes the repository name, creation date, and the username of the last committer.
    
    Args:
        repositories (list): A list of Repository dictionaries.
        username (str): The Bitbucket username.
        api_token (str): The Bitbucket API token.
    """
    for repository in repositories:
        last_committer = get_last_committer(username, api_token, repository)
        if last_committer:
            print(f"Repository: {repository['name']}")
            print(f"Created On: {repository['created_on']}")
            print(f"Last Committer: {last_committer}")
            print("------------------------")

def main():
    username = "your_username"
    api_token = "your_api_token"
    repositories = get_repositories(username, api_token)
    filtered_repositories = filter_repositories(repositories)
    generate_report(filtered_repositories, username, api_token)

if __name__ == "__main__":
    main()
