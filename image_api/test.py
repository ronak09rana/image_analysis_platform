# image_analyzer/tests/test_models.py
from django.test import TestCase
from .models import AnalyzedImage, Comment

class AnalyzedImageModelTest(TestCase):
    #for testing analyzedimage model
    def test_analyzed_image_creation(self):
        analyzed_image = AnalyzedImage.objects.create(description="Test Image Description")
        self.assertEqual(str(analyzed_image), f"AnalyzedImage object ({analyzed_image.id}): Test Image Description")

class CommentModelTest(TestCase):
    #for testing comment model
    def test_comment_creation(self):
        analyzed_image = AnalyzedImage.objects.create(description="Test Image Description")
        comment = Comment.objects.create(image=analyzed_image, text="Test Comment Text")
        self.assertEqual(str(comment), f"Comment object ({comment.id}): Test Comment Text")
