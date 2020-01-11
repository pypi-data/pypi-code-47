# coding: utf-8
from common.seo.models import ConfigSEO
from django import template

register = template.Library()


def replace_non_seo(line):
    replacements = ['=', '/', '!', '?', '*', u'«', u'»', ':', '<br>', '<', '>', '|', '+', '  ']
    for entity in replacements:
        line = line.replace(entity, ' ')
    return line


@register.inclusion_tag('meta_seo.html')
def meta_seo(obj=None, title=None, description=None, keywords=None):
    if not obj:
        """
        SEO of home page
        """
        try:
            title, keywords, description, h1 = ConfigSEO.objects.filter(group='home')
        except Exception as e:
            print(e)
    else:
        """
        SEO title
        """
        if obj and hasattr(obj, 'seo_title') and obj.seo_title:
            title = obj.seo_title
        elif obj.title:
            title = obj.title
        """
        SEO meta description
        """
        if obj and hasattr(obj, 'seo_description') and obj.seo_description:
            description = obj.seo_description
        # elif obj.title:
        #     title = obj.title
        """
        SEO meta keywords
        """
        if obj and hasattr(obj, 'seo_keywords') and obj.seo_keywords:
            keywords = obj.seo_keywords
        # elif obj.title:
        #     title = obj.title

    return dict(
        title=title,
        keywords=keywords,
        description=description,
    )

