from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(default="Hi")
    profile_picture = models.ImageField(default='default.jpg', blank=True)

class Follow(models.Model):
    Follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Follower')
    Following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Following')