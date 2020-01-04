from django.contrib import admin
from finances.models import BudgetCategories, Transaction

# Register your models here.
admin.site.register(BudgetCategories)
admin.site.register(Transaction)
