from django.shortcuts import render
from .models import Article


def articles_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "blog/article_list.html", context)
