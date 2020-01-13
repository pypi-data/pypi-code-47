import pytest
from astropy.io import fits
from dkist_hdr_validator import FitsValidator
from dkist_hdr_validator.exceptions import *


hdr_valid = {
    "NAXIS": 3,
    "BITPIX": 16,
    "NAXIS1": 2060,
    "NAXIS2": 2050,
    "NAXIS3": 1,
    "INSTRUME": "VBI-BLUE",
    "WAVELNTH": 430.0,
    "DATE-OBS": "2017-05-30T00:46:13.952",
    "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
    "ID___003": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
    "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
    "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
    "DKIST003": "OSZ4FBHWKXRWQGOVG9BJNUWNG5795B",
    "DKIST004": "Observation",
}

hdr_invalid = {
    "NAXIS": 2,
    "BITPIX": 16,
    "NAXIS1": 2060,
    "NAXIS2": 2050,
    "WAVELNTH": "NOTSUPPOSEDTOBEASTRING",
    "DATE-OBS": "2017-05-30T00:46:13.952",
    "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
    "ID___003": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
    "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
    "DKIST003": "OSZ4FBHWKXRWQGOVG9BJNUWNG5795B",
    "DKIST004": "Observation",
}


@pytest.fixture(scope="session")
def validator():
    """
    Fixture that constructs Spec0122 yaml schema
    """
    return FitsValidator()


@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "dkist_hdr_validator/tests/resources/valid_dkist_hdr.fits", id="valid_dkist_hdr.fits"
        ),
        pytest.param(hdr_valid, id="hdr_valid"),
        pytest.param(
            fits.open("dkist_hdr_validator/tests/resources/valid_dkist_hdr.fits"),
            id="valid_HDUList",
        ),
    ],
)
def test_validate_valid(summit_data, validator):
    """
    Validates Spec0122 data expected to pass
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return an empty dictionary
    :param summit_data: Data to validate
    :param validator: Fixture providing and instance of the spec 122 validator
    """
    validator.validate(summit_data)
    assert True  # if the above line didn't throw an exception the test passes


@pytest.mark.skip
@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "dkist_hdr_validator/tests/resources/invalid_dkist_hdr.fits",
            id="invalid_dkist_hdr.fits",
        ),
        pytest.param(hdr_invalid, id="hdr_invalid"),
        pytest.param(
            fits.open("dkist_hdr_validator/tests/resources/invalid_dkist_hdr.fits"),
            id="invalid_HDUList",
        ),
    ],
)
def test_validate_invalid(summit_data, validator):
    """
    Validates Spec0122 data expected to fail
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return a dictionary of ingest errors
    :param summit_data: Data to validate
    :param validator: Fixture providing and instance of the spec 122 validator
    """

    with pytest.raises(Spec122ValidationException):
        validator.validate(summit_data)
