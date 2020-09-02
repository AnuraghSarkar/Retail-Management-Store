import unittest
from Model import employee


class test_employee(unittest.TestCase):

    def setUp(self):
        """
        Function to set up the reference data for employee.Register()
        """
        super(test_employee, self).setUp()
        self.emp = employee.Register(5, 'Rajesh Khanna', 'Username', 'Password', '988884488', 'xyz@gmail.com')

    def test_setEmployee_ID(self):
        """
        Function to test if the set Product_ID works or not.
        """
        self.emp.set_Employee_ID(15)
        self.assertEqual(15, self.emp.get_Employee_ID())
        self.assertNotEqual(5, self.emp.get_Employee_ID())

    def test_getEmployee_ID(self):
        """
        Function to test if the get Employee ID works or not.
        """
        self.assertEqual(5, self.emp.get_Employee_ID())
        self.assertNotEqual(15, self.emp.get_Employee_ID())

    def test_setName(self):
        """
        Function to test if set Name works or not.
        """
        self.emp.set_Name('Raju')
        self.assertEqual('Raju', self.emp.get_Name())
        self.assertNotEqual('Raj', self.emp.get_Name())

    def test_getName(self):
        """
        Function to test if get Name works or not.
        """
        self.assertEqual('Rajesh Khanna', self.emp.get_Name())
        self.assertNotEqual('Rajesh Payal', self.emp.get_Name())

    def test_setUsername(self):
        """
        Function to test if set Username works or not.
        """
        self.emp.set_Username('Rajesh')
        self.assertEqual('Rajesh', self.emp.get_Username())
        self.assertNotEqual('Raju', self.emp.get_Username())

    def test_getUsername(self):
        """
        Function to test if get Username works or not.
        """
        self.assertEqual('Username', self.emp.get_Username())
        self.assertNotEqual('User', self.emp.get_Username())

    def test_setPassword(self):
        """
        Function to test if set Password works or not.
        """
        self.emp.set_Password('123@123')
        self.assertEqual('123@123', self.emp.get_Password())
        self.assertNotEqual('1223', self.emp.get_Password())

    def test_getPassword(self):
        """
        Function to test if get Password works or not.
        """
        self.assertEqual('Password', self.emp.get_Password())
        self.assertNotEqual('123@123', self.emp.get_Password())

    def test_setContact(self):
        """
        Function to test if set Contact works or not.
        """
        self.emp.set_Contact('98888888')
        self.assertEqual('98888888', self.emp.get_Contact())
        self.assertNotEqual('48888', self.emp.get_Contact())

    def test_getContact(self):
        """
        Function to test if get Contact works or not.
        """
        self.assertEqual('988884488', self.emp.get_Contact())
        self.assertNotEqual('88', self.emp.get_Contact())

    def test_setEmail(self):
        """
        Function to test if set Email works or not.
        """
        self.emp.set_Email('abc@gmail.com')
        self.assertEqual('abc@gmail.com', self.emp.get_Email())
        self.assertNotEqual('abc745@gmail.com', self.emp.get_Email())

    def test_getEmail(self):
        """
        Function to test if get Email works or not.
        """
        self.assertEqual('xyz@gmail.com', self.emp.get_Email())
        self.assertNotEqual('abc@gmail.com', self.emp.get_Email())

    def tearDown(self):
        """
        Function to tear down the employee reference which was set up to None
        """
        super(test_employee, self).tearDown()
        self.emp = None


if __name__ == '__main__':
    unittest.main()
