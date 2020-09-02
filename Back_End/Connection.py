import mysql.connector


class my_database:
    def __init__(self):
        self.con = mysql.connector.connect(host='127.0.0.1', user='root', passwd='Tud977031@', database='sql_hr')
        self.my_cursor = self.con.cursor(buffered=True)

    def operation(self, query, values):
        """
        Function to do any operations in a database.
        :param query:
        :type query:
        :param values:
        :type values:
        """
        self.my_cursor.execute(query, values)
        self.con.commit()

    def selectAll(self, query, values):
        """
        Function to fetch data from given query and values and then return it.
        :param query:
        :type query:
        :param values:
        :type values:
        :return: records:
        :rtype: list:
        """

        self.my_cursor.execute(query, values)
        records = self.my_cursor.fetchall()
        self.con.commit()
        return records

    def selectOne(self, query):
        """
        Function to fetch data from query only and then return it.
        :param query:
        :type query:
        :return:
        :rtype:
        """
        self.my_cursor.execute(query)
        records = self.my_cursor.fetchall()
        self.con.commit()
        return records

    def close(self):
        if self.my_cursor:
            self.my_cursor.close()
        if self.con:
            self.con.close()
