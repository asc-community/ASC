from django.urls import path
from .views import article_view

urlpatterns = [
    path("articles/<int:article_id>/<str:article_slug>", article_view, name="article")
]