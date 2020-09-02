from tkinter import *
from tkinter import ttk, messagebox
import PIL
from PIL import ImageTk, Image
from ttkthemes import ThemedStyle

from Front_End import admin_customer, admin_employee, admin_product


class Admin:
    def __init__(self, master):
        """
        Function to configure the main window.
        """
        self.master = master
        self.master.title('Admin Panel')
        self.master.state('zoomed')
        self.master.protocol("WM_DELETE_WINDOW", self.destroy)
        self.master.iconbitmap('logo.ico')

        self.style = ThemedStyle(self.master)
        self.style.set_theme('scidgreen')
        load_image = PIL.Image.open('back_admin.jpg')
        load_image = load_image.resize((1536, 864), Image.ANTIALIAS)
        render_image = ImageTk.PhotoImage(load_image)
        image_label = ttk.Label(self.master, image=render_image)
        image_label.image = render_image
        image_label.place(x=-2, y=-2)

        load_image_emp = PIL.Image.open('emp.jpg')
        load_image_emp = load_image_emp.resize((300, 300), Image.ANTIALIAS)

        self.emp_image = ImageTk.PhotoImage(load_image_emp)
        self.button_emp = ttk.Button(image_label, image=self.emp_image, command=self.admin_employee)
        self.button_emp.place(x=80, y=230)
        self.button_emp.image = self.emp_image

        load_image_invoice = PIL.Image.open('invoice.jpg')
        load_image_invoice = load_image_invoice.resize((300, 300), Image.ANTIALIAS)
        self.invoice_image = ImageTk.PhotoImage(load_image_invoice)
        self.button_inv = ttk.Button(image_label, image=self.invoice_image, command=self.admin_customer)
        self.button_inv.place(x=580, y=230)
        self.button_inv.image = self.invoice_image

        load_image_product = PIL.Image.open('product.jpg')
        load_image_product = load_image_product.resize((300, 300), Image.ANTIALIAS)
        self.product_image = ImageTk.PhotoImage(load_image_product)
        self.button_pdt = ttk.Button(image_label, image=self.product_image, command=self.admin_product)
        self.button_pdt.place(x=1160, y=230)
        self.button_pdt.image = self.product_image

        load_image_logout = PIL.Image.open('back.jpg')
        load_image_logout = load_image_logout.resize((50, 50), Image.ANTIALIAS)
        self.logout_image = ImageTk.PhotoImage(load_image_logout)

        log_out_btn = Button(self.master, image=self.logout_image, highlightthickness=0, bd=0, command=self.destroy)
        log_out_btn.place(x=1, y=1)
        log_out_btn.image = self.logout_image

    @classmethod
    def admin_employee(cls):
        """
        Function to call Admin_Employee class from admin_employee.py  and add it in a Toplevel window,
        """
        master = Toplevel()
        admin_employee.Admin_Employee(master)
        master.bind('<Escape>', lambda e: master.destroy())

    @classmethod
    def admin_product(cls):
        """
        Function to call Admin_Product class from admin_product.py  and add it in a Toplevel window,
        """
        master = Toplevel()
        admin_product.Admin_Product(master)
        master.bind('<Escape>', lambda e: master.destroy())

    @classmethod
    def admin_customer(cls):
        """
        Function to call Admin_Customer class from admin_customer.py class and add it in a Toplevel window,
        """
        master = Toplevel()
        admin_customer.Admin_Customer(master)
        master.bind('<Escape>', lambda e: master.destroy())

    def destroy(self):
        """
        Function to get back by destroying current window.
        """
        if messagebox.askyesnocancel('Confirmation', 'Are you sure to go back?', parent=self.master):
            self.master.destroy()
