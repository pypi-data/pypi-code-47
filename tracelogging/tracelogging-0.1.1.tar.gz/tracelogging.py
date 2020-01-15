from typing import NewType
"""
tracelogging
"""
from ctypes import *
from abc import ABC, ABCMeta, abstractmethod
import functools
import logging
import hashlib
import uuid
from typing import List, Tuple, Callable
from enum import Enum
import inspect
import sys
import os
import struct

# TODO: chunks
# TODO: out type for each field
# TODO: complex types/lists
# TODO: tests


def setup_logging(loggername, stream=sys.stdout):
    logger = logging.getLogger(loggername)
    logger.addHandler(logging.NullHandler())

    try:
        level = int(os.getenv('TLG_LOG', 0))
    except:
        level = 0

    if level:
        handler = logging.StreamHandler(stream)
        formatter = logging.Formatter(
            '%(asctime)s | %(funcName)25s:%(lineno)-4d | %(levelname)-9s | %(message)s', '%Y%m%d %H:%M:%S')
        handler.setFormatter(formatter)
        handler.setLevel(logging.DEBUG)

        logger.addHandler(handler)
        logger.setLevel(level)

    return logger


l = setup_logging('tracelogging')

# ---------------------------------------------native---------------------------------------------
advapi = windll.advapi32


class NativeErrorCode(Exception):
    pass


class EventDefinitionError(Exception):
    pass


class EventDispatchingError(Exception):
    pass


class MissingTypeForEventParamError(EventDefinitionError):
    pass


class UnsupportedTypeForEventParamError(EventDefinitionError):
    pass


class MissingEventParameter(EventDispatchingError):
    pass


class BadParameterValue(EventDispatchingError):
    pass


class EventDropped(EventDispatchingError):
    pass


class TraceLevel(Enum):
    Always = 0
    Critical = 1
    Error = 2
    Warning = 3
    Information = 4
    Verbose = 5


class EVENT_DESCRIPTOR(Structure):
    """
    typedef struct _EVENT_DESCRIPTOR {
        USHORT    Id;
        UCHAR     Version;
        UCHAR     Channel;
        UCHAR     Level;
        UCHAR     Opcode;
        USHORT    Task;
        ULONGLONG Keyword;
    } EVENT_DESCRIPTOR, *PEVENT_DESCRIPTOR;
    """

    _fields_ = [
        ('Id', c_uint16),
        ('Version', c_uint8),
        ('Channel', c_uint8),
        ('Level', c_uint8),
        ('Opcode', c_uint8),
        ('Task', c_uint16),
        ('Keyword', c_uint64)
    ]


class EVENT_DATA_DESCRIPTOR(Structure):
    """
    typedef struct _EVENT_DATA_DESCRIPTOR {
        ULONGLONG Ptr;
        ULONG     Size;
        ULONG Reserved;
    } EVENT_DATA_DESCRIPTOR, *PEVENT_DATA_DESCRIPTOR;
    """
    _fields_ = [
        ('Ptr', c_ulonglong),
        ('Size', c_uint32),
        ('Reserved', c_uint32),
    ]


class EventInformationClass(Enum):
    EventProviderBinaryTrackInfo = 0
    EventProviderSetReserved1 = 1
    EventProviderSetTraits = 2  # only this is required
    EventProviderUseDescriptorType = 3
    MaxEventInfo = 4


class EventDataDescriptorType(Enum):
    # the field is ignored unless EventInformationClass.EventProviderSetTraits was set
    EVENT_DATA_DESCRIPTOR_TYPE_NONE = 0
    EVENT_DATA_DESCRIPTOR_TYPE_EVENT_METADATA = 1
    EVENT_DATA_DESCRIPTOR_TYPE_PROVIDER_METADATA = 2


advapi.EventRegister.restype = c_ulong
advapi.EventRegister.argtypes = [
    c_char_p, c_void_p, c_void_p, POINTER(c_ulonglong)
]

