from django.urls import path
from .views import articles_list_view

app_name = 'blog'
urlpatterns = [
    path('', articles_list_view, name="article-list"),
]