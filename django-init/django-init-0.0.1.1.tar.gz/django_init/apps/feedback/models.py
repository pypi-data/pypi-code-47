# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

SUBJ_CALL = 1
SUBJ_ORDER = 2
SUBJ_QST = 3
SUBJECTS = (
    (SUBJ_CALL, 'Заказать звонок'),
    (SUBJ_ORDER, 'Оставить заявку'),
    (SUBJ_QST, 'Задайте нам вопрос'),
)


class AbsCreatedAt(models.Model):
    created_at = models.DateTimeField('Дата изменения', auto_now_add=True)
    updated_at = models.DateTimeField('Дата создания', auto_now=True)

    class Meta:
        abstract = True


class AbsActive(models.Model):
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        abstract = True


class Feedback(AbsCreatedAt):
    subject = models.PositiveSmallIntegerField('Тема обращения', choices=SUBJECTS)
    is_new = models.BooleanField('Новое?', default=True)

    product = models.CharField('Товар', max_length=255, blank=True)
    file = models.FileField(upload_to='uploads/', blank=True)
    name = models.CharField('Имя', max_length=255, blank=True)
    phone = models.CharField('Телефон', max_length=255, blank=True)
    email = models.EmailField('E-mail', max_length=255, blank=True)
    message = models.TextField('Сообщение', blank=True)

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'
        db_table = 'feedback_feedback'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @classmethod
    def get_new(cls):
        return cls.objects.filter(is_new=True)


class FeedConfig(AbsCreatedAt, AbsActive):
    subject = models.PositiveSmallIntegerField('Тема обращения', choices=SUBJECTS)
    email = models.TextField('E-mail', blank=True, help_text='E-mail адреса получателей через запятую')
    email_subject = models.TextField('Тема письма', blank=True)
    email_message = models.TextField('Сообщение', blank=True)

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
        db_table = 'feedback_config'

    # @classmethod
    # def get_message(cls, keylock):
    #     ns_filter = cls.objects.filter(keylock=keylock)
    #     return ns_filter[0] if ns_filter.count() > 0 else None
    #
    # @classmethod
    # def get_data(cls, keylock):
    #     ns_filter = cls.objects.filter(keylock=keylock)
    #     return ns_filter[0] if ns_filter.count() > 0 else None
    #
    # @classmethod
    # def get_msg_result(cls, keylock=None, data=None):
    #     feed = cls.get_data(keylock)
    #     emails = feed.email if feed else ''
    #     subject = render_message(feed.subject, data) if feed else MSG_NEW
    #     message = render_message(feed.message, data) if feed else MSG_SENT if not keylock == 'BS' else MSG_SENT_BS
    #     return {'result_message': message, 'subject': subject, 'emails': emails}