advapi.EventSetInformation.restype = c_ulong
advapi.EventSetInformation.argtypes = [
    c_ulonglong, c_ulong, c_void_p, c_ulong
]


advapi.EventProviderEnabled.restype = c_ulong
advapi.EventProviderEnabled.argtypes = [
    c_ulonglong, c_uint8, c_ulonglong
]

advapi.EventEnabled.restype = c_ulong
advapi.EventEnabled.argtypes = [
    c_ulonglong, POINTER(EVENT_DESCRIPTOR)
]

advapi.EventWrite.argtypes = [
    c_ulonglong, POINTER(EVENT_DESCRIPTOR), c_uint32, POINTER(
        EVENT_DATA_DESCRIPTOR)
]


def EventRegister(guid: uuid.UUID):
    # TODO: implement callback
    # TODO: check bytes_le
    hProvider = c_ulonglong()
    err = advapi.EventRegister(guid.bytes_le, None, None, byref(hProvider))
    if err:
        raise NativeErrorCode('EventRegister failed', GetLastError())

    return hProvider


def EventSetInformation(hProvider, eventInfoClass: EventInformationClass, buf: bytes):
    # this can only be called once for a provider
    err = advapi.EventSetInformation(
        hProvider, eventInfoClass.value, buf, len(buf))
    if err:
        raise NativeErrorCode('EventSetInformation failed', GetLastError())


def EventProviderEnabled(hProvider, level: TraceLevel, keyword: int) -> bool:
    return advapi.EventProviderEnabled(hProvider, level.value, keyword)


def EventEnabled(hProvider, eventDescriptor: EVENT_DESCRIPTOR):
    return advapi.EventEnabled(hProvider, eventDescriptor)


def EventWrite(hProvider, eventDescriptor: EVENT_DESCRIPTOR, data_descriptors: List[Tuple[EventDataDescriptorType, bytes]], throw_on_err=False):
    # this can only be called once for a provider
    p = (EVENT_DATA_DESCRIPTOR*len(data_descriptors))()
    for idx, (data_type, data) in enumerate(data_descriptors):
        l.debug(f'setting up data descriptor {idx} as {data_type}')
        dataptr = c_char_p(data)

        p[idx].Ptr = cast(pointer(dataptr), POINTER(c_ulonglong)).contents
        p[idx].Size = len(data)
        p[idx].Reserved = data_type.value

    return advapi.EventWrite(hProvider, byref(eventDescriptor),
                             len(data_descriptors), cast(p, POINTER(EVENT_DATA_DESCRIPTOR)))


def EventUnregister(hProvider):
    advapi.EventUnregister(hProvider)

# ------------------------------------------------------------------------------------------------


POINTER_SIZE = sizeof(c_void_p)


class ParamTypeIn(Enum):
    TlgInNULL = 0
    TlgInUNICODESTRING = 1
    TlgInANSISTRING = 2
    TlgInINT8 = 3
    TlgInUINT8 = 4
    TlgInINT16 = 5
    TlgInUINT16 = 6
    TlgInINT32 = 7
    TlgInUINT32 = 8
    TlgInINT64 = 9
    TlgInUINT64 = 10
    TlgInFLOAT = 11
    TlgInDOUBLE = 12
    TlgInBOOL32 = 13
    TlgInBINARY = 14
    TlgInGUID = 15
    _TlgInPOINTER_unsupported = 16
    TlgInFILETIME = 17
    TlgInSYSTEMTIME = 18
    TlgInSID = 19
    TlgInHEXINT32 = 20
    TlgInHEXINT64 = 21

    # Note: TlgInCOUNTEDSTRING != TDH_INTYPE_COUNTEDSTRING.
    # Semantics are the same, but enum value is different.
    TlgInCOUNTEDSTRING = 22

    # Note: TlgInCOUNTEDANSISTRING != TDH_INTYPE_COUNTEDANSISTRING.
    # Semantics are the same, but enum value is different.
    TlgInCOUNTEDANSISTRING = 23

    _TlgInSTRUCT = 24
    # New values go above this line but _TlgInMax must not exceed 32.
    _TlgInMax = 25

    TlgInINTPTR = TlgInINT64 if POINTER_SIZE == 8 else TlgInINT32
    TlgInUINTPTR = TlgInUINT64 if POINTER_SIZE == 8 else TlgInUINT32
    TlgInPOINTER = TlgInHEXINT64 if POINTER_SIZE == 8 else TlgInHEXINT32

    # Indicates that field metadata contains a const-array-count tag.
    _TlgInCcount = 32
    # Indicates that field data contains variable-array-count tag.
    TlgInVcount = 64
    _TlgInChain = 128  # Indicates that field metadata contains a TlgOut tag.
    # Indicates that the field uses a custom serializer.
    _TlgInCustom = TlgInVcount | _TlgInCcount
    _TlgInTypeMask = 31
    _TlgInCountMask = TlgInVcount | _TlgInCcount
    _TlgInFlagMask = _TlgInChain | TlgInVcount | _TlgInCcount


