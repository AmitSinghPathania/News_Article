from django.db import models

class Keyword(models.Model):
    keyword = models.CharField(max_length=255)

class Search(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    search_time = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    publication_date = models.DateTimeField()
    search = models.ForeignKey(Search, on_delete=models.CASCADE)
