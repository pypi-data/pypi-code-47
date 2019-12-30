# Copyright Netflix, 2019
from enum import Enum
from typing import Optional
from typing import Text


class DestinationType(Enum):
    """
    Which destination type/protocol are you using?
    """

    RAE = 1  # general purpose pub/sub to the RAE
    CLOUD = 2  # general purpose pub/sub to the cloud
    BROADCAST = 3  # deprecate
    EXTERNAL = 4  # deprecate
    EXTCLIENT = 5  # deprecate

    # prefer the following two protocols for request work flows
    RAE_TO_CLOUD = 6  # requests made to a cloud agent originating from something connected to the RAE
    CLOUD_TO_RAE = 7  # requests made to a RAE connected agent from something in the cloud
    BROKER_LOCAL_ONLY = 8


class TopicType(Enum):
    RESPONSE = 1
    REQUEST = 2
    HANDLER = 3
    PUBSUB = 4


def topicmaker_existing(
    cloud: bool, destinationtype: DestinationType, topictype: TopicType, userdata: Text, raeid: Optional[Text] = None,
) -> Text:
    """
    Make a topic based on the Netflix MQTT topic protocol.

    This is an OPTIONAL call that can help you form the proper request for most conditions where you
    are interacting with the Netflix request/response protocol. If you want to hard-code your topic forming,
    you are free to, but you're getting the phone call when it goes wrong.

    The topic structure is influenced by:
    whether the client is attached to a cloud or local broker
    whether the destination is one of a few defined types
    whether the destination topic is for a response, request, handler, or just general pubsub
    which direction a request is flowing (captured in destination types)

    # exisitng, comments and spacing for clarity

# RAE => Cloud: requests from RAE to cloud
topic # out 1           cloud/           external/client/{{ grains['id'] }}/
topic # in  1 _response/cloud/ _response/external/rae   /{{ grains['id'] }}/
# RAE <= Cloud: requests from cloud to RAE
topic # in  1           external/           client/rae/{{ grains['id'] }}/
topic # out 1 _response/external/ _response/client/rae/{{ grains['id'] }}/

# RAE => Cloud: request
topic # out 1           cloud/           external/client/{{ grains['id'] }}/
topic # in  1 _response/cloud/ _response/external/   rae/{{ grains['id'] }}/
# RAE <= Cloud: response
topic # in  1           external/           client/rae/{{ grains['id'] }}/
topic # out 1 _response/external/ _response/client/rae/{{ grains['id'] }}/


    """
    parts = []

    if topictype == TopicType.RESPONSE:
        parts.append("_response")

    # todo these are ignoring the aspect of "am I the cloud half or the rae half" which is becoming a problem
    if topictype == TopicType.REQUEST:
        if destinationtype == DestinationType.RAE_TO_CLOUD:
            if cloud:
                parts.append("external")
                parts.append("client")
                parts.append("rae")
                parts.append(raeid)
            else:
                parts.append("cloud")
        elif destinationtype == DestinationType.CLOUD_TO_RAE:
            if cloud:
                parts.append("client")
                parts.append("rae")
                parts.append(raeid)
            else:
                # parts.append("external")  # todo when is this done?
                pass

    if topictype == TopicType.RESPONSE:
        if destinationtype == DestinationType.RAE_TO_CLOUD:
            if cloud:
                parts.append("external")
                parts.append("client")
                parts.append("rae")
                parts.append(raeid)
            else:
                parts.append("cloud")
        elif destinationtype == DestinationType.CLOUD_TO_RAE:
            if cloud:
                parts.append("client")
                parts.append("rae")
                parts.append(raeid)
            else:
                parts.append("external")

    parts.append(userdata)

    if topictype == TopicType.HANDLER:
        parts.append("#")

    return "/".join(parts)


def topicmaker(cloud: bool, destinationtype: DestinationType, topictype: TopicType, userdata: Text, raeid: Optional[Text] = None,) -> Text:
    """
    Make a topic based on the Netflix MQTT topic protocol.

    This is an OPTIONAL call that can help you form the proper request for most conditions where you
    are interacting with the Netflix request/response protocol. If you want to hard-code your topic forming,
    you are free to, but you're getting the phone call when it goes wrong.

    The topic structure is influenced by:
    whether the client is attached to a cloud or local broker
    whether the destination is one of a few defined types
    whether the destination topic is for a response, request, handler, or just general pubsub
    which direction a request is flowing (captured in destination types)
    """
    parts = []

    if topictype == TopicType.RESPONSE:
        parts.append("_response")

    if destinationtype == DestinationType.RAE:
        if raeid is None and cloud:
            raise ValueError("The RAE ID cannot be none if the destination type is RAE")
        if cloud:
            parts.append("cloud_to_rae")
            parts.append("rae")
            parts.append(raeid)

    if destinationtype == DestinationType.CLOUD_TO_RAE:
        parts.append("cloud_to_rae")
        if cloud:
            parts.append("rae")
            if raeid is None:
                raise ValueError("The RAE ID cannot be none if the destination type is RAE")
            parts.append(raeid)

    # this is a somewhat special case - we are responding to the rae on a specific request
    if destinationtype == DestinationType.RAE_TO_CLOUD:
        parts.append("rae_to_cloud")
        if cloud:
            parts.append("rae")
            if raeid is None:
                raise ValueError("The RAE ID cannot be none if the destination type is RAE")
            parts.append(raeid)

    if destinationtype == DestinationType.CLOUD and not cloud:
        parts.append("rae_to_cloud")
        if cloud:
            parts.append("rae")

    parts.append(userdata)

    if topictype == TopicType.HANDLER:
        parts.append("#")

    return "/".join(parts)
