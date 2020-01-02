import uuid


class Args:
    def __init__(self, cluster_id=None, node_name=None, cmd=None, private_key=None, public_key=None,
                 hive_password=None):
        self.cluster_id = cluster_id or "mdh" + str(uuid.uuid1()).replace("-", "")
        self.node_name = node_name
        self.cmd = cmd
        self.private_key = private_key
        self.public_key = public_key
        self.hive_password = hive_password or self.cluster_id
