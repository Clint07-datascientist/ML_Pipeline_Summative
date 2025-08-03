from locust import HttpUser, task, between
import random

class PredictUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def predict_leaf(self):
        with open("sample_images/leaf1.jpg", "rb") as f:
            files = {"file": f}
            self.client.post("/predict", files=files)
