import abc

from optparse import OptionParser

import requests
from service_mapping_plugin_framework import settings


class DeallocateNSSIabc(metaclass=abc.ABCMeta):

    def __init__(self, nm_host, nfvo_host, subscription_host):
        global nsst_id

        self.NM_URL = settings.NM_URL.format(nm_host)
        self.NFVO_URL = settings.NFVO_URL.format(nfvo_host)
        self.SUBSCRIPTION_HOST = settings.SUBSCRIPTION_HOST.format(subscription_host)

        parser = OptionParser()
        parser.add_option("-n", "--nsst-id", help="Network Slice Subnet Template")
        (options, args) = parser.parse_args()
        nsst_id = options.nsst_id

    def get_nsst(self):
        global nsst_object
        url = settings.NM_URL + "NSS/Template/" + nsst_id
        nsst_object = requests.get(url, headers=settings.HEADERS)
        # TODO Change procedure
        # Get slice moi
        nssiid = str(id).replace('-', "")
        scope = ["BASE_NTH_LEVEL", 2]
        url = "http://localhost:8000/ObjectManagement/NetworkSliceSubnet/{}/".format(nssiid)
        payload = {'scope': str(scope),
                   'filter': "nssiId='{}'".format(nssiid)}
        headers = {'Content-type': 'application/json'}
        get_moi = requests.get(url, params=payload, headers=headers)
        slice_moi = get_moi.json()
        print(slice_moi)

        # Nsinfo assign
        nsinfo = slice_moi['attributeListOut'][0]['nsInfo']
        ns_instance = nsinfo['nsInstanceId']
        ns_descriptor = nsinfo['nsdInfoId']
        vnf_package = eval(nsinfo['vnfInfo'])
        monitor_parameter = eval(nsinfo['monitoringParameter'])
        vnfp_subscription = monitor_parameter['vnfp_subscription']
        nsd_subscription = monitor_parameter['nsd_subscription']
        nsi_subscription = monitor_parameter['nsi_subscription']

        print("Network service instance ID: {}".format(ns_instance))
        print("Network service descriptor ID: {}".format(ns_descriptor))
        print("Vnf package ID List: {}".format(vnf_package))
        print("Network service instance subscription ID: {}".format(nsi_subscription))
        print("Network service descriptor subscription ID: {}".format(nsd_subscription))
        print("Vnf package subscription ID List: {}".format(vnfp_subscription))

    def ns_termination(self):
        self.terminate_network_service_instance()
        self.delete_network_service_instance()
        self.update_network_service_descriptor()
        self.delete_network_service_descriptor()

    def nf_provisioning(self):
        self.update_vnf_package()
        self.delete_vnf_package()

    @abc.abstractmethod
    def coordinate_tn_manager(self):
        return NotImplemented

    @abc.abstractmethod
    def terminate_network_service_instance(self):
        return NotImplemented

    @abc.abstractmethod
    def delete_network_service_instance(self):
        return NotImplemented

    @abc.abstractmethod
    def update_network_service_descriptor(self):
        return NotImplemented

    @abc.abstractmethod
    def delete_network_service_descriptor(self):
        return NotImplemented

    @abc.abstractmethod
    def update_vnf_package(self):
        return NotImplemented

    @abc.abstractmethod
    def delete_vnf_package(self):
        return NotImplemented

    def allocate_nssi(self):  # TODO: if use existing nssi
        self.get_nsst()
        self.nf_provisioning()
        self.coordinate_tn_manager()
