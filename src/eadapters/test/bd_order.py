#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import unittest

import appier

import eadapters


class BDOrderTest(unittest.TestCase):

    def setUp(self):
        self.app = appier.App(level=logging.ERROR)
        self.app._register_models_m(eadapters.models, name="eadapters")

    def tearDown(self):
        self.app.unload()

    def test_set_gift_slip_s(self):
        calls = []

        adapter = eadapters.Factory.get_adapter(name="budy")
        adapter.api = appier.MockObject(
            set_gift_slip_order=lambda key, payload: calls.append((key, payload))
        )

        order = eadapters.models.BDOrder.get_l(key="key")
        order.set_gift_slip_s(True)

        self.assertEqual(calls, [("key", dict(gift_slip=True))])

        order.set_gift_slip_s(False)

        self.assertEqual(
            calls, [("key", dict(gift_slip=True)), ("key", dict(gift_slip=False))]
        )

        def set_gift_slip_order(key, payload):
            raise appier.HTTPError(
                appier.legacy.BytesIO(b'{"message": "Order not found."}'), code=404
            )

        adapter.api = appier.MockObject(set_gift_slip_order=set_gift_slip_order)

        self.assertRaises(appier.OperationalError, lambda: order.set_gift_slip_s(True))
        self.assertEqual(len(calls), 2)
