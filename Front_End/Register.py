from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PIL
from PIL import ImageTk, Image
from Model import employee
from Back_End import Connection
from ttkthemes import ThemedStyle
from Front_End import Login


class Register_Interface:
    def __init__(self, master_):
        """
        Function to configure main Tk window for Register Interface.
        """
        self.master = master_
        self.master.title('Register')
        self.master.state('zoomed')
        self.master.protocol("WM_DELETE_WINDOW", self.destroy)
        self.master.iconbitmap('logo.ico')

        self.style = ThemedStyle(self.master)
        self.style.set_theme('scidgreen')
        self.style.configure('my.TButton', font=('Verdana', 17), activeforeground='black', border='0')
        load_image = PIL.Image.open('back_admin.jpg')
        load_image = load_image.resize((1536, 864), Image.ANTIALIAS)
        render_image = ImageTk.PhotoImage(load_image)
        image_label = ttk.Label(self.master, image=render_image)
        image_label.image = render_image
        image_label.place(x=-2, y=-2)

        register_frame = LabelFrame(image_label, text='Registration Form!', height=400, width=400,
                                    highlightcolor='black', bg='#dbdbdb', font=('Courier', 18, 'bold'))
        register_frame.place(x=530, y=200)

        self.Employee_ID_label = ttk.Label(register_frame, text='ID:')
        self.Employee_ID_label.config(font=('Helvetica', 18, 'bold'))
        self.Employee_ID_label.place(x=3, y=10)
        self.Employee_ID = ttk.Entry(register_frame)
        self.Employee_ID.place(x=160, y=10)
        self.Employee_ID.config(font=('Arial', 15,))

        self.Name_label = ttk.Label(register_frame, text='Name:')
        self.Name_label.config(font=('Helvetica', 18, 'bold'))
        self.Name_label.place(x=3, y=60)
        self.Name = ttk.Entry(register_frame)
        self.Name.place(x=160, y=60)
        self.Name.config(font=('Arial', 15,))

        self.Username_label = ttk.Label(register_frame, text='Username:')
        self.Username_label.place(x=3, y=110)
        self.Username_label.config(font=('Helvetica', 18, 'bold'))

        self.Username = ttk.Entry(register_frame)
        self.Username.place(x=160, y=110)
        self.Username.config(font=('Arial', 15,))

        self.Password_label = ttk.Label(register_frame, text='Password:')
        self.Password_label.place(x=3, y=160)
        self.Password_label.config(font=('Helvetica', 18, 'bold'))

        self.Password = ttk.Entry(register_frame, show='*')
        self.Password.place(x=160, y=160)
        self.Password.config(font=('Arial', 15,))

        self.Contact_label = ttk.Label(register_frame, text='Contact:')
        self.Contact_label.place(x=3, y=210)
        self.Contact_label.config(font=('Helvetica', 18, 'bold'))
        self.Contact = ttk.Entry(register_frame)
        self.Contact.place(x=160, y=210)
        self.Contact.config(font=('Arial', 15,))

        self.Email_label = ttk.Label(register_frame, text='Email:')
        self.Email_label.place(x=3, y=260)
        self.Email_label.config(font=('Helvetica', 18, 'bold'))

        self.Email = ttk.Entry(register_frame)
        self.Email.place(x=160, y=260)
        self.Email.config(font=('Arial', 15,))

        reg_btn = ttk.Button(register_frame, text='Register  >', command=self.registration_checker)
        reg_btn.config(style='my.TButton')
        reg_btn.place(x=50, y=320)

        clear_btn = ttk.Button(register_frame, text='Clear  >', command=self.clear)
        clear_btn.config(style='my.TButton')
        clear_btn.place(x=250, y=320)

        load_image_logout = PIL.Image.open('back.jpg')
        load_image_logout = load_image_logout.resize((50, 50), Image.ANTIALIAS)
        self.logout_image = ImageTk.PhotoImage(load_image_logout)
        log_out_btn = Button(self.master, image=self.logout_image, highlightthickness=0, bd=0, command=self.destroy)
        log_out_btn.place(x=1, y=1)
        log_out_btn.image = self.logout_image

    def registration_checker(self):
        """
        Function to register Employee Data into database.
        """

        if (
                self.Employee_ID.get() == '' or self.Name.get() == '' or self.Username.get() == '' or self.Password.get() == '' or self.Contact.get() == '' or self.Email.get() == ''):
            messagebox.showerror('Oops', 'All fields are required!', parent=self.master)
        elif not self.Email.get().count('@') == 1 or not self.Email.get().count('.') == 1:
            messagebox.showwarning('Oops', 'Please use proper email!', parent=self.master)
        else:
            try:
                query = 'select Employee_ID,Username from employees;'
                records = Connection.my_database().selectOne(query, )
                Connection.my_database().close()
                item = int(self.Employee_ID.get())
                list_username = []
                list_emp_id = []
                for row in records:
                    list_username.append(row[1])
                    list_emp_id.append(row[0])
                if item in list_emp_id:
                    messagebox.showerror('Error', 'ID already registered', parent=self.master)
                    return
                elif self.Username.get() in list_username:
                    messagebox.showerror('Error', 'Username already exists', parent=self.master)
                    return
                else:
                    emp_ref = employee.Register(self.Employee_ID.get().strip(), self.Name.get().capitalize().strip()
                                                , self.Username.get().capitalize().strip(), self.Password.get().strip()
                                                , self.Contact.get().strip(), self.Email.get().capitalize().strip())
                    query = 'insert into employees values(%s,%s,%s,%s,%s,%s);'
                    values = (
                        emp_ref.get_Employee_ID(), emp_ref.get_Name(), emp_ref.get_Username(), emp_ref.get_Password(),
                        emp_ref.get_Contact(), emp_ref.get_Email())
                    Connection.my_database().operation(query, values)
                    Connection.my_database().close()
                    messagebox.showinfo('Hurray', 'Thanks for the registration.', parent=self.master)
                    self.clear()
                    self.master.destroy()
                    master = Toplevel()
                    Login.Login_Interface(master)
            except ValueError:
                messagebox.showerror('Error', 'ID and Contact Number must be integer', parent=self.master)

    def clear(self):
        """
        Function to delete the value from all Entry Boxes.
        """
        self.Employee_ID.delete(0, END)
        self.Username.delete(0, END)
        self.Password.delete(0, END)
        self.Name.delete(0, END)
        self.Contact.delete(0, END)
        self.Email.delete(0, END)

    def destroy(self):
        """
        Function to get back at home page by destroying it.
        """
        if messagebox.askyesnocancel('Confirmation', 'Are you sure to go back?', parent=self.master):
            self.master.destroy()
