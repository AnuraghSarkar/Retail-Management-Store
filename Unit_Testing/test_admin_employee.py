import unittest
from Front_End.admin_employee import *


class test_linear_search_admin_employee(unittest.TestCase):
    def setUp(self):
        """
        Function to set up the list and variables for testing.
        :return:
        :rtype:
        """
        super(test_linear_search_admin_employee, self).setUp()
        self.list_id = ['Ok', 'Rajesh', 'Check', 'Hari', 'Failed']
        self.item = 'Failed'
        self.item2 = 'Passed'

    def test_linear_search(self):
        """
        Function to test if linear search works or not.
        """
        self.assertEqual(True, Admin_Employee.search_by(self.list_id, self.item))
        self.assertFalse(False, Admin_Employee.search_by(self.list_id, self.item2))

    def tearDown(self):
        """
        Function to tear down the list and variables that are set up to None
        """
        super(test_linear_search_admin_employee, self).tearDown()
        self.list_id = []
        self.item = None
        self.item2 = None


if __name__ == '__main__':
    unittest.main()
