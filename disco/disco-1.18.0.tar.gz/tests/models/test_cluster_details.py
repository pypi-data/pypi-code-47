from disco.models import ClusterDetails
from tests.base_test import BaseTest


class TestClusterDetails(BaseTest):
    def test_cluster_create(self):
        cluster_id = self.random_str('cluster_id')
        cluster_name = self.random_str('cluster_name')
        account_id = self.random_str('id')

        cluster_data = {
            'id': cluster_id,
            'name': cluster_name,
            'type': 'aws',
            'cluster': {
                'region': 'us-west-2',
                'externalAccountId': account_id,
                'bucketName': 'disco-store-production'},
            'isLastConnectionCheckValid': True,
            'isActive': True,
            'enableCloudOffload': False
        }

        cluster = ClusterDetails(cluster_data, True)
        assert cluster.id == cluster_id
        assert cluster.name == cluster_name
        assert cluster.bucket_name == 'disco-store-production'
        assert cluster.type == 'aws'
        assert cluster.is_default
        assert cluster.is_active
        assert not cluster.cloud_offload_enabled
        assert cluster.is_last_connection_check_valid