class Types(object):
    # types for annotations of events:
    # Using custom types since aliases won't work. Will cause errors if checked using static checkers

    UnicodeString = NewType('TlgWideString', str)
    CountedUnicodeString = NewType('TlgCountedWideString', str)

    UInt32 = NewType('TlgUint32', int)
    Int32 = NewType('TlgInt32', int)

    UInt64 = NewType('TlgUint64', int)
    Int64 = NewType('TlgInt64', int)

    Double = NewType('TlgDouble', float)


class EventField(ABC):

    # TODO: support param tlgout
    @property
    @abstractmethod
    def InType(cls):
        pass

    @property
    @abstractmethod
    def Format(cls):
        pass

    def __init__(self, name):
        self.name = name

    def pack(self, data) -> bytes:
        l.debug(
            f'packing {self.name} as {self.InType.name} using "{self.Format}"')
        try:
            buf = struct.pack(self.Format, data)
        except struct.error as e:
            raise BadParameterValue from e

        return buf

    def __bytes__(self):
        null_terminator = (0).to_bytes(1, byteorder='little')
        in_type = (self.InType.value).to_bytes(1, byteorder='little')
        name_buf = bytes(self.name, encoding='utf-8')
        return name_buf+null_terminator + in_type


class EtwUnicodeString(EventField):
    InType: ParamTypeIn = ParamTypeIn.TlgInUNICODESTRING
    Format = ''  # overriding pack

    def pack(self, data: str) -> bytes:
        # null terminator
        return bytes(data, encoding='utf-16-le') + (0).to_bytes(2, byteorder='little')


class EtwCountedUnicodeString(EventField):
    InType: ParamTypeIn = ParamTypeIn.TlgInCOUNTEDSTRING
    Format = ''  # overriding pack

    def pack(self, data: str) -> bytes:
        buf = bytes(data, encoding='utf-16-le')
        cb = len(buf)
        return (cb).to_bytes(2, byteorder='little') + buf


class EtwUInt32(EventField):
    InType: ParamTypeIn = ParamTypeIn.TlgInUINT32
    Format = '<I'


class EtwInt32(EventField):
    InType: ParamTypeIn = ParamTypeIn.TlgInINT32
    Format = '<i'


class EtwUInt64(EventField):
    InType: ParamTypeIn = ParamTypeIn.TlgInUINT64
    Format = '<Q'


class EtwInt64(EventField):
    InType: ParamTypeIn = ParamTypeIn.TlgInINT64
    Format = '<q'


class EtwDouble(EventField):
    InType: ParamTypeIn = ParamTypeIn.TlgInDOUBLE
    Format = '<d'


