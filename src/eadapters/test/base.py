#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import appier

import eadapters


class BaseTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(1 + 1, 2)

    def test_create_visits(self):
        adapter = eadapters.BaseAdapter()

        self.assertRaises(
            appier.NotImplementedError,
            lambda: adapter.create_visits([dict(channel="direct")]),
        )

    def test_set_source_order(self):
        adapter = eadapters.BaseAdapter()

        self.assertRaises(
            appier.NotImplementedError,
            lambda: adapter.set_source_order(dict(channel="direct"), "key"),
        )

    def test_set_gift_slip_order(self):
        adapter = eadapters.BaseAdapter()

        self.assertRaises(
            appier.NotImplementedError,
            lambda: adapter.set_gift_slip_order(True, "key"),
        )

    def test_set_notes_order(self):
        adapter = eadapters.BaseAdapter()

        self.assertRaises(
            appier.NotImplementedError,
            lambda: adapter.set_notes_order("Wrap separately", "key"),
        )

    def test_set_source_bag(self):
        adapter = eadapters.BaseAdapter()

        self.assertRaises(
            appier.NotImplementedError,
            lambda: adapter.set_source_bag(dict(channel="direct")),
        )
