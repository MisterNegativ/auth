from django.urls import path
from .views import home_page, create_blog_page, blog_details_page, delete_blog_page, create_post,  \
    delete_post, post_details

urlpatterns = [
    path('', home_page, name='home'),
    path('blogs/create/', create_blog_page,  name='create_blog'),
    path('blogs/<int:pk>/', blog_details_page, name='blog_details'),
    path('blogs/<int:pk>/delete/', delete_blog_page, name='delete_blog'),
    path('blogs/<int:pk>/create_post/', create_post, name='create_post'),
    path('posts/<int:pk>/delete/', delete_post, name='delete_post'),
    path('posts/<int:pk>/', post_details, name='post_details'),
]