class EventMetadata(object):
    SUPPORTED_ANNOTATIONS = {
        Types.UnicodeString: EtwUnicodeString,
        Types.CountedUnicodeString: EtwCountedUnicodeString,
        Types.UInt32: EtwUInt32,
        Types.Int32: EtwInt32,
        Types.UInt64: EtwUInt64,
        Types.Int64: EtwInt64,
        Types.Double: EtwDouble,
    }

    # TODO: parse target function spec convert to tlg enum with packer/unpacker

    def __init__(self, name, fields: List[EventField]):  # TODO: fields
        self.name = name
        self.fields = fields
        self.buf = self.build(self.name, self.fields)

    @staticmethod
    def build(name: str, fields: List[EventField]):
        name = bytes(name, encoding='utf-8')
        extension = null_terminator = (0).to_bytes(1, byteorder='little')

        #TODO: logging
        fields_buf = b''.join((bytes(f) for f in fields))

        buf = extension + name + null_terminator + fields_buf
        total_len = len(buf)+2  # for the size
        buf = total_len.to_bytes(2, byteorder='little')+buf
        return buf

    @classmethod
    # TODO: use spec instead?
    def from_target(cls, targetfunction: Callable, name_override: str = '', instancemethod=True):
        fname = targetfunction.__name__
        fline = targetfunction.__code__.co_firstlineno
        fmodule = targetfunction.__module__
        event_name = name_override or fname
        # TODO: validate eventname
        sig = inspect.signature(targetfunction)
        l.info(
            f'parsing {fmodule}.{targetfunction.__name__} event name:{event_name}')

        params = iter(sig.parameters.items())
        if instancemethod:
            # TODO: infer this myself
            l.info('method bound')
            next(params)

        fields = []
        for pname, param in params:
            l.debug(f'parsing {fname}@{fline}')
            if param.annotation == param.empty:
                l.error(
                    f'no annotation for {fname}@{fline}.{pname}')
                raise MissingTypeForEventParamError(
                    f'type for {pname} is missing in {targetfunction.__name__} @ {fline}')

            if param.annotation not in cls.SUPPORTED_ANNOTATIONS:
                raise UnsupportedTypeForEventParamError()

            fldKlass = cls.SUPPORTED_ANNOTATIONS[param.annotation]
            fields.append(fldKlass(pname))

        return EventMetadata(event_name, fields)

    def pack(self, *args, **kwargs) -> bytes:
        buf = b''
        for idx, a in enumerate(args):
            f = self.fields[idx]
            l.debug(f'packing field number {idx}: {f.name}')
            buf += f.pack(a)

        if kwargs:
            l.debug('checking for missing args')
            # kwargs will always be populated if defaults were given in definition-
            # even if enough arguments were provided, in that case iterator will be empty.
            for f in self.fields[idx+1:]:
                l.debug(f'looking up value for field {f.name}')
                if not f.name in kwargs:
                    l.error(f'missing value for field {f.name}')
                    raise MissingEventParameter('missing field name', f.name)

                buf += f.pack(kwargs[f.name])

        return buf

    def __bytes__(self):
        return self.buf

    def unpack(self, buf: bytes):
        pass  # would be nice


class SelfDescribingEvent(object):
    def __init__(self, Id,  Version, Level, Channel, Opcode, Keyword, Task):
        self.metadata = None
        self.descriptor = EVENT_DESCRIPTOR(Id=Id, Version=Version,
                                           Level=Level.value, Channel=Channel,
                                           Opcode=Opcode, Keyword=Keyword, Task=Task)

    def set_metadata(self, metadata: EventMetadata):
        assert self.metadata is None
        self.metadata = metadata


class EventDispatcher(object):
    def __init__(self, target, event: SelfDescribingEvent):
        # TODO: support call_target_even_if_disabled, currently is always
        self.target = target
        self.event = event
        self.defaults = {
            k: v.default
            for k, v in inspect.signature(target).parameters.items()
            if v.default is not inspect.Parameter.empty
        }

    def __get__(self, obj, objtype):
        # to support instance method
        return functools.partial(self.__call__, obj)

    def __call__(self, otherself, *args, **kwargs):
        # using otherself
        l.info('passing event data')

        # this is done to mimic behavior of defaults in target function
        kwargs_with_defaults = {}
        kwargs_with_defaults.update(self.defaults)
        kwargs_with_defaults.update(kwargs)

        # TODO: cast field types on args?
        otherself._write(self.event, args, kwargs_with_defaults)
        l.info('calling method')
        l.debug(f'args:{args}, kwargs:{kwargs}')
        return self.target(otherself, *args, **kwargs)


