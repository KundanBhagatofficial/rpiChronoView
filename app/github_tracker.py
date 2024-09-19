import requests

class GitHubTracker:
    def __init__(self, user, repo):
        self.user = user
        self.repo = repo
        self.base_url = f"https://api.github.com/repos/{user}/{repo}/issues"

    def get_issues(self):
        response = requests.get(self.base_url)
        return response.json() if response.status_code == 200 else None
