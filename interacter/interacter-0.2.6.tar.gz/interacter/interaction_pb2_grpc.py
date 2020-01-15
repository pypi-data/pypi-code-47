# File: interaction_pb2_grpc.py
# Author: Edwinn Gamborino
# Institution: NTU Center for Artificial Intelligence and Advanced Robotics
# Version: v0.2.6

import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
import interaction_pb2 as interaction__pb2

class InteractStub(object):
  """The interact service definition.
  """

  def __init__(self, channel):
    """Constructor.
    Args:
      channel: A grpc.Channel.
    """
    self.RobotConnect = channel.unary_unary(
        '/interaction.Interact/RobotConnect',
        request_serializer=interaction__pb2.RobotConnectRequest.SerializeToString,
        response_deserializer=interaction__pb2.RobotConnectReply.FromString,
        )
    self.TabletConnect = channel.unary_unary(
        '/interaction.Interact/TabletConnect',
        request_serializer=interaction__pb2.TabletConnectRequest.SerializeToString,
        response_deserializer=interaction__pb2.TabletConnectReply.FromString,
        )
    self.RobotSend = channel.unary_unary(
        '/interaction.Interact/RobotSend',
        request_serializer=interaction__pb2.RobotInput.SerializeToString,
        response_deserializer=interaction__pb2.RobotOutput.FromString,
        )
    self.TabletSend = channel.unary_unary(
        '/interaction.Interact/TabletSend',
        request_serializer=interaction__pb2.TabletInput.SerializeToString,
        response_deserializer=interaction__pb2.TabletOutput.FromString,
        )


class InteractServicer(object):
  """The interact service definition.
  """

  def RobotConnect(self, request, context):
    """Sends connection confirm
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TabletConnect(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RobotSend(self, request, context):
    """Sends information
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TabletSend(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InteractServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RobotConnect': grpc.unary_unary_rpc_method_handler(
          servicer.RobotConnect,
          request_deserializer=interaction__pb2.RobotConnectRequest.FromString,
          response_serializer=interaction__pb2.RobotConnectReply.SerializeToString,
      ),
      'TabletConnect': grpc.unary_unary_rpc_method_handler(
          servicer.TabletConnect,
          request_deserializer=interaction__pb2.TabletConnectRequest.FromString,
          response_serializer=interaction__pb2.TabletConnectReply.SerializeToString,
      ),
      'RobotSend': grpc.unary_unary_rpc_method_handler(
          servicer.RobotSend,
          request_deserializer=interaction__pb2.RobotInput.FromString,
          response_serializer=interaction__pb2.RobotOutput.SerializeToString,
      ),
      'TabletSend': grpc.unary_unary_rpc_method_handler(
          servicer.TabletSend,
          request_deserializer=interaction__pb2.TabletInput.FromString,
          response_serializer=interaction__pb2.TabletOutput.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'interaction.Interact', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
