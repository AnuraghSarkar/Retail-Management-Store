from tkinter import *
from tkinter import messagebox, ttk
import PIL
from PIL import ImageTk, Image
from Back_End import Connection
from Model import products
from ttkthemes import ThemedStyle


class Admin_Product:
    def __init__(self, master_):
        """
        Function to configure the main window
        """
        self.master = master_
        self.master.title('Product Management:')
        self.master.state('zoomed')
        self.master.protocol("WM_DELETE_WINDOW", self.destroy)
        self.master.iconbitmap('logo.ico')

        self.style = ThemedStyle()
        self.style.set_theme('scidgreen')
        self.style.configure('my.TButton', font=('Verdana', 9), activeforeground='black', border='0')

        load_image = PIL.Image.open('back_admin.jpg')
        load_image = load_image.resize((1536, 864), Image.ANTIALIAS)
        render_image = ImageTk.PhotoImage(load_image)
        image_label = ttk.Label(self.master, image=render_image)
        image_label.image = render_image
        image_label.place(x=-2, y=-2)

        panedwindow = ttk.Panedwindow(image_label, orient=HORIZONTAL)

        frame1 = ttk.Frame(panedwindow, height=460, width=500, relief=SUNKEN)
        frame2 = ttk.Frame(panedwindow, height=460, width=600, relief=SUNKEN)
        panedwindow.place(x=200, y=180)
        panedwindow.add(frame1, weight=1)
        panedwindow.add(frame2, weight=3)

        self.Product_ID = ttk.Label(frame1, text='Product ID:')
        self.Product_ID.config(font=('Courier', 18,))
        self.Product_ID.place(x=4, y=45)
        self.Product_ID_entry = ttk.Entry(frame1)
        self.Product_ID_entry.config(font=('', 16,))
        self.Product_ID_entry.place(x=220, y=45)

        self.Product_Category = ttk.Label(frame1, text='Category:')
        self.Product_Category.config(font=('Courier', 18,))
        self.Product_Category.place(x=4, y=105)
        self.Product_Category_entry = ttk.Entry(frame1)
        self.Product_Category_entry.config(font=('', 16,))
        self.Product_Category_entry.place(x=220, y=105)

        self.Product_Name = ttk.Label(frame1, text='Name:')
        self.Product_Name.config(font=('Courier', 18,))
        self.Product_Name.place(x=4, y=165)
        self.Product_Name_entry = ttk.Entry(frame1)
        self.Product_Name_entry.config(font=('', 16,))
        self.Product_Name_entry.place(x=220, y=165)

        self.Quantity = ttk.Label(frame1, text='Quantity in:')
        self.Quantity.config(font=('Courier', 18,))
        self.Quantity.place(x=4, y=225)
        self.Quantity_entry = ttk.Entry(frame1)
        self.Quantity_entry.config(font=('', 16,))
        self.Quantity_entry.place(x=220, y=225)

        self.Stock = ttk.Label(frame1, text='Stock In:')
        self.Stock.config(font=('Courier', 18,))
        self.Stock.place(x=4, y=285)
        self.Stock_entry = ttk.Entry(frame1)
        self.Stock_entry.config(font=('', 16,))
        self.Stock_entry.place(x=220, y=285)

        self.Amount = ttk.Label(frame1, text='Amount:')
        self.Amount.config(font=('Courier', 18,))
        self.Amount.place(x=4, y=345)
        self.Amount_entry = ttk.Entry(frame1)
        self.Amount_entry.config(font=('', 16,))
        self.Amount_entry.place(x=220, y=345)

        self.add_btn = ttk.Button(frame1, text='Add Product')
        self.add_btn.place(x=10, y=400)
        self.add_btn.config(style='my.TButton')
        self.add_btn.bind('<ButtonRelease-1>', self.add_product)

        self.update_btn = ttk.Button(frame1, text='Update Product')
        self.update_btn.place(x=130, y=400)
        self.update_btn.config(style='my.TButton')
        self.update_btn.bind('<ButtonRelease-1>', self.update_product)

        self.delete_btn = ttk.Button(frame1, text='Delete Product')
        self.delete_btn.place(x=265, y=400)
        self.delete_btn.config(style='my.TButton')
        self.delete_btn.bind('<ButtonRelease-1>', self.delete_product)

        self.clear_btn = ttk.Button(frame1, text='Clear', command=self.clear)
        self.clear_btn.place(x=390, y=400)
        self.clear_btn.config(style='my.TButton')

        data_frame = ttk.Frame(frame2, relief=SOLID)
        data_frame.place(x=20, y=80, height=360, width=570)
        data_frame.config(border=3)
        scroll_x = Scrollbar(data_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(data_frame, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.Data_table = ttk.Treeview(data_frame, columns=(
            'Product_ID', 'Product_Category', 'Product_Name', 'Quantity_In', 'Product_Stock', 'Amount'),
                                       xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set, show='headings')
        scroll_x.config(command=self.Data_table.xview)
        scroll_y.config(command=self.Data_table.yview)
        self.Data_table.heading('Product_ID', text='Product_ID')
        self.Data_table.heading('Product_Category', text='Product_Category')
        self.Data_table.heading('Product_Name', text='Product_Name')
        self.Data_table.heading('Quantity_In', text='Quantity_In')
        self.Data_table.heading('Product_Stock', text='Product_Stock')
        self.Data_table.heading('Amount', text='Amount')

        self.Data_table.pack(fill=BOTH, expand=1)

        query = 'select * from product;'
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
        self.search_select['values'] = ('Product ID', 'Product Name')

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

    def _build_tree(self):
        """
        Function to insert the value of databases in a tree view.
        """
        query = 'select * from product;'
        rows = Connection.my_database().selectOne(query, )
        Connection.my_database().close()
        if len(rows) != 0:
            self.Data_table.delete(*self.Data_table.get_children())
            for row in rows:
                self.Data_table.insert('', END, values=row)

    def get_cursor(self, event):
        """
        Function to insert data in entry box when an row on tree view is focused.
        """
        cursor = self.Data_table.focus()
        content = self.Data_table.item(cursor)
        row = content['values']
        self.Product_ID_entry.delete(0, END)
        self.Product_ID_entry.insert(0, row[0])
        self.Product_Category_entry.delete(0, END)
        self.Product_Category_entry.insert(0, row[1])
        self.Product_Name_entry.delete(0, END)
        self.Product_Name_entry.insert(0, row[2])
        self.Quantity_entry.delete(0, END)
        self.Quantity_entry.insert(0, row[3])
        self.Stock_entry.delete(0, END)
        self.Stock_entry.insert(0, row[4])
        self.Amount_entry.delete(0, END)
        self.Amount_entry.insert(0, row[5])

    def add_product(self, event):
        """
        Function to add product by admin into database and display on a tree view.
        """
        try:
            if (
                    self.Product_ID_entry.get() == '' or self.Product_Category_entry.get() == '' or self.Product_Name_entry.get() == ''
                    or self.Quantity_entry.get() == '' or self.Stock_entry.get() == '' or self.Amount_entry.get() == ''):
                messagebox.showerror('Oops', 'All fields are required!', parent=self.master)
            else:
                query = 'select Product_ID from product;'
                records = Connection.my_database().selectOne(query, )
                Connection.my_database().close()
                item = int(self.Product_ID_entry.get())
                for row in records:
                    if row[0] == item:
                        messagebox.showerror('Error', 'Product ID already registered', parent=self.master)
                else:
                    product_ref = products.Products(self.Product_ID_entry.get(), self.Product_Category_entry.get(),
                                                    self.Product_Name_entry.get(), self.Quantity_entry.get(),
                                                    int(self.Stock_entry.get()), int(self.Amount_entry.get()))
                    query = 'insert into product values(%s,%s,%s,%s,%s,%s);'
                    values = (product_ref.getProduct_ID(), product_ref.getProduct_Category(), product_ref.getProduct_Name(),
                              product_ref.getQuantity_In(), product_ref.getProduct_Stock(),
                              product_ref.getAmount())

                    Connection.my_database().operation(query, values)
                    Connection.my_database().close()
                    messagebox.showinfo('Hurray', 'Thanks for adding product.', parent=self.master)
                    self.clear()
        except ValueError:
            messagebox.showerror('Oops', 'ID and Stock must be integer!')

    def delete_product(self, event):
        """
        Function to delete the product from database and tree view by admin.
        """
        self.Data_table.get_children()
        self.Data_table.focus_get()
        answer = messagebox.askquestion('Confirm', 'Are you sure to delete this product?', parent=self.master)
        if answer == 'yes':
            query = 'delete from product where Product_ID=%s;'
            values = (self.Product_ID_entry.get(),)
            Connection.my_database().operation(query, values)
            Connection.my_database().close()
            messagebox.showinfo('Hurray', 'Product Deleted Successfully!!', parent=self.master)
            self.clear()
            self._build_tree()

    def update_product(self, event):
        """
        Function to update product in database and tree view by admin.
        """
        self.Data_table.get_children()
        self.Data_table.focus_get()
        if self.Product_ID_entry.get != '' or self.Product_Category_entry.get() != '' or self.Product_Name_entry.get() != '' or self.Quantity_entry.get() != '' or self.Stock_entry.get() != '' or self.Amount_entry.get() != '':
            answer = messagebox.askquestion('Confirm', 'Are you sure to update this details?', parent=self.master)
            if answer == 'yes':
                query = 'update product set Product_Category=%s,Product_Name=%s,Quantity_In=%s,Product_Stock=%s,Amount=%s where Product_ID=%s'
                values = (self.Product_Category_entry.get(), self.Product_Name_entry.get(), self.Quantity_entry.get()
                          , self.Stock_entry.get(), self.Amount_entry.get(), self.Product_ID_entry.get())
                Connection.my_database().operation(query, values)
                Connection.my_database().close()
                messagebox.showinfo('Info', 'Product Details Updated!', parent=self.master)
                self.clear()
                self._build_tree()

        else:
            messagebox.showerror('Error', 'Fields cannot be empty!', parent=self.master)

    def clear(self):
        self.Product_ID_entry.delete(0, END)
        self.Product_Category_entry.delete(0, END)
        self.Product_Name_entry.delete(0, END)
        self.Quantity_entry.delete(0, END)
        self.Stock_entry.delete(0, END)
        self.Amount_entry.delete(0, END)

    @classmethod
    def search_by(cls, product_list, product_detail):
        """
        Function to perform linear search:
        :param product_list:list of products
        :type product_list:list
        :param product_detail:specification of product
        :type product_detail:str
        :return: True
        :return: False
        :rtype: bool
        """
        for i in range(len(product_list)):
            if product_detail == product_list[i]:
                return True
        return False

    def search_in_database(self):
        """
        Function to search data in database with the help of linear search and focus it on a tree view.
        """
        query = 'select * from product;'
        record = Connection.my_database().selectOne(query, )
        Connection.my_database().close()
        list_product_id = []
        list_product_name = []
        for i in record:
            list_product_id.append(i[0])
            list_product_name.append(i[2])

        if self.search_select.get() == 'Product ID':
            try:
                if self.search_by(list_product_id, int(self.search_box.get().strip())):
                    query = 'select * from product where Product_ID=%s;'
                    values = (int(self.search_box.get().strip()),)
                    get_data_id = Connection.my_database().selectAll(query, values)
                    Connection.my_database().close()
                    if len(get_data_id) != 0:
                        self.Data_table.delete(*self.Data_table.get_children())
                        for row in get_data_id:
                            self.Data_table.insert('', END, values=row)
                else:
                    messagebox.showerror('Sorry', 'No such Product ID!', parent=self.master)
            except ValueError:
                messagebox.showerror('Oops', 'ID must be in integer!', parent=self.master)

        elif self.search_select.get() == 'Product Name':
            try:
                if self.search_by(list_product_name, self.search_box.get().capitalize().strip()):
                    query = 'select * from product where Product_Name=%s;'
                    value = (self.search_box.get().capitalize().strip(),)
                    get_data_name = Connection.my_database().selectAll(query, value)
                    Connection.my_database().close()
                    if len(get_data_name) != 0:
                        self.Data_table.delete(*self.Data_table.get_children())
                        for row in get_data_name:
                            self.Data_table.insert('', END, values=row)
                else:
                    messagebox.showerror('Sorry', 'No such Product Name!', parent=self.master)
            except ValueError:
                messagebox.showwarning('Oops', 'Product Name must be in alphabets!', parent=self.master)

    def destroy(self):
        """
        Function to get back by destroying current window.
        """
        if messagebox.askyesnocancel('Confirmation', 'Are you sure to go back?', parent=self.master):
            self.master.destroy()
