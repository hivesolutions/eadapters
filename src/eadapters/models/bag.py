#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class SBag(base.SBase):

    currency = appier.field()

    total = appier.field(
        type = float
    )

    lines = appier.field(
        type = appier.references(
            "SBagLine",
            name = "id"
        )
    )
