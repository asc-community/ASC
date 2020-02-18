from django.shortcuts import render
from .models import Article
from django.http import Http404


class PostArticleView:
    CUT_TAG = "<cut/>"

    @staticmethod
    def cut(text):
        if PostArticleView.CUT_TAG in text:
            return text[:text.find(PostArticleView.CUT_TAG)]
        else:
            # TODO
            return ""

    def __init__(self, article):
        self.title = article.title
        self.brief = PostArticleView.cut(article.content)
        self.author_name = str(article.author_id)
        self.link = "/articles/" + str(article.id) + "/" + str(article.slug)


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


def article_list_view(request):
    # TODO
    posts = Article.objects.all()
    post_views = [PostArticleView(post) for post in posts]
    context = {
        "articles": post_views
    }
    return render(request, "article_list_view_template.html", context)
