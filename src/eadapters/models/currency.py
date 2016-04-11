#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class SCurrency(base.SBase):

    name = appier.field()

    currency_code = appier.field()
