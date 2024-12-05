import sys
from tkinter import*
from tkinter import messagebox
from users import Database
from bill import BillingApp
from reset import ForgotPasswordApp
from inventory import Inventory_Page
from customer import Customer_Page
from customers import Customers
import os
from PIL import ImageTk,Image

# sys.path.insert(1,'C://Users//abhik//OneDrive//Desktop//Projects//Tkinter Projects//Khata-App//ResetCode')
class Home_Page:
    def __init__(self):  
        """
        Class constructor method, creates the main window of the application with a geometry 
        that matches the screen size and a background color of #4CC9FE. The window title is set to 'Login-Form'
        and the favicon is set to favicon.ico. The login GUI is then initialized by calling the 
        login_gui method. Finally, the mainloop method is called to start the application event loop.
        """
        self.dbo=Database()
        self.cust=Customers()
        self.root=Tk()
        self.root.title('Login-Form')
        
        base_path = getattr(sys, '_MEIPASS', os.path.abspath('.'))
        favicon_path = os.path.join(base_path, 'icon.ico')
        icon = ImageTk.PhotoImage(Image.open(favicon_path))
        
        self.root.iconphoto(False, icon)
        screen_width = self.root.winfo_screenwidth()
        screen_height =self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.configure(bg='#4CC9FE')
        self.login_gui()
        self.root.mainloop()
        
    def clear(self):
        """
        Method to clear the current window by destroying all the widgets in it.
        It is used to switch between different GUIs, by clearing the current window and
        then creating the new widgets for the new GUI.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_gui(self):        
        """
        Method to create the login GUI. It first clears the current window by 
        destroying all the widgets in it. Then it creates the necessary widgets for the 
        login GUI such as the application name, page name, email, password, login button, 
        forget password button and the register button. Finally, the widgets are placed 
        in the window using the pack and place methods.
        """
        self.clear()
        app_name=Label(self.root,text="Welcome to Khata App",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        app_name.pack(pady=(40,10))
        page_name=Label(self.root,text="Login Here",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        page_name.pack(pady=(40,10))
        
        phone_number=Label(self.root,text="Mobile Number",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        phone_number.pack(pady=(10,10),padx=(500,10),anchor='w')
        self.phone_number_value=Entry(self.root,width=70)
        self.phone_number_value.pack(pady=(10,10),padx=(500,10),ipady=4,anchor='w')
        
        password=Label(self.root,text="Enter your password",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        password.pack(pady=(40,3),padx=(500,10),anchor='w')
        self.password_value=Entry(self.root,width=70,show='*')
        self.password_value.pack(pady=(20,10),padx=(500,10),ipady=4,anchor='w')
        
        login_btn=Button(self.root,text='Login',width=10,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.login_operation)  
        forget_btn=Button(self.root,text='Forget Password ?',width=18,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.reset_password_gui)  
        login_btn.place(x=500,y=450)  
        forget_btn.place(x=700,y=448)
        
        register=Label(self.root,text="Not a member ? Register Now ",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',12,'bold'))
        register.pack(pady=(100,10),padx=(500,10),anchor='w')
        register_btn=Button(self.root,text='Register',width=10,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.register_gui)
        register_btn.pack(ipadx=(3),ipady=(3),pady=(30,3),padx=(500,10),anchor='w')

    def login_operation(self):
        """
        Method to validate the user's login credentials. This method is called when the user clicks on the login button in the login page.
        The method first gets the email and password entered by the user and then checks if the email is registered in the database.
        If the email is registered, the method checks if the password is correct. If the password is correct, the method shows a success
        message box and then calls the nav_gui method to switch to the navigation page. If the email is not registered or the password is
        wrong, the method shows an error message box and then calls the login_gui method to switch back to the login page.
        """
        email=self.phone_number_value.get()
        password=self.password_value.get()
        
        if self.dbo.validation(email,password):
            messagebox.showinfo('Success','Login Successful')
            self.nav_gui()
        else:
            messagebox.showerror('Error','Incorrect Email or Password')
            self.login_gui()
    def register_gui(self):
        """
        Method to create the GUI for the registration page. This method is called when the user clicks on the register button in the login page.
        This method clears the current GUI and creates a new one with the labels and entry fields for the user to enter his/her registration details.
        The method also creates a button to submit the registration request and a button to go back to the login page if the user is already a member.
        """
        self.clear()
        self.root.title('Register-Form')
        app_name=Label(self.root,text="Welcome to Khata App",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        app_name.pack(pady=(20,10))
        page_name=Label(self.root,text="Register Here",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        page_name.pack(pady=(20,10))
        
        owner_name=Label(self.root,text="Enter Owner Name",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        owner_name.pack(pady=(20,3),padx=(440,10),anchor='w')
        self.owner_name_value=Entry(self.root,width=70)
        self.owner_name_value.pack(pady=(10,10),padx=(440,10),ipady=4,anchor='w')
        
        
        email=Label(self.root,text="Enter your email",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        email.pack(pady=(10,10),padx=(440,10),anchor='w')
        self.email_value=Entry(self.root,width=70)
        self.email_value.pack(pady=(10,10),padx=(440,10),ipady=4,anchor='w')
        
        phone_number=Label(self.root,text="Enter mobile Number",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        phone_number.pack(pady=(10,10),padx=(440,10),anchor='w')
        self.phone_number_value=Entry(self.root,width=70)
        self.phone_number_value.pack(pady=(10,10),padx=(440,10),ipady=4,anchor='w')
        
        
        password=Label(self.root,text="Enter your password",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        password.pack(pady=(10,3),padx=(440,10),anchor='w')
        self.password_value=Entry(self.root,width=70,show='*')
        self.password_value.pack(pady=(10,10),padx=(440,10),ipady=4,anchor='w')
        
        confirm_password=Label(self.root,text="Confirm your password",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        confirm_password.pack(pady=(10,3),padx=(440,10),anchor='w')
        self.confirm_password_value=Entry(self.root,width=70,show='*')
        self.confirm_password_value.pack(pady=(10,10),padx=(440,10),ipady=4,anchor='w')
        
        btn=Button(self.root,text='Register',width=10,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.register_operation)
        btn.pack(ipadx=(3),ipady=(3),pady=(20,3),padx=(440,10),anchor='w')
        
        
        register=Label(self.root,text="Already a member ? Login Now ",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',12,'bold'))
        register.pack(pady=(15,3),padx=(440,10),anchor='w')
        
        login_btn=Button(self.root,text='Login',width=10,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.login_gui)
        login_btn.pack(ipadx=(3),ipady=(3),pady=(15,3),padx=(440,10),anchor='w')
        
        
    def register_operation(self):
        """
        Handles the user registration process by collecting input from the GUI fields 
        (email, password, confirm password, owner name, and mobile number). Validates 
        the input fields to ensure none are empty and that the password fields match. 
        If validation fails, displays an error message and reloads the registration 
        form. If validation passes, attempts to add the user to the database. If the 
        user is successfully added, displays a success message and navigates to the 
        login GUI. If the email already exists, displays an error message.
        """
        email=self.email_value.get()
        password=self.password_value.get()
        confirm_password=self.confirm_password_value.get()
        owner_name=self.owner_name_value.get()    
        mobile_number=self.phone_number_value.get()
        
        if email=="" or password=="" or confirm_password=="" or owner_name=="" or mobile_number=="":
            messagebox.showerror('Error','All fields are required')
            self.register_gui()
        
        if password!=confirm_password:
            messagebox.showerror('Error','Password and Confirm Password do not match')
            self.register_gui()
        else:
            self.dbo.create_table()
            res=self.dbo.add_user(int(mobile_number),owner_name,email,password)
            if res:
                messagebox.showinfo('Success','Registration Successful')
            else:
                messagebox.showerror('Error','Email Already Exists and number')
            self.login_gui()

    
    def reset_password_gui(self):
        """
        Method to create the GUI for the registration page. This method is called when the user clicks on the register button in the login page.
        This method clears the current GUI and creates a new one with the labels and entry fields for the user to enter his/her registration details.
        The method also creates a button to submit the registration request and a button to go back to the login page if the user is already a member.
        """
        obj=ForgotPasswordApp(self.root,self.login_gui)
            
    def nav_gui(self):
        """
        Method to create the navigation GUI. This method clears the current window 
        and sets the title to 'Navigation'. It creates and places the application 
        name and page name labels, and several buttons for navigating to different 
        parts of the application: creating a new bill, managing inventory, managing 
        customers, and logging out to return to the login GUI. The buttons trigger 
        respective methods when clicked.
        """
        self.clear()
        self.root.title('Navigation')
        
        app_name=Label(self.root,text="Welcome to Khata App",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        app_name.pack(pady=(40,10))
        page_name=Label(self.root,text="Login Here",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        page_name.pack(pady=(40,10))
        
        
        bill=Button(self.root,text='New Bill',width=30,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.bill_gui)
        bill.pack(ipadx=(3),ipady=(3),pady=(60,3),padx=(590,10),anchor='w')
        
        inventory=Button(self.root,text='Manage Inventory',width=30,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.inventory_gui)
        inventory.pack(ipadx=(3),ipady=(3),pady=(30,3),padx=(590,10),anchor='w')
        
        cust=Button(self.root,text='Manage Customers',width=30,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.customer_gui)
        cust.pack(ipadx=(3),ipady=(3),pady=(30,3),padx=(590,10),anchor='w')
        
        logout=Button(self.root,text='Logout',width=30,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.login_gui)
        logout.pack(ipadx=(3),ipady=(3),pady=(30,3),padx=(590,10),anchor='w')
        
    def bill_gui(self):
        """
        Method to create the GUI for billing. This method first clears the current window 
        and sets the title to 'Customer_Details'. It creates and places labels and entry 
        fields for customer details such as mobile number, name, address, and email. 
        Additionally, it includes buttons for creating a bill and navigating back to 
        the main navigation GUI. The buttons trigger respective methods when clicked.
        """
        self.clear()
        self.root.title('Customer_Details')
        
        app_name=Label(self.root,text="Welcome to Khata App",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        app_name.pack(pady=(40,10))
        page_name=Label(self.root,text="Login Here",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        page_name.pack(pady=(40,10))
        
        phone_number=Label(self.root,text="Mobile Number",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        phone_number.pack(pady=(10,10),padx=(570,10),anchor='w')
        self.phone_number_value=Entry(self.root,width=70)
        self.phone_number_value.pack(pady=(10,10),padx=(570,10),ipady=4,anchor='w')
        
        customer_name=Label(self.root,text="Enter Name",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        customer_name.pack(pady=(10,3),padx=(570,10),anchor='w')
        self.customer_name_value=Entry(self.root,width=70)
        self.customer_name_value.pack(pady=(10,10),padx=(570,10),ipady=4,anchor='w')
        
        address=Label(self.root,text="Enter Address",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        address.pack(pady=(10,3),padx=(570,10),anchor='w')
        self.address_value=Entry(self.root,width=70)
        self.address_value.pack(pady=(10,10),padx=(570,10),ipady=4,anchor='w')
        
        email=Label(self.root,text="Enter your email",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        email.pack(pady=(10,10),padx=(570,10),anchor='w')
        self.email_value=Entry(self.root,width=70)
        self.email_value.pack(pady=(10,10),padx=(570,10),ipady=4,anchor='w')
        
        bill=Button(self.root,text='Create Bill',width=30,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.bill_operation)
        bill.pack(ipadx=(3),ipady=(3),pady=(60,3),padx=(590,10),anchor='w')
        
        back=Button(self.root,text='Back',width=30,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.nav_gui)
        back.pack(ipadx=(3),ipady=(3),pady=(30,3),padx=(590,10),anchor='w')
        
    def bill_operation(self):
        
        """
        This method is called when the 'Create Bill' button is clicked. It validates the user input, checks if the customer already exists in the database, if not adds the customer to the database and then opens the billing app.
        """
        self.cust.create_table()
        mobile_number=self.phone_number_value.get()
        customer_name=self.customer_name_value.get()
        address=self.address_value.get()
        email=self.email_value.get()
        if not mobile_number or not customer_name or not address :
            messagebox.showerror('Error','All fields are required')

        data=self.cust.view_users()
        for item in data:
            if item[1]==int(mobile_number) and item[3]==email:
                messagebox.showerror('Error','Customer Already Exists')
                BillingApp(self.root,self.nav_gui)
                return
        self.cust.add_user(int(mobile_number),customer_name,address,email)
        messagebox.showinfo('Success','Bill Created')
        BillingApp(self.root,self.nav_gui)
        
    def inventory_gui(self):
        """
        This method initializes the inventory GUI by creating an instance of the Inventory_Page
        class. It sets up the inventory interface for the application by passing the root widget 
        and navigation GUI to the Inventory_Page class.
        """
        Inventory_Page(self.root,self.nav_gui)
        
    def customer_gui(self):
        """
        This method initializes the customer GUI by creating an instance of the Customer_Page
        class. It sets up the customer interface for the application by passing the root widget 
        and navigation GUI to the Customer_Page class.
        """
        Customer_Page(self.root,self.nav_gui)
   
    


    
obj=Home_Page()