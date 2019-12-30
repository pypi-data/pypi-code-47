import grpc
from google.protobuf.json_format import ParseDict
from mesh_rpc.mesh import MeshRPC
from mesh_rpc.exp import MeshRPCException

from .lib.solar_production_pb2 import FeedMessage
from .defaults import Default

class MeshSolarPowerProduction(MeshRPC):
    def __init__(self, endpoint='127.0.0.1:5555'):
        super().__init__(endpoint)

    def subscribe(self, geospace):
        s = super().subscribe(Default.channel, geospace)

        feed = FeedMessage()

        channelLen = len(Default.channel)

        try:
            for msg in s:
                feed.ParseFromString(msg.raw)
                yield feed, msg.topic.pop()[channelLen:]
        except grpc.RpcError as e:
            raise MeshRPCException(e.details())
    
    def unsubscribe(self, geospaces):
        return super().unsubscribe(Default.channel, geospaces)
    
    def registerToPublish(self, geospace):
        try:
            super().registerToPublish(Default.channel, geospace)
        except MeshRPCException as e:
            raise 

    def publish(self, geospace, d):
        d['header']['version'] = "0.0.1"
        
        feed = FeedMessage()
        ParseDict(d, feed, True)
        raw = feed.SerializeToString()

        try:
            res = super().publish(Default.channel, geospace, raw)
        except MeshRPCException as e:
            raise 
    
    def get_channel(self):
        return Default.channel
    
