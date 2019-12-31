#
# Copyright (c) 2018, Grigoriy Kramarenko
# All rights reserved.
# This file is distributed under the BSD 3-Clause License.
#
"""
Функционал для поиска, сортировки и сериализации данных из моделей и передачи
их представлениям.
"""
from functools import reduce
from logging import getLogger
from operator import or_ as OR

from django.core.exceptions import ValidationError, FieldError
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q, CharField
from django.forms.forms import BaseForm
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import _get_queryset
from django.views.generic import TemplateView

from djangokit.serializers import ObjectSerializer


class Controller:
    """
    Filtering, ordering and pagination controller for QuerySet.
    """
    model = None
    search_fields = None
    ordering_fields = None
    filtering_fields = None
    exclude_fields = ('password',)
    select_related = None
    prefetch_related = None
    serializer = None
    use_distinct = False

    def __init__(self, model=None, search_fields=None, ordering_fields=None,
                 filtering_fields=None, exclude_fields=None, serializer=None,
                 select_related=None, prefetch_related=None):
        if model:
            self.model = model
        else:
            model = self.model
        meta = model._meta
        if search_fields is not None:
            self.search_fields = search_fields
        if ordering_fields is not None:
            self.ordering_fields = ordering_fields
        if filtering_fields is not None:
            self.filtering_fields = filtering_fields
        if exclude_fields is not None:
            self.exclude_fields = exclude_fields
        if select_related is not None:
            self.select_related = select_related
        if prefetch_related is not None:
            self.prefetch_related = prefetch_related
        exclude = self.exclude_fields
        fields = [f for f in meta.fields if f.name not in exclude]
        if meta.many_to_many:
            fields.extend([
                f for f in meta.many_to_many if f.name not in exclude
            ])
        self.fields = fields
        if self.serializer is None:
            self.serializer = (
                serializer or ObjectSerializer(model=model, exclude=exclude)
            )
        if isinstance(self.serializer, type):
            self.serializer = self.serializer(model=model, exclude=exclude)
        # Устанавливаем логгер.
        if self.__class__.__module__ != __name__:
            orig_name = 'djangokit.Controller.' + str(self)
        else:
            orig_name = 'djangokit.Controller'
        self.logger = getLogger(orig_name + '(' + str(meta) + ')')

    def __str__(self):
        cls = self.__class__
        return cls.__module__ + '.' + cls.__name__

    def get_queryset(self):
        qs = _get_queryset(self.model)
        if self.select_related:
            qs = qs.select_related(*self.select_related)
        if self.prefetch_related:
            qs = qs.prefetch_related(*self.prefetch_related)
        return qs

    def get_search_fields(self):
        if self.search_fields is None:
            fields = [f.name for f in self.fields if isinstance(f, CharField)]
            # Search by models without text fields.
            if not fields:
                exclude = self.exclude_fields
                for field in self.fields:
                    rel = field.related_model
                    if rel:
                        prefix = field.name + '__%s'
                        for f in rel._meta.fields:
                            if isinstance(f, CharField):
                                fname = prefix % f.name
                                if fname not in exclude:
                                    fields.append(fname)
            self.search_fields = fields
        return self.search_fields

    def get_ordering_fields(self):
        if self.ordering_fields is None:
            self.ordering_fields = [f.name for f in self.fields if
                                    not f.related_model]
        return self.ordering_fields

    def get_filtering_fields(self):
        if self.filtering_fields is None:
            self.filtering_fields = [f.name for f in self.fields]
            self.filtering_fields += [
                rel.name for rel in self.model._meta.related_objects
            ]
        return self.filtering_fields

    def ordering(self, queryset, ordering):
        """
        Функция проверяет параметры сортировки и применяет только допустимые.
        """
        logger = self.logger
        fields = self.get_ordering_fields()
        if not fields:
            logger.debug('%s has no fields for ordering', self)

        if not ordering or not fields:
            # Fix UnorderedObjectListWarning:
            if not getattr(queryset, 'ordered', True):
                queryset = queryset.order_by('pk')
            return queryset, []

        def valid(x):
            v = bool(
                x and not x.startswith('--') and
                x.lstrip('-') in fields
            )
            if not v:
                logger.debug('invalid ordering field: %s', x)
            return v

        if isinstance(ordering, str):
            if ordering.startswith('[') and ordering.endswith(']'):
                ordering = ordering[1:-1]
            ordering = ordering.split(',')
        ordering = [x for x in ordering if valid(x)]
        if ordering:
            queryset = queryset.order_by(*ordering)
            logger.debug('ordering by %s', ordering)
        return queryset, ordering

    def search(self, queryset, query):
        """
        Фильтрует набор данных поиском по запросу.
        """
        logger = self.logger

        fields = self.get_search_fields()

        def construct_search(field_name):
            if field_name.startswith('^'):
                return "%s__istartswith" % field_name[1:]
            elif field_name.startswith('='):
                return "%s__iexact" % field_name[1:]
            elif field_name.startswith('@'):
                return "%s__search" % field_name[1:]
            else:
                return "%s__icontains" % field_name

        if fields and query not in ('', None, False, True):
            lookups = [construct_search(str(f)) for f in fields]
            for bit in query.split():
                queries = [Q(**{lookup: bit}) for lookup in lookups]
                queryset = queryset.filter(reduce(OR, queries))
            logger.debug('search "%s" by %s', query, lookups)

        return queryset

    def filtering(self, queryset, filters):
        """Фильтрует набор данных."""
        logger = self.logger

        if not filters:
            return queryset, {}

        fields = self.get_filtering_fields()

        def test_filtered(field):
            return field.split('__')[0] in fields

        def test_inverse(s):
            return s.startswith('-')

        def test_bool(s, v):
            return s.endswith('__isnull') or v in ('true', 'false')

        def test_list(s):
            return s.endswith('__in') or s.endswith('__range')

        applied = {}

        for field, query in filters.items():
            if field == 'q':
                queryset = self.search(queryset, query)
                applied[field] = query
                continue

            if test_inverse(field):
                field = field[1:]
                func = queryset.exclude
            else:
                func = queryset.filter

            if not test_filtered(field):
                logger.debug('field %s not filtered', field)
                continue

            if isinstance(query, str):
                if query.startswith('[') and query.endswith(']'):
                    query = [x for x in query[1:-1].split(',') if x]
                    if not query:
                        continue
                elif test_list(field):
                    query = [x for x in query.split(',') if x]
                    if not query:
                        continue
                elif query == 'null':
                    query = None
                elif test_bool(field, query):
                    query = bool(query == 'true')
            try:
                queryset = func(Q(**{field: query}))
            except (ValueError, ValidationError, FieldError):
                pass
            else:
                applied[field] = query

        return queryset, applied

    def pagination(self, queryset, limit, page):
        """Возвращает пагинатор и страницу для набора данных."""
        paginator = Paginator(queryset, limit)
        try:
            page = paginator.page(page)
        except EmptyPage:
            self.logger.debug('page %s is empty', page)
            page = paginator.page(1)
        return paginator, page

    def distinct(self, queryset):
        query = queryset.query
        fields = query.extra_order_by or query.order_by
        meta = query.get_meta()
        if not fields and query.default_ordering:
            fields = meta.ordering
        fields = [f.lstrip('-') for f in fields]
        pk = meta.pk.name
        fields = [f for f in fields if f != pk]
        queryset = queryset.distinct(pk, *fields)
        self.logger.debug('distinct by %s', fields)
        return queryset

    def get(self, request, queryset=None, page=1, limit=100, max_limit=1000):
        """
        Подготавливает запрос и возвращает страницу, заказы и фильтры.
        """
        logger = self.logger
        data = request.GET.dict()
        if queryset is None:
            queryset = self.get_queryset()
        else:
            assert self.model == queryset.model
        if 'p' in data:
            _p = data.pop('p')
            try:
                page = int(_p)
            except ValueError:
                logger.debug('invalid page "%s" in request', _p)
                pass
        if 'l' in data:
            _l = data.pop('l')
            try:
                limit = int(_l)
            except ValueError:
                logger.debug('invalid limit "%s" in request', _l)
                pass
        if limit > max_limit:
            logger.debug('limit "%s" changed to max "%s"', limit, max_limit)
            limit = max_limit
        if 'o' in data:
            queryset, orders = self.ordering(queryset, data.pop('o'))
        else:
            orders = []
        if self.use_distinct:
            queryset = self.distinct(queryset)
        queryset, filters = self.filtering(queryset, data)
        logger.debug('%s', queryset.query)
        paginator, page = self.pagination(queryset, limit, page)
        return page, orders, filters

    def get_serialized(self, *args, **kwargs):
        serializer = kwargs.pop('serializer', None)
        page, orders, filters = self.get(*args, **kwargs)
        page = self.serialize_page(page, serializer)
        return page, orders, filters

    def serialize_page(self, page, serializer):
        if serializer is None:
            serializer = self.serializer
        paginator = page.paginator
        return {
            'objects': [serializer(obj) for obj in page.object_list],
            'number': page.number,
            'limit': paginator.per_page,
            'count': paginator.count,
            'pages': paginator.num_pages,
        }


