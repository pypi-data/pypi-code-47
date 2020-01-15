from modeltranslation.translator import register, TranslationOptions
from .models import MenuItem


@register(MenuItem)
class MenuItemTrans(TranslationOptions):
    # fields = ['title']
    pass