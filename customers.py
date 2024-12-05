import sqlite3

class Customers:
    def connect_db(self):
            
        """
        Establish a connection to the 'customers.db' SQLite database.

        Returns:
            sqlite3.Connection: A connection object to the 'customers.db' database.
        """
        return sqlite3.connect('customers.db')

    def create_table(self):
        """
        Create the 'customers' table in the 'customers.db' database if it does not exist.

        The 'customers' table has the following columns:

        - ID (INTEGER): The unique id of the customer.
        - mobile_number (INTEGER): The mobile number of the customer.
        - customer_name (TEXT): The name of the customer.
        - email (TEXT): The email address of the customer.
        - address (TEXT): The address of the customer.

        This method commits the changes to the database and then closes the connection.
        """
        conn=self.connect_db() 
        cursor=conn.cursor()
        cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS customers(    
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    mobile_number INTEGER NOT NULL,
                    customer_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT NOT NULL)
                    """)
        conn.commit()
        conn.close()
        
    def view_users(self):
        """
        Retrieve all customers from the 'customers' table in the database.

        Returns:
            list: A list of tuples, where each tuple contains the id, mobile number, customer name, email, and address of a customer.

        This method commits the changes to the database and then closes the connection.
        """
        conn = self.connect_db()  # Open connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")  # Query all rows
        rows = cursor.fetchall()
        conn.close()  # Close connection
        return rows
    
    def add_user(self,mobile_number,customer_name,address,email):
        """
        Add a new customer to the 'customers' table in the database.

        Args:
            mobile_number (int): The mobile number of the customer.
            customer_name (str): The name of the customer.
            address (str): The address of the customer.
            email (str): The email of the customer.

        This method commits the changes to the database and then closes the connection.
        """
        
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO customers(mobile_number,customer_name,address,email) VALUES(?,?,?,?)",(mobile_number,customer_name,address,email))
        conn.commit()
        conn.close()
        
    def update_user(self,id,mobile_number,customer_name,address,email):
        """
        Update the customer with the given id in the 'customers' table.

        Args:
            id (int): The id of the customer to be updated.
            mobile_number (int): The mobile number of the customer.
            customer_name (str): The name of the customer.
            address (str): The address of the customer.
            email (str): The email of the customer.

        This method commits the changes to the database and then closes the connection.
        """
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("UPDATE customers SET customer_name=?,address=?,email=? ,mobile_number=? WHERE ID=?",(customer_name,address,email,mobile_number,id))
        conn.commit()
        conn.close()
    
    def delete_user(self,id):
        """
        Delete the customer with the given id from the 'customers' table in the database.

        Args:
            id (int): The id of the customer to be deleted.

        This method commits the changes to the database and then closes the connection.
        """
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("DELETE FROM customers WHERE ID=?",(id,))
        conn.commit()
        conn.close()