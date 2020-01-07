from cdf_ifs_file_extractor.utils import read_yaml


def test_read_yaml():
    parsed_yaml = read_yaml("config/default.yml")
    assert parsed_yaml["client_name"] == "cdf-ifs-file-extractor"
    assert parsed_yaml["client_timeout"] == 100
    assert parsed_yaml["log_path"] == "log"
    assert parsed_yaml["log_level"] == "info"
    assert parsed_yaml["project"] == "project-that-api-key-is-for"
