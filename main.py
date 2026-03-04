
from analyzer import most_active_authors, commit_messages
from models import Commit

commits = [
    Commit("Sasha", "Initial commit"),
    Commit("Bob", "Bug fix"),
    Commit("Daniel", "Says hellp"),
]

top = most_active_authors(commits)

print("Top contributors:")

for author, count in top:
    print(author, count)

print("\nCommit messages:")
for message in commit_messages(commits):
    print(message)