# Copyright (C) 2015-2019 Virgil Security, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     (1) Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
#     (2) Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#
#     (3) Neither the name of the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived from
#     this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Lead Maintainer: Virgil Security Inc. <support@virgilsecurity.com>


from ctypes import *
from ._c_bridge import VscfSha512
from ._c_bridge import VscfImplTag
from ._c_bridge import VscfStatus
from virgil_crypto_lib.common._c_bridge import Data
from virgil_crypto_lib.common._c_bridge import Buffer
from .alg import Alg
from .hash import Hash


class Sha512(Alg, Hash):
    """This is MbedTLS implementation of SHA512."""

    # Length of the digest (hashing output) in bytes.
    DIGEST_LEN = 64
    # Block length of the digest function in bytes.
    BLOCK_LEN = 128

    def __init__(self):
        """Create underlying C context."""
        self._lib_vscf_sha512 = VscfSha512()
        self._c_impl = None
        self._ctx = None
        self.ctx = self._lib_vscf_sha512.vscf_sha512_new()

    def __delete__(self, instance):
        """Destroy underlying C context."""
        self._lib_vscf_sha512.vscf_sha512_delete(self.ctx)

    def alg_id(self):
        """Provide algorithm identificator."""
        result = self._lib_vscf_sha512.vscf_sha512_alg_id(self.ctx)
        return result

    def produce_alg_info(self):
        """Produce object with algorithm information and configuration parameters."""
        result = self._lib_vscf_sha512.vscf_sha512_produce_alg_info(self.ctx)
        instance = VscfImplTag.get_type(result)[0].take_c_ctx(cast(result, POINTER(VscfImplTag.get_type(result)[1])))
        return instance

    def restore_alg_info(self, alg_info):
        """Restore algorithm configuration from the given object."""
        status = self._lib_vscf_sha512.vscf_sha512_restore_alg_info(self.ctx, alg_info.c_impl)
        VscfStatus.handle_status(status)

    def hash(self, data):
        """Calculate hash over given data."""
        d_data = Data(data)
        digest = Buffer(self.DIGEST_LEN)
        self._lib_vscf_sha512.vscf_sha512_hash(d_data.data, digest.c_buffer)
        return digest.get_bytes()

    def start(self):
        """Start a new hashing."""
        self._lib_vscf_sha512.vscf_sha512_start(self.ctx)

    def update(self, data):
        """Add given data to the hash."""
        d_data = Data(data)
        self._lib_vscf_sha512.vscf_sha512_update(self.ctx, d_data.data)

    def finish(self):
        """Accompilsh hashing and return it's result (a message digest)."""
        digest = Buffer(self.DIGEST_LEN)
        self._lib_vscf_sha512.vscf_sha512_finish(self.ctx, digest.c_buffer)
        return digest.get_bytes()

    @classmethod
    def take_c_ctx(cls, c_ctx):
        inst = cls.__new__(cls)
        inst._lib_vscf_sha512 = VscfSha512()
        inst.ctx = c_ctx
        return inst

    @classmethod
    def use_c_ctx(cls, c_ctx):
        inst = cls.__new__(cls)
        inst._lib_vscf_sha512 = VscfSha512()
        inst.ctx = inst._lib_vscf_sha512.vscf_sha512_shallow_copy(c_ctx)
        return inst

    @property
    def c_impl(self):
        return self._c_impl

    @property
    def ctx(self):
        return self._ctx

    @ctx.setter
    def ctx(self, value):
        self._ctx = self._lib_vscf_sha512.vscf_sha512_shallow_copy(value)
        self._c_impl = self._lib_vscf_sha512.vscf_sha512_impl(self.ctx)
