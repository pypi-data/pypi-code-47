from ..main import main
import json
import pytest


def test_without_arg():
    with pytest.raises(AssertionError):
        main()

# TODO: Create basic dataset that can be used in regression tests
