from django.shortcuts import render, HttpResponse
from rest_framework import generics, pagination 
from rest_framework.response import Response
from rest_framework import status
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, EndpointConnectionError
from PIL import UnidentifiedImageError
import boto3
import logging
from .models import AnalyzedImage, Comment
from .serializers import AnalyzedImageSerializer, CommentSerializer

#define views classes for each api
class AnalyzeImageView(generics.CreateAPIView):
    serializer_class = AnalyzedImageSerializer

    def create_description(self, labels):
        # Customize this method based on your application's requirements
        if labels:
            return f"This image contains: {', '.join(labels)}"
        else:
            return "No recognizable objects found in the image"

    def perform_create(self, serializer):
        try:
            # Get the uploaded image
            image = self.request.data['image']

            # Call the external image analysis service (AWS Rekognition)
            analysis_result = self.analyze_image(image)

            # Save the analysis result to the database
            serializer.save(analysis_result=analysis_result)
        
        except UnidentifiedImageError:
            # Handle invalid image uploads (e.g., non-image files)
            return Response({'error': 'Invalid image file'}, status=status.HTTP_400_BAD_REQUEST)

        except (NoCredentialsError, PartialCredentialsError):
            # Handle AWS credentials issues
            return Response({'error': 'AWS credentials not provided or incomplete'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except EndpointConnectionError:
            # Handle network issues with AWS Rekognition
            return Response({'error': 'Failed to connect to the AWS Rekognition API'},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)

        except Exception as e:
            # Handle other unexpected errors
            return Response({'error': f'An unexpected error occurred: {str(e)}'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def analyze_image(self, image):
        try:
            # Set up AWS Rekognition client
            aws_region = 'ap-south-1'  # Replace with your AWS region
            client = boto3.client('rekognition', region_name=aws_region)

            # Read image content
            content = image.read()

            # Perform image analysis
            response = client.detect_labels(Image={'Bytes': content})

            # Extract labels from the response (you may customize this based on API response)
            labels = [label['Name'] for label in response['Labels']]

            # Combine the labels into a string
            #result = ', '.join(labels)
            result = self.create_description(labels)

            return result
        
        except Exception as e:
            # Handle errors during image analysis
            raise e

class ImagesPagination(pagination.PageNumberPagination):
    page_size = 10  # Adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ImagesView(generics.ListAPIView):
    queryset = AnalyzedImage.objects.all().order_by('-id')
    serializer_class = AnalyzedImageSerializer
    pagination_class = ImagesPagination

class ImageView(generics.RetrieveAPIView):
    queryset = AnalyzedImage.objects.all()
    serializer_class = AnalyzedImageSerializer
    lookup_field = 'id'
    pagination_class = ImagesPagination

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        # Extract image_id from the request (modify this based on your URL structure)
        image_id = self.kwargs.get('id')  # Replace with the actual parameter name in your URL

        # Associate the comment with the specified image
        image = AnalyzedImage.objects.get(pk=image_id)
        serializer.save(image=image)


logger = logging.getLogger(__name__)

def your_view(request):
    try:
        # Your view logic here
        logger.info("View executed successfully.")
    except Exception as e:
        logger.error(f"Error in view: {str(e)}", exc_info=True)
        # Handle the exception or let it propagate

    return HttpResponse("Your response")
