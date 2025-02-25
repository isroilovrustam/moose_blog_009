from django.core.validators import validate_comma_separated_integer_list
from django.shortcuts import render, redirect
from django.template.defaulttags import comment

from contact.forms import SubscriptionForm
from .models import Blog, Comment
from .forms import CommentForm


# Create your views here.


def index(request):
    return render(request, "index.html")


def blog(request):
    blog = Blog.objects.all()
    sub = SubscriptionForm(request.POST or None)
    if sub.is_valid():
        sub.save()
        return redirect(".")
    ctx = {
        "blogs": blog,
        'sub':sub
    }
    return render(request, 'blog.html', ctx)


def detail(request, pk):
    blog = Blog.objects.get(id=pk)
    comment = CommentForm(request.POST or None)
    if comment.is_valid():
        com = comment.save(commit=False)
        com.blog = blog
        com.save()
        return redirect(".")

    ctx = {
        "blog": blog,
        "comment": comment
    }
    return render(request, 'blog-single.html', ctx)
