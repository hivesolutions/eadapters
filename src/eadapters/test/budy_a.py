#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import unittest

import appier

import eadapters


class BudyAdapterTest(unittest.TestCase):

    def setUp(self):
        self.app = appier.App(level=logging.ERROR)
        self.app._register_models_m(eadapters.models, name="eadapters")

    def tearDown(self):
        self.app.unload()

    def test_set_gift_slip_order(self):
        calls = []

        adapter = eadapters.Factory.get_adapter(name="budy")
        adapter.api = appier.MockObject(
            set_gift_slip_order=lambda key, payload: calls.append((key, payload))
        )

        adapter.set_gift_slip_order(True, "key")

        self.assertEqual(calls, [("key", dict(gift_slip=True))])

        adapter.set_gift_slip_order(False, "other")

        self.assertEqual(
            calls, [("key", dict(gift_slip=True)), ("other", dict(gift_slip=False))]
        )
