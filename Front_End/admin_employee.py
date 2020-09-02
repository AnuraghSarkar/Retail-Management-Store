from tkinter import *
from tkinter import messagebox, ttk
import PIL
from PIL import ImageTk, Image
from ttkthemes import ThemedStyle
from Back_End import Connection


class Admin_Employee:
    def __init__(self, master):
        """
        Function to configure the main window.
        """
        self.master = master
        self.master.title('Employee Management:')
        self.master.state('zoomed')
        self.master.protocol("WM_DELETE_WINDOW", self.destroy)
        self.master.iconbitmap('logo.ico')

        self.style = ThemedStyle(self.master)
        self.style.set_theme('scidgreen')
        self.style.configure('my.TButton', font=('Verdana', 12), activeforeground='black', border='0')

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

        self.Employee_ID = ttk.Label(frame1, text='Employee ID:')
        self.Employee_ID.config(font=('Courier', 18,))
        self.Employee_ID.place(x=4, y=45)
        self.Emp_entry = ttk.Entry(frame1)
        self.Emp_entry.config(font=('', 16,))
        self.Emp_entry.place(x=220, y=45)

        self.Name = ttk.Label(frame1, text='Full Name:')
        self.Name.config(font=('Courier', 18,))
        self.Name.place(x=4, y=105)
        self.Name_entry = ttk.Entry(frame1)
        self.Name_entry.config(font=('', 16,))
        self.Name_entry.place(x=220, y=105)

        self.Username = ttk.Label(frame1, text='Username:')
        self.Username.config(font=('Courier', 18,))
        self.Username.place(x=4, y=165)
        self.Username_entry = ttk.Entry(frame1)
        self.Username_entry.config(font=('', 16,))
        self.Username_entry.place(x=220, y=165)

        self.Password = ttk.Label(frame1, text='Password:')
        self.Password.config(font=('Courier', 18,))
        self.Password.place(x=4, y=225)
        self.Password_entry = ttk.Entry(frame1)
        self.Password_entry.config(font=('', 16,))
        self.Password_entry.place(x=220, y=225)

        self.Contact = ttk.Label(frame1, text='Contact:')
        self.Contact.config(font=('Courier', 18,))
        self.Contact.place(x=4, y=285)
        self.Contact_entry = ttk.Entry(frame1)
        self.Contact_entry.config(font=('', 16,))
        self.Contact_entry.place(x=220, y=285)

        self.Email = ttk.Label(frame1, text='Email:')
        self.Email.config(font=('Courier', 18,))
        self.Email.place(x=4, y=345)
        self.Email_entry = ttk.Entry(frame1)
        self.Email_entry.config(font=('', 16,))
        self.Email_entry.place(x=220, y=345)

        self.update_btn = ttk.Button(frame1, text='Update Details')
        self.update_btn.place(x=10, y=400)
        self.update_btn.config(style='my.TButton')
        self.update_btn.bind('<ButtonRelease-1>', self.update_employee)

        self.delete_btn = ttk.Button(frame1, text='Delete Employee')
        self.delete_btn.place(x=170, y=400)
        self.delete_btn.config(style='my.TButton')
        self.delete_btn.bind('<ButtonRelease-1>', self.delete_employee)

        self.clear_btn = ttk.Button(frame1, text='Clear', command=self.clear)
        self.clear_btn.place(x=350, y=400)
        self.clear_btn.config(style='my.TButton')

        Data_frame = ttk.Frame(frame2, relief=SOLID)
        Data_frame.place(x=20, y=80, height=360, width=570)
        Data_frame.config(border=3)
        scroll_x = Scrollbar(Data_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Data_frame, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.Data_table = ttk.Treeview(Data_frame,
                                       columns=('Employee_ID', 'Name', 'Username', 'Password', 'Contact', 'Email'),
                                       xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set, show='headings')
        scroll_x.config(command=self.Data_table.xview)
        scroll_y.config(command=self.Data_table.yview)
        self.Data_table.heading('Employee_ID', text='Employee_ID')
        self.Data_table.heading('Name', text='Name')
        self.Data_table.heading('Username', text='Username')
        self.Data_table.heading('Password', text='Password')
        self.Data_table.heading('Contact', text='Contact')
        self.Data_table.heading('Email', text='Email')

        self.Data_table.pack(fill=BOTH, expand=1)

        query = 'select * from employees;'
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
        self.search_select['values'] = ('Employee ID', 'Username')

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
        Function to insert the database values to tree view.
        """
        query = 'select * from employees;'
        rows = Connection.my_database().selectOne(query, )
        Connection.my_database().close()
        if len(rows) != 0:
            self.Data_table.delete(*self.Data_table.get_children())
            for row in rows:
                self.Data_table.insert('', END, values=row)

    def get_cursor(self, event):
        """
        Function to get the focused row in tree view and insert it in Entry Boxes.
        """
        cursor = self.Data_table.focus()
        content = self.Data_table.item(cursor)
        row = content['values']
        self.Emp_entry.delete(0, END)
        self.Emp_entry.insert(0, row[0])
        self.Name_entry.delete(0, END)
        self.Name_entry.insert(0, row[1])
        self.Username_entry.delete(0, END)
        self.Username_entry.insert(0, row[2])
        self.Password_entry.delete(0, END)
        self.Password_entry.insert(0, row[3])
        self.Contact_entry.delete(0, END)
        self.Contact_entry.insert(0, row[4])
        self.Email_entry.delete(0, END)
        self.Email_entry.insert(0, row[5])

    def delete_employee(self, event):
        """
        Function to delete the selected employee, from the database and tree view.
        """
        self.Data_table.get_children()
        self.Data_table.focus_get()
        answer = messagebox.askquestion('Confirm', 'Are you sure to delete this employee?', parent=self.master)
        if answer == 'yes':
            query = 'delete from employees where Employee_ID=%s;'
            values = (self.Emp_entry.get(),)
            Connection.my_database().operation(query, values)
            Connection.my_database().close()
            messagebox.showinfo('Hurray', 'Successfully removed from employee table!', parent=self.master)
            self.clear()
            self._build_tree()

    def update_employee(self, event):
        """
        Function to update the employee details, in database and tree view.
        """
        data = self.Data_table.get_children()
        self.Data_table.focus_get()
        if self.Emp_entry.get != '' or self.Username_entry.get() != '' or self.Name_entry.get() != '' or self.Password_entry.get() != '' or self.Email_entry.get() != '' or self.Contact_entry.get() != '':
            answer = messagebox.askquestion('Confirm', 'Are you sure to update this details?', parent=self.master)
            if answer == 'yes':
                try:

                    query = 'select Employee_ID,Username from employees;'
                    records = Connection.my_database().selectOne(query, )
                    Connection.my_database().close()
                    item = int(self.Emp_entry.get())
                    list_emp_id = []
                    list_username = []
                    for row in records:
                        list_emp_id.append(row[0])
                        list_username.append(row[1])
                    if item not in list_emp_id:
                        messagebox.showerror('Error', 'ID cannot be changed', parent=self.master)
                        return
                    elif self.Username_entry.get() not in list_username:
                        messagebox.showwarning('Oops',
                                               'Username cannot be updated!. If you want to update then delete your existing account and register again!',
                                               parent=self.master)
                    else:
                        query = 'update employees set Name=%s,Username=%s,Password=%s,Contact=%s,Email=%s where Employee_ID=%s'
                        values = (self.Name_entry.get(), self.Username_entry.get(), self.Password_entry.get()
                                  , self.Contact_entry.get(), self.Email_entry.get(), self.Emp_entry.get())
                        Connection.my_database().operation(query, values)
                        Connection.my_database().close()
                        messagebox.showinfo('Info', 'Employee Details Updated!', parent=self.master)
                        self.clear()
                        self._build_tree()

                except ValueError:
                    messagebox.showerror('Error', 'ID must be integer', parent=self.master)

        else:
            messagebox.showerror('Error', 'Fields cannot be empty!', parent=self.master)

    def clear(self):
        """
        Function to delete all the values from Entry boxes.
        """
        self.Emp_entry.delete(0, END)
        self.Name_entry.delete(0, END)
        self.Username_entry.delete(0, END)
        self.Password_entry.delete(0, END)
        self.Contact_entry.delete(0, END)
        self.Email_entry.delete(0, END)

    @classmethod
    def search_by(cls, employee_list, employee_detail):
        """
        Function to do linear search
        :param employee_list:list of employees who are registered
        :type employee_list:list
        :param employee_detail:specification of employee
        :type employee_detail:str
        :return: True:
        :return: False:
        :rtype: bool
        """
        for i in range(len(employee_list)):
            if employee_detail == employee_list[i]:
                return True
        return False

    def search_in_database(self):
        """
        Function to search the data from database and focus it in a tree view with help of linear search.
        """
        query = 'select * from employees;'
        record = Connection.my_database().selectOne(query, )
        Connection.my_database().close()
        list_emp_id = []
        list_emp_username = []
        list_emp_name = []
        for i in record:
            list_emp_id.append(i[0])
            list_emp_username.append(i[2])
            list_emp_name.append(i[1])

        if self.search_select.get() == 'Employee ID':
            try:
                if self.search_by(list_emp_id, int(self.search_box.get())):
                    query = 'select * from employees where Employee_ID=%s;'
                    values = (self.search_box.get(),)
                    get_data = Connection.my_database().selectAll(query, values)
                    Connection.my_database().close()
                    if len(get_data) != 0:
                        self.Data_table.delete(*self.Data_table.get_children())
                        for row in get_data:
                            self.Data_table.insert('', END, values=row)
                else:
                    messagebox.showerror('Sorry', 'No such Employee ID!', parent=self.master)
            except ValueError:
                messagebox.showwarning('Oops', 'ID must be in integer!', parent=self.master)

        elif self.search_select.get() == 'Username':
            if self.search_by(list_emp_username, self.search_box.get().capitalize().strip()):
                try:
                    query = 'select * from employees where Username=%s;'
                    values = (self.search_box.get().capitalize().strip(),)
                    get_data = Connection.my_database().selectAll(query, values)
                    Connection.my_database().close()
                    if len(get_data) != 0:
                        self.Data_table.delete(*self.Data_table.get_children())
                        for row in get_data:
                            self.Data_table.insert('', END, values=row)
                    else:
                        messagebox.showerror('Sorry', 'No such Username!', parent=self.master)
                except ValueError:
                    messagebox.showwarning('Oops', 'Username must be alphabets.', parent=self.master)

    def destroy(self):
        """
        Function to get back by destroying current window.
        """
        if messagebox.askyesnocancel('Confirmation', 'Are you sure to go back?', parent=self.master):
            self.master.destroy()

