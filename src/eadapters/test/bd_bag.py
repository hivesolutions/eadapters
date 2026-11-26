#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import unittest

import appier

import eadapters


class BDBagTest(unittest.TestCase):

    def setUp(self):
        self.app = appier.App(level=logging.ERROR)
        self.app._register_models_m(eadapters.models, name="eadapters")

    def tearDown(self):
        self.app.unload()

    def test_set_source_s(self):
        calls = []

        adapter = eadapters.Factory.get_adapter(name="budy")
        adapter.api = appier.MockObject(
            set_source_bag=lambda key, payload: calls.append((key, payload))
        )

        bag = eadapters.models.BDBag.get_l(key="key")
        bag.set_source_s(dict(channel="referral", referer="www.kuantokusta.pt"))

        self.assertEqual(
            calls,
            [
                (
                    "key",
                    dict(source=dict(channel="referral", referer="www.kuantokusta.pt")),
                )
            ],
        )

        def set_source_bag(key, payload):
            raise appier.HTTPError(
                appier.legacy.BytesIO(b'{"message": "Bag not found."}'), code=404
            )

        adapter.api = appier.MockObject(set_source_bag=set_source_bag)

        self.assertRaises(
            appier.OperationalError,
            lambda: bag.set_source_s(dict(channel="direct")),
        )
        self.assertEqual(len(calls), 1)
