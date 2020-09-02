from tkinter import *
from tkinter import messagebox
import PIL
from PIL import Image, ImageTk

x = 1


class customer_photos:
    def __init__(self, master):
        """
        Function to configure the main Tk window.
        """
        self.master = master
        self.master.title('Customers')
        self.master.state('zoomed')
        self.master.protocol("WM_DELETE_WINDOW", self.destroy)
        self.master.iconbitmap('logo.ico')

        self.load_image1 = PIL.Image.open('cus1.jpg')
        self.render_image1 = ImageTk.PhotoImage(self.load_image1)

        load_image2 = PIL.Image.open('cus2.jpg')
        self.render_image2 = ImageTk.PhotoImage(load_image2)

        load_image3 = PIL.Image.open('cus3.jpg')
        self.render_image3 = ImageTk.PhotoImage(load_image3)

        load_image4 = PIL.Image.open('cus4.jpg')
        self.render_image4 = ImageTk.PhotoImage(load_image4)

        load_image5 = PIL.Image.open('cu5.jpg')
        self.render_image5 = ImageTk.PhotoImage(load_image5)

        self.image_label = Label(self.master, background='black', height=864, width=1536)
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

    def destroy(self):
        """
        Function to get back by destroying current window.
        """
        if messagebox.askyesnocancel('Confirmation', 'Are you sure to go back?', parent=self.master):
            self.master.destroy()
