import unittest
from Back_End import Connection


class test_admin_product(unittest.TestCase):

    def setUp(self):
        """
        Function to setup the list for the testing.
        """
        super(test_admin_product, self).setUp()
        self.values = (123, 'Meat & Fish', 'Pork', 'Kilogram', 120, 1300)
        self.give_list = [(123, 'Meat & Fish', 'Pork', 'Kilogram', 120, 1300)]
        self.give_list_false = [(564, 'Meat & Fish', 'Pork', 'Kilogram', 120, 1300)]
        self.update_data = [(123, 'Meat & Fish', 'Pork', 'Kilogram', 100, 1500)]

    def test_add_product(self):
        """
        Function to test if the product is added to database or not.
        """
        query = 'insert into product values(%s,%s,%s,%s,%s,%s);'
        Connection.my_database().operation(query, self.values)
        Connection.my_database().close()
        query_select = 'select * from product where Product_ID=%s;'
        id_value = (123,)
        self.get_list = Connection.my_database().selectAll(query_select, id_value)
        Connection.my_database().close()
        self.assertEqual(self.give_list, self.get_list)
        self.assertNotEqual(self.give_list_false, self.get_list)

    def test_update_product(self):
        """
        Function to test if the product is updated in database or not.
        """
        query = 'insert into product values(%s,%s,%s,%s,%s,%s);'
        Connection.my_database().operation(query, self.values)
        Connection.my_database().close()
        query = 'update product set Product_Category=%s,Product_Name=%s,Quantity_In=%s,Product_Stock=%s,Amount=%s where Product_ID=123;'
        value = ('Meat & Fish', 'Pork', 'Kilogram', 100, 1500)
        update_data = Connection.my_database().operation(query, value)
        query2 = 'select * from product where Product_ID=123;'
        self.updated_data = Connection.my_database().selectOne(query2)
        Connection.my_database().close()
        self.assertEqual(self.updated_data, self.update_data)
        self.assertNotEqual(self.give_list_false, update_data)

    def tearDown(self):
        """
        Function to tear down the all list that are setup.
        """
        super(test_admin_product, self).tearDown()
        self.values = None
        self.give_list = []
        self.give_list_false = []
        self.update_data = []
        query = 'delete from product where Product_ID=%s;'
        Connection.my_database().operation(query, (123,))
        Connection.my_database().close()


if __name__ == '__main__':
    unittest.main()
