import click
import click_config_file
import json
import os
import sys
from .api import Session
from . import export

@click.command()
@click.option('--email', prompt=True, show_envvar=True,
        help="Account email address")
@click.password_option(show_envvar=True, 
        help="Account password")
@click.option("--type", "record_type",
        type=click.Choice(["shortages", "discontinuations"], case_sensitive=False),
        default='shortages', show_default=True)
@click.option("--params", "-p", 
        type=(str,str), multiple=True, 
        help="Arbitrary search parameters to pass to the API, e.g. -p din 0123123")
@click.option('--fmt', 
        type=click.Choice(['json', 'flat', 'csv'], case_sensitive=False), 
        default="json")
@click_config_file.configuration_option(show_default=True)
def search(email, password, record_type, params, fmt):
    """Searches the drugshortagescanada.ca database
   
       See https://www.drugshortagescanada.ca/blog/52 for all the gory details.

       When using --params, the following parameters are supported: 

        \b
        term            main text search value
        din             Drug Identification Number
        report_id       Database report ID
        orderby         specify the column to sort the results by
        order           asc for ascending; desc for descending
        filter_status   only return reports of the given status
                        (i.e. anticipated_shortage, active_confirmed, avoided_shortage,
                         resolved, reversed, to_be_discontinued, discontinued)
        limit           the maximum number of objects returned in the single request
        offset          the starting index of the response (defaults to 0)

        \b
        *orderby* can be one of the following 
        id              report ID
        company_name    the company associated with the report
        brand_name      the drug associated with the report
        status          the current status of the report
        type            the type of report (shortage or discontinuation)
        updated_date    the date of the last change to the report
    """
    s = Session(email, password)
    s.login()
    params=dict(params)
    shortages=(record_type == 'shortages')

    if fmt == 'json':
        results = s.search(**params)
        print(json.dumps(results, indent=2))
    if fmt == 'flat':
        results = export.isearch_flatten(s, **params)
        print('[')
        for i in results:
            print(json.dumps(i, indent=2), ',')
        print(']')
    if fmt == 'csv':
        export.as_csv(s, sys.stdout, shortages=shortages, **params)


def run(): 
    search(auto_envvar_prefix='DSC')

if __name__ == '__main__':
    run()
