from django import forms
from finances.models import Transaction, BudgetCategories, PaymentMethod
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class TransactionForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(
            queryset=user.budgetcategories_set.all()
        )
        self.fields['payment_method'] = forms.ModelChoiceField(
            queryset=user.paymentmethod_set.all()
        )

    class Meta:
        model = Transaction
        fields = (
            "date",
            "amount",
            "category",
            "payment_method",
            "notes",
        )   # NOTE: the trailing comma is required


class TransactionFormValidation(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = (
            "user",
            "date",
            "amount",
            "category",
            "payment_method",
            "notes",
        )


class BudgetCategoriesForm(forms.ModelForm):
    class Meta:
        model = BudgetCategories
        fields = (
            "category",
            "amount",
            "category_type",
        )


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = (
            "payment_method",
        )


class UploadTransactionsForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'accept':'text/csv; charset=utf-8'}))
