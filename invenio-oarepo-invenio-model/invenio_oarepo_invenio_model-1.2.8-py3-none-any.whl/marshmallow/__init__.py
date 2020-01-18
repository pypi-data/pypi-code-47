# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CIS UCT Prague.
#
# CIS theses repository is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

import uuid

from invenio_records_rest.schemas.fields import SanitizedUnicode
from marshmallow import Schema, fields, missing, pre_load

try:
    from marshmallow import __version_info__ as marshmallow_version
except:
    marshmallow_version = (2, 'x')

if marshmallow_version[0] >= 3:
    def load_dump(x):
        return dict(data_key=x)
else:
    def load_dump(x):
        return dict(load_from=x, dump_to=x)


# noinspection PyUnusedLocal
def get_id(obj, context):
    """Get record id."""
    pid = context.get('pid')
    return pid.object_uuid if pid else missing


class InvenioRecordMetadataSchemaV1Mixin(Schema):
    schema = SanitizedUnicode(required=False, attribute='$schema', **load_dump('$schema'))


class InvenioRecordSchemaV1Mixin(Schema):
    """Invenio record"""

    id = fields.String(required=True, validate=[lambda x: uuid.UUID(x)])
    _bucket = fields.String(required=False)
    _files = fields.Raw(dump_only=True)
    metadata = fields.Nested(InvenioRecordMetadataSchemaV1Mixin, required=False)

    @pre_load
    def handle_load(self, instance, **kwargs):
        instance.pop('_files', None)

        #
        # modified handling id from default invenio way:
        #
        # we need to use the stored id in dump (in case the object
        # is referenced, the id should be the stored one, not the context one)
        #
        # for data loading, we need to overwrite the id by the context - to be sure no one
        # is trying to overwrite the id
        #
        id_ = get_id(instance, self.context)
        if id_ is not missing:
            instance['id'] = str(id_)
        else:
            instance.pop('id', None)
        return instance
