import tkinter as tk
from tkinter import ttk
import os
from functools import partial
from tkinter import messagebox
from stock import Stock

class BillingApp:
    def __init__(self, root,nav_gui):
        """
        Constructor method for the BillingApp class. This method initializes the main window of the application with a geometry that matches the screen size and a background color of #4CC9FE. The window title is set to 'Product Billing System' and the favicon is set to favicon.ico. The method then creates the necessary widgets for the billing GUI such as the product list, selection inputs, bill tree and the print button. Finally, the method calls the mainloop method to start the application event loop.
        """
        self.root = root
        self.nav_gui=nav_gui
        self.stocks=Stock()
        self.root.title("Product Billing System")
        self.root.geometry("800x600")
        
        self.create_product_list()
        self.create_selection_inputs()
        self.create_bill_tree()
        self.create_print_button()

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
        Creates the product list treeview widget and packs it into the root window.
        
        This method is called when the user navigates to the billing GUI from the main menu.
        It first clears the current window by destroying all the widgets in it, then creates a new
        LabelFrame with the title "Product List". Inside this LabelFrame, it creates a Treeview widget
        with columns "ID", "Name", "Price", and "Quantity". It then populates this Treeview with the
        product data from the database by calling the view_users method of the Stock class. Finally,
        it packs the Treeview into the LabelFrame and the LabelFrame into the root window.
        """
        self.clear()
        product_frame = tk.LabelFrame(self.root, text="Product List", padx=10, pady=10,font=("Arial", 12, "bold"))
        product_frame.pack(pady=10, padx=10, fill="both", expand=True)
       
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

    def create_selection_inputs(self):
        """
        Creates the selection inputs for the billing GUI, including a weight type dropdown, amount entry, add to bill button, and status label.

        This method is called when the user navigates to the billing GUI from the main menu. It first clears the current window by destroying all the widgets in it, then creates a new LabelFrame with the title "Select Product Details". Inside this LabelFrame, it creates a dropdown for selecting the weight type (kg, gm, or piece), an entry field for entering the amount, a button to add the selected product to the bill, and a label to display the status of the action. Finally, it packs the LabelFrame into the root window.
        """
        selection_frame = tk.LabelFrame(self.root, text="Select Product Details", padx=10, pady=10)
        selection_frame.pack(pady=10, padx=10, fill="x")

       
        tk.Label(selection_frame, text="Weight Type:").grid(row=0, column=0, padx=5, pady=5)
        self.weight_var = tk.StringVar(value="kg")
        weight_dropdown = ttk.OptionMenu(selection_frame, self.weight_var, "kg", "kg", "gm","piece")
        weight_dropdown.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(selection_frame, text="Amount:").grid(row=0, column=2, padx=5, pady=5)
        self.amount_entry = ttk.Entry(selection_frame)
        self.amount_entry.grid(row=0, column=3, padx=5, pady=5)

        add_button = ttk.Button(
            selection_frame,
            text="Add to Bill",
            command=lambda: self.add_to_bill() 
        )
        add_button.grid(row=0, column=4, padx=5, pady=5)
        
        self.status_label = tk.Label(selection_frame, text="", fg="green")
        self.status_label.grid(row=1, column=0, columnspan=5)

    def create_bill_tree(self):
        """
        Creates the bill tree for the billing GUI.

        This method creates a new LabelFrame with the title "Bill", and inside it, a Treeview widget to display the bill. The Treeview widget has columns for the product name, weight type, amount, and total price. The columns are configured to have a certain width and alignment. The Treeview widget is then packed into the LabelFrame, which is in turn packed into the root window.
        """
        bill_frame = tk.LabelFrame(self.root, text="Bill", padx=10, pady=10)
        bill_frame.pack(pady=10, padx=10, fill="both", expand=True)

        bill_columns = ("Product Name", "Weight Type", "Amount", "Total Price")
        self.bill_tree = ttk.Treeview(bill_frame, columns=bill_columns, show="headings", height=10)
        self.bill_tree.heading("Product Name", text="Product Name")
        self.bill_tree.heading("Weight Type", text="Weight Type")
        self.bill_tree.heading("Amount", text="Amount")
        self.bill_tree.heading("Total Price", text="Total Price")
        self.bill_tree.column("Product Name", width=200, anchor="w")
        self.bill_tree.column("Weight Type", width=100, anchor="center")
        self.bill_tree.column("Amount", width=100, anchor="center")
        self.bill_tree.column("Total Price", width=120, anchor="center")
        self.bill_tree.pack(fill="both", expand=True)

    def create_print_button(self):
        # Print Button
        """
        Creates the Print Bill button for the billing GUI.

        This method creates a new Button widget with the text "Print Bill" and assigns the print_bill method to its command option. The button is then packed into the root window with a vertical padding of 10 pixels.

        Additionally, a Back button is created with the text "Back" and assigned the back method as its command option. This button is also packed into the root window with a horizontal padding of 50 pixels and a vertical padding of 10 pixels.
        """
        print_button = ttk.Button(self.root, text="Print Bill", command=self.print_bill)
        print_button.pack(pady=10)
        back=ttk.Button(self.root,text="Back",command=self.back)
        back.pack(padx=50,pady=10)
        
    def back(self):
        """
        Go back to the navigation page.

        This method is called when the "Back" button is clicked. It clears the current window and calls the nav_gui method to switch to the navigation page.
        """
        self.nav_gui()
        
    def add_to_bill(self):
        """
        Add the selected product to the bill.

        This method is called when the "Add to Bill" button is clicked. It validates the user input, checks if the product is selected and if the amount is valid, calculates the total price based on the selected weight type and quantity, and then adds the product to the bill.

        If any errors occur during the process, an error message is displayed on the status label. Otherwise, a success message is displayed.
        """
        try:
            selected_item = self.tree.focus()  
            if not selected_item:
                raise ValueError("No product selected!")

            product_values = self.tree.item(selected_item, "values")
            product_name = product_values[1]
            product_price = float(product_values[2])
            product_id=int(product_values[0])
            product_quantity=int(product_values[3])

            weight_type = self.weight_var.get()
            if weight_type not in ["kg", "gm", "piece"]:
                raise ValueError("Invalid weight type!")

            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Amount must be greater than zero!")
            elif amount > product_quantity:
                raise ValueError("Amount exceeds product quantity!")

            if weight_type == "gm":
                total_price = (product_price / 1000) * amount
            elif weight_type == "piece":
                total_price = product_price*amount
            else:
                total_price = product_price * amount

            self.stocks.update_product(product_id,product_name,product_price,int(product_quantity-amount))
            self.tree.item(selected_item, values=(product_id,product_name, product_price, product_quantity-amount,product_id))
            self.bill_tree.insert("", tk.END, values=(product_name, weight_type, amount, round(total_price, 2)))
            self.status_label.config(text=f"Added {product_name} to the bill! ", fg="green")
        except ValueError as e:
            self.status_label.config(text=f"Error: {e}", fg="red")
        except Exception as e:
            self.status_label.config(text=f"Unexpected Error: {e}", fg="red")

    def print_bill(self):
            """
            Print the current bill to a text file and then print it manually.

            This method is called when the "Print Bill" button is clicked. It collects all the bill data from the Treeview widget, saves it to a text file named "bill.txt" and then opens the file in the default application for printing.

            If any errors occur during the process, an error message is displayed. Otherwise, a success message is displayed.

            :return: None
            """
            try:
               
                bill_data = []
                for row in self.bill_tree.get_children():
                    bill_data.append(self.bill_tree.item(row, "values"))

                if not bill_data:
                    messagebox.showerror("Error", "No items in the bill to print!")
                    return

                # Save to a text file
                with open("bill.txt", "w") as bill_file:
                    bill_file.write(f"{'Product Name'.ljust(20)}{'Weight Type'.ljust(15)}{'Amount'.ljust(10)}{'Total Price'.rjust(15)}\n")
                    bill_file.write("=" * 60 + "\n")
                    for item in bill_data:
                        product_name, weight_type, amount, total_price = item
                        bill_file.write(f"{product_name.ljust(20)}{weight_type.ljust(15)}{str(amount).ljust(10)}{str(total_price).rjust(15)}\n")
                    bill_file.write("="*60 + "\n")
                    total_price = sum(float(item[3]) for item in bill_data)
                    bill_file.write(f"Total Price: {total_price}\n")

                messagebox.showinfo("Success", "Bill saved to 'bill.txt'. You can print it manually.")
                os.startfile("bill.txt", "print")
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error: {e}")
