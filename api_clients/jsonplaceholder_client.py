import requests


class JSONPlaceholderClient:
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "qa-api-pytest-jsonplaceholder/1.0",
                "Accept": "application/json",
            }
        )

    def list_users(self):
        return self.session.get(f"{self.base_url}/users", timeout=15)

    def get_post(self, post_id: int):
        return self.session.get(f"{self.base_url}/posts/{post_id}", timeout=15)

    def create_post(self, title: str, body: str, user_id: int):
        payload = {"title": title, "body": body, "userId": user_id}
        return self.session.post(f"{self.base_url}/posts", json=payload, timeout=15)
