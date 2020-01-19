import unittest
from secretfy_template.template import template


class TestRepoPath(unittest.TestCase):
    """Test for checking git repo directory of file. """

    def test_git_repo_file(file_path):
        list = [
            "/Users/s0s0249/workspace/open_source/Jarvis/jarviscli/packages/\
                forecast.py",
            "/Users/s0s0249/workspace/open_source/SKF-Chatbot/Basic_Approach/\
                notebook/data.json",
            "/Users/s0s0249/workspace/open_source/cloudmarker/cloudmarker/\
                cloudmarker.yaml",
            "/Users/s0s0249/workspace/open_source/makesite/\
                content/blog/2018-01-01-proin-quam.md",
            "/Users/s0s0249/workspace/open_source/RTTM/scrapper_config/\
                scanner-configuration.properties"]

        for path in list:
            print('\n\n', template.Template().get_git_repo_path(path))


if __name__ == '__main__':
    unittest.main()
