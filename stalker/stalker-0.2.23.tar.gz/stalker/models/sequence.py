# -*- coding: utf-8 -*-
# Stalker a Production Asset Management System
# Copyright (C) 2009-2018 Erkan Ozgur Yilmaz
#
# This file is part of Stalker.
#
# Stalker is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# Stalker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with Stalker.  If not, see <http://www.gnu.org/licenses/>

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, validates

from stalker.models.mixins import ReferenceMixin, CodeMixin
from stalker.models.task import Task

from stalker.log import logging_level
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging_level)


class Sequence(Task, CodeMixin):
    """Stores data about Sequences.

    Sequences are a way of grouping the Shots according to their temporal
    position to each other.

    **Initialization**

    .. warning::

       .. deprecated:: 0.2.0

       Sequences do not have a lead anymore. Use the :class:`.Task.responsible`
       attribute of the super (:class:`.Task`).
    """
    __auto_name__ = False
    __tablename__ = "Sequences"
    __mapper_args__ = {"polymorphic_identity": "Sequence"}
    sequence_id = Column("id", Integer, ForeignKey("Tasks.id"),
                         primary_key=True)

    shots = relationship(
        "Shot",
        secondary='Shot_Sequences',
        back_populates="sequences",
        doc="""The :class:`.Shot`\ s assigned to this Sequence.

        It is a list of :class:`.Shot` instances.
        """
    )

    def __init__(self, **kwargs):
        super(Sequence, self).__init__(**kwargs)

        # call the mixin __init__ methods
        ReferenceMixin.__init__(self, **kwargs)
        CodeMixin.__init__(self, **kwargs)
        self.shots = []

    @validates("shots")
    def _validate_shots(self, key, shot):
        """validates the given shot value
        """
        from stalker.models.shot import Shot

        if not isinstance(shot, Shot):
            raise TypeError(
                '%s.shots should be all stalker.models.shot.Shot instances, '
                'not %s' % (self.__class__.__name__, shot.__class__.__name__)
            )
        return shot

    def __eq__(self, other):
        """the equality operator
        """
        return isinstance(other, Sequence) and \
            super(Sequence, self).__eq__(other)

    def __hash__(self):
        """the overridden __hash__ method
        """
        return super(Sequence, self).__hash__()
