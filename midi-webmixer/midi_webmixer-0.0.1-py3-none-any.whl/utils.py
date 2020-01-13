#!/usr/bin/env python3

def _createChannelMap():

    """"
    Auto generate the channel map like so:

    {"aux1": {"channel1": {"cc": 0, "value": 74}....}
    """

    mix_map = {}
    for mix in range(1,5):
        mix_map[f'aux{mix}'] = {}
        for channel in range(0,12):
            # Generate offsets for cc numbers
            if mix == 1:
                offset = 0
            elif mix == 2:
                offset = 12
            elif mix == 3:
                offset = 24
            elif mix == 4:
                offset = 36
            mix_map[f'aux{mix}'][f'channel{channel+1}'] = {'cc':channel + offset, 'value':0}
    return mix_map
