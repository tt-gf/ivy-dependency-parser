# -*- coding: utf-8 -*-

import ivydepparse.ivydepparse as ivydepparse
import unittest

class IvyDepParseTests(unittest.TestCase):
    def test_example(self):
        actual = ivydepparse.convert('ivy-example.xml')
        self.assertIn('org=com.ttgf|name=myGreatDep|rev=1.2.3|conf=' +
                      ','.join(set(['debug', 'release', 'other'])),
                      actual)
        self.assertIn('org=com.ttgf|name=myGreatDebugDep|rev=2.3.4|conf=debug',
                      actual)
