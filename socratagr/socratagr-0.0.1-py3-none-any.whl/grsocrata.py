from socrata.authorization import Authorization
from socrata import Socrata
import pandas as pd
import os
import requests

def create_dataset(data, name, description, private=True):
    auth = Authorization(
        'data.grandrapidsmi.gov',
        os.environ['SOCRATA_USERNAME'],
        os.environ['SOCRATA_PASSWORD']
    )
    socrata = Socrata(auth)

    (revision, output) = socrata.create(
        name=name,
        description=description
    ).df(data)

    (ok, job) = revision.apply()
    (ok, job) = job.wait_for_finish()

    if private:
        (ok, view) = socrata.views.lookup(revision.attributes['fourfour'])
        (ok, revision) = view.revisions.create_replace_revision(permission='private')
        assert ok, revision
        (ok, source) = revision.source_from_dataset()

    return revision.source_from_dataset().get_latest_input_schema().get_latest_output_schema()

def update_dataset(data_id, config, dataframe):
    auth = Authorization(
        'data.grandrapidsmi.gov',
        os.environ['SOCRATA_USERNAME'],
        os.environ['SOCRATA_PASSWORD']
    )
    socrata = Socrata(auth)

    # ADD NEW ROWS TO DATASET
    (ok, view) = socrata.views.lookup(data_id)
    (revision, job) = socrata.using_config(
        config,
        view
    ).df(dataframe)
    (ok, job) = job.wait_for_finish(progress=lambda job: print('Job progress:', job.attributes['status']))


# DELETE ROWS OUTSIDE MONTH TIMEFRAME
# Define function to get data outside of 48 hours
def query_data(dataset_id, id_col, date_col, start_date):
    # returns a DataFrame whose results in date_col are older than the number of days specified in "ago"

    # find total number of rows (to set limit)
    soda_auth = (os.environ['SOCRATA_USERNAME'], os.environ['SOCRATA_PASSWORD'])
    l = requests.get(f'https://data.grandrapidsmi.gov/resource/{dataset_id}.json?$select=count(*)', auth=soda_auth)
    limit = l.json()[0]['count']

    # calculate date threshhold
    from_date = start_date.date()

    # construct URL
    root = f'https://data.grandrapidsmi.gov/resource/{dataset_id}.json'
    spec = f'$select={id_col},session_start&$where={date_col}<"{from_date}"'
    url = f'{root}?{spec}&$limit={limit}'

    # pull down data
    r = requests.get(url, auth=soda_auth).json()
    return (pd.DataFrame(r))

# Define function to delete rows from dataset
def delete_rows(dataset_id, data):
    # deletes rows in a dataset given an ID and a dataframe
    # dataframe must contain a column aligning with the dataset's ID column (it can contain only this column)
    auth = Authorization(
        'data.grandrapidsmi.gov',
        os.environ['SOCRATA_USERNAME'],
        os.environ['SOCRATA_PASSWORD']
    )
    socrata = Socrata(auth)

    (ok, view) = socrata.views.lookup(dataset_id)
    assert ok
    (ok, revision) = view.revisions.create_delete_revision(permission='private')
    assert ok
    (ok, upload) = revision.create_upload('deleted_data')
    assert (ok)
    (ok, source) = upload.df(data)
    assert (ok)
    output_schema = source.get_latest_input_schema().get_latest_output_schema()
    (ok, job) = revision.apply(output_schema=output_schema)
    assert (ok)
    (ok, job) = job.wait_for_finish(progress=lambda job: print('Job progress:', job.attributes['status']))