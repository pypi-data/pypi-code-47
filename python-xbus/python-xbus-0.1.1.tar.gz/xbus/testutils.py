from . import client, envelope_writer, xbus_pb2
from .envelope_receiver import EnvelopeReceiver


class Actor:
    def __init__(self, id_, name, kind, roles, settings={}):
        self.client = None
        self.id = id_
        self.name = name
        self.kind = kind
        self.roles = roles
        self.settings = client.Settings(settings)


# build an envelope from [('eventtype', 'content' or [items])]
async def make_envelope(*events):
    result = None

    async def send(fragment):
        nonlocal result
        result = fragment

    writer = envelope_writer.EnvelopeWriter(send, [name for name, _ in events])
    for name, content in events:
        if not isinstance(content, list):
            content = [content]
        print(content)
        await writer.add_items(name, *content)

    await writer.close()

    return result


async def make_request(**inputs):
    r = xbus_pb2.ActorProcessRequest()
    for inputname, envelope in inputs.items():
        in_ = r.inputs.add()
        in_.name = inputname
        if isinstance(envelope, tuple):
            envelope = await make_envelope(envelope)
        elif isinstance(envelope, list):
            envelope = await make_envelope(*envelope)
        in_.envelope.CopyFrom(envelope)
    return r


class APC:
    def __init__(self, actor, request):
        self.actor = actor
        self.request = request
        self.outputs = {}

    def detach(self):
        self._detached = True

    async def success(self):
        self._success = True

    async def error(self, err):
        self._error = err

    def read_envelope(self, input_name):
        for input_ in self.request.inputs:
            if input_.name == input_name:
                return EnvelopeReceiver(input_name, input_.envelope)

    async def read_envelope_complete(self, input_name, timeout):
        er = self.read_envelope(input_name)
        return await er.complete(timeout)

    def open_output(self, output, eventtypes):
        async def send(fragment):
            self.outputs.setdefault(output, []).append(fragment)

        return envelope_writer.EnvelopeWriter(send, eventtypes)