class ControlModelView(TemplateView):
    template_name = None
    ctrl = None
    form = None
    redirect_after_add = None
    limit = 100
    max_limit = 1000

    def __init__(self, *args, **kwargs):
        ctrl = self.ctrl
        assert isinstance(ctrl, Controller)
        self.model = ctrl.model
        assert issubclass(self.form, BaseForm)
        return super().__init__(*args, **kwargs)

    def get_default_context(self):
        return {}

    def add_form_to_context(self, request, instance, context):
        Form = self.form
        kw = {'instance': instance}
        if hasattr(Form, 'request'):
            kw['request'] = request
        if request.method == 'POST':
            kw['files'] = request.FILES
            context['form'] = form = Form(request.POST, **kw)
            if form.is_valid():
                context['instance'] = form.save()
        else:
            context['form'] = Form(**kw)
        return context

    def make_context(self, request, id):
        ctx = self.get_default_context()
        extra = self.extra_context
        if extra:
            ctx.update(extra)
        if id:
            instance = get_object_or_404(self.model, id=id)
        else:
            instance = None
            page, orders, filters = self.ctrl.get(
                request, limit=self.limit, max_limit=self.max_limit,
            )
            ctx.update({
                'page': page,
                'orders': orders,
                'orders_string': ','.join(orders) if orders else '',
                'filters': filters,
            })
            ctx['next'] = request.path
        ctx['model'] = self.model
        ctx['ctrl'] = self.ctrl
        ctx['instance'] = instance
        self.add_form_to_context(request, instance, ctx)
        return ctx

    def get(self, request, id=None):
        ctx = self.make_context(request, id)
        if 'next' in request.GET:
            ctx['next'] = request.GET['next']
        return self.render_to_response(ctx)

    def post(self, request, id=None):
        ctx = self.make_context(request, id)
        form = ctx['form']
        is_valid = form.is_bound and not form._errors
        if not is_valid:
            return self.render_to_response(ctx)
        to = request.POST.get('next')
        if to:
            return redirect(to)
        instance = ctx.get('instance')
        if instance and id is None and self.redirect_after_add:
            return redirect(self.redirect_after_add, id=instance.id)
        if instance and hasattr(instance, 'get_absolute_url'):
            return redirect(instance.get_absolute_url())
        return self.render_to_response(ctx)
