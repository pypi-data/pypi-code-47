from disco.base_controller import BaseController
from disco.models import ClusterDetails


class Cluster(BaseController):
    """
    Cluster methods
    """

    @classmethod
    def list_clusters(cls, limit=None, next_=None):
        """Show a list of all the clusters applicable for this user.

                Args:
                    limit (int): pagination limit
                    next_: pagination next

                Returns:
                    list(ClusterDetails): List of the clusters belonging to this user.
                """

        res = cls.query('fetchProfileClusters', limit=limit,
                        id=cls.get_current_user(), next=next_)

        if res is None:
            return []
        return [ClusterDetails(cluster, res['fetchProfile']['defaultClusterId'] == cluster['id'])
                for cluster in res['fetchProfile']['clusters']]
