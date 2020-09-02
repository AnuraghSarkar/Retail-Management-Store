import unittest
from Back_End import Connection


class TestRegister_Interface(unittest.TestCase):
    def setUp(self):
        """
        Function to set up the list  and insert a employee data and in database.
        """
        super(TestRegister_Interface, self).setUp()
        self.values = (5111, 'Rajesh', 'Kale123', '123456', '456456', 'ram@gmail.com')
        self.get_list = [(5111, 'Rajesh', 'Kale123', '123456', '456456', 'ram@gmail.com')]
        self.get_list2 = [(5141, 'Rajesh', 'Kale123', '123456', '456456', 'ram@gmail.com')]
        query = 'insert into employees values(%s,%s,%s,%s,%s,%s);'
        Connection.my_database().operation(query, self.values)
        Connection.my_database().close()

    def test_registration_checker(self):
        """
        Function to check if employee data is added or not to database and added data is equal to given data or not.
        """
        query_select = 'select * from employees where Employee_ID=%s;'
        value = (5111,)
        data = Connection.my_database().selectAll(query_select, value)
        Connection.my_database().close()
        self.assertEqual(self.get_list, data)
        self.assertNotEqual(self.get_list2, data)

    def tearDown(self):
        """
        Function to delete the the employee data that is added to database and tear down the list to null which are being setup.
        """
        super(TestRegister_Interface, self).tearDown()
        self.values = None
        self.get_list = []
        self.get_list2 = []
        query = 'delete from employees where Employee_ID=%s;'
        value = (5111,)
        Connection.my_database().operation(query, value)
        Connection.my_database().close()


if __name__ == '__main__':
    unittest.main()