class EventDefinition(object):

    def __init__(self,  event: SelfDescribingEvent, name: str):
        self.event = event
        self.name = name

    def __call__(self, target):
        l.info('building event meta')
        l.info('passing event built data to dispatcher')
        mtdta = EventMetadata.from_target(target, self.name)
        self.event.set_metadata(mtdta)
        return EventDispatcher(target, self.event)


# TODO: figure out why ID was changed in consumer to 0xfeff
def event(Name=None, Id=0,   Version=0, Level: TraceLevel = TraceLevel.Information, Channel=0, Opcode=0, Keyword=0, Task=0):
    # id 0 is used to tell the metaclass to generate an event by itself.
    e = SelfDescribingEvent(Id, Version, Level,
                            Channel, Opcode, Keyword, Task)
    return EventDefinition(e, Name)


def traceevent_guid_from_name(name):
    event_source_seed = uuid.UUID('482c2db2-c390-47c8-87f8-1a15bfc130fb')
    name_hash = hashlib.sha1(event_source_seed.bytes +
                             bytes(name.upper().encode('utf-16-be'))).digest()
    guid = uuid.UUID(bytes_le=name_hash[: 16])
    guid2 = uuid.UUID(fields=(guid.time_low, guid.time_mid,
                              (guid.time_hi_version & 0x0FFF) | 0x5000,
                              guid.clock_seq_hi_variant, guid.clock_seq_low, guid.node))
    return guid2


class ProviderDefinition(ABCMeta):
    _instances = {}

    def __new__(meta, name, bases, dct):
        l.info(f'defining new provider: {name}')
        meta.__setup_provider_fields(name, dct)
        return super(ProviderDefinition, meta).__new__(meta, name, bases, dct)

    def __init__(mcs, name, bases, dct):
        inherited_events = {}
        for base in bases:
            try:
                inherited_events.update(base._events)
            except AttributeError:
                pass

        mcs.__collect_events(dct, inherited_events)

    def __setup_provider_fields(name, dct):
        '''
        initialize the fields of the provider
        '''
        provider_name = dct.get('Name', name)
        provider_guid = dct.get(
            'Guid', traceevent_guid_from_name(provider_name))
        dct['Name'] = provider_name
        dct['Guid'] = provider_guid
        dct['Traits'] = ProviderTraits(provider_name)
        dct['_handle'] = None
        dct['_events'] = {}
        l.debug(f'provider fields setup for {provider_name} ({provider_guid})')

    def __collect_events(meta, dct, inherited_events):
        '''
        populate events dictonary, including any inherited events
        '''
        # inherit events from bases
        for event_name, event_dispatcher in dct.items():
            if isinstance(event_dispatcher, EventDispatcher):
                l.info(f'registering event for {event_name}')
                # will override, TODO: warn?
                if event_name in inherited_events:
                    l.warn('going to override event named {event_name}')
                inherited_events[event_name] = event_dispatcher
                # TODO: infer event ids?? what about inherited ones?
                # TODO: override id of dispatcher's descriptor
        dct['_events'].update(inherited_events)

    def __call__(cls, *args, **kwargs):
        if cls.Guid not in cls._instances:
            l.info(f'new instance of provider {cls.__name__}')
            cls._instances[cls.Guid] = super(
                ProviderDefinition, cls).__call__(*args, **kwargs)
        else:
            l.info('returning cached intance of provider')
        return cls._instances[cls.Guid]

    def __repr__(cls):
        # TODO: make prettier
        return '\n'.join((ename for ename in cls._events))


