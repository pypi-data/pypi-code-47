from flask import request
from flask_restful import Resource, reqparse, abort
from .models import Args
from .main import ClusterHandler


class ServiceAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('replicas', type=int, help='Number of cluster members provisioned',
                                   required=True, location='json')
        self.reqparse.add_argument('clusters', type=int, help='Number of clusters provisioned', required=True,
                                   location='json')

        super(ServiceAPI, self).__init__()

    def get(self):
        """ HTTP GET method for /Service api
        Examples:
            /Service?add_service - add's new service
            /Service?add_node&cluster_id=xxxx - add new backend node to cluster
            /Servce?rm_node&cluster_id - removes backend node from cluster
        Returns (list): Cluster status

        """
        res = []
        cluster_id = request.args.get('cluster_id')
        cmd = request.args.get('cmd')
        if cmd == "add_service":
            handler = ClusterHandler(Args(cluster_id=cluster_id))
            handler.prepare()
            res = handler.setup_cluster_infra()
        elif cmd == "add_node" and cluster_id:
            handler = ClusterHandler(Args(cluster_id=cluster_id))
            handler.prepare()
            res = handler.add_node_to_cluster()
        elif cmd == "rm_node" and cluster_id:
            handler = ClusterHandler(Args(cluster_id=cluster_id))
            handler.prepare()
            res = handler.remove_node_from_cluster()
        return res

    def post(self):
        """HTTP POST method for API /Service entrypoint for cluster creation
        Examples:
            POST to /Service entrypoint with data
             { "clusters": "1", "replicas" : "1" }
             creates one cluster with one backned node
        Returns (list): Created cluster info

        """
        posted_data = request.get_json()
        if not posted_data:
            abort("Missing input data")
        replicas = int(posted_data.get("replicas"))
        clusters = int(posted_data.get("clusters"))
        res = []
        if clusters and replicas:
            for cluster in range(clusters):
                args = Args()
                handler = ClusterHandler(args)
                handler.prepare()
                handler.setup_cluster_infra()
                if replicas > 1:
                    handler = ClusterHandler(args)
                    handler.prepare()
                    for replica in range(replicas - 1):
                        handler.add_node_to_cluster()
                res.append({handler.cluster_id: handler.show_cluster()})
        return res

    def patch(self):
        """ HTTP PATCH method for /Service entrypoint for cluster change

        Examples:
            PATCH to /Service?cluster_id=xxx... - With data {"replicas": "1"} changes cluster backend replicas to one


        Returns (list): Updated cluster info

        """
        posted_data = request.get_json()
        if not posted_data:
            abort("Missing input data")
        new_replicas = int(posted_data.get("replicas"))
        cluster_id = request.args.get('cluster_id')
        if not cluster_id:
            abort("Missing cluster_id from args")
        handler = ClusterHandler(Args(cluster_id=cluster_id))
        if handler.prepare():
            return abort("Bad cluster_id")
        if len(handler.mdh_backends) == new_replicas:
            return handler.show_cluster()
        elif len(handler.mdh_backends) > new_replicas:
            while len(handler.mdh_backends) != new_replicas:
                handler.prepare()
                handler.remove_node_from_cluster()
        elif len(handler.mdh_backends) < new_replicas:
            while len(handler.mdh_backends) != new_replicas:
                handler.prepare()
                handler.add_node_to_cluster()
        return handler.show_cluster()

    def delete(self):
        """ HTTP POST method for cluster deletion
        Examples:
            DELETE to /Service?cluster_id=xxx...  - removes cluster

        Returns (list): List of removed containers statuses

        """
        cluster_id = request.args.get('cluster_id')
        if not cluster_id:
            abort("Missing cluster_id from args")
        handler = ClusterHandler(Args(cluster_id=cluster_id))
        if not handler.prepare():
            abort("Bad cluster_id")
        return handler.remove_cluster()


class StateAPI(Resource):
    def get(self):
        """ HTTP GET method for API /State entrypoint
        Examples:
            /State - returns all available clusters info
            /State?cluster_id=xxx.. - returns specified cluster_id info

        Returns (list): Cluster info.

        """
        cluster_id = request.args.get('cluster_id')
        handler = ClusterHandler(Args(cluster_id=cluster_id))
        handler.prepare()
        return handler.show_cluster(show_all=False if cluster_id else True)


class Root(Resource):
    def get(self):
        """ HTTP GET method for API / entrypoint

        Returns (dict): dict formated welcome message

        """
        return {'message': 'welcome'}
