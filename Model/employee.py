class Register:
    def __init__(self, Employee_ID, Name, Username, Password, Contact, Email):
        self.__Employee_ID = Employee_ID
        self.__Name = Name
        self.__Username = Username
        self.__Password = Password
        self.__Contact = Contact
        self.__Email = Email

    def set_Employee_ID(self, Employee_ID):
        """
        Function to set the value for Employee ID
        :param Employee_ID:set Employee_ID
        :type Employee_ID: int
        """
        self.__Employee_ID = Employee_ID

    def get_Employee_ID(self):
        """
        Function to return the set value of Employee_ID.
        :rtype: int
        """
        return self.__Employee_ID

    def set_Name(self, Name):
        """
        Function to set the value for Name
        :param Name: set Name
        :type Name: str
        """
        self.__Name = Name

    def get_Name(self):
        """
        Function to return the set value of Name.
        :rtype: str
        """
        return self.__Name

    def set_Username(self, Username):
        """
        Function to set the value for Username
        :param Username: set Username
        :type Username: str
        """
        self.__Username = Username

    def get_Username(self):
        """
        Function to return the set value of Username.
        :rtype: str
        """
        return self.__Username

    def set_Password(self, Password):
        """
        Function to set value for Password
        :param Password:set Password
        :type Password:str
        """
        self.__Password = Password

    def get_Password(self):
        """
        Function to return the set value of Password.
        :rtype: str
        """
        return self.__Password

    def set_Contact(self, Contact):
        """
        Function to set the value for Contact
        :param Contact:set Contact
        :type Contact:int
        """
        self.__Contact = Contact

    def get_Contact(self):
        """
        Function to return the set value of Contact
        :rtype: int
        """
        return self.__Contact

    def set_Email(self, Email):
        """
        Function to set the value for Email
        :param Email:set Email
        :type Email:str
        """
        self.__Email = Email

    def get_Email(self):
        """
        Function to return the set value of Email.
        :return: Email:
        :rtype: str:
        """
        return self.__Email
