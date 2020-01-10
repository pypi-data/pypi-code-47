import click
import requests
from .api import LmsApi, InvalidRequest
from tritise import Tritise

def gotify(url, token, title, message, prio=2):
    resp = requests.post(url,
        params = {'token': token},
        json={
            "message": message,
            "priority": prio,
            "title": title
        }
    )

@click.command()
@click.option('--database', '-d', default='lms-prepaid.sqlite', envvar='LMS_PREPAID_DATABASE')
@click.option('--card', '-c', required=True, help='The number of the prepaid card (AB-CDE-123456-X)', envvar='LMS_PREPAID_CARD')
@click.option('--quiet', '-q', help='Only print the amount, nothing else', is_flag=True)
@click.option('--currency/--no-currency', ' /-R', help='Print the currency the amount is in', default=True)
@click.option('--gotify-url', '-g', default=None, envvar='LMS_PREPAID_GOTIFY_URL')
@click.option('--gotify-token', '-k', default=None, envvar='LMS_PREPAID_GOTIFY_TOKEN')
@click.option('--gotify-prio', '-o', default=2, envvar='LMS_PREPAID_GOTIFY_PRIO')
@click.option('--dump-responses', '-u', default=False, is_flag=True)
def query(database, card, quiet, currency, dump_responses, gotify_url, gotify_token, gotify_prio):
    t = Tritise(filename=database)
    api = LmsApi(card)
    api.set_dump_responses(dump_responses)
    if (not quiet):
        print('Querying data for card: %s' % card)
    try:
        credit = api.get_credit()
    except InvalidRequest:
        print('The request was invalid. Check the supplied card number.')
        return
    notify_change = gotify_token and gotify_url
    if notify_change:
        last_credit = t.last()
        if not last_credit or (last_credit.value != credit.amount):
            gotify(gotify_url,
                   gotify_token,
                   'Prepaid card credit changed', 'New credit: %.2f' % credit.amount,
                   gotify_prio)
    t.add(credit.amount)
    output = '%.2f' % credit.amount
    if (currency):
        output = output + ' ' + credit.currency
    print(output)

if __name__ == '__main__':
    query()