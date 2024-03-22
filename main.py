from tkinter import *
from authGUI import *

class Main:

    def __init__(self):
        self.root = Tk()
        self.root.title("Salary Manager")
        self.root.geometry("400x300")
        self.menu()
        self.authform = authGUI(self.root)

    def menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label='Signup', command=self.open_signup)
        file_menu.add_command(label='Login', command=self.open_login)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.root.quit)
        menubar.add_cascade(label='File', menu=file_menu)
        self.create_btn()
    
    def create_btn(self):
        self.signup_button = Button(self.root, text="Signup", command=self.open_signup)
        self.signup_button.pack(pady=10)
        self.login_button = Button(self.root, text='Login', command=self.open_login)
        self.login_button.pack(pady=10)

    def open_signup(self):
        # Implement the signup logic here
        self.signup_button.pack_forget()
        self.login_button.pack_forget()
        self.authform.sign_up_form()

    def open_login(self):
        # Implement the login logic here
        print("Opening login page")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Main()
    app.run()