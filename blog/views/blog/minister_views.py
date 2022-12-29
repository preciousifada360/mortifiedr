# Core Django imports.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
)

# Blog application imports.
from blog.models.article_models import Article


class MinisterArticlesListView(ListView):
    model = Article
    paginate_by = 12
    context_object_name = 'articles'
    template_name = 'blog/minister/minister_articles.html'

    def get_queryset(self):
        minister = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(minister=minister, status=Article.PUBLISHED, deleted=False)

    def get_context_data(self, **kwargs):
        context = super(MinisterArticlesListView, self).get_context_data(**kwargs)
        minister = get_object_or_404(User, username=self.kwargs.get('username'))
        context['minister'] = minister
        return context


class MinistersListView(ListView):
    model = User
    paginate_by = 12
    context_object_name = 'ministers'
    template_name = 'blog/ministers/ministers_list.html'

    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')
