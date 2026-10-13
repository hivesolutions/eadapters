#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import appier

import eadapters


class BaseTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(1 + 1, 2)

    def test_set_gift_slip_order(self):
        adapter = eadapters.BaseAdapter()

        self.assertRaises(
            appier.NotImplementedError,
            lambda: adapter.set_gift_slip_order(True, "key"),
        )
