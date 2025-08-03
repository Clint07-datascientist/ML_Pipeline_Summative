from locust import HttpUser, task, between
import random
import os
from io import BytesIO

class PredictUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        """Setup method called when a simulated user starts"""
        # Create a dummy image file for testing if it doesn't exist
        self.test_image_data = self.create_dummy_image_data()

    def create_dummy_image_data(self):
        """Create dummy image data for testing"""
        # This creates a simple test image data
        # In a real scenario, you'd use actual test images
        return b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\xff\xc0\x00\x11\x08\x00\x01\x00\x01\x01\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00\x3f\x00\x00\xff\xd9'

    @task(3)
    def predict_leaf(self):
        """Test the prediction endpoint"""
        files = {"file": ("test_image.jpg", self.test_image_data, "image/jpeg")}
        with self.client.post("/predict", files=files, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Prediction failed with status {response.status_code}")

    @task(1)
    def health_check(self):
        """Test a simple health check endpoint"""
        with self.client.get("/", catch_response=True) as response:
            if response.status_code in [200, 404]:  # 404 is acceptable if no root endpoint
                response.success()
            else:
                response.failure(f"Health check failed with status {response.status_code}")

    @task(1) 
    def retrain_endpoint(self):
        """Test the retrain endpoint (if it exists)"""
        with self.client.post("/retrain/", catch_response=True) as response:
            if response.status_code in [200, 202, 404]:  # Various acceptable responses
                response.success()
            else:
                response.failure(f"Retrain failed with status {response.status_code}")
