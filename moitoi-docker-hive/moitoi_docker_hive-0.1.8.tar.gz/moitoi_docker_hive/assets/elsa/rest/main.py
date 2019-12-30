"""Main module."""
import logging
import os
from argparse import ArgumentParser

from paramiko import RSAKey
import docker

DEFAULT_MDH_LD_PORT = 5000
DEFAULT_MDH_BACKEND_PORT = 5000


class ClusterHandler:
    ssh_public_key = None
    cluster_id = None
    cluster_network = None
    cluster_data_volume = None
    lb_container = None
    elsa_container = None
    prom_container = None
    grafana_container = None
    mdh_backends = []

    def __init__(self, args):
        self.args = args
        self.cluster_id = args.cluster_id
        self.docker_client = docker.from_env()
        self.prepare()

    @staticmethod
    def generate_ssh_key_pairs(filename, phrase):
        """ SSH key pairs generator for remote docker host provider

        Args:
            filename (str):The filename path where ssh keys will be saved.
            phrase (str):The password phrase.

        Returns:

        """
        # generating private key
        prv = RSAKey.generate(bits=2048, progress_func=None)
        prv.write_private_key_file(filename, password=phrase)

        # generating public key
        pub = RSAKey(filename=filename, password=phrase)
        with open("%s.pub" % filename, "w") as f:
            f.write("%s %s" % (pub.get_name(), pub.get_base64()))
            f.write(" %s" % "moitoi_docker_hive_key")

    def load_ssh_keys(self):
        """ Helper method to load ssh keys
        """
        if not os.path.isfile(self.args.private_key):
            self.generate_ssh_key_pairs(self.args.private_key, self.args.hive_password)

        if not self.ssh_public_key:
            with open(self.args.public_key) as f:
                self.ssh_public_key = ''.join(f.readline())

    def _lookup_container_by_label(self, label_key):
        """ Lookup from current cluster container by label key

        Args:
            label_key (str):The key of label.

        Returns:
            containers (list): The list of found container objects.

        """
        containers = []
        for container in self.docker_client.containers.list():
            if container.labels.get(label_key) and container.labels.get("mdh_cluster_id") == self.cluster_id:
                containers.append(container)
        return containers

    def _lookup_container_by_name(self, container_name):
        """ Lookup from current cluster container by container name

        Args:
            container_name (str):The container name to lookup.

        Returns:
            containers (list): The list of found container objects.

        """
        containers = []
        for container in self.docker_client.containers.list():
            if container.name == container_name and container.labels.get("mdh_cluster_id") == self.cluster_id:
                containers.append(container)
        return containers

    def _lookup_container_by_cluster_id(self):
        """ List all current cluster containers

        Returns:
            containers (list): The list of found container objects.

        """
        containers = []
        for container in self.docker_client.containers.list():
            if container.labels.get("mdh_cluster_id") == self.cluster_id:
                containers.append(container)
        return containers

    def _show_all_mdh_containers(self):
        """ Helper method to list all mdh containers
        Returns:
            containers (list): The list of found container objects.

        """
        return list(filter(lambda x: x.labels.get("mdh_cluster_id"), self.docker_client.containers.list()))

    def _show_all_mdh_cluster_ids(self):
        """ Helper method to list all mdh cluster id
        Returns:
            res (list): The list of found cluster id's.

        """
        containers = self.docker_client.containers.list(filters={"label": ["mdh_lb=true"]})
        res = []
        for container in containers:
            cluster_id = container.labels.get("mdh_cluster_id")
            if cluster_id not in res:
                res.append(cluster_id)
        return res

    def _get_or_create_data_volume(self):
        """ Helper method to get or crate data volume for image
        Returns:
            mdh_volumes (list): The list of found or created volume objects.

        """
        mdh_volumes = []
        for _v in self.docker_client.volumes.list():
            labels = _v.attrs['Labels']
            if not labels:
                continue
            if labels.get("mdh_data_volume") and labels.get("mdh_cluster_id", "NULL") == self.cluster_id:
                mdh_volumes.append(_v)
        if not len(mdh_volumes):
            volume = self.docker_client.volumes.create(name='{}_data'.format(self.cluster_id), driver='local',
                                                       labels={"mdh_data_volume": "true",
                                                               "mdh_cluster_id": self.cluster_id})
            mdh_volumes.append(volume)
        return mdh_volumes

    def _get_or_create_network(self):
        """ Helper method to get or create network for service
        Returns:
            mdh_networks (list): The list of found or created network objects.

        """
        mdh_networks = []
        for _n in self.docker_client.networks.list():
            labels = _n.attrs['Labels']
            if not labels:
                continue
            if labels.get("mdh_network") and labels.get("mdh_cluster_id", "NULL") == self.cluster_id:
                mdh_networks.append(_n)
                return mdh_networks

        if not len(mdh_networks):
            network = self.docker_client.networks.create(name='{}_network'.format(self.cluster_id), driver='bridge',
                                                         labels={"mdh_network": "true",
                                                                 "mdh_cluster_id": self.cluster_id})
            mdh_networks.append(network)
        return mdh_networks

    def _get_or_create_image(self, image_type):
        """ Helper method to get or create docker image
        Returns:
            mdh_images (list): The list of found or created docker image objects.

        """
        mdh_images = []
        for _i in self.docker_client.images.list():
            labels = _i.labels
            if not labels:
                continue
            if labels.get("mdh_{}".format(image_type), "NULL") == "true":
                logging.info(_i)
                mdh_images.append(_i)
        if not len(mdh_images):
            labels = {}
            labels["mdh_{}".format(image_type)] = "true"
            image = self.docker_client.images.build(
                path=os.path.dirname(os.path.realpath(__file__)) + "/assets/{}".format(image_type),
                tag="mdh_{}".format(image_type),
                pull=True,
                labels=labels
            )
            mdh_images.append(image)

        return mdh_images

    def _lookup_next_lb_port(self):
        """ Helper method to identify next available host port
        Returns:
            containers (int): Next next available host port.

        """
        p = []
        for container in self.docker_client.containers.list():
            if container.labels.get("mdh_lb", "null") == "true":
                for _k, _v in container.attrs.get('NetworkSettings').get("Ports").items():
                    if _v:
                        for __v in _v:
                            p.append(int(__v.get('HostPort')))
        if p:
            return sorted(p)[-1] + 1
        return DEFAULT_MDH_LD_PORT

    def setup_cluster_infra(self):
        """ Init cluster infra.
        Returns:
            cluster_data (dict): Created cluster data.

        """
        logging.info("Creating new cluster with id {}".format(self.cluster_id))

        # Build images
        images_to_build = ["statsd", "lb", "elsa", "backend", "prom", "grafana", ]
        images = {}
        for image in images_to_build:
            logging.info("Building {} image".format(image.upper()))
            images["{}_image"] = self._get_or_create_image(image_type=image)

        # Create volumes
        _data_volume = {self._get_or_create_data_volume()[0].attrs['Name']: {'bind': '/data', 'mode': 'rw'}}
        _docker_socket_volume = {'/var/run/docker.sock': {'bind': '/var/run/docker.sock', 'mode': 'rw'}}

        # Create network
        _networks = self._get_or_create_network()
        self.cluster_network = _networks[0]
        logging.info("Network {}".format(self.cluster_network.short_id))

        # Run LB container
        next_available_port, mdh_lb = self.run_lb_container(_data_volume)

        # Run monitoring stuff first
        for name in ["statsd", "prom", "grafana"]:
            self.run_container(name)

        # Run backend container
        self.run_backend_container(_data_volume)

        # Run ELSA container
        self.run_elsa_container(_docker_socket_volume)

        # Start LB container if its not running
        if self.lb_container.status != "running":
            self.lb_container.start()

        res = {"mdh_cluster_id": self.cluster_id,
               "mdh_backends": self.mdh_backends[0].short_id,
               "mdh_lb": self.lb_container.short_id,
               "mdh_elsa": self.elsa_container.short_id,
               "mdh_prom": self.prom_container.short_id,
               "mdh_statsd": self.statsd_container.short_id,
               "mdh_grafana": self.grafana_container.short_id,
               "mdh_network": self.cluster_network.short_id,
               "mdh_port": next_available_port}
        logging.info(res)
        return res

    def run_backend_container(self, _data_volume):
        """ Run backend container

        Args:
            _data_volume (dict): Shared volume

        Returns (obj): Container object

        """
        self.mdh_backends = self._lookup_container_by_label("mdh_backend")
        if not len(self.mdh_backends):
            container = self.run_mdh_backend(_data_volume, "1")
            logging.info("Running BACKEND conatiner {}, Status: {}".format(container.short_id,
                                                                           container.status))
            self.mdh_backends.append(container)
        return self.mdh_backends

    def run_lb_container(self, _data_volume):
        """Run load balancer container

        Args:
            _data_volume (dict): Shared volume

        Returns (tuple): Tuple of attached load balancer external port and load balancer Container object

        """
        next_available_port = DEFAULT_MDH_LD_PORT
        mdh_lb = self._lookup_container_by_label("mdh_lb")
        if not len(mdh_lb):
            next_available_port = self._lookup_next_lb_port()
            self.lb_container = self.docker_client.containers.run('mdh_lb',
                                                                  name="mdh_lb_{}".format(self.cluster_id),
                                                                  labels=dict(mdh_lb="true",
                                                                              mdh_cluster_id=self.cluster_id),
                                                                  ports={'5000/tcp': next_available_port},
                                                                  environment={"MDH_CLUSTER_ID": self.cluster_id,
                                                                               "MDH_BACKEND_PORT": os.environ.get(
                                                                                   "MDH_BACKEND_PORT", 5000),
                                                                               "MDH_HOSTNAME": "mdh_ld"
                                                                               },
                                                                  volumes=_data_volume,
                                                                  detach=True)
            logging.info("Running LB conatiner {}, Status: {}".format(self.lb_container.short_id,
                                                                      self.lb_container.status))
            self.cluster_network.connect(self.lb_container, aliases=["mdh_lb"])
            mdh_lb.append(self.lb_container.short_id)
        return next_available_port, mdh_lb

    def run_container(self, container_name):
        """ Run general container. If vontainer already exist it just returns list with container
        Args:
            container_name (str): Container image name for example prom, grafana eg

        Returns (list): Container list

        """
        container_list = self._lookup_container_by_label("mdh_{}".format(container_name))
        if not len(container_list):
            env = {"MDH_CLUSTER_ID": self.cluster_id, "MDH_HOSTNAME": "mdh_{}".format(container_name)}
            if container_name == "grafana":
                env.update({"GF_SECURITY_ADMIN_PASSWORD": self.cluster_id[:10]})
            container = self.docker_client.containers.run('mdh_{}'.format(container_name),
                                                          name="mdh_{}_{}".format(container_name, self.cluster_id),
                                                          labels={"mdh_{}".format(container_name): "true",
                                                                  "mdh_cluster_id": self.cluster_id},
                                                          environment=env,
                                                          volumes_from=[self.lb_container.name],
                                                          detach=True)
            self.cluster_network.connect(container, aliases=["mdh_{}".format(container_name)])
            setattr(self, "{}_container".format(container_name), container)
            container_list.append(container.short_id)
            logging.info("Running {} conatiner {}, Status: {}".format(container_name.upper(),
                                                                      container.short_id,
                                                                      container.status))
        return container_list

    def run_elsa_container(self, _docker_socket_volume):
        """ Run ELSA container.
        Args:
            _docker_socket_volume (dict): Shared host volume to access docker info

        Returns (list): Container list

        """
        mdh_elsa = self._lookup_container_by_label("mdh_elsa")
        if not len(mdh_elsa):
            elsa_volumes = {}
            elsa_volumes.update(_docker_socket_volume)
            self.elsa_container = self.docker_client.containers.run('mdh_elsa',
                                                                    name="mdh_elsa_{}".format(self.cluster_id),
                                                                    labels=dict(mdh_elsa="true",
                                                                                mdh_cluster_id=self.cluster_id),
                                                                    environment={"MDH_CLUSTER_ID": self.cluster_id,
                                                                                 "MDH_BACKEND_PORT": os.environ.get(
                                                                                     "MDH_BACKEND_PORT", 5000),
                                                                                 "MDH_HOSTNAME": "mdh_elsa"
                                                                                 },
                                                                    volumes_from=[self.lb_container.name],
                                                                    volumes=elsa_volumes,
                                                                    detach=True)
            self.cluster_network.connect(self.elsa_container, aliases=["mdh_elsa"])
            mdh_elsa.append(self.elsa_container.short_id)
            logging.info("Running ELSA conatiner {}, Status: {}".format(self.elsa_container.short_id,
                                                                        self.elsa_container.status
                                                                        ))
        return mdh_elsa

    def run_mdh_backend(self, _data_volume, nr):
        """ Run mdh_backend image

        Args:
            _data_volume (dict): Shared data volume
            nr (str): Backend container number

        Returns:
            container (object): Created container object

        """
        container = self.docker_client.containers.run('mdh_backend',
                                                      name="mdh_backend{}_{}".format(nr, self.cluster_id),
                                                      labels=dict(mdh_backend="true",
                                                                  mdh_cluster_id=self.cluster_id,
                                                                  mdh_backend_member_nr=nr),
                                                      environment={"MDH_CLUSTER_ID": self.cluster_id,
                                                                   "MDH_BACKEND_PORT":
                                                                       os.environ.get("MDH_BACKEND_PORT", 5000),
                                                                   "MDH_HOSTNAME": "mdh_backend{}".format(nr)
                                                                   },
                                                      volumes=_data_volume,
                                                      detach=True)
        self.cluster_network.connect(container, aliases=["mdh_backend{}".format(nr)])
        return container

    def show_cluster(self, show_all=False):
        """ Show cluster status

        Args:
            show_all (bool): True returns all clusters, False return only self.cluster_id info

        Returns:
            res (list): List of cluster(s)

        """
        res = []
        clusters = self._show_all_mdh_cluster_ids()
        if isinstance(self.args, ArgumentParser):
            print("Cluster ID\t\t\t\tContainer Name\t\t\t\t\t\t\tContainer ID")
        if self.cluster_id not in clusters or show_all:
            for cluster_id in clusters:
                containers = []
                for container in list(filter(lambda x: x.get("Labels").get("mdh_cluster_id", "not_set") == cluster_id,
                                             self.docker_client.api.containers())):
                    containers.append(container)
                    if isinstance(self.args, ArgumentParser):
                        print("{}\t{}\t{}".format(container.get("Labels").get("mdh_cluster_id"),
                                                  container.get("Names")[0].split("/")[1],
                                                  container.get("Id")))
                res.append({cluster_id: containers})

        else:
            for container in list(filter(lambda x: x.get("Labels").get("mdh_cluster_id", "not_set") == self.cluster_id,
                                         self.docker_client.api.containers())):
                if isinstance(self.args, ArgumentParser):
                    print("{}\t{}\t{}".format(container.get("Labels").get("mdh_cluster_id"),
                                              container.get("Names")[0].split("/")[1], container.get("Id")))
                res.append(container)
        return res

    def get_all_backend_nodes(self):
        """ Get cluster backned conatiners

        Returns (list): List of sorted backend containers

        """
        containers = self._lookup_container_by_label("mdh_backend")
        return sorted(containers, key=lambda x: x.labels.get("mdh_backend_member_nr"))

    def add_node_to_cluster(self):
        """ Add backend node to cluster

        Returns:
            res (list): Cluster status

        """
        self.mdh_backends = self.get_all_backend_nodes()
        last_backend_nr = sorted(list(map(lambda x: int(x.labels.get("mdh_backend_member_nr")), self.mdh_backends)))[-1]
        self.run_mdh_backend(self.cluster_data_volume, str(last_backend_nr + 1))
        return self.show_cluster()

    def remove_node_from_cluster(self):
        """ Removes node from cluster

        Returns:
            res (list): Cluster status

        """
        self.mdh_backends = self.get_all_backend_nodes()
        if len(self.mdh_backends) > 1:
            if self.args.node_name:
                container = self._lookup_container_by_name(self.args.node_name)[0]
                container.stop()
                container.remove()
                self.show_cluster()
                return
            last_backend_node = self.mdh_backends[-1]
            last_backend_node.stop()
            last_backend_node.remove()
        return self.show_cluster()

    def prepare(self):
        """ Helper to prepare current class

        Returns:
            status (bool): Status of prepare. True on successful info retrieval.
            False if cluster_id is missing from clusters.
        """
        clusters = self._show_all_mdh_cluster_ids()
        if self.cluster_id not in clusters:
            print("--cluster-id is missing")
            return False
        self.cluster_network = self._get_or_create_network()[0]
        self.cluster_data_volume = {self._get_or_create_data_volume()[0].attrs['Name']: {'bind': '/data', 'mode': 'rw'}}
        self.mdh_backends = self.get_all_backend_nodes()
        return True

    def invoke(self):
        """ Helper method for cli
        """

        if "init" in getattr(self.args, "cmd"):
            self.setup_cluster_infra()
        elif "show" in getattr(self.args, "cmd"):
            self.show_cluster()
        elif "delete" in getattr(self.args, "cmd"):
            self.remove_cluster()
        elif "+" in getattr(self.args, "cmd"):
            if self.prepare():
                self.add_node_to_cluster()
        elif "-" in getattr(self.args, "cmd"):
            if self.prepare():
                self.remove_node_from_cluster()

    def remove_cluster(self):
        """ Removes all instances from cluster

        Returns (list): Removed containers statuses

        """
        res = []
        clusters = self._show_all_mdh_cluster_ids()
        if len(clusters) == 1 and not isinstance(self.args, ArgumentParser):
            if clusters[0] == self.cluster_id:
                return res
        for container in self.show_cluster():
            res.append({"stop": container.stop(), "remove": container.remove()})
        return res
