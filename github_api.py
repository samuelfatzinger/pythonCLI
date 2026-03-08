import requests
from models import Commit

BASE_URL = "https://api.github.com"

def fetch_commits(owner: str, repo: str, limit: int = 30) -> list[Commit]:

    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"

    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    commits = []

    for item in data[:limit]:
        author = item["commit"]["author"]["name"]
        message = item["commit"]["message"]

        commits.append(Commit(author, message))

    return commits