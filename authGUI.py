from tkinter import *
from PlaceholderEntry import PlaceholderEntry

class authGUI:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.user_name_entry = PlaceholderEntry(self.frame, placeholder='Enter your name', fg='grey')
        self.company_name_entry = Entry(self.frame) 
        self.email_entry = Entry(self.frame) 
        self.password_entry = Entry(self.frame)

    def sign_up_form(self):
        # form title
        self.signup_label = Label(self.frame, text='Sign Up', font=('Helvetica', 16))
        self.signup_label.pack(pady=10)

        # form input fields
        self.user_name_label = Label(self.frame, text='Name')
        self.user_name_label.pack()
        self.user_name_entry.pack()

        self.company_name_label = Label(self.frame, text='Company Name')
        self.company_name_label.pack()
        self.company_name_entry.pack()

        self.email_label = Label(self.frame, text='Email')
        self.email_label.pack()
        self.email_entry.pack()

        self.password_label = Label(self.frame, text='Password')
        self.password_label.pack()
        self.password_entry.pack()

        self.confirm_password_label = Label(self.frame, text='Confirm password')
        self.confirm_password_label.pack()
        self.confirm_password_entry = Entry(self.frame)
        self.confirm_password_entry.pack()

        self.signup_button = Button(self.frame, text='Signup', command=self.on_submit)
        self.signup_button.pack()
        
        self.frame.pack()

    def login_form(self):
        # form title
        self.login_label = Label(self.frame, text='Sign Up', font=('Helvetica', 16))
        self.login_label.pack(pady=10)

        # form input fields
        self.email_label = Label(self.frame, text='Email')
        self.email_label.pack()
        self.email_entry.pack()

        self.password_label = Label(self.frame, text='Password')
        self.password_label.pack()
        self.password_entry.pack()

        self.login_button = Button(self.frame, text='Login', command=self.on_submit)
        self.login_button.pack()

        self.frame.pack()

    def on_submit(self):
        print(f'Name: {self.user_name_entry.get() or "-"} \nCompany Name: {self.company_name_entry.get() or "-"} \nEmail: {self.email_entry.get() or "-"} \nPassword: {self.password_entry.get() or "-"}')
        self.unpack_frame()

    def unpack_frame(self):
        self.frame.pack_forget()