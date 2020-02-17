from django.shortcuts import render
from .models import Article
from django.http import Http404


def article_view(request, article_id, article_slug):
    try:
        article = Article.objects.get(id=article_id, slug=article_slug)
    except Article.DoesNotExist:
        raise Http404("404")
    context = {
        "title": article.title,
        "content": article.content,
    }
    if request.user.is_authenticated:
        context["edit_link"] = "/admin/article/article/" + str(article_id) + "/change"
    return render(request, "one_article_view_template.html", context)
