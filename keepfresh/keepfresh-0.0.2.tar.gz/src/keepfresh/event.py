#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field

@dataclass
class Event:
    path: str
    created: bool = field(default=lambda:False)
    modified: bool = field(default=lambda:False)
    deleted: bool = field(default=lambda:False)
