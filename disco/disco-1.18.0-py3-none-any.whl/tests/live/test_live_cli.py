import subprocess

import pytest
from tests.live import env


@pytest.mark.skipif(env.skip, reason=env.reason)
class TestLiveCLI(object):

    def test_login_list_jobs_logout(self):
        output = subprocess.check_output(['disco', 'login', '-u',
                                          'testsdkuser@iqoqo.co', '-p', '12345678']).decode("utf-8")
        print(output)
        assert output.splitlines()[-1] == "Signed in successfully"
        output = subprocess.check_output(['disco', 'job', 'list']).decode("utf-8")
        assert output.find("Done ") >= 0

