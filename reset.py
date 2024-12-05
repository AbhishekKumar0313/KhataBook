import json
from tkinter import *
from tkinter import messagebox
import sys
import smtplib
import secrets
import random
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from users import Database

class ForgotPasswordApp:
    def __init__(self, root,login_fn):
        """
        Class constructor method, creates the main window of the application with a geometry 
        that matches the screen size and a background color of #3C3D37. The window title is set to 'Login-Form'
        and the favicon is set to favicon.ico. The login GUI is then initialized by calling the 
        login_gui method. Finally, the mainloop method is called to start the application event loop.
        """
        self.dbo=Database()
        self.root=root
        self.login_gui=login_fn
        self.reset_gui()


    def clear(self):
        """
        Method to clear the current window by destroying all the widgets in it.
        It is used to switch between different GUIs, by clearing the current window and
        then creating the new widgets for the new GUI.
        """
        for widget in self.root.winfo_children():
            widget.destroy()
   
    def reset_gui(self):
        
        """
        Method to create the GUI for the reset password form. This method is called when the user clicks on the forget password button in the login page.
        This method clears the current GUI and creates a new one with the labels and entry fields for the user to enter his/her email to reset the password.
        The method also creates a button to send the reset link and a button to go back to the login page if the user is already a member.
        """
        self.clear()
        self.root.title('Reset-Form')
        app_name=Label(self.root,text="Welcome to Khata App",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        app_name.pack(pady=(20,10))
        page_name=Label(self.root,text="Register Here",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        page_name.pack(pady=(20,10))
        
        self.phone_label=Label(self.root,text="Enter your Mobile Number",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        self.phone_label.pack(pady=(10,10),padx=(550,10),anchor='w')
        self.phone_val=Entry(self.root,width=70)
        self.phone_val.pack(pady=(10,10),padx=(550,10),ipady=4,anchor='w')        
        
        self.email_label=Label(self.root,text="Enter your email",bg="#4CC9FE",fg="white",font=('verdana',15,'bold'))
        self.email_label.pack(pady=(10,10),padx=(550,10),anchor='w')
        self.email_entry=Entry(self.root,width=70)
        self.email_entry.pack(pady=(10,10),padx=(550,10),ipady=4,anchor='w')
        
        self.linkbutton=self.send_link_button=Button(self.root,text='Send Reset Link',width=18,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.save_and_destroy)
        self.linkbutton.pack(ipadx=(3),ipady=(3),pady=(50,3),padx=(640,10),anchor='w')
        self.back=self.send_link_button=Button(self.root,text='Go Back',width=18,bg="#006BFF",fg="white",font=('verdana',12,'bold'),command=self.login_gui)
        self.back.pack(ipadx=(3),ipady=(3),pady=(50,3),padx=(640,10),anchor='w')
        
        


    def save_and_destroy(self):
            # Save the values from the entry fields
            """
            Method to save the values from the entry fields and destroy all widgets in the current window.
            It then calls the send_reset_link method to create the second window with the saved data.
            """
            self.mobile_number = self.phone_val.get()
            self.email = self.email_entry.get()

            # Destroy all widgets in the current window
            for widget in self.root.winfo_children():
                widget.destroy()

            # Call method to create the second window with the saved data
            self.send_reset_link()
    def send_reset_link(self):
        """
        Method to send a password reset link to the user's email. This method is called when the user clicks on the send reset link button in the reset password page.
        It checks if the email is in the database and if so, it generates a random reset token, stores it in the database and sends a password reset email with the link to the user.
        The method then shows a message box with a success message and calls the reset_password_form method to switch to the reset password form.
        If the email is not found in the database, the method shows an error message box with an appropriate message.
        """
        
        email = self.email
        phone=self.mobile_number
        isexist=self.dbo.validate_emailnumber(email,phone)
        if  isexist:
            reset_token = random.randint(1000, 9999)
            
            expiration_time = datetime.now() + timedelta(minutes=30)
            
            with open('token.json', 'w') as f:
                data={
                    'token': reset_token,
                    'expiration': expiration_time.isoformat()}
                json.dump(data, f)
            self.send_reset_email(email, reset_token)

            messagebox.showinfo("Success", "A password reset link has been sent to your email.")
            self.reset_password_form()
        else:
            messagebox.showerror("Error", "Email with this number not found, please try again.")
            self.reset_gui()

    def send_reset_email(self, to_email, token):
        # Set up the email content
        """
        Method to send a password reset email to the user's email. This method takes in
        the user's email and a random reset token as parameters. It sets up the email
        content using the MIMEText class and sends the email via SMTP using the
        smtplib.SMTP class. If the email fails to send, an error message box is shown with
        the exception message.
        """
        msg = MIMEText(f"Your OTP is : {token}, please enter it to reset your password.")
        msg['Subject'] = 'Password Reset Request'
        msg['From'] = 'abhicoding1303@gmail.com'
        msg['To'] = to_email

        # Send email via SMTP
        try:
            with smtplib.SMTP('smtp.gmail.com') as server:
                server.starttls()
                server.login('abhicoding1303@gmail.com', 'lfghnbkeieelcabm')
                server.sendmail('abhicoding1303@gmail.com', to_email, msg.as_string())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")

    def reset_password_form(self):
        # Close the current window
        """
        Method to create the GUI for the reset password form. This method is called when the user clicks on the send reset link button in the reset password page.
        It clears the current GUI and creates a new one with the labels and entry fields for the user to enter his/her OTP to reset the password.
        The method also creates a button to submit the OTP and calls the reset_password method to reset the user's password.
        """
        self.clear()
        self.root.title('Reset-Form')
        app_name=Label(self.root,text="Welcome to Khata App",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        app_name.pack(pady=(40,10))
        page_name=Label(self.root,text="Login Here",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        page_name.pack(pady=(40,10))

        # New password form
        self.otp_label = Label(self.root, text="Enter your OTP:",bg='#4CC9FE',fg='white',font=('verdana',15,'bold'))
        self.otp_label.pack(pady=(60,40),padx=(640,10),anchor='w')
        self.otp_entry = Entry(self.root,width=70)
        self.otp_entry.pack(pady=20,padx=(550,10),ipady=4,anchor='w')

        self.submit_button = Button(self.root,width=18,bg="#006BFF",fg="white",font=('verdana',12,'bold'), text="Submit OTP", command=self.reset_password)
        self.submit_button.pack(pady=40,padx=(640,10),anchor='w')

    def reset_password(self):        
        """
        Method to reset the user's password. This method is called when the user clicks on the submit OTP button in the reset password form.
        It checks if the token is valid and not expired. If the token is invalid or expired, an error message box is shown with an appropriate message.
        If the token is valid, the method calls the new_password_gui method to switch to the new password form.
        """
        with open('token.json', 'r') as f:
            users_db=json.load(f)
        
            if datetime.fromisoformat(users_db["expiration"]) < datetime.now() :
                messagebox.showerror("Error", "Token expired, please request a new password reset.")
                return
            elif  users_db['token'] != int(self.otp_entry.get()) :
                messagebox.showerror("Error", "Invalid OTP, please try again.")
                return
            
        self.new_password_gui()


    def new_password_gui(self):
        # New password form
        """
        Method to create the GUI for the new password form. This method is called when the user clicks on the submit OTP button in the reset password form.
        It clears the current GUI and creates a new one with the labels and entry fields for the user to enter his/her new password to reset the password.
        The method also creates a button to submit the new password and calls the updatepassword method to update the user's password.
        """
        self.clear()
        self.root.title('Reset-Form')
        app_name=Label(self.root,text="Welcome to Khata App",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        app_name.pack(pady=(40,10))
        page_name=Label(self.root,text="Login Here",bg="#4CC9FE",fg="#4C1F7A",font=('verdana',20,'bold'))
        page_name.pack(pady=(40,10))
        
        self.password_label = Label(self.root, text="Enter your New Password:",bg='#4CC9FE',fg='white',font=('verdana',15,'bold'))
        self.password_label.pack(pady=(40,20),padx=(545,10),anchor='w')
        self.password_entry = Entry(self.root,width=70)
        self.password_entry.pack(pady=10,padx=(550,10),ipady=4,anchor='w')
        self.cnfrmpassword_label = Label(self.root, text="Confirm your Password:",bg='#4CC9FE',fg='white',font=('verdana',15,'bold'))
        self.cnfrmpassword_label.pack(pady=(30,20),padx=(545,10),anchor='w')
        self.cnfrmpassword_entry = Entry(self.root,width=70)
        self.cnfrmpassword_entry.pack(pady=10,padx=(550,10),ipady=4,anchor='w')
        self.submit_button = Button(self.root,width=18,bg="#006BFF",fg="white",font=('verdana',12,'bold'), text="Submit Password", command= self.updatepassword)
        self.submit_button.pack(pady=20,padx=(640,10),anchor='w')
        
    def updatepassword(self):
        """
        Method to update the user's password. It gets the new password and confirm password from the entry fields and checks if they are the same.
        If they are the same, it updates the user's password in the database and shows a success message. If not, it shows an error message and calls the new_password_gui method to reset the form.
        """
        new_password = self.password_entry.get()
        confirm_password = self.cnfrmpassword_entry.get()
        if new_password == confirm_password:
            self.dbo.update_user(self.mobile_number,new_password)
            messagebox.showinfo("Success", "Your password has been updated successfully!")
            self.login_gui()
        else:
            messagebox.showerror("Error", "Passwords do not match, please try again.")
            self.new_password_gui()
        return    
    