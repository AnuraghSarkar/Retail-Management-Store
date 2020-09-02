class Products:
    def __init__(self, Product_ID, Product_Category, Product_Name, Quantity_In, Product_Stock, Amount):
        self.__Product_ID = Product_ID
        self.__Product_Category = Product_Category
        self.__Product_Name = Product_Name
        self.__Quantity_In = Quantity_In
        self.__Product_Stock = Product_Stock
        self.__Amount = Amount

    def setProduct_ID(self, Product_ID):
        """
        Function to set value for Product_ID
        :param Product_ID: set Product_ID
        :type Product_ID: int
        """
        self.__Product_ID = Product_ID

    def getProduct_ID(self):
        """
        Function to return set value of Product_ID
        :return:
        :rtype:
        """
        return self.__Product_ID

    def setProduct_Category(self, Product_Category):
        """
        Function to set value for Product_Category
        :param Product_Category: set Product_Category
        :type Product_Category: str
        """
        self.__Product_Category = Product_Category

    def getProduct_Category(self):
        """
        Function to return set value of Product_Category
        :return: Product_Category
        :rtype: str
        """
        return self.__Product_Category

    def setProduct_Name(self, Product_Name):
        """
        Function to set value for Product_Name
        :param Product_Name: set Product_Name
        :type Product_Name: str
        """
        self.__Product_Name = Product_Name

    def getProduct_Name(self):
        """
        Function to return set value of Product_Name
        :return: Product_Name
        :rtype: str
        """
        return self.__Product_Name

    def setQuantity_In(self, Quantity_In):
        """
        Function to set value for Quantity_In
        :param Quantity_In: set Quantity_In
        :type Quantity_In: str
        """
        self.__Quantity_In = Quantity_In

    def getQuantity_In(self):
        """
        Function to return the set value of Quantity_In
        :return: Quantity_In
        :rtype: str
        """
        return self.__Quantity_In

    def setProduct_Stock(self, Product_Stock):
        """
        Function to set value for Product_Stock
        :param Product_Stock: set Product_Stock
        :type Product_Stock: int
        """
        self.__Product_Stock = Product_Stock

    def getProduct_Stock(self):
        """
        Function to return the set value of Product_Stock
        :return: Product_Stock
        :rtype: int
        """
        return self.__Product_Stock

    def setAmount(self, Amount):
        """
        Function to set value for Amount
        :param Amount: set Amount
        :type Amount: int
        """
        self.__Amount = Amount

    def getAmount(self):
        """
        Function to return set value of Amount
        :return: Amount
        :rtype: int
        """
        return self.__Amount
