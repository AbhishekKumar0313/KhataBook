from bill import BillingApp
from tkinter import Tk
from stock import Stock
import tkinter as tk
from tkinter import ttk
import os
from functools import partial
from tkinter import messagebox
from customers import Customers


class Customer_Page():
    def __init__(self,root,nav_gui):
        
        """
        Initializes the Customer_Page class by setting up the root window properties and
        creating instances of Stock and Customers. This constructor also prepares the 
        customer list by calling create_customer_list method. It sets the window title 
        to "Customer-Details" and the geometry to 800x600.

        Args:
            root (Tk): The root window object for the Tkinter application.
            nav_gui (function): The navigation function to switch between different GUIs.
        """
        self.stocks=Stock()
        self.customer=Customers()
        self.root = root
        self.nav_gui=nav_gui
        self.root.title("Customer-Details")
        self.root.geometry("800x600")

        self.create_customer_list()
        
    def clear(self):
        """
        Method to clear the current window by destroying all the widgets in it.
        It is used to switch between different GUIs, by clearing the current window and
        then creating the new widgets for the new GUI.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_customer_list(self):
        """
        Creates the customer list for the customer GUI.

        This method first clears the current window by calling the clear method.
        It then creates a new LabelFrame with the title "Customer List" and packs it into the root window.
        Inside the LabelFrame, it creates a Treeview widget to display the customer list.
        The Treeview widget has columns for the customer ID, mobile number, name, email, and address.
        The columns are configured to have a certain width and alignment.
        The Treeview widget is then packed into the LabelFrame, which is in turn packed into the root window.
        The method then creates the CRUD operation frame, which contains input fields and buttons for performing CRUD operations on customers.
        The input fields are created with the grid geometry manager and the buttons are created with the grid geometry manager.
        The buttons are configured to call the respective CRUD operation methods when clicked.
        The method finally packs the CRUD operation frame into the root window.
        """
        self.clear()
        customer_frame = tk.LabelFrame(self.root, text="Customer List", padx=10, pady=10,font=("Arial", 12, "bold"))
        customer_frame.pack(pady=10, padx=10, fill="both", expand=True)
       
        columns = ("ID", "Mobile Number", "Name", "Email", "Address")
        self.tree = ttk.Treeview(customer_frame, columns=columns, show="headings", height=10)
        self.tree.heading("ID", text="Customer ID")
        self.tree.heading("Mobile Number", text="Mobile No.")
        self.tree.heading("Name", text="Customer Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address",text="Address")
        self.tree.column("ID", width=20, anchor="center")
        self.tree.column("Mobile Number", width=100, anchor="w")
        self.tree.column("Name", width=100, anchor="center")
        self.tree.column("Email", width=150, anchor="center")
        self.tree.column("Address", width=350, anchor="center")
        
        self.products=self.customer.view_users()
        for product in self.products:
            self.tree.insert("", tk.END, values=(product[0], product[1], product[2],product[3],product[4]))

        self.tree.pack(fill="both", expand=True)
        
        
        # CRUD Operation Frame
        crud_frame = tk.LabelFrame(
            self.root, text="CRUD Operations", padx=10, pady=10, font=("Arial", 12, "bold")
        )
        crud_frame.pack(pady=10, padx=10, fill="x")

        # Input Fields
        tk.Label(crud_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = ttk.Entry(crud_frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(crud_frame, text=" Name").grid(row=0, column=2, padx=5, pady=5)
        self.name_entry = ttk.Entry(crud_frame)
        self.name_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(crud_frame, text="Mobile Number").grid(row=0, column=4, padx=5, pady=5)
        self.number_entry = ttk.Entry(crud_frame)
        self.number_entry.grid(row=0, column=5, padx=5, pady=5)
        
        tk.Label(crud_frame, text="Email").grid(row=0, column=6, padx=5, pady=5)
        self.email_entry = ttk.Entry(crud_frame)
        self.email_entry.grid(row=0, column=7, padx=5, pady=5)
        
        tk.Label(crud_frame, text="Address").grid(row=0, column=8, padx=5, pady=5)
        self.address_entry = ttk.Entry(crud_frame)
        self.address_entry.grid(row=0, column=9, padx=5, pady=5)

        # CRUD Buttons
        ttk.Button(crud_frame, text="Add Cusomter", command=self.add_product).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(crud_frame, text="Update Customer", command=self.update_product).grid(row=1, column=2, padx=5, pady=5)
        ttk.Button(crud_frame, text="Delete Customer", command=self.delete_product).grid(row=1, column=4, padx=5, pady=5)
        ttk.Button(crud_frame, text="Search Customer", command=self.search_product).grid(row=1, column=6, padx=5, pady=5)
        ttk.Button(crud_frame,text="Back",command=self.back).grid(row=1, column=8, padx=5, pady=5)

    def add_product(self):
        """Adds a new product to the inventory."""
        try:
            if not self.id_entry.get() or not self.name_entry.get() or not self.number_entry.get() or not self.email_entry.get() or not self.address_entry.get():
                raise ValueError("Customer details cannot be empty!")
            cust_id = int(self.id_entry.get())
            name = self.name_entry.get()
            mobile = int(self.number_entry.get())
            email=self.email_entry.get()
            address=self.address_entry.get()

            
            self.customers_data=self.customer.view_users()

            for item in self.customers_data:
                if item[0] == cust_id:
                    raise ValueError("Customer ID already exists!")

            # self.products.append({"id": product_id, "name": name, "price": price})
            self.customer.add_user(mobile,name,address,email)
            self.tree.insert("", tk.END, values=(cust_id,mobile,name,email,address))
            messagebox.showinfo("Success", f"Product '{name}' added successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_product(self):
        """Updates the selected product."""
        try:
            selected_item = self.tree.focus()
            if not selected_item:
                raise ValueError("No Customer selected!")

            cust_id = int(self.id_entry.get())
            name = self.name_entry.get()
            mobile = int(self.number_entry.get())
            email=self.email_entry.get()
            address=self.address_entry.get()
            
            if not name or not cust_id or not mobile or not email or not address:
                raise ValueError("Customer details cannot be empty!")
            self.customers_data=self.customer.view_users()
            # Update product in the product list
            for item in self.customers_data:
                if item[0] == cust_id:
                    break
            else:
                raise ValueError("Customer ID not found!")

            # Update product in the Treeview
            self.customer.update_user(cust_id,mobile,name,address,email)
            self.tree.item(selected_item, values=(cust_id,mobile, name, email, address))
            messagebox.showinfo("Success", f"Customer '{name}' updated successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_product(self):
        """Deletes the selected product."""
        try:
            selected_item = self.tree.focus()
            if not selected_item:
                raise ValueError("No Customer selected!")

            customer_values = self.tree.item(selected_item, "values")
            cust_id = int(customer_values[0])

            # Remove from the product list
            # self.products = [product for product in self.products if product["id"] != product_id]
            self.customer.delete_user(cust_id)
            # Remove from the Treeview
            self.tree.delete(selected_item)
            messagebox.showinfo("Success", f"Product ID {cust_id} deleted successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def search_product(self):
        """Searches for a product by ID."""
        try:
            if not self.id_entry.get():
                raise ValueError("Customer ID cannot be empty!")
            product_id = int(self.id_entry.get())
            for child in self.tree.get_children():
                self.tree.item(child, tags="")  # Clear previous highlights
            for child in self.tree.get_children():
                values = self.tree.item(child, "values")
                if int(values[0]) == product_id:
                    self.tree.selection_set(child)
                    self.tree.item(child, tags=("found",))
                    messagebox.showinfo("Success", f"Customer ID {product_id} found!")
                    return
            raise ValueError("Customer ID not found!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def back(self):
        """Goes back to the navigation GUI."""
        self.nav_gui()
