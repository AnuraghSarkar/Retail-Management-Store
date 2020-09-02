from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Front_End import after_login_admin
from ttkthemes import ThemedStyle
import PIL
from PIL import ImageTk, Image


class Admin_Interface:
    def __init__(self, master):
        """
        Function to configure the main window.
        """
        self.master = master
        self.master.state('zoomed')
        self.master.title('Admin Login')
        self.master.protocol("WM_DELETE_WINDOW", self.destroy)
        self.master.iconbitmap('logo.ico')

        self.style = ThemedStyle(self.master)
        self.style.theme_use('scidgreen')
        self.style.configure('my.TButton', font=('Verdana', 17), activeforeground='black', border='0')
        load_image = PIL.Image.open('back_admin.jpg')
        load_image = load_image.resize((1536, 864), Image.ANTIALIAS)
        render_image = ImageTk.PhotoImage(load_image)
        image_label = ttk.Label(self.master, image=render_image)
        image_label.image = render_image
        image_label.place(x=-2, y=-2)
        login_frame = LabelFrame(image_label, text='Login for Admin!', height=300, width=400,
                                 highlightcolor='black', bg='#dbdbdb', font=('Courier', 18, 'bold'))
        login_frame.place(x=580, y=200)

        self.Username = ttk.Label(login_frame, text='Admin ID:')
        self.Username.config(font=('Helvetica', 18, 'bold'))
        self.Username.place(x=3, y=60)
        self.Username_entry = ttk.Entry(login_frame)
        self.Username_entry.place(x=160, y=60)
        self.Username_entry.config(font=('Arial', 15,))

        self.Password = ttk.Label(login_frame, text='Password:')
        self.Password.config(font=('Helvetica', 18, 'bold'))
        self.Password.place(x=3, y=140)
        self.Password_entry = ttk.Entry(login_frame, show='*')
        self.Password_entry.place(x=160, y=140)
        self.Password_entry.config(font=('Arial', 15,))

        reg_btn = ttk.Button(login_frame, text='Login  >', command=self.admin_login)
        reg_btn.config(style='my.TButton')
        reg_btn.place(x=10, y=210)

        clear_btn = ttk.Button(login_frame, text='Clear  >', command=self.clear)
        clear_btn.config(style='my.TButton')
        clear_btn.place(x=260, y=210)

        load_image_logout = PIL.Image.open('back.jpg')
        load_image_logout = load_image_logout.resize((50, 50), Image.ANTIALIAS)
        self.logout_image = ImageTk.PhotoImage(load_image_logout)

        log_out_btn = Button(self.master, image=self.logout_image, highlightthickness=0, bd=0, command=self.destroy)
        log_out_btn.place(x=1, y=1)
        log_out_btn.image = self.logout_image

    def clear(self):
        """
        Function to delete the value in Entry Boxes.
        """
        self.Username_entry.delete(0, END)
        self.Password_entry.delete(0, END)

    def admin_login(self):
        """
        Function to open the Admin Panel after validation.
        """
        if self.Username_entry.get() == 'Admin1010' and self.Password_entry.get() == 'Password':
            messagebox.showinfo('Yo', 'Welcome back Admin', parent=self.master)
            master = Toplevel()
            after_login_admin.Admin(master)
        else:
            messagebox.showerror('Oops', 'Fake Admin', parent=self.master)

    def destroy(self):
        """
        Function to get back by destroying current window.
        """
        if messagebox.askyesnocancel('Confirmation', 'Are you sure to go back?', parent=self.master):
            self.master.destroy()
