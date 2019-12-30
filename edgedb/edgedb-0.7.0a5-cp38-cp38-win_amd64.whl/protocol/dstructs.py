#
# This source file is part of the EdgeDB open source project.
#
# Copyright 2019-present MagicStack Inc. and the EdgeDB authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


"""Structs for the dump/restore sub-protocol."""


import typing
import uuid


class DumpDataBlock(typing.NamedTuple):

    schema_object_id: uuid.UUID
    number: int
    data: bytes


class DumpBlock(typing.NamedTuple):

    schema_object_id: uuid.UUID
    schema_deps: typing.List[uuid.UUID]
    type_desc: bytes

    data_blocks_count: int
    data_size: int


class DumpDesc(typing.NamedTuple):

    schema: bytes

    server_version: bytes
    server_ts: int

    blocks: typing.List[DumpBlock]
