import unittest
from Front_End.admin_customer import *


class test_bubble_sort(unittest.TestCase):

    def setup(self):
        super(test_bubble_sort, self).setUp()

    def test_bubble_sort(self):
        """
        Function to test if bubble sorting is working.
        """
        self.list_name = ['Ram', 'Shyam', 'Anabella', 'Kale']
        self.expected = ['Anabella', 'Kale', 'Ram', 'Shyam']
        self.assertEqual(self.expected, Admin_Customer.bubbleSort(self.list_name))

    def tearDown(self):
        """
        Function to tear down the list to empty
        """
        super(test_bubble_sort, self).tearDown()
        self.list_name = []
        self.expected = []


if __name__ == '__main__':
    unittest.main()
