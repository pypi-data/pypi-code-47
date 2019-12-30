# This file is part of the Trezor project.
#
# Copyright (C) 2012-2019 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

from . import messages
from .tools import Address, expect

if False:
    from .client import TrezorClient


@expect(messages.Entropy, field="entropy")
def get_entropy(client: "TrezorClient", size: int) -> messages.Entropy:
    return client.call(messages.GetEntropy(size=size))


@expect(messages.SignedIdentity)
def sign_identity(
    client: "TrezorClient",
    identity: messages.IdentityType,
    challenge_hidden: bytes,
    challenge_visual: str,
    ecdsa_curve_name: str = None,
) -> messages.SignedIdentity:
    return client.call(
        messages.SignIdentity(
            identity=identity,
            challenge_hidden=challenge_hidden,
            challenge_visual=challenge_visual,
            ecdsa_curve_name=ecdsa_curve_name,
        )
    )


@expect(messages.ECDHSessionKey)
def get_ecdh_session_key(
    client: "TrezorClient",
    identity: messages.IdentityType,
    peer_public_key: bytes,
    ecdsa_curve_name: str = None,
) -> messages.ECDHSessionKey:
    return client.call(
        messages.GetECDHSessionKey(
            identity=identity,
            peer_public_key=peer_public_key,
            ecdsa_curve_name=ecdsa_curve_name,
        )
    )


@expect(messages.CipheredKeyValue, field="value")
def encrypt_keyvalue(
    client: "TrezorClient",
    n: Address,
    key: str,
    value: bytes,
    ask_on_encrypt: bool = True,
    ask_on_decrypt: bool = True,
    iv: bytes = b"",
) -> messages.CipheredKeyValue:
    return client.call(
        messages.CipherKeyValue(
            address_n=n,
            key=key,
            value=value,
            encrypt=True,
            ask_on_encrypt=ask_on_encrypt,
            ask_on_decrypt=ask_on_decrypt,
            iv=iv,
        )
    )


@expect(messages.CipheredKeyValue, field="value")
def decrypt_keyvalue(
    client: "TrezorClient",
    n: Address,
    key: str,
    value: bytes,
    ask_on_encrypt: bool = True,
    ask_on_decrypt: bool = True,
    iv: bytes = b"",
) -> messages.CipheredKeyValue:
    return client.call(
        messages.CipherKeyValue(
            address_n=n,
            key=key,
            value=value,
            encrypt=False,
            ask_on_encrypt=ask_on_encrypt,
            ask_on_decrypt=ask_on_decrypt,
            iv=iv,
        )
    )
