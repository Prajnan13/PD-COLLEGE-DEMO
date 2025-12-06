from locust import HttpUser, task, between

class KYCUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def upload_doc(self):
        # This is a stub; Locust needs files to POST; for local testing, extend this.
        self.client.get("/")
