#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class SWishlistLine(base.SBase):

    quantity = appier.field(
        type = float
    )

    total = appier.field(
        type = float
    )

    product = appier.field(
        type = appier.reference(
            "SProduct",
            name = "id"
        )
    )
