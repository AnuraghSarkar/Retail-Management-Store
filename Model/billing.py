class Customer:
    def __init__(self, Customer_Name, Product_ID, Quantity, Payment_Method, Shipped_Data):
        self.__Customer_Name = Customer_Name
        self.__Product_ID = Product_ID
        self.__Quantity = Quantity
        self.__Payment_Method = Payment_Method
        self.__Shipped_Date = Shipped_Data

    def set_Customer_Name(self, Customer_Name):
        """
        Function to set value for Customer Name.
        :param Customer_Name:set Customer_Name
        :type Customer_Name:str
        """
        self.__Customer_Name = Customer_Name

    def get_Customer_Name(self):
        return self.__Customer_Name

    def set_Product_ID(self, Product_ID):
        """
        Function to set value for Product_ID
        :param Product_ID: set Product-Id
        :type Product_ID: int
        """
        self.__Product_ID = Product_ID

    def get_Product_ID(self):
        """
        Function to return set value of Product_ID
        :return: Product_ID
        :rtype: int

        """
        return self.__Product_ID

    def set_Quantity(self, Quantity):
        """
        Function to set value for Quantity
        :param Quantity: set Quantity
        :type Quantity: int
        """

        self.__Quantity = Quantity

    def get_Quantity(self):
        """
        Function to return set value of Quantity
        :return: Quantity
        :rtype: int
        """
        return self.__Quantity

    def set_Payment_Method(self, Payment_Method):
        """
        Function to set Payment Method.
        :param Payment_Method: set Payment_Method
        :type Payment_Method: str
        """
        self.__Payment_Method = Payment_Method

    def get_Payment_Method(self):
        """
        Function to return set value of Payment_Method
        :return: Payment_Method
        :rtype: str
        """
        return self.__Payment_Method

    def set_Shipped_Date(self, Shipped_Date):
        """
        Function to set Shipped Date
        :param Shipped_Date: set Shipped Date
        :type Shipped_Date: str
        """
        self.__Shipped_Date = Shipped_Date

    def get_Shipped_Date(self):
        """
        Function to return set value of Shipped_Date
        :return: Shipped_Date
        :rtype: str
        """

        return self.__Shipped_Date
