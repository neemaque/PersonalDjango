from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list),
    path('posts/<int:post_id>/', views.post),
    path('posts/create', views.create_post),
    path('posts/<int:post_id>/edit', views.edit_post),
    path('posts/<int:post_id>/delete', views.delete_post),
    path('posts/<int:post_id>/comment', views.comment),
]