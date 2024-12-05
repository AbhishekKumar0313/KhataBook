from bill import BillingApp
from tkinter import Tk
from stock import Stock
import tkinter as tk
from tkinter import ttk
import os
from functools import partial
from tkinter import messagebox

class Inventory_Page():
    def __init__(self,root,nav_gui):
        
        """
        Constructor method for the Inventory_Page class. This method initializes the main window of the application with a geometry that matches the screen size and a background color of #4CC9FE. The window title is set to 'Inventory' and the favicon is set to favicon.ico. The method then creates the necessary widgets for the inventory GUI such as the product list. Finally, the method calls the mainloop method to start the application event loop.
        """
        self.stocks=Stock()
        self.root = root
        self.nav_gui=nav_gui
        self.root.title("Inventory")
        self.root.geometry("800x600")

        self.create_product_list()
        
    def clear(self):
        """
        Method to clear the current window by destroying all the widgets in it.
        It is used to switch between different GUIs, by clearing the current window and
        then creating the new widgets for the new GUI.
        """
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def create_product_list(self):
        """
        Creates the product list for the inventory GUI.

        This method first clears the current window by calling the clear method.
        It then creates a new LabelFrame with the title "Product List" and packs it into the root window.
        Inside the LabelFrame, it creates a Treeview widget to display the product list.
        The Treeview widget has columns for the product ID, name, price, and quantity.
        The columns are configured to have a certain width and alignment.
        The Treeview widget is then packed into the LabelFrame, which is in turn packed into the root window.
        The method then creates the CRUD operation frame, which contains input fields and buttons for performing CRUD operations on products.
        The input fields are created with the grid geometry manager and the buttons are created with the grid geometry manager.
        The buttons are configured to call the respective CRUD operation methods when clicked.
        The method finally packs the CRUD operation frame into the root window.
        """
        self.clear()
        product_frame = tk.LabelFrame(self.root, text="Product List", padx=10, pady=10,font=("Arial", 12, "bold"))
        product_frame.pack(pady=10, padx=10, fill="both", expand=True)
        # Treeview for products
        columns = ("ID", "Name", "Price","Quantity")
        self.tree = ttk.Treeview(product_frame, columns=columns, show="headings", height=10)
        self.tree.heading("ID", text="Product ID")
        self.tree.heading("Name", text="Product Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Name", width=200, anchor="w")
        self.tree.column("Price", width=100, anchor="center")
        self.tree.column("Quantity", width=100, anchor="center")
        
        self.products=self.stocks.view_users()
        for product in self.products:
            self.tree.insert("", tk.END, values=(product[0], product[1], product[2],product[3]))

        self.tree.pack(fill="both", expand=True)
                
        # CRUD Operation Frame
        crud_frame = tk.LabelFrame(
            self.root, text="CRUD Operations", padx=10, pady=10, font=("Arial", 12, "bold")
        )
        crud_frame.pack(pady=10, padx=10, fill="x")

        # Input Fields
        tk.Label(crud_frame, text="Product ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = ttk.Entry(crud_frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(crud_frame, text="Product Name:").grid(row=0, column=2, padx=5, pady=5)
        self.name_entry = ttk.Entry(crud_frame)
        self.name_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(crud_frame, text="Price:").grid(row=0, column=4, padx=5, pady=5)
        self.price_entry = ttk.Entry(crud_frame)
        self.price_entry.grid(row=0, column=5, padx=5, pady=5)
        
        tk.Label(crud_frame, text="Quantity:").grid(row=0, column=6, padx=5, pady=5)
        self.quantity_entry = ttk.Entry(crud_frame)
        self.quantity_entry.grid(row=0, column=7, padx=5, pady=5)

        # CRUD Buttons
        ttk.Button(crud_frame, text="Add Product", command=self.add_product).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(crud_frame, text="Update Product", command=self.update_product).grid(row=1, column=2, padx=5, pady=5)
        ttk.Button(crud_frame, text="Delete Product", command=self.delete_product).grid(row=1, column=4, padx=5, pady=5)
        ttk.Button(crud_frame, text="Search Product", command=self.search_product).grid(row=1, column=6, padx=5, pady=5)
        ttk.Button(crud_frame,text="Back",command=self.back).grid(row=1, column=8, padx=5, pady=5)

    def add_product(self):
        """Adds a new product to the inventory."""
        try:
            product_id = int(self.id_entry.get())
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            quantity=int(self.quantity_entry.get())

            if not name or not price or not product_id or price <= 0:
                raise ValueError("Product details cannot be empty!")
            self.products=self.stocks.view_users()

            for product in self.products:
                if product[0] == product_id:
                    raise ValueError("Product ID already exists!")

            # self.products.append({"id": product_id, "name": name, "price": price})
            self.stocks.add_product(name,price,quantity)
            self.tree.insert("", tk.END, values=(product_id, name, price,quantity))
            messagebox.showinfo("Success", f"Product '{name}' added successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_product(self):
        """Updates the selected product."""
        try:
            selected_item = self.tree.focus()
            if not selected_item:
                raise ValueError("No product selected!")

            product_id = int(self.id_entry.get())
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            quantity=int(self.quantity_entry.get())
            
            if not name or not price or not product_id or price <= 0:
                raise ValueError("Product details cannot be empty!")

            # Update product in the product list
            for product in self.products:
                if product[0] == product_id:
                    break
            else:
                raise ValueError("Product ID not found!")

            # Update product in the Treeview
            self.stocks.update_product(product_id,name,price,quantity)
            self.tree.item(selected_item, values=(product_id, name, price,quantity))
            messagebox.showinfo("Success", f"Product '{name}' updated successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_product(self):
        """Deletes the selected product."""
        try:
            selected_item = self.tree.focus()
            if not selected_item:
                raise ValueError("No product selected!")

            product_values = self.tree.item(selected_item, "values")
            product_id = int(product_values[0])

            # Remove from the product list
            # self.products = [product for product in self.products if product["id"] != product_id]
            self.stocks.delete_product(product_id)
            # Remove from the Treeview
            self.tree.delete(selected_item)
            messagebox.showinfo("Success", f"Product ID {product_id} deleted successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def search_product(self):
        """Searches for a product by ID."""
        try:
            product_id = int(self.id_entry.get())
            for child in self.tree.get_children():
                self.tree.item(child, tags="")  # Clear previous highlights
            for child in self.tree.get_children():
                values = self.tree.item(child, "values")
                if int(values[0]) == product_id:
                    self.tree.selection_set(child)
                    self.tree.item(child, tags=("found",))
                    messagebox.showinfo("Success", f"Product ID {product_id} found!")
                    return
            raise ValueError("Product ID not found!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def back(self):
        self.nav_gui()
