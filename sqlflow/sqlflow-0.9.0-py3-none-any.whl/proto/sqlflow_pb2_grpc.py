# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from sqlflow.proto import sqlflow_pb2 as sqlflow_dot_proto_dot_sqlflow__pb2


class SQLFlowStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Run = channel.unary_stream(
        '/proto.SQLFlow/Run',
        request_serializer=sqlflow_dot_proto_dot_sqlflow__pb2.Request.SerializeToString,
        response_deserializer=sqlflow_dot_proto_dot_sqlflow__pb2.Response.FromString,
        )
    self.Fetch = channel.unary_unary(
        '/proto.SQLFlow/Fetch',
        request_serializer=sqlflow_dot_proto_dot_sqlflow__pb2.FetchRequest.SerializeToString,
        response_deserializer=sqlflow_dot_proto_dot_sqlflow__pb2.FetchResponse.FromString,
        )


class SQLFlowServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Run(self, request, context):
    """Run executes a sql statement

    SQL statements like `SELECT ...`, `DESCRIBE ...` returns a rowset.
    The rowset might be big. In such cases, Query returns a stream
    of RunResponse

    SQLFlow implements the Run interface with two mode:

    1. Local model
    The SQLFlow server execute the SQL statements on the localhost.

    SQL statements like `USE database`, `DELETE` returns only a success
    message.

    SQL statement like `SELECT ... TO TRAIN/PREDICT ...` returns a stream of
    messages which indicates the training/predicting progress

    2. Argo Workflow mode
    The SQLFlow server submits an Argo workflow into a Kubernetes cluster,
    and returns a stream of messages indicates the WorkFlow ID and the 
    submitting progress.

    The SQLFlow gRPC client should fetch the logs of the workflow by
    calling the Fetch interface in a polling manner.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Fetch(self, request, context):
    """Fetch fetches the SQLFlow job phase and logs in a polling manner. A corresponding
    client can be implemented as

    wfJob := Submit(argoYAML)
    req := &FetchRequest {
    Job : { Id: wfJob },
    }
    for {
    res := Fetch(req)
    fmt.Println(res.Logs)
    if isComplete(res) {
    break
    }
    req = res.UpdatedFetchSince
    time.Sleep(time.Second)
    }

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SQLFlowServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Run': grpc.unary_stream_rpc_method_handler(
          servicer.Run,
          request_deserializer=sqlflow_dot_proto_dot_sqlflow__pb2.Request.FromString,
          response_serializer=sqlflow_dot_proto_dot_sqlflow__pb2.Response.SerializeToString,
      ),
      'Fetch': grpc.unary_unary_rpc_method_handler(
          servicer.Fetch,
          request_deserializer=sqlflow_dot_proto_dot_sqlflow__pb2.FetchRequest.FromString,
          response_serializer=sqlflow_dot_proto_dot_sqlflow__pb2.FetchResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.SQLFlow', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
