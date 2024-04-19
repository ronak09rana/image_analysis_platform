# image_analyzer/tests/test_views.py
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from image_api.models import AnalyzedImage, Comment

#unit test cases for api tesing
class AnalyzeImageViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_analyze_image_endpoint(self):
        # Assuming you have a valid image file named test_image.jpg in your test directory
        with open("path/to/test_image.jpg", "rb") as image_file:
            response = self.client.post(
                "/analyze-image/",
                {"image": image_file},
                format="multipart"
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertIn("analysis_result", response.data)

class ImagesViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_images_endpoint(self):
        AnalyzedImage.objects.create(description="Test Image 1")
        AnalyzedImage.objects.create(description="Test Image 2")
        response = self.client.get("/images/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

class ImageViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_image_detail_endpoint(self):
        analyzed_image = AnalyzedImage.objects.create(description="Test Image")
        response = self.client.get(f"/image/{analyzed_image.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], "Test Image")
