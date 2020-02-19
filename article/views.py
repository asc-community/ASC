from django.shortcuts import render
from .models import Article
from django.http import Http404
from .processors import PostProcessor

class AuthorView:
    def __init__(self, author):
        self.name = author.username


class PostArticlePreview:
    CUT_TAG = "<cut/>"

    @staticmethod
    def cut(text):
        if PostArticlePreview.CUT_TAG in text:
            return text[:text.find(PostArticlePreview.CUT_TAG)]
        else:
            # TODO
            return ""

    def __init__(self, article):
        self.title = article.title
        self.brief = PostArticlePreview.cut(article.content)
        authors = article.authors.all()
        self.authors = []
        for author in authors:
            self.authors.append(AuthorView(author))
        self.link = "/articles/" + str(article.id) + "/" + str(article.slug)


def article_view(request, article_id, article_slug):
    try:
        article = Article.objects.get(id=article_id, slug=article_slug)
    except Article.DoesNotExist:
        raise Http404("404")
    context = {
        "title": article.title,
        "content": PostProcessor.process(article.content),
        "authors": [AuthorView(i) for i in article.authors.all()]
    }
    context["author_list"] = ", ".join([author.name for author in context["authors"]])

    if request.user.is_authenticated:
        context["edit_link"] = "/admin/article/article/" + str(article_id) + "/change"
    return render(request, "one_article_view_template.html", context)


def article_list_view(request):
    # TODO add paging
    # filter all published posts
    posts = Article.objects.filter(status="published")
    post_views = [PostArticlePreview(post) for post in posts]
    context = {
        "articles": post_views
    }
    return render(request, "article_list_view_template.html", context)
