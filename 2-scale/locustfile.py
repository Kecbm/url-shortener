from locust import HttpUser, task, between
import random
import string

class URLShortenerUser(HttpUser):
    # Simulation of user wait 1 or 2 seconds between actions
    wait_time = between(1, 2)

    def on_start(self):
        # When a user born, they create an URL for access before
        random_url = f"https://example.com/{''.join(random.choices(string.ascii_letters, k=10))}"
        response = self.client.post("/shorten", json={"url": random_url})

        if response.status_code == 200:
            self.short_hash = response.json().get("short_url").split("/")[-1]
        else:
            self.short_hash = None

    # Read 3x more of write
    @task(3)
    def redirect_url(self):
        if self.short_hash:
            # Use catch_response=True for Locust do not see the redirect (307) when an error
            with self.client.get(f"/{self.short_hash}", catch_response=True, allow_redirects=False) as response:
                if response.status_code in [301, 302, 307]:
                    response.success()

    # Action of write
    @task(1)
    def create_short_url(self):
        random_url = f"https://example.com/{''.join(random.choices(string.ascii_letters, k=10))}"
        self.client.post("/shorten", json={"url": random_url})