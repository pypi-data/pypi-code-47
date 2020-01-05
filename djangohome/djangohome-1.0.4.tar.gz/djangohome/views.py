from itertools import chain
from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from republictime.articles import Article


# Create your homepage views here.
class HomePageView(View):
    template_name = "djangoadmin/djangohome/homepage_view.html"

    def get(self, request, *args, **kwargs):
        article = Article('djangoarticle', settings.APIKEY, settings.RTAPI_URL)
        post = Article('djangopost', settings.APIKEY, settings.RTAPI_URL)
        article_promoted = article.get_article(promoted=True, trending=None)
        post_promoted = post.get_article(promoted=True, trending=None)
        article_promo = article.get_article(promoted=True, trending=True)
        post_promo = post.get_article(promoted=True, trending=True)
        promo = sorted(chain(article_promo, post_promo), key=lambda instance: instance['serial'], reverse=True)
        article_trending = article.get_article(promoted=None, trending=True)
        post_trending = post.get_article(promoted=None, trending=True)
        is_trending = sorted(chain(article_trending, post_trending), key=lambda instance: instance['serial'], reverse=True)
        context = {"article_filter": article_promoted, "is_promoted": post_promoted, "promo": promo, "is_trending": is_trending}
        return render(request, self.template_name, context)
