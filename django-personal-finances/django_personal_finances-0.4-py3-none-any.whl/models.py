from django.db import models
from django.utils import timezone

import datetime

from users.models import User


BUDGET_TYPES_CHOICES = [
    ('Annual', 'Annual'),
    ('Monthly', 'Monthly'),
]


class BudgetCategories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(verbose_name="budget Category", max_length=100)
    amount = models.FloatField(verbose_name="category Amount")
    category_type = models.CharField(
        verbose_name="category Type",
        max_length=7,
        choices=BUDGET_TYPES_CHOICES
    )

    def __str__(self):
        return f'{self.category}'


class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.payment_method}'


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField()
    category = models.ForeignKey(BudgetCategories, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    notes = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
