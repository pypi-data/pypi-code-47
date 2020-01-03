# Copyright (C) 2019-2020 Codenocold
#
# The following terms apply to all files associated
# with the software unless explicitly disclaimed in individual files.
#
# The authors hereby grant permission to use, copy, modify, distribute,
# and license this software and its documentation for any purpose, provided
# that existing copyright notices are retained in all copies and that this
# notice is included verbatim in any distributions. No written agreement,
# license, or royalty fee is required for any of the authorized uses.
# Modifications to this software may be copyrighted by their authors
# and need not follow the licensing terms described here, provided that
# the new terms are clearly indicated on the first page of each file where
# they apply.
#
# IN NO EVENT SHALL THE AUTHORS OR DISTRIBUTORS BE LIABLE TO ANY PARTY
# FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES
# ARISING OUT OF THE USE OF THIS SOFTWARE, ITS DOCUMENTATION, OR ANY
# DERIVATIVES THEREOF, EVEN IF THE AUTHORS HAVE BEEN ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# THE AUTHORS AND DISTRIBUTORS SPECIFICALLY DISCLAIM ANY WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.  THIS SOFTWARE
# IS PROVIDED ON AN "AS IS" BASIS, AND THE AUTHORS AND DISTRIBUTORS HAVE
# NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR
# MODIFICATIONS.

__author__ = 'Codenocold'

import usb.core
import usb.util
from struct import *

# cando dev open flags
CANDO_FLAG_LISTEN_ONLY = (1 << 0)
CANDO_FLAG_LOOP_BACK = (1 << 1)
CANDO_FLAG_ONE_SHOT = (1 << 2)

# cando can bus error
CAN_ERR_BUSOFF = 0x00000001
CAN_ERR_RX_TX_WARNING = 0x00000002
CAN_ERR_RX_TX_PASSIVE = 0x00000004
CAN_ERR_OVERLOAD = 0x00000008
CAN_ERR_STUFF = 0x00000010
CAN_ERR_FORM = 0x00000020
CAN_ERR_ACK = 0x00000040
CAN_ERR_BIT_RECESSIVE = 0x00000080
CAN_ERR_BIT_DOMINANT = 0x00000100
CAN_ERR_CRC = 0x00000200

# control request
__CANDO_BREQ_MODE = 0
__CANDO_BREQ_BITTIMING = 1
__CANDO_BREQ_CAN_STATUS = 2
__CANDO_BREQ_BT_CONST = 3
__CANDO_BREQ_DEVICE_CONFIG = 4


class Frame:
    def __init__(self):
        self.flag = 0
        self.is_extend = 0
        self.is_rtr = 0
        self.can_dlc = 0
        self.can_id = 0
        self.data = [0x00] * 8
        self.timestamp_us = 0


def list_scan():
    r"""
    Retrieve the list of cando devices handle
    :return: list of cando devices handle
    """
    return list(usb.core.find(find_all=True, idVendor=0x1D50, idProduct=0x606F))


def dev_start(dev, flag=0):
    r"""
    Start cando device
    :param dev: cando device handle
    :param flag: flags @ CANDO_FLAG_*
    :return: none
    """
    mode = 1
    flag = flag
    data = pack('II', mode, flag)
    dev.ctrl_transfer(0x41, __CANDO_BREQ_MODE, 0, 0, data)


def dev_stop(dev):
    r"""
    Stop cando device
    :param dev: cando device handle
    :return: none
    """
    mode = 0
    flag = 0
    data = pack('II', mode, flag)
    dev.ctrl_transfer(0x41, __CANDO_BREQ_MODE, 0, 0, data)


def dev_set_timing(dev, prop_seg, phase_seg1, phase_seg2, sjw, brp):
    r"""
    Set CAN bit timing
    :param dev: cando device handle
    :param prop_seg: propagation Segment (const 1)
    :param phase_seg1: phase segment 1 (1~15)
    :param phase_seg2: phase segment 2 (1~8)
    :param sjw: synchronization segment (1~4)
    :param brp: prescaler for quantum #base_clk = 48MHz (1~1024)
    :return: none
    """
    data = pack('5I', prop_seg, phase_seg1, phase_seg2, sjw, brp)
    dev.ctrl_transfer(0x41, __CANDO_BREQ_BITTIMING, 0, 0, data)


def dev_get_serial_number_str(dev):
    r"""
    Get cando device serial number in string format
    :param dev: cando device handle
    :return: cando device serial number string
    """
    return dev.serial_number


def dev_get_dev_info_str(dev):
    r"""
    Get cando device info
    :param dev: cando device handle
    :return: cando device info string
    """
    data = dev.ctrl_transfer(0xC1, __CANDO_BREQ_DEVICE_CONFIG, 0, 0, 12)
    tup = unpack('4B2I', data)
    info = "fw: " + str(tup[4] / 10) + " hw: " + str(tup[5] / 10)
    return info


def dev_get_state(dev):
    r"""
    Get can bus status
    :param dev: cando device handle
    :return: <tuple> error_code @ CAN_ERR_*, err_tx, err_rx
    """
    data = dev.ctrl_transfer(0xC1, __CANDO_BREQ_CAN_STATUS, 0, 0, 8)
    tup = unpack('I4B', data)
    return tup[0], tup[1], tup[2]


def dev_frame_send(dev, frame):
    r"""
    Send frame
    :param dev: cando device handle
    :param frame: cando frame @ class Frame
    :return: none
    """
    data = pack("4BI8BI", frame.flag, frame.is_extend, frame.is_rtr, frame.can_dlc, frame.can_id, *frame.data,
                frame.timestamp_us)
    dev.write(0x02, data)


def dev_frame_read(dev, frame, timeout_ms):
    r"""
    Read frame
    :param dev: cando device handle
    :param frame: cando frame @ class Frame
    :param timeout_ms: read time out in ms
    :return: return True if success else False
    """
    try:
        data = dev.read(0x81, 20, timeout_ms)
    except usb.core.USBError:
        return False
    frame.flag, frame.is_extend, frame.is_rtr, frame.can_dlc, frame.can_id, *frame.data, frame.timestamp_us = unpack(
        "4BI8BI", data)
    return True
