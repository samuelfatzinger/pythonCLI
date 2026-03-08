import json
from models import Commit

def load_commits_from_file(path: str):
    with open(path) as f:
        data = json.load(f)

    return [Commit(item["author"], item["message"]) for item in data]