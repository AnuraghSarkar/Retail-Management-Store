import datetime
import time
from random import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import PIL
from PIL import ImageTk, Image
from ttkthemes import ThemedStyle
from Back_End import Connection
from Model import cart, billing  
Time = time.strftime('%H:%M%p')
rand_num = randint(1000, 9999)
bill_num = str(f'BILL{rand_num}')
Today = datetime.date.today()
Date = Today.strftime("%d/%m/%Y")


class after_login:
    def __init__(self, master):
        """
        Function to configure the main window.
        """
        self.master = master
        self.master.title('Employee Page:')
        self.master.state('zoomed')
        self.master.protocol("WM_DELETE_WINDOW", self.destroy)
        self.master.iconbitmap('logo.ico')

        self.style = ThemedStyle(self.master)
        self.style.set_theme('scidgreen')
        self.style.configure('my.TButton', font=('Verdana', 16), activeforeground='black', border='0')
        load_image = PIL.Image.open('back_admin.jpg')
        load_image = load_image.resize((1536, 864), Image.ANTIALIAS)
        render_image = ImageTk.PhotoImage(load_image)
        image_label = ttk.Label(self.master, image=render_image)
        image_label.image = render_image
        image_label.place(x=-2, y=-2)

        panedwindow = ttk.Panedwindow(image_label, orient=HORIZONTAL)

        frame1 = ttk.Frame(panedwindow, height=600, width=560, relief=SUNKEN)
        frame2 = ttk.Frame(panedwindow, height=600, width=450, relief=SUNKEN)
        panedwindow.place(x=210, y=120)
        panedwindow.add(frame1, weight=4)
        panedwindow.add(frame2, weight=4)

        self.date_l = ttk.Label(frame1, text=str(Time))
        self.date_l.config(font=('arial', 16, 'bold'))
        self.date_l.place(x=2, y=10)

        self.customer_name = ttk.Label(frame1, text='Customer Name:')
        self.customer_name.config(font=('Courier', 18,))
        self.customer_name.place(x=4, y=45)

        self.customer_name_entry = ttk.Entry(frame1)
        self.customer_name_entry.config(font=('', 16,))
        self.customer_name_entry.place(x=260, y=45)

        self.product_category = ttk.Label(frame1, text='Product Category:')
        self.product_category.config(font=('Courier', 18,))
        self.product_category.place(x=4, y=105)

        self.product_category_entry = ttk.Combobox(frame1)
        self.product_category_entry.place(x=260, y=105)
        self.product_category_entry.config(font=('', 16,))
        self.product_category_function()
        self.product_category_entry.bind('<<ComboboxSelected>>', self.product_name_function)

        self.product_name = ttk.Label(frame1, text='Product Name:')
        self.product_name.config(font=('Courier', 18,))
        self.product_name.place(x=4, y=165)

        self.product_name_entry = ttk.Combobox(frame1)
        self.product_name_entry.place(x=260, y=165)

        self.product_name_entry.config(font=('', 16,))
        self.product_name_entry.bind('<<ComboboxSelected>>', self.quantity_in_function)

        self.quantity_in_label = ttk.Label(frame1, text='Quantity in:')
        self.quantity_in_label.config(font=('Courier', 18,))
        self.quantity_in_label.place(x=4, y=225)

        self.quantity_in_entry = ttk.Combobox(frame1)
        self.quantity_in_entry.place(x=260, y=225)
        self.quantity_in_entry.config(font=('', 16))
        self.quantity_in_entry.bind('<<ComboboxSelected>>', self.in_stock, add="+")
        self.quantity_in_entry.bind('<<ComboboxSelected>>', self.get_product_id_function, add="+")

        self.quantity_label = ttk.Label(frame1, text='Quantity:')
        self.quantity_label.config(font=('Courier', 18,))
        self.quantity_label.place(x=4, y=285)

        self.quantity_get_entry = ttk.Entry(frame1)
        self.quantity_get_entry.config(font=('', 16))
        self.quantity_get_entry.place(x=260, y=285)

        self.Product_ID = ttk.Label(frame1, text='Product ID:')
        self.Product_ID.config(font=('Courier', 18,))
        self.Product_ID.place(x=4, y=345)
        self.Product_ID_entry = ttk.Entry(frame1)
        self.Product_ID_entry.config(font=('', 16))
        self.Product_ID_entry.place(x=260, y=345)

        self.Total = ttk.Label(frame1, text='Total:')
        self.Total.config(font=('Courier', 18,))
        self.Total.place(x=4, y=405)
        self.Total_entry = ttk.Entry(frame1)
        self.Total_entry.config(font=('', 16))
        self.Total_entry.place(x=260, y=405)

        self.payment_method = ttk.Label(frame1, text='Payment Method:')
        self.payment_method.place(x=4, y=470)
        self.payment_method.config(font=('Courier', 18,))

        self.payment_method_entry = ttk.Combobox(frame1)
        self.payment_method_entry.place(x=260, y=470)
        self.payment_method_entry.config(values=('Cash', 'Cheque', 'Debit Card', 'Credit Card'), font=('', 16,))

        self.cart_btn = ttk.Button(frame1, text='Add to Cart', command=self.add_to_cart)
        self.cart_btn.place(x=50, y=540)
        self.cart_btn.config(style='my.TButton')

        self.total_btn = ttk.Button(frame1, text='Total', command=self.product_amount_function)
        self.total_btn.place(x=280, y=540)
        self.total_btn.config(style='my.TButton')

        self.clear_btn = ttk.Button(frame1, text='Clear', command=self.clear)
        self.clear_btn.place(x=420, y=540)
        self.clear_btn.config(style='my.TButton')

        Data_frame = ttk.Frame(frame2, relief=SOLID)
        Data_frame.place(x=25, y=15, height=500, width=400)
        Data_frame.config(border=3)
        scroll_x = Scrollbar(Data_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Data_frame, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.Data_table = ttk.Treeview(Data_frame, columns=('Product_ID', 'Quantity', 'Price'),
                                       xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set, show='headings')
        scroll_x.config(command=self.Data_table.xview)
        scroll_y.config(command=self.Data_table.yview)
        self.Data_table.heading('Product_ID', text='Product_ID')
        self.Data_table.heading('Quantity', text='Quantity')
        self.Data_table.heading('Price', text='Price')
        self.Data_table.pack(fill=BOTH, expand=1)

        query = 'select * from cart;'
        rows = Connection.my_database().selectOne(query, )
        Connection.my_database().close()
        for i in rows:
            self.Data_table.insert('', 'end', values=i)

        self._build_tree()
        self.Data_table.bind('<ButtonRelease-1>', self.get_cursor)

        self.delete_cart_btn = ttk.Button(frame2, text='Delete', command=self.delete_from_cart)
        self.delete_cart_btn.place(x=10, y=540)
        self.delete_cart_btn.config(style='my.TButton')

        self.save_cart_btn = ttk.Button(frame2, text='Add to Database', command=self.add_to_database)
        self.save_cart_btn.place(x=130, y=540)
        self.save_cart_btn.config(style='my.TButton')

        self.generate_bill = ttk.Button(frame2, text='Get Bill', command=self.bill)
        self.generate_bill.place(x=350, y=540)
        self.generate_bill.config(style='my.TButton')

        load_image_logout = PIL.Image.open('back.jpg')
        load_image_logout = load_image_logout.resize((50, 50), Image.ANTIALIAS)
        self.logout_image = ImageTk.PhotoImage(load_image_logout)

        log_out_btn = Button(self.master, image=self.logout_image, highlightthickness=0, bd=0, command=self.destroy)
        log_out_btn.place(x=1, y=1)
        log_out_btn.image = self.logout_image

    def _build_tree(self):
        """
        Function to insert the database value in a tree view.:
        """
        query = 'select * from cart;'
        rows = Connection.my_database().selectOne(query, )
        Connection.my_database().close()
        if len(rows) != 0:
            self.Data_table.delete(*self.Data_table.get_children())
            for row in rows:
                self.Data_table.insert('', END, values=row)

    def get_cursor(self, event):
        """
        Function to insert data in Entry Box whenever a row is focused in tree view.
        """
        cursor = self.Data_table.focus()
        content = self.Data_table.item(cursor)
        row = content['values']
        self.Product_ID_entry.delete(0, END)
        self.Product_ID_entry.insert(0, row[0])
        self.quantity_get_entry.delete(0, END)
        self.quantity_get_entry.insert(0, row[1])
        self.Total_entry.delete(0, END)
        self.Total_entry.insert(0, row[2])

        query = 'select * from product where Product_ID=%s'
        values = (self.Product_ID_entry.get(),)
        record = Connection.my_database().selectAll(query, values)
        Connection.my_database().close()
        for i in record:
            self.product_category_entry.delete(0, END)
            self.product_category_entry.insert(0, i[1])
            self.product_name_entry.delete(0, END)
            self.product_name_entry.insert(0, i[2])
            self.quantity_in_entry.delete(0, END)
            self.quantity_in_entry.insert(0, i[3])

    def product_category_function(self):
        """
        Function to get the product category from database and add it in a combobox value.
        """
        query = 'SELECT DISTINCT Product_Category FROM product;'
        result = Connection.my_database().selectOne(query, )
        Connection.my_database().close()
        data = []
        for row in result:
            data.append(row[0])
        self.product_category_entry['values'] = data

    def quantity_in_function(self, event):
        """
        Function to get the quantities name from database when certain combobox is selected and insert it in a combobox value.
        """
        query = 'select DISTINCT Quantity_In from product where Product_Category=%s and Product_Name=%s;'
        product_description = (self.product_category_entry.get(), self.product_name_entry.get())
        result = Connection.my_database().selectAll(query, product_description)
        Connection.my_database().close()
        data_quantity = []
        for row in result:
            data_quantity.append(row[0])
            self.quantity_in_entry['values'] = data_quantity
        return result

    def in_stock(self, event):
        """
        Function to get the stock quantity  from database when combobox is selected and insert it in a entry box.
        """
        query = 'select Product_Stock from product where Product_Name=%s and Quantity_In=%s;'
        product_description = (self.product_name_entry.get(), self.quantity_in_entry.get())
        result = Connection.my_database().selectAll(query, product_description)
        Connection.my_database().close()
        for rows in result:
            self.quantity_get_entry.delete(0, END)
            self.quantity_get_entry.insert(0, f'In Stock {rows[0]}')
        return result

    def product_name_function(self, event):
        """
        Function to get the product name from database and insert it in a combobox value.
        """
        query = 'SELECT DISTINCT Product_Name from product where Product_Category=%s;'
        product_category = (self.product_category_entry.get(),)
        result = Connection.my_database().selectAll(query, product_category)
        Connection.my_database().close()
        data = []
        for row in result:
            data.append(row[0])
        self.product_name_entry['values'] = data

    def product_amount_function(self):
        """
        Function to get the totals amount after when the quantities and product is chosen.
        """
        if self.product_category_entry.get() != '' and self.product_name_entry.get() != '' and self.quantity_in_entry.get() != '' and self.quantity_get_entry.get() != '':
            query = 'SELECT Amount from product where Product_Name=%s and Quantity_in=%s'
            product_description = (self.product_name_entry.get(), self.quantity_in_entry.get())
            result = Connection.my_database().selectAll(query, product_description)
            Connection.my_database().close()
            for row in result:
                prices = row[0]
                quantities = int(self.quantity_get_entry.get())
                totals = prices * quantities
                self.Total_entry.delete(0, END)
                self.Total_entry.insert(0, totals)

        else:
            messagebox.showerror('Oops', 'Important Fields are missing!', parent=self.master)

    def get_product_id_function(self, event):
        """
        Function to insert the ID into ID entry box after combobox is selected
        """
        if self.product_category_entry.get() != '' and self.product_name_entry.get() != '' and self.quantity_in_entry.get() != '':
            query = 'select Product_ID from product where Product_Name=%s and Quantity_in=%s'
            product_detail = (self.product_name_entry.get(), self.quantity_in_entry.get())
            result = Connection.my_database().selectAll(query, product_detail)
            Connection.my_database().close()
            for row in result:
                self.Product_ID_entry.delete(0, END)
                self.Product_ID_entry.insert(0, row[0])
            return result
        else:
            messagebox.showerror('Error', 'Select Product Name and Quantity properly!.', parent=self.master)

    def add_to_cart(self):
        """
        Function to add products into database.
        """
        query = 'select Product_Stock from product where Product_Name=%s and Quantity_In=%s;'
        product_description = (self.product_name_entry.get(), self.quantity_in_entry.get())
        result = Connection.my_database().selectAll(query, product_description)
        Connection.my_database().close()
        get_stocks = []
        for i in result:
            get_stocks.append(i[0])
        Connection.my_database().close()
        if self.product_category_entry.get() == '' or self.product_name_entry.get() == '' or self.quantity_get_entry.get() == '' or self.quantity_in_entry.get() == '' or self.Total_entry.get() == '':
            messagebox.showerror('Error', 'Please Fill required data!', parent=self.master)
        elif int(self.quantity_get_entry.get()) > get_stocks[0]:
            messagebox.showwarning('Warning', 'Not Sufficient Quantity Stock!', parent=self.master)
        else:
            cart_ref = cart.Add_to_cart(self.Product_ID_entry.get(), self.quantity_get_entry.get(),
                                        self.Total_entry.get())
            query = 'insert into cart values(%s,%s,%s);'
            values = (cart_ref.get_Product_ID(), cart_ref.get_Quantity(), cart_ref.get_Price())
            Connection.my_database().operation(query, values)
            Connection.my_database().close()
            query_update = 'update product set Product_Stock=%s where Product_ID=%s;'
            value = (get_stocks[0] - int(self.quantity_get_entry.get()), self.Product_ID_entry.get())
            Connection.my_database().operation(query_update, value)
            Connection.my_database().close()
            messagebox.showinfo('Hurray', 'Product Added to Cart!', parent=self.master)
            self.clear()
            self._build_tree()

    def delete_from_cart(self):
        """
        Function to delete the cart values from database and tree view.
        """
        self.Data_table.get_children()
        self.Data_table.focus_get()
        answer = messagebox.askquestion('Confirm', 'Are you sure to remove from cart?', parent=self.master)
        if answer == 'yes':
            query = 'delete from cart where Product_ID=%s;'
            values = (self.Product_ID_entry.get(),)
            Connection.my_database().operation(query, values)
            Connection.my_database().close()
            messagebox.showinfo('Hurray', 'Successfully removed from cart!', parent=self.master)
            self.clear()
            self._build_tree()

    def add_to_database(self):
        """
        Function to add the customer detail, product details in database table.
        """
        query = 'select Product_Stock from product where Product_Name=%s and Quantity_In=%s;'
        product_description = (self.product_name_entry.get(), self.quantity_in_entry.get())
        result = Connection.my_database().selectAll(query, product_description)
        Connection.my_database().close()
        get_stocks = []
        for i in result:
            get_stocks.append(i[0])
        if self.customer_name_entry.get() != '' and self.payment_method_entry.get() != '':
            if int(self.quantity_get_entry.get()) > get_stocks[0]:
                messagebox.showwarning('Warning', 'Not Sufficient Quantity Stock!', parent=self.master)
            else:
                answer = messagebox.askquestion('Confirm', 'Do you want to add to database!', parent=self.master)
                if answer == 'yes':
                    billing_ref = billing.Customer(self.customer_name_entry.get().capitalize(),
                                                   self.Product_ID_entry.get(),
                                                   self.quantity_get_entry.get(), self.payment_method_entry.get(), Date)

                    query = 'insert into customer values(%s,%s,%s,%s,%s)'
                    values = (billing_ref.get_Customer_Name(), billing_ref.get_Product_ID(),
                              billing_ref.get_Quantity(), billing_ref.get_Payment_Method(),
                              billing_ref.get_Shipped_Date())
                    Connection.my_database().operation(query, values)
                    Connection.my_database().close()
                    query_update = 'update product set Product_Stock=%s where Product_ID=%s;'
                    value = (get_stocks[0] - int(self.quantity_get_entry.get()), self.Product_ID_entry.get())
                    Connection.my_database().operation(query_update, value)
                    Connection.my_database().close()
                    messagebox.showinfo('Hurray', 'Data added to database!', parent=self.master)
                    self.clear()
        else:
            messagebox.showerror('Error', 'Please enter Customer Name & Payment Method', parent=self.master)

    def clear(self):
        """
        Function to delete all the values from Entry Boxes.
        """
        self.customer_name_entry.delete(0, END)
        self.product_category_entry.delete(0, END)
        self.product_name_entry.delete(0, END)
        self.quantity_in_entry.delete(0, END)
        self.quantity_get_entry.delete(0, END)
        self.Total_entry.delete(0, END)
        self.Product_ID_entry.delete(0, END)
        self.payment_method_entry.delete(0, END)

    def bill(self):
        """
        Function to show the bill of the Customer in a new window if s/he is added to database.
        """
        global pdt_id, pay_method, total, price, quantity_in, quantity, pdt_name, dates
        query = 'select Customer_Name from customer;'
        data = Connection.my_database().selectOne(query)
        list_name = []
        for i in data:
            list_name.append(i[0])
        if self.customer_name_entry.get() == '':
            messagebox.showerror('Oops', 'Enter Customer Name First!', parent=self.master)
        elif self.customer_name_entry.get() not in list_name:
            messagebox.showwarning('Oops', 'No such Customer Name in database!, Please add s/he in database first!',
                                   parent=self.master)

        else:
            query = 'select * from customer where Customer_Name=%s;'
            value = (self.customer_name_entry.get(),)
            data = Connection.my_database().selectAll(query, value)
            Connection.my_database().close()
            for result in data:
                pdt_id = result[1]
                pay_method = result[3]
                dates = result[4]
            query1 = 'select * from product where Product_ID=%s;'
            value1 = (pdt_id,)
            data1 = Connection.my_database().selectAll(query1, value1)
            Connection.my_database().close()
            for j in data1:
                pdt_name = j[2]
                quantity_in = j[3]
                price = j[5]
            query2 = 'select * from cart where Product_ID=%s;'
            value2 = (pdt_id,)
            data2 = Connection.my_database().selectAll(query2, value2)
            Connection.my_database().close()
            for i in data2:
                quantity = i[1]
                total = i[2]
            master = Tk()
            master.geometry('500x400')
            master.title('Billing:')
            frame1 = Frame(master)
            Label(frame1, text='Customer Name:', font=('jokerman', 16,)).grid(row=0, column=0)
            Label(frame1, text='Date:', font=('jokerman', 15,)).grid(row=1, column=0)
            Label(frame1, text=f'{value[0]}', font=('jokerman', 14,)).grid(row=0, column=1)
            Label(frame1, text=f'{dates}', font=('jokerman', 14,)).grid(row=1, column=1)
            Label(frame1, text='Product ID:', font=('jokerman', 16,)).grid(row=2, column=0)
            Label(frame1, text=f'{pdt_id}', font=('jokerman', 14,)).grid(row=2, column=1)
            Label(frame1, text='Product Name:', font=('jokerman', 16,)).grid(row=3, column=0)
            Label(frame1, text=f'{pdt_name}', font=('jokerman', 14,)).grid(row=3, column=1)
            Label(frame1, text='Quantity:', font=('jokerman', 16,)).grid(row=4, column=0)
            Label(frame1, text=f'{quantity}', font=('jokerman', 14,)).grid(row=4, column=1)
            Label(frame1, text='In:', font=('jokerman', 16,)).grid(row=5, column=0)
            Label(frame1, text=f'{quantity_in}', font=('jokerman', 14,)).grid(row=5, column=1)
            Label(frame1, text='Rate:', font=('jokerman', 16,)).grid(row=6, column=0)
            Label(frame1, text=f'{price}', font=('jokerman', 14,)).grid(row=6, column=1)
            Label(frame1, text='Total:', font=('jokerman', 16,)).grid(row=7, column=0)
            Label(frame1, text=f'{total}', font=('jokerman', 14,)).grid(row=7, column=1)
            Label(frame1, text='Payment Method:', font=('jokerman', 14,)).grid(row=8, column=0)
            Label(frame1, text=f'{pay_method}', font=('jokerman', 14,)).grid(row=8, column=1)
            frame1.pack()

    def destroy(self):
        """
        Function to get back by destroying current window.
        """
        if messagebox.askyesnocancel('Confirmation', 'Are you sure to go back?', parent=self.master):
            self.master.destroy()

