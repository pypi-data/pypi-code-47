# bchhun, {2019-12-18}

"""

module for managing the type of micro-manager communication interface
    Coms method, socket, and entry point (ep) must be set before utilization

"""
import time
import numpy as np
from ..acquisition import AcquisitionBase


class Coms:
    """
    Call these methods for image and metadata retrieval from micromanager 2.0
    """

    method = None
    socket = None
    ep = None

    # ============ meta and image retrieval methods  ==========================

    @classmethod
    def wait_for_last_meta(cls):
        try:
            ct = 0
            meta = cls.ep.getLastMeta()
            while not meta:
                time.sleep(0.0001)
                ct += 1
                meta = cls.ep.getLastMeta()
                if ct >= 10000:
                    raise FileExistsError("timeout waiting for file exists")
        except Exception as ex:
            raise ex
        return meta

    @classmethod
    def get_image(cls, meta):
        data_pixelshape = (meta.getxRange(), meta.getyRange())
        data_pixeldepth = meta.getBitDepth()

        if data_pixeldepth == 16:
            depth = np.uint16
        elif data_pixeldepth == 8:
            depth = np.uint8
        else:
            depth = np.uint16

        if cls.method == 'zeromq':
            try:
                if cls.socket is None:
                    raise AttributeError("must define socket for data retrieval using zmq")

                # send data to socket
                cls.ep.getImage(meta)

                # receive data from socket
                data = cls.socket.recv()
                image = np.frombuffer(data, dtype=depth).reshape(data_pixelshape)

                if image is None:
                    print('data is none')
            except Exception as ex:
                raise ex

        elif cls.method == 'mmap':
            try:
                # retrieve filepath from metadatastore
                data_filename = meta.getFilepath()
                data_buffer_position = meta.getBufferPosition()

                image = np.memmap(filename=data_filename,
                                  dtype=depth,
                                  offset=data_buffer_position,
                                  shape=data_pixelshape)

                if image is None:
                    print("data is none")

            except Exception as ex:
                raise ex
        else:
            raise AttributeError("communication method not defined")

        return image

    @classmethod
    def snap_and_get_image(cls):
        mm = cls.ep.getStudio()

        # snap image
        mm.live().snap(True)

        try:
            meta = cls.wait_for_last_meta()
        except FileExistsError:
            print("timeout waiting for metadata")
            return None

        data = cls.get_image(meta)

        return data

    # ============ channelname methods  ==========================

    @classmethod
    def wait_for_last_meta_channel_name(cls, channel_name_):
        try:
            meta = cls.ep.getLastMetaByChannelName(channel_name_)
            ct = 0
            while not meta:
                time.sleep(0.0001)
                ct += 1
                meta = cls.ep.getLastMetaByChannelName(channel_name_)
                if ct >= 10000:
                    raise FileExistsError("timeout waiting for file exists")
        except Exception as ex:
            raise ex
        return meta

    @classmethod
    def set_channel(cls, channel_):
        try:

            mmc = cls.ep.getCMMCore()

            # micro-manager is slow (not mm2python). we need a monitor to be sure it gets set....
            mmc.setChannelGroup('Channel')
            # start = datetime.now()
            c = 0
            while mmc.getCurrentConfig('Channel') != channel_:
                time.sleep(0.0001)
                mmc.setConfig('Channel', channel_)
                c += 1
                if c >= 10000:
                    raise AttributeError("timeout waiting to set channel")
            # stop = datetime.now()
            # print("time to check channel = %06d" % (stop - start).microseconds)
        except Exception as ex:
            raise ex

    @classmethod
    def set_and_snap_channel(cls, channel_):
        try:
            cls.set_channel(channel_)
        except AttributeError as ar:
            raise ar

        data = cls.snap_and_get_image()

        return data

    @classmethod
    def get_image_by_channel_name(cls, channel_):

        meta = cls.wait_for_last_meta_channel_name(channel_)

        image = cls.get_image(meta)


class SnapAndRetrieve(AcquisitionBase):

    @classmethod
    @AcquisitionBase.emitter(channel=4)
    def snap_and_retrieve(cls):
        """
        use snap/live manager to snap an image then return image
        This class-approach allows us to transmit the image by pyqt signals
        :return: np.ndarray
        """
        return Coms.snap_and_get_image()
