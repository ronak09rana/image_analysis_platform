# image_api/models.py
from django.db import models


#define all models here
class AnalyzedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField(null=True, blank=True)
    analysis_result = models.TextField(null=True, blank=True)

class Comment(models.Model):
    image = models.ForeignKey(AnalyzedImage, on_delete=models.CASCADE, related_name='comments', null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
