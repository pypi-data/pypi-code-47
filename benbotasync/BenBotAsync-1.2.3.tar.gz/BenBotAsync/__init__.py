"""
“Commons Clause” License Condition v1.0
Copyright Oli 2019
The Software is provided to you by the Licensor under the
License, as defined below, subject to the following condition.
Without limiting other conditions in the License, the grant
of rights under the License will not include, and the License
does not grant to you, the right to Sell the Software.
For purposes of the foregoing, “Sell” means practicing any or
all of the rights granted to you under the License to provide
to third parties, for a fee or other consideration (including
without limitation fees for hosting or consulting/ support
services related to the Software), a product or service whose
value derives, entirely or substantially, from the functionality
of the Software. Any license notice or attribution required by
the License must also include this Commons Clause License
Condition notice.
Software: fortnitepy-bot
License: Apache 2.0
"""

from .enums import *
from .http import HTTPClient
from .cosmetics import fortniteCosmetic
from .api import API

name = 'BenBotAsync'
version = '1.2.3'
author = 'xMistt'

http = HTTPClient()

async def get_cosmetic(query, params=Tags.NAME, filter=None, raw=False):
    url = f'http://benbotfn.tk:8080/api/cosmetics/search/multiple?{params.value}={query}'
    request = await http.benbot_request(url=url)

    if filter is None:
        if raw is True:
            return request
        else:
            try:
                cosmetic = fortniteCosmetic(request[0])
                return cosmetic
            except IndexError:
                return None
    else:
        for result in request:
            if result[f'{filter[0].value}'] == filter[1]:
                if raw is True:
                    return result
                else:
                    cosmetic = fortniteCosmetic(result)
                    return cosmetic
            else:
                pass

async def vtid_to_variants(query):
    url = f'http://benbotfn.tk:8080/api/assetProperties?file=FortniteGame/Content/Athena/Items/CosmeticVariantTokens/{query}.uasset'
    request = await http.request(url=url)

    try:
        parsed_cid = request['export_properties'][0]['cosmetic_item']
        parsed_channel = request['export_properties'][0]['VariantChanelTag']['TagName'].split(".")[3]
        
        raw_name = request['export_properties'][0]['VariantNameTag']['TagName'].split(".")[3]

        parsed_name = int("".join(filter(lambda x: x.isnumeric(), raw_name)))

        if parsed_channel == 'ClothingColor':
            return parsed_cid, 'clothing_color', parsed_name
        else:
            return parsed_cid, parsed_channel, parsed_name
    except TypeError:
        return None

# DEPRECATED FUNCTIONS BELOW.

async def getCosmetic(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getCosmeticId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getCosmeticFromId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Outfit.

async def getSkin(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getSkinId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Harvesting Tool.

async def getPickaxe(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getPickaxeId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Back Bling.

async def getBackpack(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getBackpackId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Glider.

async def getGlider(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getGliderId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Emote.

async def getEmote(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getEmoteId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Pet.

async def getPet(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getPetId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')