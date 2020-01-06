from django.conf import settings
from django.templatetags.static import static
from django.utils.html import format_html

from wagtail.core import hooks

@hooks.register('insert_editor_css')
def editor_css():
    if not 'WAGTAILUIPLUS_ENHANCE_STREAM_FIELD' in settings \
            or settings.WAGTAILUIPLUS_ENHANCE_STREAM_FIELD:
        return format_html((
                '<link rel="stylesheet" href="{}">'
                '<link rel="stylesheet" href="{}">'
            ),
            static('css/wagtailuiplus.css'),
            static('css/wagtailuiplus-stream-field.css')
        )
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('css/wagtailuiplus.css')
    )

@hooks.register('insert_editor_js')
def editor_js():
    if not 'WAGTAILUIPLUS_ENHANCE_STREAM_FIELD' in settings \
            or settings.WAGTAILUIPLUS_ENHANCE_STREAM_FIELD:
        return format_html((
                '<script src="{}"></script>',
                '<script src="{}"></script>',
            ),
            static('js/wagtailuiplus.js'),
            static('js/wagtailuiplus-stream-field.js')
        )
    return format_html(
        '<script src="{}"></script>',
        static('js/wagtailuiplus.js')
    )
