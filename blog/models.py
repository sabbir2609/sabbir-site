from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, null=True)  # new

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
