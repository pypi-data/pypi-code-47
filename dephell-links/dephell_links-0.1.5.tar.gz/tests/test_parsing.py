# built-in
from pathlib import Path

# project
import pytest
from dephell_links import DirLink, FileLink, URLLink, VCSLink, parse_link, IS_WINDOWS


skipif_not_windows = pytest.mark.skipif(not IS_WINDOWS, reason='not Windows')


@pytest.mark.parametrize('link_type, url, expected', [
    (VCSLink, 'https://github.com/r1chardj0n3s/parse.git', None),
    (URLLink, 'https://github.com/divio/django-cms/archive/release/3.4.x.zip', None),
    (FileLink, './tests/test_parsing.py', None),
    (FileLink, 'file://./tests/test_parsing.py', './tests/test_parsing.py'),
    (FileLink, 'file://{}'.format(Path('./tests/test_parsing.py').absolute()),
     str(Path('./tests/test_parsing.py').absolute())),
    (FileLink, 'file://{}'.format(Path('./tests/test_parsing.py').absolute().as_posix()),
     Path('./tests/test_parsing.py').absolute().as_posix()),
    (FileLink, './this_file_does_not_exists.py', None),
    (DirLink, '.', None),
    (DirLink, 'file://.', '.'),
    (DirLink, 'file://{}'.format(Path('.').absolute()), str(Path('.').absolute())),
    (DirLink, 'file://{}'.format(Path('.').absolute().as_posix()), Path('.').absolute().as_posix()),

    # Windows only
    pytest.param(FileLink, 'file:///{}'.format(Path('./tests/test_parsing.py').absolute().as_posix()),
                 Path('./tests/test_parsing.py').absolute().as_posix(), marks=skipif_not_windows),
    pytest.param(FileLink, 'file:///{}'.format(Path('./tests/test_parsing.py').absolute()),
                 str(Path('./tests/test_parsing.py').absolute()), marks=skipif_not_windows),
    pytest.param(DirLink, 'file:///{}'.format(Path('.').absolute().as_posix()),
                 Path('.').absolute().as_posix(), marks=skipif_not_windows),
    pytest.param(DirLink, 'file:///{}'.format(Path('.').absolute()),
                 str(Path('.').absolute()), marks=skipif_not_windows),
])
def test_parsing(link_type, url, expected):
    link = parse_link(url)
    assert isinstance(link, link_type)

    if not expected:
        expected = url
    assert link.short == expected
