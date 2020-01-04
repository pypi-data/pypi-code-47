from finances.models import Transaction, BudgetCategories, PaymentMethod
from finances.forms import TransactionFormValidation

from pandas import read_csv
import numpy as np
import logging

logger = logging.getLogger(__name__)


def is_valid_row(row, user, category_dict, payment_method_dict, transaction_object_list):

    if len(row) != 5:
        return False

    # Assign variables for rows
    date = row[0]
    amount = row[1]
    category = row[2]
    payment_method = row[3]
    notes = row[4]

    # Strip the dollar sign if it is there.
    if isinstance(amount, str):
        if amount[0] == "$":
            amount = float(amount[1:])

    if category in category_dict:
        category_pk = category_dict[category]
    else:
        return False

    if payment_method in payment_method_dict:
        payment_method_pk = payment_method_dict[payment_method]
    else:
        return False

    # Make the form for validation purposes
    transaction_form = TransactionFormValidation({
        "user": user.id,
        "date": date,
        "amount": amount,
        "category": category_pk,
        "payment_method": payment_method_pk,
        "notes": notes,
    })
    transaction_object_list.append(transaction_form)

    return transaction_form.is_valid()


def handle_transaction_upload(csv_file, user):

    # Build a hashmap of categories and payment maethods that maps to pk
    categories = user.budgetcategories_set.all()
    payment_methods = user.paymentmethod_set.all()

    category_dict = {}
    for category in categories:
        category_dict[category.category] = category.pk

    payment_method_dict = {}
    for payment_method in payment_methods:
        payment_method_dict[payment_method.payment_method] = payment_method.pk

    try:
        reader_df = read_csv(
            csv_file, sep=",", chunksize=100, engine="c",
            names=["date", "amount", "category", "payment_method", "notes"],
        )
    except:
        logger.warning("Iterator could not be created with the CSV file.")
        return False, "There was a problem while reading the CSV file. " \
                      "Please ensure that the correct file type was supplied."

    # Check all of the rows
    valid_file = True
    bad_row_list = []
    form_object_list = []
    try:
        for df in reader_df:
            for i, row in enumerate(df.itertuples(index=False)):
                # Is valid row will append form objects to the form_object_list param
                if not (is_valid_row(row, user, category_dict, payment_method_dict, form_object_list)):
                    valid_file = False
                    bad_row_list.append(i + 1)
    except:
        logging.exception(
            "CSV could not be read, improper format or file type.")
        return False, "There was a problem while reading the CSV file. " \
                      "Please ensure that the correct file type was supplied."
    if not valid_file:
        return False, "There was a problem in the way the CSV was formatted. Make sure that the " \
                      "CSV is formatted as in the example below, stripped of whitespace, and that " \
                      "the payment methods and type of charge are the same as your settings. " \
                      "The following rows had errors: {}".format(bad_row_list)

    # If the rows were all valid, then save all of the data
    for form_object in form_object_list:
        form_object.save()

    return True, "NA"
