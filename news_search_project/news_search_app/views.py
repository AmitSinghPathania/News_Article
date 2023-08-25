from django.shortcuts import render
from .models import Keyword, Search, Article
from .utils import fetch_articles


def search_articles(request):
    # if request.method == "GET":
    #     keyword_text = request.POST.get("keyword")
    #     keyword, created = Keyword.objects.get_or_create(keyword=keyword_text)
    #
    #     search = Search.objects.create(keyword=keyword)
    #     articles = fetch_articles(keyword_text)
    #
    #     for article_data in articles:
    #         Article.objects.create(
    #             title=article_data["title"],
    #             url=article_data["url"],
    #             publication_date=article_data["publishedAt"],
    #             search=search
    #         )

        return render(request, "search.html")


def results(request):
    searches = Search.objects.all()
    return render(request, "results.html", {"searches": searches})

def show(request):
    return render(request,"show.html")