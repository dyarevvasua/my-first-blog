
from django.urls import path
from blogs import views

urlpatterns = [
    path('api/blogs', views.blogs_handler),
    path('api/blogs/<int:pk>', views.blog_handler),
]