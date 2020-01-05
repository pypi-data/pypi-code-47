from pathlib import Path
import json

import pytest

from src.carboncopy.cli import get_local_config
from src.carboncopy.config_defaults import CONFIG_DEFAULTS
from src.carboncopy.constants import RCFILE_PATH

def test_get_local_config_returns_default_if_no_rc_file_present(tmp_path, capsys, snapshot):
    current_files = list(tmp_path.iterdir())

    assert Path(RCFILE_PATH) not in current_files

    loaded_config = get_local_config()

    assert loaded_config == CONFIG_DEFAULTS
    assert capsys.readouterr().out == snapshot

def test_get_local_config_returns_merged_local_and_defaults_if_rc_file_present(tmp_path, snapshot, capsys):
    mock_custom_configuration = { "current_time": "big-brain-time" }
    mock_config_json = json.dumps(mock_custom_configuration)

    rcfile = tmp_path / RCFILE_PATH
    rcfile.write_text(mock_config_json)

    current_files = list(tmp_path.iterdir())

    loaded_config = get_local_config(tmp_path)
    
    expected = { **CONFIG_DEFAULTS, **mock_custom_configuration }

    assert loaded_config == expected
    assert capsys.readouterr().out == snapshot


