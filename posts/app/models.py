from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=255)

    def __str__(self):
        return f"{self.id}. {self.name}"

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category,
                                 related_name='posts',
                                 on_delete=models.CASCADE)
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}. {self.title}'

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        ordering = ['id']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=255)
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}. {self.author}'
