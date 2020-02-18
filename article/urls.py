from django.urls import path
from .views import article_view, article_list_view

urlpatterns = [
    path("articles/", article_list_view, name="article_list"),
    path("articles/<int:article_id>/<str:article_slug>", article_view, name="article"),
]

