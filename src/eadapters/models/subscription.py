#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class SSubscription(base.SBase):

    email = appier.field()
