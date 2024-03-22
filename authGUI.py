from tkinter import *

class authGUI:
    def __init__(self, root):
        self.root = root

    def sign_up_form(self):
        # form title
        self.signup_label = Label(self.root, text='Sign Up', font=('Helvetica', 16))
        self.signup_label.pack(pady=10)

        # form input fields
        self.user_name_label = Label(self.root, text='Name')
        self.user_name_label.pack()
        self.user_name_entry = Entry(self.root)
        self.user_name_entry.pack()

        self.company_name_label = Label(self.root, text='Company Name')
        self.company_name_label.pack()
        self.company_name_entry = Entry(self.root)
        self.company_name_entry.pack()

        self.email_label = Label(self.root, text='Email')
        self.email_label.pack()
        self.email_entry = Entry(self.root)
        self.email_entry.pack()

        self.password_label = Label(self.root, text='Password')
        self.password_label.pack()
        self.password_entry = Entry(self.root)
        self.password_entry.pack()

        self.confirm_password_label = Label(self.root, text='Confirm password')
        self.confirm_password_label.pack()
        self.confirm_password_entry = Entry(self.root)
        self.confirm_password_entry.pack()

        self.signup_button = Button(self.root, text='Signup', command=self.on_submit)
        self.signup_button.pack()

    def on_submit(self):
        print(f'Name: {self.user_name_entry.get()} \nCompany Name: {self.company_name_entry.get()} \nEmail: {self.email_entry.get()} \nPassword: {self.password_entry.get()}')