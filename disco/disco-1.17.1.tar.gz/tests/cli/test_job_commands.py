from pathlib import Path
from time import sleep
import os
from disco import Job
from disco.task import TaskResult

from .sdk_mocks import MockListJobsResponse, MockViewJobResponse, MockBadIdException
from mock import patch, call
from click.testing import CliRunner
from disco_cli import cli, setup_cli
from .cli_test_utils import output_message_includes
from tests.base_test import BaseTest


class TestJobCommands(BaseTest):

    def setup_class(self):
        setup_cli()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    def test_job_list(self, is_logged_in_mock):
        """
        Tests job list
        Returns:

        """
        is_logged_in_mock.return_value = True
        with patch('disco.Job.list_jobs') as list_jobs_mock:
            list_jobs_mock.return_value = MockListJobsResponse
            runner = CliRunner()
            result = runner.invoke(cli, ['job', 'list'])
            assert result.exit_code == 0
            list_jobs_mock.assert_called()
            is_logged_in_mock.assert_called()
            assert output_message_includes(result, '| 5d66595208edfa000a250dda | Cool Humor       | Done     |')

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.list_jobs')
    def test_action_without_login(self, list_jobs_mock, is_logged_in_mock):
        list_jobs_mock.return_value = []
        is_logged_in_mock.return_value = False
        runner = CliRunner()
        result = runner.invoke(cli, ['job', 'list'])
        assert result.exit_code == 0
        assert result.output == "You must be logged in to perform this operation\n"

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.get_details')
    def test_view_job(self, get_details_mock, is_logged_in_mock):
        """
        Tests a successful job view command
        Returns:

        """
        is_logged_in_mock.return_value = True
        get_details_mock.return_value = MockViewJobResponse
        runner = CliRunner()
        result = runner.invoke(cli, ['job', 'view', 'job_id'])
        get_details_mock.assert_called_once()
        assert result.exit_code == 0
        assert output_message_includes(result, "Status: Done")
        assert output_message_includes(result, "Name: dsfgfdsgs")
        assert output_message_includes(result, "failed: 1")

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.get_details')
    def test_view_job_malformed_id(self, get_details_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        get_details_mock.side_effect = MockBadIdException
        get_details_mock.return_value = MockViewJobResponse
        runner = CliRunner()
        result = runner.invoke(cli, ['job', 'view', 'job_id'])
        get_details_mock.assert_called_once()
        assert result.exit_code == 0
        assert output_message_includes(result, "Bad format for Id")

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_input_file(self, asset_upload_mock, path_is_dir_mock,
                                   path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using input files
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py -i input_file".split(' '))
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with('file_id', ['file_id'], [],
                                                   'job_name',
                                                   's', None, False, upload_requirements_file=True)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.upload')
    def test_create_job_quite_mode(self, asset_upload_mock, job_create_mock, is_logged_in_mock):
        """
        Run create job in quite mode
        """
        is_logged_in_mock.return_value = True
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py --quite")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with('file_id', [], [],
                                                   'job_name',
                                                   's', None, False, upload_requirements_file=True)

                asset_upload_mock.assert_called_with('script_file.py', Path('script_file.py'),
                                                     cluster_id=None, show_progress_bar=False)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.upload')
    def test_create_job_quite_mode_disabled_by_default(self, asset_upload_mock, job_create_mock, is_logged_in_mock):
        """
        Run create job, quite mode disabled by default
        """
        is_logged_in_mock.return_value = True
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with('file_id', [], [],
                                                   'job_name',
                                                   's', None, False, upload_requirements_file=True)

                asset_upload_mock.assert_called_with('script_file.py', Path('script_file.py'),
                                                     cluster_id=None, show_progress_bar=True)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_without_req_file(self, asset_upload_mock, path_is_dir_mock,
                                         path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using input files
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py -i "
                                            "input_file --dont-generate-req-file".split(' '))
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with('file_id', ['file_id'], [],
                                                   'job_name',
                                                   's', None, False, upload_requirements_file=False)


    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_constant_file(self, asset_upload_mock, path_is_dir_mock,
                                      path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using constant files
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py -c const_file".split(' '))
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with('file_id', [], ['file_id'],
                                                   'job_name',
                                                   's', None, False, upload_requirements_file=True)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_many_files(self, asset_upload_mock, path_is_dir_mock,
                                      path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using many input and constant files
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py "
                                            "-i input_file1,input_file2 "
                                            "-c const_file1,const_file2".split(' '))
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with('file_id', ['file_id', 'file_id'],
                                                   ['file_id', 'file_id'], 'job_name',
                                                   's', None, False, upload_requirements_file=True)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('pathlib.Path.glob')
    @patch('disco.asset.Asset.upload')
    def test_create_job_directory(self, asset_upload_mock, path_glob_mock, path_is_dir_mock,
                                      path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using directory as input
        Args:
            asset_upload_file_mock:
            path_glob_mock:
            path_is_dir_mock:
            path_exists_mock:
            job_create_mock:

        Returns:

        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = True
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        path_glob_mock.return_value = [Path('file1'), Path('file2')]
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py "
                                            "-i dir_path ")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with('file_id', ['file_id', 'file_id'],
                                                   [], 'job_name',
                                                   's', None, False, upload_requirements_file=True)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('pathlib.Path.glob')
    @patch('disco.asset.Asset.upload')
    def test_create_job_wildcard(self, asset_upload_mock, path_glob_mock, path_is_dir_mock,
                                      path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using file with wildcards
        """
        script_file_id = self.random_str("script_file_id")
        input_file_id1 = self.random_str("input_file_id1")
        input_file_id2 = self.random_str("input_file_id2")

        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = True
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.side_effect = [script_file_id,  input_file_id1, input_file_id2]
        path_glob_mock.return_value = [Path('file1'), Path('file2')]
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f, open("input_file1.txt", 'w') as i1:
                sleep(1)
                i2 = open("input_file2.txt", 'w')
                input_file_contents1 = self.random_str("input_contents1")
                input_file_contents2 = self.random_str("input_contents2")
                i1.write(input_file_contents1)

                i2.write(input_file_contents2)
                i2.close()
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py "
                                            "-i inp* ")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with(script_file_id, [input_file_id1, input_file_id2],
                                                   [], 'job_name',
                                                   's', None, False, upload_requirements_file=True)
                assert asset_upload_mock.call_args_list[1][0] == ('input_file1.txt', Path('input_file1.txt'))
                asset_upload_mock.assert_called_with('input_file2.txt', Path('input_file2.txt'),
                                                     cluster_id=None, show_progress_bar=True)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    def test_create_job_not_supported_script(self, path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Unsuccessful path for creating a job with a script file that is not supported
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Cannot use script file. '
                                                       'Currently only Python and '
                                                       'bash scripts are supported')
                job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('pathlib.Path.glob')
    def test_create_job_empty_directory(self, path_glob_mock, path_is_dir_mock,
                                        path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using directory as input
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = True
        path_glob_mock.return_value = []
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py "
                                            "-i dir_path ")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Folder dir_path is empty')
                job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    def test_create_job_missing_input(self, path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Unsuccessful path for creating a job with a script file that is not supported
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = False
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py -i input_file")
                assert result.exit_code == 0
                assert output_message_includes(result, 'input_file doesn\'t exist')
                job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.upload')
    def test_create_job_script_file_in_home_dir(self, asset_upload_mock, job_create_mock, is_logged_in_mock):
        """
        Create job with script file from user's home directory, i.e `~/script_file.py`
        """
        script_file_id = self.random_str("script_file_id")
        input_file_id1 = self.random_str("input_file_id1")
        input_file_id2 = self.random_str("input_file_id2")
        constant_file_id = self.random_str("constant_file_id")

        is_logged_in_mock.return_value = True
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.side_effect = [script_file_id, input_file_id1, input_file_id2, constant_file_id]
        runner = CliRunner()

        script_filename = 'script_file.py'
        input_filename1 = 'input1.txt'
        input_filename2 = 'input2.txt'
        constant_filename = 'constant.txt'

        script_file_path = os.path.join("~", script_filename)
        input_file_path1 = os.path.join("~", input_filename1)
        input_file_path2 = os.path.join("~", input_filename2)
        constant_file_path = os.path.join("~", constant_filename)

        script_full_file_path = str(Path.home() / script_filename)
        input_file_full_path1 = str(Path.home() / input_filename1)
        input_file_full_path2 = str(Path.home() / input_filename2)
        constant_file_full_path = str(Path.home() / constant_filename)

        try:
            with open(script_full_file_path, 'w') as script_file:
                script_file.write("print('hi!')")

            with open(input_file_full_path1, 'w') as input_file1:
                input_file1.write(self.random_str('input1_content'))

            with open(input_file_full_path2, 'w') as input_file2:
                input_file2.write(self.random_str('input2_content'))

            with open(constant_file_full_path, 'w') as constant_file:
                constant_file.write(self.random_str('constant_file_content'))

            result = runner.invoke(cli, f"job create -n job_name --script {script_file_path} "
                                   f"--input {input_file_path1},{input_file_path2} "
                                   f"--constants {constant_file_path}")
            assert result.exit_code == 0
            assert output_message_includes(result, 'Created job with id job_id')
            job_create_mock.assert_called_with(script_file_id, [input_file_id1, input_file_id2], [constant_file_id],
                                               'job_name', 's', None, False,
                                               upload_requirements_file=True)

            asset_upload_mock.assert_has_calls([
                call(script_filename, Path(script_full_file_path), cluster_id=None, show_progress_bar=True),
                call(input_filename1, Path(input_file_full_path1), cluster_id=None, show_progress_bar=True),
                call(input_filename2, Path(input_file_full_path2), cluster_id=None, show_progress_bar=True),
                call(constant_filename, Path(constant_file_full_path), cluster_id=None, show_progress_bar=True),
            ], any_order=True)

        finally:
            os.remove(script_full_file_path)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.start')
    def test_start_job(self, job_start_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        runner = CliRunner()
        result = runner.invoke(cli, 'job start job_id')
        assert result.exit_code == 0
        assert result.output == 'Job job_id started\n'
        job_start_mock.assert_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.stop')
    def test_stop_job(self, job_stop_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        runner = CliRunner()
        result = runner.invoke(cli, 'job stop job_id')
        assert result.exit_code == 0
        assert result.output == 'Stopping job job_id\n'
        job_stop_mock.assert_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.archive')
    def test_archive_job(self, job_archive_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        runner = CliRunner()
        result = runner.invoke(cli, 'job archive job_id')
        assert result.exit_code == 0
        assert result.output == 'Job job_id was archived\n'
        job_archive_mock.assert_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.get_results')
    @patch('pathlib.Path.exists', return_value=True)
    @patch('pathlib.Path.is_dir', return_value=True)
    @patch('os.makedirs')
    @patch('disco.task.TaskResult.write_files')
    def test_download_results(self, write_files_mock, makedirs_mock, is_dir_mock, path_exists_mock,
                         get_results_mock, is_logged_in_mock):
        get_results_mock.return_value = [TaskResult('task_id', {'Iqoqo.stdout.log': 'some output'})]
        is_logged_in_mock.return_value = True
        runner = CliRunner()
        result = runner.invoke(cli, 'job download-results job_id -d destdir')
        assert result.exit_code == 0
        assert result.output == 'Results downloaded successfully\n'
        get_results_mock.assert_called()
        makedirs_mock.assert_called()





