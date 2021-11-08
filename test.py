# -*- coding: utf-8 -*-
import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import emoji


class BookTest(unittest.TestCase):
    
    def setUp(self):
        with open('Book/Chapters/01.md', 'r') as file:
            self.chapter01 = file.read().replace('\n', '')

    def test_chapter01(self):
        self.assertEqual(self.chapter01, '# Chapter 1It was a dark and stormy night...')

    @unittest.skip("not implemented yet")
    def test_characters(self):
        self.fail("not implemented yet")

    @unittest.skip("not implemented yet")
    def test_places(self):
        self.fail("not implemented yet")

    @unittest.skip("not implemented yet")
    def test_tech(self):
        self.fail("not implemented yet")

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
