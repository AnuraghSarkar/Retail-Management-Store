from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PIL
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image
from Back_End import Connection
from Front_End import After_login


class Login_Interface:
    def __init__(self, master):
        """
        Function to configure main TK window
        """
        self.master = master
        self.master.title('Login Employee')
        self.master.state('zoomed')
        self.master.protocol("WM_DELETE_WINDOW", self.destroy)
        self.master.iconbitmap('logo.ico')

        self.style = ThemedStyle(self.master)
        self.style.set_theme('scidgreen')

        self.style.configure('my.TButton', font=('Verdana', 17), activeforeground='black', border='0',
                             foreground='black')

        load_image = PIL.Image.open('back_admin.jpg')
        load_image = load_image.resize((1536, 864), Image.ANTIALIAS)
        render_image = ImageTk.PhotoImage(load_image)
        image_label = ttk.Label(self.master, image=render_image)
        image_label.image = render_image
        image_label.place(x=-2, y=-2)

        login_frame = LabelFrame(image_label, text='Login for Employees!', height=300, width=400,
                                 highlightcolor='black', foreground='Black', bg='#dbdbdb', font=('Courier', 18, 'bold'))
        login_frame.place(x=530, y=235)

        self.Username = ttk.Label(login_frame, text='Username:')
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

        log_in_btn = ttk.Button(login_frame, text='Login  >', command=self.login_checker)
        log_in_btn.config(style='my.TButton')
        log_in_btn.place(x=40, y=200)

        clear_btn = ttk.Button(login_frame, text='Clear  >', command=self.clear)
        clear_btn.config(style='my.TButton')
        clear_btn.place(x=240, y=200)

        load_image_logout = PIL.Image.open('back.jpg')
        load_image_logout = load_image_logout.resize((50, 50), Image.ANTIALIAS)
        self.logout_image = ImageTk.PhotoImage(load_image_logout)

        log_out_btn = Button(self.master, image=self.logout_image, highlightthickness=0, bd=0, command=self.destroy)
        log_out_btn.place(x=1, y=1)
        log_out_btn.image = self.logout_image

    def clear(self):
        """
        Function to delete all value from all Entry Boxes.
        """
        self.Username_entry.delete(0, END)
        self.Password_entry.delete(0, END)

    def login_checker(self):
        """
        Function to open a new window after  successful login of employee.
        """
        if self.Username_entry.get() == '' or self.Password_entry.get() == '':
            messagebox.showerror('Error', 'All fields are required!', parent=self.master)
        else:
            query = 'select Username from employees where Username=%s;'
            values = (self.Username_entry.get().strip(),)
            records = Connection.my_database().selectAll(query, values)
            Connection.my_database().close()
            if not records:
                messagebox.showwarning('Error', 'No such Username', parent=self.master)
            else:
                query = 'select Password from employees where Username=%s;'
                values = (self.Username_entry.get().strip(),)
                records = Connection.my_database().selectAll(query, values)
                Connection.my_database().close()
                data = []
                for i in records:
                    data.append(i[0])
                if data[0] == self.Password_entry.get().strip():
                    messagebox.showinfo('Success', 'Login Successfully!', parent=self.master)
                    self.clear()
                    master = Toplevel()
                    After_login.after_login(master)
                    self.master.destroy()
                    master.bind('<Escape>', lambda e: master.destroy())

                else:
                    messagebox.askretrycancel('Retry', 'Password not matching', parent=self.master)
                    self.Password_entry.delete(0, END)

    def destroy(self):
        """
        Function to get back at home page by destroying it.
        """
        if messagebox.askyesnocancel('Confirmation', 'Are you sure to go back?', parent=self.master):
            self.master.destroy()
