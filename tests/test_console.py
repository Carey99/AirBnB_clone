#!/usr/bin/python3
"""
    Tests The console
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import Myconsole


class TestMyconsole(unittest.TestCase):
    def test_EOF(self):
        """EOF"""
        console = Myconsole()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            console.do_EOF('')
            self.assertEqual(fake_out.getvalue(), '\n')

    def test_quit(self):
        """quit"""
        console = Myconsole()
        self.assertTrue(console.do_quit(''))


if __name__ == '__main__':
    unittest.main()