class ProviderTraits(object):
    # arbitrary, just to limit input in case of future traits
    TRAIT_PROVIDER_NAME_MAX_LEN = 512

    def __init__(self, name):
        self.name = name
        name_buf = bytes(self.name, 'utf-8')
        null_terminator = (0).to_bytes(1, byteorder='little')
        assert len(name_buf) < self.TRAIT_PROVIDER_NAME_MAX_LEN

        buf = name_buf+null_terminator
        self.buf = (len(buf)+2).to_bytes(2, 'little')+buf

    def __bytes__(self):
        return self.buf


class Provider(metaclass=ProviderDefinition):
    Guid: uuid.UUID
    Name: str
    Traits: ProviderTraits
    _events = None
    _handle = None

    def enabled(self, level: TraceLevel = None, keyword=0):
        # 0 keyword should mean any
        if level is None:
            enabled = False
            for tl in TraceLevel:
                enabled = EventProviderEnabled(self._handle, tl, keyword)
                if enabled:
                    l.debug(
                        f'{self.Name} has listeners for {tl.name} for keyword:{keyword}')
            return enabled

        return EventProviderEnabled(self._handle, level, keyword)

    def __init__(self, throw_on_write_error=False):
        self.throw_on_write_error = throw_on_write_error
        l.info('registering provider')
        self._handle = EventRegister(self.Guid)
        l.info(f'registered provider {self.Name} - {self.Guid}')

        # TODO: add assert test that traits are ok
        EventSetInformation(
            self._handle, EventInformationClass.EventProviderSetTraits, bytes(self.Traits))

        if not self.enabled():
            l.warn(f'probably no listeners for provider {self.Name}')

        l.info('setting provider as tlg')

    def _write(self, event: SelfDescribingEvent, args, kwargs):
        """
        returns true if event was written
        """
        l.info('checking event enabled')
        descriptor = event.descriptor
        if not EventEnabled(self._handle, descriptor):
            # NOTE: sometimes this will yield a false response due to an orphan session
            d = descriptor
            l.debug(
                f'event disabled {event.metadata.name}: id:{d.Id}, version:{d.Version}, level:{d.Level}, channel:{d.Channel}, opcode:{d.Opcode}, keyword:{d.Keyword} task:{d.Task}')
            l.info(f'event disabled {event.metadata.name}')
            return False

        l.info('going to build event metadata')
        event_metadata = bytes(event.metadata)

        l.info('going to build event payload')
        event_payload = event.metadata.pack(*args, **kwargs)

        data = [(EventDataDescriptorType.EVENT_DATA_DESCRIPTOR_TYPE_PROVIDER_METADATA, bytes(self.Traits)),
                (EventDataDescriptorType.EVENT_DATA_DESCRIPTOR_TYPE_EVENT_METADATA, event_metadata),
                (EventDataDescriptorType.EVENT_DATA_DESCRIPTOR_TYPE_NONE, event_payload)]

        l.info('going to send event')
        err = EventWrite(self._handle, descriptor, data)
        if err:
            l.warn(f'event not written, err:{err}')
            if self.throw_on_write_error:
                # TODO: raise EventDropped only on relevant errorcodes, other exception on others
                raise EventDropped('failed writing event', err, GetLastError())

        l.info('write done')
        return err == 0

    def __del__(self):
        EventUnregister(self._handle)
        l.info('unregistered')


class BaseLoggingProvider(Provider, ABC):
    @event(Level=TraceLevel.Verbose)
    def debug(self, message: Types.UnicodeString):
        pass

    @event(Level=TraceLevel.Information)
    def info(self, message: Types.UnicodeString):
        pass

    @event(Level=TraceLevel.Warning)
    def warning(self, message: Types.UnicodeString):
        pass

    @event(Level=TraceLevel.Error)
    def error(self, message: Types.UnicodeString):
        pass

    @event(Level=TraceLevel.Critical)
    def critical(self, message: Types.UnicodeString):
        pass


def getLogger(name):
    assert name
    # TODO: support guid?
    return ProviderDefinition(name, (BaseLoggingProvider,), {})()


version = (0, 1, 1)
__all__ = ['version', 'Provider', 'event',
           'traceevent_guid_from_name', 'Types', 'getLogger']
