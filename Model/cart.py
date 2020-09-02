class Add_to_cart:
    def __init__(self, Product_ID, Quantity, Price):
        self.__Product_ID = Product_ID
        self.__Quantity = Quantity
        self.__Price = Price

    def set_Product_ID(self, Product_ID):
        """
        Function to set value for Product_ID
        :param Product_ID: set Product_ID
        :type Product_ID: int
        """
        self.__Product_ID = Product_ID

    def get_Product_ID(self):
        """
        Function to get the set value of Product_ID
        :return: Product-ID
        :rtype: int
        """
        return self.__Product_ID

    def set_Quantity(self, Quantity):
        """
        Function to set value for Quantity
        :param Quantity: set Quantity value
        :type Quantity: int
        """
        self.__Quantity = Quantity

    def get_Quantity(self):
        """
        Function to get the set value of Quantity
        :return: Quantity
        :rtype: int
        """
        return self.__Quantity

    def set_Price(self, Price):
        """
        Function to set value for Price
        :param Price: set Price
        :type Price: int
        """
        self.__Price = Price

    def get_Price(self):
        """
        Function to get set value of Price
        :return: Price
        :rtype: int
        """
        return self.__Price
