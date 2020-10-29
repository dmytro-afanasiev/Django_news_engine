from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings

from .forms import PersonalPreferencesForm
from .models import Category
from .models import News
from .models import History


# Create your views here.


def index(request):
    required_fields = ('title', 'description', 'published_at', 'url_to_image', 'slug')
    if request.user.is_anonymous:
        articles = News.objects.all().only(*required_fields)[:10]
    else:
        articles = News.objects.all().only(*required_fields).difference(request.user.checked_news.all().only(*required_fields)).order_by('-published_at')[:10]

    categories = Category.objects.filter(is_main=True).only('name', 'slug')
    return render(request, template_name='news/index.html', context={'categories': categories, 'articles': articles})

def category_news(request, slug):
    required_fields = ('title', 'description', 'published_at', 'url_to_image', 'slug')
    if request.user.is_anonymous:
        category_articles = News.objects.filter(category__slug=slug).only(*required_fields)[:10]
    else:
        category_articles = News.objects.filter(category__slug=slug).only(*required_fields).difference(request.user.checked_news.filter(category__slug=slug).only(*required_fields)).order_by('-published_at')[:10]
    categories = Category.objects.filter(is_main=True).only('name', 'slug')
    return render(request, template_name='news/index.html', context={'categories': categories, 'articles': category_articles, 'selected_category_slug': slug, 'selected_category_name': Category.objects.get(slug=slug).name})

class NewsDetail(DetailView):
    model = News
    context_object_name = 'article'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if not request.user.is_anonymous:
            History.objects.create(user=request.user, news=self.object)
        return response


class PersonalAccount(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        form = PersonalPreferencesForm()
        for category in user.categories.filter(is_main=True).only('slug'):
            form.initial[category.slug] = True
        form.initial['send_news_to_email'] = user.send_news_to_email
        return render(request, template_name='news/personal_account.html', context={'user': user, 'form': form})

    def post(self, request):
        user = request.user
        form = PersonalPreferencesForm(request.POST)
        if form.is_valid():
            categories = Category.objects.filter(slug__in=form.changed_data)
            user.categories.set(categories, clear=True)
            user.send_news_to_email = form.cleaned_data['send_news_to_email']
            user.save()
            messages.success(request, 'Дані успішно збережені!')
        return redirect('news:start')

