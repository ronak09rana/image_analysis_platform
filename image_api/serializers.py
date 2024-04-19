# image_api/serializers.py
from rest_framework import serializers
from .models import AnalyzedImage, Comment

class CommentSerializer(serializers.ModelSerializer):
    #serializer for comment model
    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at']

class AnalyzedImageSerializer(serializers.ModelSerializer):
    #serializer for analyze-image model
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = AnalyzedImage
        fields = ['id', 'image', 'description', 'analysis_result', 'comments']
