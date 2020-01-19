"""
Test tcx2gpy.
"""
from pathlib import Path

from tcxparser import TCXParser
from gpxpy.gpx import GPX

TCX_DIR = Path(__file__).resolve().parents[1]
GPX_FILE = TCX_DIR / 'resources' / '2019-10-20 12:51:21.0.gpx'


def test_tcx2gpx_init(tcx_file):
    """
    Test instantiation results in the correct object type.
    """
    assert isinstance(tcx_file.tcx_path, Path)
    assert isinstance(tcx_file.gpx, GPX)


def test_read_tcx(tcx_file):
    """
    Test reading of TCX
    """
    tcx_file.read_tcx()

    assert isinstance(tcx_file.tcx, TCXParser)


def test_extract_track_points(tcx_file):
    """
    Test reading of TCX
    """
    tcx_file.read_tcx()
    tcx_file.extract_track_points()

    assert isinstance(tcx_file.track_points, zip)


def test_create_gpx(tcx_file):
    """
    Test reading of TCX
    """
    tcx_file.read_tcx()
    tcx_file.extract_track_points()
    tcx_file.create_gpx()

    assert isinstance(tcx_file.gpx, GPX)


def test_write_gpx(tcx_file):
    """
    Test reading of TCX
    """
    tcx_file.read_tcx()
    tcx_file.extract_track_points()
    tcx_file.create_gpx()
    tcx_file.write_gpx()

    assert Path(GPX_FILE).exists()


def test_convert(tcx_file):
    """
    Test conversion wrapper
    """
    tcx_file.convert()

    assert isinstance(tcx_file.track_points, zip)
    assert isinstance(tcx_file.gpx, GPX)
