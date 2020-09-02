from tkinter import *
from tkinter import messagebox, ttk
import PIL
from PIL import ImageTk, Image
from Back_End import Connection
from ttkthemes import ThemedStyle


class Admin_Customer:
    def __init__(self, master):
        """
        Function to configure the main window.
        """
        self.master = master
        self.master.title('Customer Management:')
        self.master.state('zoomed')
        self.master.protocol("WM_DELETE_WINDOW", self.destroy)
        self.master.iconbitmap('logo.ico')

        self.style = ThemedStyle(self.master)
        self.style.theme_use('scidgreen')
        self.style.configure('my.TButton', font=('Verdana', 13), activeforeground='black', border='0')

        load_image = PIL.Image.open('back_admin.jpg')
        load_image = load_image.resize((1536, 864), Image.ANTIALIAS)
        render_image = ImageTk.PhotoImage(load_image)
        image_label = ttk.Label(self.master, image=render_image)
        image_label.image = render_image
        image_label.place(x=-2, y=-2)

        panedwindow = ttk.Panedwindow(image_label, orient=HORIZONTAL)

        frame1 = ttk.Frame(panedwindow, height=395, width=500, relief=SUNKEN)
        frame2 = ttk.Frame(panedwindow, height=395, width=600, relief=SUNKEN)
        panedwindow.place(x=200, y=180)
        panedwindow.add(frame1, weight=1)
        panedwindow.add(frame2, weight=3)

        self.Customer_Name = ttk.Label(frame1, text='Customer Name:')
        self.Customer_Name.config(font=('Courier', 18,))
        self.Customer_Name.place(x=4, y=45)
        self.Customer_Name_entry = ttk.Entry(frame1)
        self.Customer_Name_entry.config(font=('', 16,))
        self.Customer_Name_entry.place(x=220, y=45)

        self.Product_ID = ttk.Label(frame1, text='Product ID:')
        self.Product_ID.config(font=('Courier', 18,))
        self.Product_ID.place(x=4, y=105)
        self.Product_ID_entry = ttk.Entry(frame1)
        self.Product_ID_entry.config(font=('', 16,))
        self.Product_ID_entry.place(x=220, y=105)

        self.Quantity = ttk.Label(frame1, text='Quantity:')
        self.Quantity.config(font=('Courier', 18,))
        self.Quantity.place(x=4, y=165)
        self.Quantity_entry = ttk.Entry(frame1)
        self.Quantity_entry.config(font=('', 16,))
        self.Quantity_entry.place(x=220, y=165)

        self.Pay_Method = ttk.Label(frame1, text='Payment Method:')
        self.Pay_Method.config(font=('Courier', 18,))
        self.Pay_Method.place(x=4, y=225)
        self.Pay_Method_entry = ttk.Entry(frame1)
        self.Pay_Method_entry.config(font=('', 16,))
        self.Pay_Method_entry.place(x=220, y=225)

        self.Date = ttk.Label(frame1, text='Shipped Date:')
        self.Date.config(font=('Courier', 18,))
        self.Date.place(x=4, y=285)
        self.Date_entry = ttk.Entry(frame1)
        self.Date_entry.config(font=('', 16,))
        self.Date_entry.place(x=220, y=285)

        self.delete_btn = ttk.Button(frame1, text='Delete Customer >')
        self.delete_btn.place(x=50, y=340)
        self.delete_btn.config(style='my.TButton')
        self.delete_btn.bind('<ButtonRelease-1>', self.delete_customer)

        self.clear_btn = ttk.Button(frame1, text='Clear', command=self.clear)
        self.clear_btn.place(x=280, y=340)
        self.clear_btn.config(style='my.TButton')

        Data_frame = ttk.Frame(frame2, relief=SOLID)
        Data_frame.place(x=20, y=80, height=280, width=570)
        Data_frame.config(border=3)
        scroll_x = Scrollbar(Data_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Data_frame, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.Data_table = ttk.Treeview(Data_frame, columns=(
            'Customer_Name', 'Product_ID', 'Quantity', 'Payment Method', 'Shipped Date'),
                                       xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set, show='headings')
        scroll_x.config(command=self.Data_table.xview)
        scroll_y.config(command=self.Data_table.yview)
        self.Data_table.heading('Customer_Name', text='Customer_Name')
        self.Data_table.heading('Product_ID', text='Product_ID')
        self.Data_table.heading('Quantity', text='Quantity')
        self.Data_table.heading('Payment Method', text='Payment Method')
        self.Data_table.heading('Shipped Date', text='Shipped Date')

        self.Data_table.pack(fill=BOTH, expand=1)

        query = 'select * from customer;'
        rows = Connection.my_database().selectOne(query, )
        Connection.my_database().close()
        for i in rows:
            self.Data_table.insert('', 'end', values=i)
        self._build_tree()
        self.Data_table.bind('<ButtonRelease-1>', self.get_cursor)

        self.search_label = ttk.Label(frame2, text='Search By:')
        self.search_label.config(font=('Helvetica', 15,))
        self.search_label.place(x=4, y=10)

        self.search_select = ttk.Combobox(frame2)
        self.search_select.place(x=120, y=10)
        self.search_select.config(font=('', 15,), width=15)
        self.search_select['values'] = ('Customer_Name')

        self.search_box = ttk.Entry(frame2)
        self.search_box.place(x=350, y=10)
        self.search_box.config(font=('', 15,), width=15)

        self.search_btn = ttk.Button(frame2, text='Search', command=self.search_in_database)
        self.search_btn.place(x=250, y=42)
        self.search_btn.config(style='my.TButton')

        load_image_logout = PIL.Image.open('back.jpg')
        load_image_logout = load_image_logout.resize((50, 50), Image.ANTIALIAS)
        self.logout_image = ImageTk.PhotoImage(load_image_logout)

        log_out_btn = Button(self.master, image=self.logout_image, highlightthickness=0, bd=0, command=self.destroy)
        log_out_btn.place(x=1, y=1)
        log_out_btn.image = self.logout_image

        load_image_refresh = PIL.Image.open('refresh.jpg')
        load_image_refresh = load_image_refresh.resize((40, 40), Image.ANTIALIAS)
        self.refresh_image = ImageTk.PhotoImage(load_image_refresh)

        log_out_btn = Button(frame2, image=self.refresh_image, highlightthickness=0, bd=0, command=self._build_tree)
        log_out_btn.place(x=530, y=5)
        log_out_btn.image = self.refresh_image

    @classmethod
    def bubbleSort(cls, array):
        """
        Function to do a bubble sort.
        :param array:list of customers name
        :type array:list
        :return: array
        :rtype: list
        """
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    (array[j], array[j + 1]) = (array[j + 1], array[j])
        return array

    def _build_tree(self):
        """
        Function to insert the value of databases in a tree view.
        """
        query = 'select * from customer;'
        rows = Connection.my_database().selectOne(query, )
        Connection.my_database().close()
        new_data = []
        for i in rows:
            new_data.append(i)
        self.bubbleSort(new_data)
        if len(rows) != 0:
            self.Data_table.delete(*self.Data_table.get_children())
            for row in new_data:
                self.Data_table.insert('', END, values=row)

    def get_cursor(self, event):
        """
        Function to insert data in entry box when an row on tree view is focused.
        """
        cursor = self.Data_table.focus()
        content = self.Data_table.item(cursor)
        row = content['values']
        self.Customer_Name_entry.delete(0, END)
        self.Customer_Name_entry.insert(0, row[0])
        self.Product_ID_entry.delete(0, END)
        self.Product_ID_entry.insert(0, row[1])
        self.Quantity_entry.delete(0, END)
        self.Quantity_entry.insert(0, row[2])
        self.Pay_Method_entry.delete(0, END)
        self.Pay_Method_entry.insert(0, row[3])
        self.Date_entry.delete(0, END)
        self.Date_entry.insert(0, row[4])

    def delete_customer(self, event):
        """
        Function to delete the customer details from database and tree view.
        """
        self.Data_table.get_children()
        self.Data_table.focus_get()
        answer = messagebox.askquestion('Confirm', 'Are you sure to delete this customer detail?', parent=self.master)
        if answer == 'yes':
            query = 'delete from customer where Customer_Name=%s and Product_ID=%s;'
            values = (self.Customer_Name_entry.get().strip(), self.Product_ID_entry.get().strip())
            Connection.my_database().operation(query, values)
            Connection.my_database().close()
            messagebox.showinfo('Hurray', 'Successfully removed  customer details!', parent=self.master)
            self.clear()
            self._build_tree()

    def clear(self):
        """
        Function to delete all the values in Entry Boxes.
        """
        self.Customer_Name_entry.delete(0, END)
        self.Product_ID_entry.delete(0, END)
        self.Quantity_entry.delete(0, END)
        self.Pay_Method_entry.delete(0, END)
        self.Date_entry.delete(0, END)

    @classmethod
    def search_by(cls, customer_list, customer_detail):
        """
        Function for the linear search
        :param customer_list: list of customer who are in customer table
        :type customer_list:list
        :param customer_detail:specification of customer
        :type customer_detail:str
        :return: True
        :return: False
        :rtype: bool
        """
        for i in range(len(customer_list)):
            if customer_detail == customer_list[i]:
                return True
        return False

    def search_in_database(self):
        """
        Function to search the data from database with help of linear search function and focus it in a tree view .
        """
        query = 'select Customer_Name from customer;'
        record = Connection.my_database().selectOne(query, )
        Connection.my_database().close()
        list_customer_name = []
        for i in record:
            list_customer_name.append(i[0])
        if self.search_select.get() == 'Customer_Name':
            try:
                if self.search_by(list_customer_name, self.search_box.get().capitalize()):
                    query = 'select * from customer where Customer_Name=%s;'
                    values = (self.search_box.get(),)
                    get_data = Connection.my_database().selectAll(query, values)
                    Connection.my_database().close()

                    if len(get_data) != 0:
                        self.Data_table.delete(*self.Data_table.get_children())
                        for row in get_data:
                            self.Data_table.insert('', END, values=row)
                else:
                    messagebox.showerror('Sorry', 'No such Customer Name found!', parent=self.master)
            except ValueError:
                messagebox.showerror('Oops', 'Customer Name must be in alphabets!', parent=self.master)

    def destroy(self):
        """
        Function to get back by destroying current window.
        """
        if messagebox.askyesnocancel('Confirmation', 'Are you sure to go back?', parent=self.master):
            self.master.destroy()
