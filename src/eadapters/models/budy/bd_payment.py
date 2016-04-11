#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import bd_common

from .. import payment

class BDPayment(payment.SPayment, bd_common.BDCommon):
    pass
