from django.shortcuts import render

from articles.models import Article, Scope, Tag


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    article = Article.objects.order_by(ordering)
    print(article[0].scope.all())
    context = {'object_list':article}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    return render(request, template, context)
