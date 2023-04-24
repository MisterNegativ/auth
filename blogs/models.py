from django.db import models
from django.contrib.auth.models import User


class Oblast(models.Model):
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    oblast = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=False, related_name='oblasts')

    class Meta:
        verbose_name = 'Oblast'
        verbose_name_plural = 'Oblasts'


class City(models.Model):
    city = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE, related_name='cities')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class House(models.Model):
    address = models.CharField(null=False, max_length=255)
    region = models.CharField(null=False, max_length=255)
    street = models.CharField(null=False, max_length=255, default=False)
    flat = models.IntegerField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE, related_name='houses')

    class Meta:
        verbose_name = 'House'
        verbose_name_plural = 'Houses'


class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255)
    content = models.TextField(null=False, blank='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='posts')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

