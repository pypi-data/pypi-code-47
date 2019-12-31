#
# Copyright (c) 2019, Grigoriy Kramarenko
# All rights reserved.
# This file is distributed under the same license as the current project.
#
from django.forms.fields import BooleanField, NullBooleanField
from django.template import Library
from django.utils.encoding import force_text
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe


register = Library()


@register.filter
def form_group(bound):
    """
    Formed HTML for visible fields of a forms (boundfield).
    """
    field = bound.field
    if field.__class__.__name__ == 'ReCaptchaField':
        return mark_safe('<div>' + force_text(bound) + '</div>')
    is_nullbool = isinstance(field, NullBooleanField)
    is_checkbox = not is_nullbool and isinstance(field, BooleanField)
    if is_checkbox:
        html = (
            '<div class="form-group %(error_class)s">'
            '<div class="checkbox">'
            '<label>%(widget)s %(label)s</label>'
            '%(errors)s'
            '%(help)s'
            '</div>'
            '</div>'
        )
    elif field.required:
        html = (
            '<div class="form-group %(error_class)s">'
            '<strong>%(label)s</strong>'
            '%(widget)s'
            '%(errors)s'
            '%(help)s'
            '</div>'
        )
    else:
        html = (
            '<div class="form-group %(error_class)s">'
            '%(label)s'
            '%(widget)s'
            '%(errors)s'
            '%(help)s'
            '</div>'
        )
    kw = {'error_class': '', 'errors': '', 'help': ''}
    if is_checkbox:
        kw['widget'] = force_text(bound)
        kw['label'] = force_text(bound.label)
    else:
        widget = field.widget
        attrs = widget.attrs
        input_type = getattr(widget, 'input_type', None)
        skip_types = ('hidden', 'file', 'checkbox', 'select', 'radio')
        if 'placeholder' not in attrs and input_type not in skip_types:
            attrs['placeholder'] = force_text(bound.label)
        classes = [c for c in attrs.get('class', '').split(' ') if c]
        if 'form-control' not in classes:
            classes.insert(0, 'form-control')
        attrs['class'] = ' '.join(classes)
        kw['widget'] = bound.as_widget(attrs=attrs)
        kw['label'] = bound.label_tag()
    if bound.errors:
        kw['error_class'] = 'text-danger'
        errors = bound.errors.as_data()
        kw['errors'] = format_html(
            '<ul class="text-danger mt-2">{}</ul>',
            format_html_join('', '<li>{}</li>', [e for e in errors])
        )
    if bound.help_text:
        kw['help'] = '<small class="form-text text-muted">%s</small>' % bound.help_text
    return mark_safe(html % kw)
