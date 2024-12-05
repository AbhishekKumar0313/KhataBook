import sqlite3

class Stock:
    def connect_db(self):
        """
        Establish a connection to the 'stock.db' SQLite database.

        Returns:
            sqlite3.Connection: A connection object to the 'stock.db' database.
        """
        return sqlite3.connect('stock.db')

    def create_table(self):
        """
        Create the 'stocks' table in the 'stock.db' database if it does not exist.

        The 'stocks' table has the following columns:

        - ID (INTEGER): The unique id of the stock item.
        - product (TEXT): The name of the product.
        - price (FLOAT): The price of the product.
        - quantity (INTEGER): The quantity of the product in stock.

        This method commits the changes to the database and then closes the connection.
        """
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS stocks(    
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    product TEXT NOT NULL,
                    price FLOAT NOT NULL,
                    quantity INTEGER NOT NULL
                    )
                    """)
       
        conn.commit()
        conn.close()
        
    def update_product(self,id,product,price,quantity):
        """
        Update the stock item with the given id in the 'stocks' table.

        Args:
            id (int): The id of the stock item to be updated.
            product (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.

        This method commits the changes to the database and then closes the connection.
        """
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("UPDATE stocks SET product=?,price=?,quantity=? WHERE ID=?",(product,price,quantity,id))
        conn.commit()
        conn.close()
        
    def add_product(self,product,price,quantity):
        """
        Add a new stock item to the 'stocks' table.

        Args:
            product (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.

        This method commits the changes to the database and then closes the connection.
        """
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO stocks(product,price,quantity) VALUES(?,?,?)",(product,price,quantity))
        conn.commit()
        conn.close()   
    def view_users(self):
        """
        Retrieve all stock items from the 'stocks' table in the database.

        Returns:
            list: A list of tuples, where each tuple contains the id, product name, price, and quantity of a stock item.

        This method commits the changes to the database and then closes the connection.
        """
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stocks")  
        rows = cursor.fetchall()
        conn.close() 
        return rows

    def delete_product(self,id):
        """
        Delete the stock item with the given id from the 'stocks' table in the database.

        Args:
            id (int): The id of the stock item to be deleted.

        This method commits the changes to the database and then closes the connection.
        """
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("DELETE FROM stocks WHERE ID=?",(id,))
        conn.commit()
        conn.close()

