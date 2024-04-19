# image_analyzer/tests/test_integration.py
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
from image_api.models import AnalyzedImage

class AnalyzeImageViewIntegrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch("boto3.client")
    def test_analyze_image_integration(self, mock_boto3_client):
        # Assuming you have a valid image file named test_image.jpg in your test directory
        with open("path/to/test_image.jpg", "rb") as image_file:
            mock_boto3_client.return_value.detect_labels.return_value = {
                "Labels": [{"Name": "Object1"}, {"Name": "Object2"}]
            }

            response = self.client.post(
                "/analyze-image/",
                {"image": image_file},
                format="multipart"
            )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertIn("analysis_result", response.data)
        self.assertEqual(response.data["analysis_result"], "This image contains: Object1, Object2")
