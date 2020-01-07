# bchhun, {2019-08-13}

from recorder_base.recOrder import AcquisitionBase
from PyQt5.QtCore import pyqtSlot
from recorder_base.recOrder.base.program import Program
import pytest

# ==========================================================================


@pytest.fixture(scope='session')
def pre_slot_fixture():

    class EmitterTestOne(AcquisitionBase):
        sent = None

        @pyqtSlot(object)
        @AcquisitionBase.emitter(channel=0)
        def emitter_one_arg(self, send):
            self.sent = send
            return send

    class ReceiverTestOne(AcquisitionBase):
        received = None

        @pyqtSlot(object)
        @AcquisitionBase.receiver(channel=0)
        def receiver_one_arg(self, rec):
            self.received = rec + 1
            return rec + 1

    return EmitterTestOne(), ReceiverTestOne()


@pytest.fixture(scope='session')
def post_slot_fixture():

    class EmitterTestOne(AcquisitionBase):
        sent = None

        @AcquisitionBase.emitter(channel=0)
        @pyqtSlot(object)
        def emitter_one_arg(self, send):
            self.sent = send
            return send

    class ReceiverTestOne(AcquisitionBase):
        received = None

        @AcquisitionBase.receiver(channel=0)
        @pyqtSlot(object)
        def receiver_one_arg(self, rec):
            self.received = rec + 1
            return rec + 1

    return EmitterTestOne(), ReceiverTestOne()


@pytest.fixture(scope='session')
def pre_static_fixture():

    class EmitterTestOne(AcquisitionBase):

        @staticmethod
        @AcquisitionBase.emitter(channel=0)
        def emitter_one_arg(send):
            return send

    class ReceiverTestOne(AcquisitionBase):

        received = None

        @staticmethod
        @AcquisitionBase.receiver(channel=0)
        def receiver_one_arg(rec):
            ReceiverTestOne.received = rec + 1
            return rec+1

    return EmitterTestOne(), ReceiverTestOne()


# ==========================================================================


def test_connection_one_arg():

    class EmitterTestOne(AcquisitionBase):
        sent = None

        @AcquisitionBase.emitter(channel=0)
        def emitter_one_arg(self, send):
            self.sent = send
            return send

    class ReceiverTestOne(AcquisitionBase):
        received = None

        @AcquisitionBase.receiver(channel=0)
        def receiver_one_arg(self, rec):
            self.received = rec+1
            return rec+1

    e = EmitterTestOne()
    r = ReceiverTestOne()

    e.get_QChannel(0).QChannel.connect(r.receiver_one_arg)

    assert e.emitter_one_arg(1) == 1
    assert r.received == 2
    assert e.sent == 1
    assert r.receiver_one_arg(5) == 6


def test_connection_two_args():

    class EmitterTestTwo(AcquisitionBase):
        sent = None
        sent2 = None

        @AcquisitionBase.emitter(channel=0)
        def emitter_two_arg(self, send, send2):
            self.sent = send
            self.sent2 = send2
            return send, send2

    class ReceiverTestTwo(AcquisitionBase):
        received = None

        @AcquisitionBase.receiver(channel=0)
        def receiver_two_arg(self, rec):
            self.received = rec[0]+rec[1]
            return rec[0]+rec[1]

    e = EmitterTestTwo()
    r = ReceiverTestTwo()
    rectest = ReceiverTestTwo

    e.get_QChannel(0).QChannel.connect(r.receiver_two_arg)

    assert e.emitter_two_arg(1, 1) == (1, 1)
    assert r.receiver_two_arg((2, 2)) == 4

    # check that receiver function receives only one argument
    assert rectest.receiver_two_arg.__code__.co_argcount == 1

    e.emitter_two_arg(1, 1)
    assert r.received == 2
    assert e.sent == 1
    assert e.sent2 == 1


def test_connection_slot_dec(pre_slot_fixture):
    """
    test that decorating an emitter or slot with pyqtSlot will not interfere with operation

    :return:
    """

    e, r = pre_slot_fixture

    e.get_QChannel(0).QChannel.connect(r.receiver_one_arg)

    assert e.emitter_one_arg(1) == 1
    assert r.received == 2
    assert e.sent == 1
    assert r.receiver_one_arg(5) == 6


def test_connection_slot_dec_2(pre_slot_fixture):
    e2, r2 = pre_slot_fixture

    # test that program building connection works
    p = Program()
    p.add_module(e2)
    p.add_module(r2)
    p.build()

    assert e2.emitter_one_arg(1) == 1
    assert r2.received == 2
    assert e2.sent == 1
    assert r2.receiver_one_arg(5) == 6


def test_connection_slot_dec_3(post_slot_fixture):
    """
    test that decorating an emitter or slot with pyqtSlot will not interfere with operation

    :return:
    """

    e, r = post_slot_fixture

    e.get_QChannel(0).QChannel.connect(r.receiver_one_arg)

    assert e.emitter_one_arg(1) == 1
    assert r.received == 2
    assert e.sent == 1
    assert r.receiver_one_arg(5) == 6


def test_connection_slot_dec_4(post_slot_fixture):
    e2, r2 = post_slot_fixture

    # test that program building connection works
    p = Program()
    p.add_module(e2)
    p.add_module(r2)
    p.build()

    assert e2.emitter_one_arg(1) == 1
    assert r2.received == 2
    assert e2.sent == 1
    assert r2.receiver_one_arg(5) == 6


def test_connection_static_dec(pre_static_fixture):
    e1, r1 = pre_static_fixture

    e1.get_QChannel(0).QChannel.connect(r1.receiver_one_arg)

    assert e1.emitter_one_arg(1) == 1
    assert r1.received == 2


def test_connection_static_dec_2(pre_static_fixture):
    e1, r1 = pre_static_fixture

    p = Program()
    p.add_module(e1)
    p.add_module(r1)
    p.build()

    assert e1.emitter_one_arg(1) == 1
    assert r1.received == 2


#todo: wrapper calls:
# function receives one parameter with self
# function receives no paramters with self
# function receives nothing

#receiver
#todo:  - no param received
#todo:  - one param received
#todo:  - self param received
#todo:  - repeat above with func that is also a slot

#emitter
#todo:  - function emits nothing
#todo:  - function emits one param
#todo:  - function emits two params
#todo:  - repeat above with func that is also a slot


