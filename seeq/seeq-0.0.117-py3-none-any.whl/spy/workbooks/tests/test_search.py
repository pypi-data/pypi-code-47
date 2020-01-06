import pytest

from seeq import spy

from ...tests import test_common
from . import test_load


def setup_module():
    test_common.login()


@pytest.mark.system
def test_non_recursive():
    workbooks = test_load.load_example_export()
    spy.workbooks.push(workbooks, path='Non-Recursive Import', errors='catalog')
    workbooks_df = spy.workbooks.search({
        'Path': 'Non-Recursive*'
    })
    assert len(workbooks_df) == 2

    workbooks_df = spy.workbooks.search({
        'Path': 'Non-Recursive*',
        'Name': '*Analysis'
    })
    assert len(workbooks_df) == 1
    assert workbooks_df.iloc[0]['Name'] == 'Example Analysis'

    workbooks_df = spy.workbooks.search({
        'Path': 'Non-Recursive*',
        'Workbook Type': 'Topic'
    })
    assert len(workbooks_df) == 1
    assert workbooks_df.iloc[0]['Name'] == 'Example Topic'


@pytest.mark.system
def test_recursive():
    workbooks = test_load.load_example_export()
    spy.workbooks.push(workbooks, path='Recursive Import >> Another Folder Level', errors='catalog')
    workbooks_df = spy.workbooks.search({
        'Path': 'Recursive I?port'
    })
    assert len(workbooks_df) == 1
    assert workbooks_df.iloc[0]['Name'] == 'Another Folder Level'
    assert workbooks_df.iloc[0]['Type'] == 'Folder'

    # The items will have been moved from the non-recursive location
    workbooks_df = spy.workbooks.search({
        'Path': 'Non-Recursive*'
    })
    assert len(workbooks_df) == 0

    workbooks_df = spy.workbooks.search({
        'Path': r'/Recursive\sImport/',
        'Name': '*Analysis'
    }, recursive=True)
    assert len(workbooks_df) == 1
    assert workbooks_df.iloc[0]['Name'] == 'Example Analysis'

    workbooks_df = spy.workbooks.search({
        'Path': r'/^Recursive.*/',
        'Workbook Type': 'Topic'
    }, recursive=True)
    assert len(workbooks_df) == 1
    assert workbooks_df.iloc[0]['Name'] == 'Example Topic'
