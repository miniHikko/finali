from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    post_Author = models.ForeignKey(User, on_delete=models.CASCADE)
    data_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    header = models.CharField(max_length=50)
    text = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='images/')

    def preview(self):
        return self.text[:125] + '...' if len(self.text) > 124 else self.text

    def __str__(self):
        return f'{self.header.title()}: {self.text[:20]}'

    def get_url(self):
        return f'/noticeboard/{self.id}'

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Coment(models.Model):
    post_coment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_coment = models.ForeignKey(User, on_delete=models.CASCADE)
    coment_text = models.TextField(max_length=3000)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])
