import os
import sys
# unittestモジュールを読み込んで利用
import unittest

# importで参照するパスをappend
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

class TestFunc(unittest.TestCase):
    def test_func(self):
        from hello import func
        self.assertIsNone(func('こんにちは'))
