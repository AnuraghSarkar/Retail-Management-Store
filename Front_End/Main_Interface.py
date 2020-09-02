from tkinter import *
from tkinter import ttk, messagebox
import PIL
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
from Front_End import Register, Login, admin_login, customer_photos, emp_photos
x = 1


class Interface:
    def __init__(self, master):
        """
        Function to initialize the master window.
        """
        self.master = master
        self.master.title('Omen Retail Store')
        self.master.state('zoomed')
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.master.iconbitmap('logo.ico')
        self.style = ttk.Style()
        self.style = ThemedStyle(self.master)
        self.style.set_theme('scidgreen')

        master.option_add('*tearOff', False)
        menubar = Menu(master)
        master.config(menu=menubar)
        Employee = Menu(menubar)
        Admin = Menu(menubar)
        Enquiry = Menu(menubar)
        Exit = Menu(menubar)

        menubar.add_cascade(menu=Employee, label='Employee')  # labelling four tabs for menu
        menubar.add_cascade(menu=Admin, label='Admin')
        menubar.add_cascade(menu=Enquiry, label='Explore')
        menubar.add_cascade(menu=Exit, label='Exit')

        Employee.add_command(label='Login', command=self.login)  # giving commands in secondary tab in menubar
        Employee.add_separator()
        Employee.add_command(label='Register', command=self.register)
        Admin.add_command(label='Login', command=self.admin_login)  # giving commands in secondary tab in menubar

        Enquiry.add_command(label='Employees', command=self.employee_photos)
        Enquiry.add_command(label='Customers', command=self.customer_photos)

        Exit.add_command(label='Close', command=self.on_closing)

        self.load_image1 = PIL.Image.open('sm1.jpg')
        self.render_image1 = ImageTk.PhotoImage(self.load_image1)

        load_image2 = PIL.Image.open('sm2.jpg')
        self.render_image2 = ImageTk.PhotoImage(load_image2)

        load_image3 = PIL.Image.open('sm3.jpg')
        self.render_image3 = ImageTk.PhotoImage(load_image3)

        load_image4 = PIL.Image.open('sm4.jpg')
        self.render_image4 = ImageTk.PhotoImage(load_image4)

        load_image5 = PIL.Image.open('sm5.jpg')
        self.render_image5 = ImageTk.PhotoImage(load_image5)

        self.image_label = Label(self.master)
        self.image_label.pack()
        self.move()

    def move(self):
        """
        Function that helps the label to be incremented by 1 after certain interval.
        """
        global x
        if x == 6:
            x = 1
        if x == 1:
            self.image_label.config(image=self.render_image1)
        elif x == 2:
            self.image_label.config(image=self.render_image2)
        elif x == 3:
            self.image_label.config(image=self.render_image3)
        elif x == 4:
            self.image_label.config(image=self.render_image4)
        elif x == 5:
            self.image_label.config(image=self.render_image5)

        x += 1

        self.master.after(4000, self.move)

    def on_closing(self):
        """
        Function to ask user to quit or not.
        """

        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            messagebox.showinfo('From Developer!', 'Thank You for using The App <3')
            self.master.destroy()

    @classmethod
    def register(cls):
        """
        Function to call Register_Interface class from Register.py  and insert it in a toplevel
        """
        master = Toplevel()
        Register.Register_Interface(master)
        master.bind('<Escape>', lambda e: master.destroy())

    @classmethod
    def login(cls):
        """
        Function to call Login_Interface class from Login.py and insert it in a toplevel
        """
        master = Toplevel()
        Login.Login_Interface(master)
        master.bind('<Escape>', lambda e: master.destroy())

    @classmethod
    def admin_login(cls):
        """
        Function to call Admin_Interface class from admin_login.py  and insert it in a toplevel
        """
        master = Toplevel()
        admin_login.Admin_Interface(master)
        master.bind('<Escape>', lambda e: master.destroy())

    @classmethod
    def customer_photos(cls):
        """
        Function to call customer class from customer_photos.py  and insert it in a toplevel
        """
        master = Toplevel()
        customer_photos.customer_photos(master)
        master.bind('<Escape>', lambda e: master.destroy())

    @classmethod
    def employee_photos(cls):
        """
        Function to call emp_photos class from emp_photos.py  add insert it in a toplevel
        """
        master = Toplevel()
        emp_photos.employee_photos(master)
        master.bind('<Escape>', lambda e: master.destroy())


def main():
    """
    Function to create a Tk window for Interface class
    """
    master = Tk()
    Interface(master)
    master.wm_attributes('-alpha', 1)
    master.mainloop()


if __name__ == '__main__':
    main()
