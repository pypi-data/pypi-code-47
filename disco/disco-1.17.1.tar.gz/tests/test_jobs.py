#  Copyright (c) 2019 Samsung, Inc. and its affiliates.
#
#  This source code is licensed under the RESTRICTED license found in the
#  LICENSE file in the root directory of this source tree.

import os
import subprocess
import sys
import mock
import pytest

import disco
from disco.core import constants as const, exceptions
from disco.models import JobDetails
from .base_test import BaseTest

    
class TestJobs(BaseTest):

    def test_job_summary(self):
        with mock.patch('disco.Job.list_jobs') as list_jobs_mock:

            expected_statuses = ['Done', 'Working', 'Done', 'Failed', 'Failed']
            jobs_details = [JobDetails(dict(status=status)) for status in expected_statuses]
            list_jobs_mock.return_value = jobs_details

            jobs_summary = disco.Job.jobs_summary()

        assert jobs_summary == {'Done': 2, 'Failed': 2, 'Working': 1}

    def test_job_summary_empty(self):
        with mock.patch('disco.Job.list_jobs') as list_jobs_mock:
            list_jobs_mock.return_value = []

            jobs_summary = disco.Job.jobs_summary()

        assert jobs_summary == {}

    @BaseTest.with_config_and_env(authenticated=True)
    def test_get_tasks(self):

        job_id = self.random_str('job-id')

        task_id1 = self.random_str('task_id1')
        task_status1 = 'Success'
        task_duration1 = self.random_int()
        task_input_file_id1 = self.random_str('input_file_id1')
        artifact_ids1 = [self.random_str('artifactA_id1'), self.random_str('artifactB_id1')]

        task_id2 = self.random_str('task_id2')
        task_status2 = 'Running'
        task_duration2 = self.random_int()
        task_input_file_id2 = self.random_str('input_file_id2')
        artifact_ids2 = [self.random_str('artifactA_id2'), self.random_str('artifactB_id2')]

        with mock.patch('disco.Job.query') as graphql_mock:
            graphql_mock.return_value = {
                'findTasks': {
                    'results': [
                        {
                            'id': task_id1,
                            'status': task_status1,
                            'stats': {'duration': task_duration1},
                            'request': {'inputFile': {'id': task_input_file_id1}},
                            'result': {'artifactIds': artifact_ids1}
                        },
                        {
                            'id': task_id2,
                            'status': task_status2,
                            'stats': {'duration': task_duration2},
                            'request': {'inputFile': {'id': task_input_file_id2}},
                            'result': {'artifactIds': artifact_ids2}
                        },
                    ]
                }
            }

            tasks = disco.Job(job_id).get_tasks()

        assert isinstance(tasks, list)
        assert len(tasks) == 2

        [task1, task2] = tasks

        assert task1.id == task_id1
        assert task1.status == task_status1
        assert task1.duration == task_duration1
        assert task1.input_file_id == task_input_file_id1
        assert task1.artifact_ids == artifact_ids1

        assert task2.id == task_id2
        assert task2.status == task_status2
        assert task2.duration == task_duration2
        assert task2.input_file_id == task_input_file_id2
        assert task2.artifact_ids == artifact_ids2

    @BaseTest.with_config_and_env(authenticated=True)
    def test_list_jobs(self):

        job_id1 = self.random_str('job-id1')
        job_name1 = self.random_str('job-name1')
        job_status1 = 'Done'

        job_id2 = self.random_str('job-id2')
        job_name2 = self.random_str('job-name2')
        job_status2 = 'Failed'

        with mock.patch('disco.Job.query') as graphql_mock:
            graphql_mock.return_value = {
                'findJobs': {
                    'results': [
                        {
                            'id': job_id1,
                            'status': job_status1,
                            'request': {'meta': {'name': job_name1}},
                        },
                        {
                            'id': job_id2,
                            'status': job_status2,
                            'request': {'meta': {'name': job_name2}},
                        },
                    ]
                }
            }

            job_details = disco.Job.list_jobs()

        assert isinstance(job_details, list)
        assert len(job_details) == 2

        [job_detail1, job_detail2] = job_details

        assert job_detail1.id == job_id1
        assert job_detail1.name == job_name1
        assert job_detail1.status == job_status1
        assert job_detail1.tasks_summary is None

        assert job_detail2.id == job_id2
        assert job_detail2.name == job_name2
        assert job_detail2.status == job_status2
        assert job_detail2.tasks_summary is None

    @BaseTest.with_config_and_env(authenticated=True)
    def test_list_jobs_empty(self):
        with mock.patch('disco.Job.query') as graphql_mock:
            graphql_mock.return_value = None

            result = disco.Job.list_jobs()

        assert result == []

    @BaseTest.with_config_and_env()
    @mock.patch('disco.job.Job._get_venv_requirements', return_value=None)
    def test_return_id(self, _):
        expected_job_id = 'fake_job_id'
        with mock.patch('disco.gql.Query.send') as graphql_mock:
            graphql_mock.return_value = {
                'createJob': {
                    'id': expected_job_id
                }
            }

            job = disco.Job.create('fake_script_id')
            assert job.job_id == expected_job_id

    @mock.patch('disco.Job.get_status',
                mock.MagicMock(return_value=const.JobStatus.listed))
    def test_timeout(self):
        job = disco.job.Job('lucky')
        with pytest.raises(exceptions.TimeOutError):
            job.wait_for_finish(interval=1, timeout=0)

    @BaseTest.with_config_and_env()
    @mock.patch('disco.job.is_venv', return_value=True)
    def test__get_venv_requirements(self, _is_venv):
        with mock.patch('subprocess.Popen') as _popen, \
                mock.patch('disco.asset.Asset.upload') as _upload:
            res = '\n'.join([self.random_str() for _ in range(10)])
            bin_res = res.encode('utf-8')
            fid = self.random_str('requirements.txt_fid')
            cluster_id = self.random_str('cluster_id')

            _upload.return_value = fid
            _popen.return_value.communicate.return_value = (bin_res, self.random_bytes(10))

            res_fid = disco.Job._get_venv_requirements(cluster_id=cluster_id)

            assert res_fid == fid

            _popen.return_value.communicate.assert_called_once()
            _popen.assert_called_once_with(
                [sys.executable, '-m', 'pip', 'freeze'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            _upload.assert_called_once()
            _is_venv.assert_called_once()
