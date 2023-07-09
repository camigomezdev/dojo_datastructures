""" Test file for BinarySearchAlgorithms"""
# __doc__ (Test file for little data structure app testing
# Binary Search Algorithms)

import unittest

from pmvcp.core.models.about import About


class TestBinarySearchAlgorithms(unittest.TestCase):
    """
    Class for unittest BinarySearchAlgorithms
    """

    def setUp(self):
        """
        Instance the app()
        """
        self.about = About()

    def test_credits(self):
        """
        Get from Info the Test App title 
        """
        resolve = self.about.get('title')
        title = 'Test App'

        self.assertEqual(title, resolve['title'])


if __name__ == '__main__':
    unittest.main()
