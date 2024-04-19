# image_analyzer/tests/test_models.py
from django.test import TestCase
from image_api.models import AnalyzedImage, Comment

class AnalyzedImageModelTest(TestCase):
    def test_analyzed_image_creation(self):
        analyzed_image = AnalyzedImage.objects.create(description="Test Image Description")
        actual_description = analyzed_image.description  # Get the actual description
        self.assertEqual(actual_description, "Test Image Description")
        print("A")
        print(str(analyzed_image)) 
        self.assertEqual(str(analyzed_image), f"AnalyzedImage object ({analyzed_image.id}): Test Image Description")

class CommentModelTest(TestCase):
    def test_comment_creation(self):
        analyzed_image = AnalyzedImage.objects.create(description="Test Image Description")
        comment = Comment.objects.create(image=analyzed_image, text="Test Comment Text")
        print(str(comment))
        self.assertEqual(str(comment), f"Comment object ({comment.id}): Test Comment Text")
