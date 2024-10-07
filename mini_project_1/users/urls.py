from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:user_id>/', views.profile),
    path('users/<int:user_id>/edit/', views.edit_profile),
    path('users/<int:user_id>/follow/', views.follow_user),
    path('users/<int:user_id>/unfollow/', views.unfollow_user),
    path('register/', views.register)
]