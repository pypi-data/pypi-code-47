# Django Imports
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.utils import timezone
from django.contrib import messages
from django.views.generic.dates import MonthArchiveView
from django.db.models import Sum
from django.db.models.functions import Coalesce

# Standard Library
import json
from pprint import pprint

# Project
from finances.forms import TransactionForm, TransactionFormValidation, BudgetCategoriesForm, \
    PaymentMethodForm, UploadTransactionsForm
from finances.models import BudgetCategories, PaymentMethod, Transaction
from finances.helpers.upload_transactions import handle_transaction_upload
import finances.helpers.reports as h_reports
from users.models import User

# External Dependencies
from crispy_forms.utils import render_crispy_form


def home(request):
    return render(request, "finances/index.html")


@login_required
def add_budget_categories(request):

    if request.POST:

        budget_categories_form = BudgetCategoriesForm(data=request.POST)

        if budget_categories_form.is_valid():
            user = User(id=request.user.id)

            budget_category = BudgetCategories(
                user=user,
                category=budget_categories_form.cleaned_data["category"],
                amount=budget_categories_form.cleaned_data["amount"],
                category_type=budget_categories_form.cleaned_data["category_type"]
            )
            budget_category.save()

            return redirect(request.path_info)
    else:
        user = User.objects.get(pk=request.user.id)
        budget_categories = user.budgetcategories_set.all()

        form = BudgetCategoriesForm()

        context = {
            "budget_categories": budget_categories,
            "form": form,
        }

    return render(request, "finances/add_budget_categories.html", context)


@login_required
def add_payment_methods(request):

    form = PaymentMethodForm()

    user = User(id=request.user.id)
    payment_methods = user.paymentmethod_set.all()

    context = {
        "form": form,
        'payment_methods': payment_methods,
    }

    return render(request, "finances/add_payment_methods.html", context)


@login_required
def save_payment_methods_form(request):

    form = PaymentMethodForm(request.POST or None)

    if form.is_valid():

        user = User(id=request.user.id)

        payment_method = PaymentMethod(
            user=user,
            payment_method=form.cleaned_data['payment_method'],
        )

        payment_method.save()

        response = {
            'success': True,
            'payment_methods_last': payment_method.payment_method,
        }

        return JsonResponse(response)

    # Make sure the csrf token is in the newly rendered form
    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)

    return JsonResponse({'success': False, 'form_html': form_html})


@login_required
def add_transactions(request):

    user = User(id=request.user.id)
    transactions = user.transaction_set.filter(
        created__lte=timezone.now()
    ).order_by('-created')[:5]

    form = TransactionForm(user)

    context = {
        "form": form,
        "transactions": transactions,
    }

    return render(request, "finances/add_transactions.html", context=context)


@login_required
def save_transaction_form(request):

    user = User(id=request.user.id)

    # Get the transaction data from POST request
    date = request.POST.get("date", None)
    amount = request.POST.get("amount", None)
    category = request.POST.get("category", None)
    payment_method = request.POST.get("payment_method", None)
    notes = request.POST.get("notes", None)

    form = TransactionForm(user, request.POST)

    if form.is_valid():

        transaction = Transaction(
            user=user,
            date=form.cleaned_data['date'],
            amount=form.cleaned_data['amount'],
            category=form.cleaned_data['category'],
            payment_method=form.cleaned_data['payment_method'],
            notes=form.cleaned_data['notes'],
        )

        transaction.save()

        # Rerender the form to replace old error messages
        ctx = {}
        # Make sure the csrf token is in the newly rendered form
        ctx.update(csrf(request))
        form = TransactionForm(user)  # Reinitialize the form to make it blank
        form_html = render_crispy_form(form, context=ctx)

        response = {
            'success': True,
            # A bit of a hacky workaround to avoid cross-platform errors
            'date': transaction.date.strftime("%b. FILL, %Y").replace("FILL", str(transaction.date.day)),
            'amount': transaction.amount,
            # Category and payment method are stored as objects, so
            # we need to get the actual values
            'category': transaction.category.category,
            'payment_method': transaction.payment_method.payment_method,
            'notes': transaction.notes,
            'form_html': form_html
        }

        return JsonResponse(response)

    # If there were errors in the form, rerender it with error messages.
    ctx = {}
    # Make sure the csrf token is in the newly rendered form
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)

    return JsonResponse({'success': False, 'form_html': form_html})


@login_required
def upload_transactions(request):

    if request.method == 'POST':
        form = UploadTransactionsForm(request.POST, request.FILES)
        if form.is_valid():
            success, error_message = handle_transaction_upload(
                csv_file=request.FILES['file'],
                user=User(id=request.user.id),
            )

            if success:
                messages.success(request, "File Uploaded!")
                return redirect('finances-home')
            else:
                messages.error(
                    request, error_message,
                    extra_tags='danger'
                )
                return redirect('finances-upload_transactions')
        else:
            messages.error(
                request, "There was an error in the file upload.",
                extra_tags='danger'
            )
            return redirect('finances-upload_transactions')
    else:
        form = UploadTransactionsForm()

    return render(request, 'finances/upload_transactions.html', {'form': form})


class TransactionMonthlyArchiveView(MonthArchiveView):
    queryset = Transaction.objects.all().order_by('-date')
    template_name = 'finances/historic_transactions.html'
    date_field = "date"


def reports(request):

    current_time = timezone.now()
    # year = current_time.year
    # month = current_time.month

    year = current_time.year
    month = 7  # CHANGE THIS AFTER TESTING

    sum_groupby_category_annual = Transaction.objects.filter(date__year__gte=year,
                                                             date__year__lte=year).values('category').order_by('category').annotate(total_amount=Sum('amount'))
    annual_results = [h_reports.ReportQueryResults(annual_dict, "Annual")
                      for annual_dict in sum_groupby_category_annual]

    sum_groupby_category_month = Transaction.objects.filter(date__year__gte=year,
                                                            date__month__gte=month,
                                                            date__year__lte=year,
                                                            date__month__lte=month).values('category').order_by('category').annotate(total_amount=Sum('amount'))
    month_results = [h_reports.ReportQueryResults(month_dict, "Monthly")
                     for month_dict in sum_groupby_category_month]

    context = {
        "results": list(zip(annual_results, month_results))
    }

    print(len(annual_results), len(month_results))
    return render(request, "finances/reports.html", context)
