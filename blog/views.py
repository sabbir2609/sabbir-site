from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView


class BlogListView(ListView):
    model = Post
    template_name = "home.html"
