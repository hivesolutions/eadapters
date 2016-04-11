#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import bd_common

from .. import voucher

class BDVoucher(voucher.SVoucher, bd_common.BDCommon):

    key = appier.field()

    @classmethod
    def _ident_name(cls):
        return "key"
