from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# from catalog.models import Category, Product
from sections.models import Article, Section


class SectionMap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Section.objects.filter(in_sitemap=True).order_by('pk')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('sections:section', kwargs={'full_slug': obj.full_slug})


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Article.objects.filter(in_sitemap=True).order_by('-sort', 'pk')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('sections:section', kwargs={'full_slug': obj.full_slug})


# class CategorySitemap(Sitemap):
#     changefreq = "daily"
#     priority = 0.5
#
#     def items(self):
#         return Category.objects.filter(in_sitemap=True).order_by('-sort', 'pk')
#
#     def lastmod(self, obj):
#         return obj.updated_at
#
#     def location(self, obj):
#         return reverse('catalog:category', kwargs={'full_slug': obj.full_slug})
#
#
# class ProductSitemap(Sitemap):
#     changefreq = "daily"
#     priority = 0.5
#
#     def items(self):
#         return Product.objects.filter(in_sitemap=True).order_by('-sort', 'pk')
#
#     def lastmod(self, obj):
#         return obj.updated_at
#
#     def location(self, obj):
#         return reverse('catalog:category', kwargs={'full_slug': obj.slug})


SITEMAPS = dict(
    sections=SectionMap,
    articles=ArticleSitemap,
    # categories=CategorySitemap,
    # products=ProductSitemap
)
