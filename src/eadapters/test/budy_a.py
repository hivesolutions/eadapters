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

    def test_secret_key(self):
        adapter = eadapters.BudyAdapter(secret_key="secret")
        api = adapter._get_api()

        self.assertEqual(api.secret_key, "secret")
        self.assertEqual("secret_key" in adapter.get_context(), False)

        adapter = eadapters.Factory.get_adapter(
            name="budy", extra=dict(secret_key="other")
        )

        self.assertEqual(adapter._get_api().secret_key, "other")

        adapter = eadapters.BudyAdapter()

        self.assertEqual(adapter.secret_key, None)
        self.assertEqual(adapter._get_api().secret_key, None)

    def test_create_visits(self):
        calls = []

        adapter = eadapters.Factory.get_adapter(name="budy")
        adapter.api = appier.MockObject(
            create_visits=lambda visits: calls.append(visits) or dict(count=len(visits))
        )

        visits = [dict(channel="direct"), dict(channel="email", source="newsletter")]
        result = adapter.create_visits(visits)

        self.assertEqual(result, dict(count=2))
        self.assertEqual(calls, [visits])

    def test_set_source_order(self):
        calls = []

        adapter = eadapters.Factory.get_adapter(name="budy")
        adapter.api = appier.MockObject(
            set_source_order=lambda key, payload: calls.append((key, payload))
        )

        source = dict(channel="paid_search", source="google", medium="cpc")
        adapter.set_source_order(source, "key")

        self.assertEqual(calls, [("key", dict(source=source))])

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

    def test_set_notes_order(self):
        calls = []

        adapter = eadapters.Factory.get_adapter(name="budy")
        adapter.api = appier.MockObject(
            set_notes_order=lambda key, payload: calls.append((key, payload))
        )

        adapter.set_notes_order("Wrap separately", "key")

        self.assertEqual(calls, [("key", dict(notes="Wrap separately"))])

        adapter.set_notes_order("", "other")

        self.assertEqual(
            calls, [("key", dict(notes="Wrap separately")), ("other", dict(notes=""))]
        )

    def test_set_source_bag(self):
        calls = []

        adapter = eadapters.Factory.get_adapter(name="budy")
        adapter.api = appier.MockObject(
            key_bag=lambda: dict(key="bag"),
            set_source_bag=lambda key, payload: calls.append((key, payload)),
        )

        source = dict(channel="organic_social", source="instagram")
        adapter.set_source_bag(source)

        self.assertEqual(adapter.bag_key, "bag")
        self.assertEqual(calls, [("bag", dict(source=source))])

        adapter.set_source_bag(None, bag_id="other")

        self.assertEqual(
            calls, [("bag", dict(source=source)), ("other", dict(source=None))]
        )
