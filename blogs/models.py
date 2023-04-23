from django.db import models
from django.contrib.auth.models import User


class Oblast(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class City(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE)


class House(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    region = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default='unknown')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default='')


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE, default='')
    city = models.ForeignKey(City, on_delete=models.CASCADE, default='')
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE, default='')


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts', default='unknown')
    house = models.ForeignKey(House, on_delete=models.CASCADE)
