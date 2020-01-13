from django.shortcuts import render
from django.http import Http404
from rest_framework import routers, serializers, viewsets
from sections.serializers import *
from django.core.paginator import Paginator
from common.views import BaseView
from .models import *
# from catalog.models import Category, Product
from django.shortcuts import get_object_or_404


class HomeView(BaseView):
    template_name = 'sections/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # categories = Category.get_active().filter(parent=None)
        context.update(
            categories='categories',
        )
        return context


class SectionView(BaseView):
    template_name = 'sections/article-detail.html'

    def get_context_data(self, **kwargs):
        context = super(SectionView, self).get_context_data(**kwargs)
        full_slug = kwargs.get('full_slug')
        # section = get_object_or_none(Section, full_slug=full_slug)
        article = get_object_or_404(Article.objects.select_related('template'), slug=full_slug, is_active=True)
        self.template_name = article.template.path
        breadcrumbs = [{'title': article.title, 'url': self.request.path}]

        if self.template_name == 'catalog/product-list.html':
            pass
            # products = Product.get_active()
            # page = self.request.GET.get('page')
            # products = Paginator(products, 3).get_page(page)
            # context.update(products=products)

        if self.template_name == 'sections/contact.html':
            pass
            # from feedback.forms import ContactForm
            # form = ContactForm()
            # context.update(form=form)

        # if not section and not article:
        #     raise Http404

        # context['news'] = Article.objects.filter(is_active=True, section__full_slug='blizhajshie-meropriyatiya').order_by('-date')[:4]
        # context['categories'] = Category.objects.filter(section_id=6, is_active=True, parent__isnull=True, on_main=True)[:4]
        # context['articles'] = Article.objects.filter(on_main=True).first()

        context.update(
            breadcrumbs=self.get_breadcrumbs(breadcrumbs),
            page=article,
        )
        return context


class SectionApiView(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
