from django.urls import path
from .views import BlogListView, BlogDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
