from ast import List
from collections import Counter
from models import Commit
from utils import meassure_time


@meassure_time
def most_active_authors(commits : List[Commit]):
    authors = [commit.author for commit in commits]
    counter = Counter(authors)
    return counter.most_common(3)


def commit_messages(commits : List[Commit]):
    for commit in commits:
        yield commit.message