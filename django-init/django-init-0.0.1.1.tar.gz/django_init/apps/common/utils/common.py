# # -*- coding: utf-8 -*-
#
# from urllib.parse import quote_plus
#
# from django.utils.datetime_safe import datetime
# from django.utils.deconstruct import deconstructible
# import os
# import random
# import urllib.request
# import xmltodict
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from pytils.translit import translify, slugify
# from dateutil import parser
# from django.conf import settings
#
#
# def add_slash_right(url):
#     return url + '/' if url and not url.endswith('/') else url
#
#
# def add_slash_left(url):
#     return '/' + url if url and not url.startwith('/') else url
#
#
# def get_date_or_none(value, formats):
#     if not formats:
#         formats = '%Y-%m-%dT%H:%M:%S.%fZ'
#     try:
#         return datetime.strptime(value, formats).date() if value else None
#     except ValueError:
#         return None
#
# def add_slashes(path):
#     return '/' + path.lstrip('/').rstrip('/') + '/' if path and path != '/' else path
#
# def float0(st):
#     try:
#         return float(st)
#     except ValueError:
#         return 0.0
#
#
# @deconstructible
# class UploadPath(object):
#     def __init__(self, sub_path):
#         self.path = sub_path  # + datetime.now().strftime('/%Y/%m')
#
#     def __call__(self, instance, filename):
#         name, ext = os.path.splitext(filename)
#         filename = '{}{}'.format(slugify(translify(name)), ext)
#         return os.path.join(self.path, instance._meta.app_label, filename)
#
#
# def get_object_or_none(model, *args, **kwargs):
#     try:
#         return model.objects.get(*args, **kwargs)
#     except model.DoesNotExist:
#         return None
#
#
# def get_or_none(queryset):
#     return queryset[0] if queryset else None
#
#
# def get_date_none(value):
#     return parser.parse(value, dayfirst=True) if value else None
#
#
# def unicode_to_int(value):
#     try:
#         value = int(value)
#     except ValueError:
#         value = 0
#     return value
#
#
# def get_images_from_path(path):
#     types = ('jpg', 'png', 'jpeg')
#     try:
#         abspath = os.path.join(settings.MEDIA_ROOT, path)
#         if not os.path.exists(os.path.dirname(abspath)):
#             os.makedirs(os.path.dirname(abspath))
#         listdir = os.listdir(abspath)
#         # m = os.path.join(MEDIA_URL, path)
#         images = [os.path.join(path, x) for x in listdir if x.lower().endswith(types)]
#         images = sorted(images) if len(images) > 1 else images
#     except Exception:
#         return None
#     return images
#
#
# def replace_list(line, replacements):
#     #  replacements = [(u"Белгород и область", u"Белгород"), (u"- ", u"-"), (u"-N ", u"")]
#     for entity, replacement in replacements:
#         line = line.replace(entity, replacement)
#     return line
#
#
# # Преобразование в int избегая `Exception`
# def to_int_or_none(value):
#     if value == "" or value is None:
#         return None
#     try:
#         value = int(value)
#     except ValueError:
#         return None
#     return value
#
#
# def x_str(s):
#     return '' if s is None else str(s)  # convert None to empty string
#
#
# def int_def(st, default=0):
#     try:
#         return int(st) if st else default
#     except ValueError:
#         return default
#
#
# # -------------- GET ALL PARAMS IN LIST --------------
# def get_url_params_in_list(new_params, param_list):
#     if not new_params: return ''
#     param = []
#     for key in new_params.keys():
#         if key in param_list:
#             if '[]' in key:
#                 valuelist = new_params.getlist(key)
#                 param.extend(['%s=%s' % (key, val) for val in valuelist])
#             else:
#                 value = new_params.get(key)
#                 param.append('%s=%s' % (key, value))
#
#     s = '&'.join(sorted(param))  # s = urlencode(param, True)
#     return '?%s' % s if s else ''
#
#
# def random_digit_challenge():
#     ret = u''
#     for i in range(4):
#         ret += str(random.randint(0, 9))
#     return ret, ret
#
#
# def paginate(query_set, page_size, page_num):
#     paginator = Paginator(query_set, page_size)
#     try:
#         page = paginator.page(page_num)
#     except PageNotAnInteger:
#         page = paginator.page(1)  # If page is not an integer, deliver first page.
#     except EmptyPage:  # If page is out of range (e.g. 9999), deliver last page of results.
#         page = paginator.page(paginator.num_pages)
#
#     return page
#
#
# def get_ymap_coordinates(arg):  # arg - full address for location
#     try:
#         f = urllib.request.urlopen('http://geocode-maps.yandex.ru/1.x/?geocode=' + quote_plus(arg) + '&results=1')
#         data = f.read()
#         f.close()
#         data = xmltodict.parse(data)
#         longitude, latitude = data['ymaps']['GeoObjectCollection']['featureMember']['GeoObject']['Point']['pos'].split()
#     except KeyError:
#         return '', ''
#     return longitude, latitude
#
#
# def hms_string(sec_elapsed):
#     h = int(sec_elapsed / (60 * 60))
#     m = int((sec_elapsed % (60 * 60)) / 60)
#     s = sec_elapsed % 60.
#     return "{}:{:>02}:{:>05.2f}".format(h, m, s)
#
#
# def set_last_page(request, context, value):
#     if 'prev_page' not in request.session:
#         request.session['prev_page'] = ''
#
#     if 'last_page' in request.session:
#         if not value == request.session['last_page']:
#             request.session['prev_page'] = request.session['last_page']
#             request.session['last_page'] = value
#             context['last_page'] = request.session['last_page']
#     context['prev_page'] = request.session['prev_page']
#     return context
