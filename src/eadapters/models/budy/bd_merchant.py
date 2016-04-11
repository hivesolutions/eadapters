#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import bd_common

from .. import merchant

class BDMerchant(merchant.SMerchant, bd_common.BDCommon):
    pass
