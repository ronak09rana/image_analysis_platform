from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AnalyzeImageView, ImagesView, ImageView, CommentCreateView

#define api urls
urlpatterns = [
    path('analyze-image/', AnalyzeImageView.as_view(), name='analyze-image'),
    path('images/', ImagesView.as_view(), name='images'),
    path('image/<int:id>/', ImageView.as_view(), name='image-detail'),
    path('image/<int:id>/comment/', CommentCreateView.as_view(), name='add-comment'),
]

# Serve uploaded media during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
