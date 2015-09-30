# -*- coding: utf-8 -*-

import ivydepparse.ivydepparse as ivydepparse
import unittest

class IvyDepParseTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(ivydepparse.convert('ivy-example.xml'),
            'org=com.ttgf|name=myGreatDep|rev=1.2.3|conf=debug,release;org=com.ttgf|name=myGreatDebugDep|rev=2.3.4|conf=debug')
