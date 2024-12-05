import sqlite3
class Database:
    def connect_db(self):
        """
        Establish a connection to the 'users.db' SQLite database.

        Returns:
            sqlite3.Connection: A connection object to the 'users.db' database.
        """
        return sqlite3.connect('users.db')

    def create_table(self):
        
        """
        Create the 'users' table in the 'users.db' database if it does not exist.

        The 'users' table has the following columns:

        - mobile_number (INTEGER): The unique mobile number of the user.
        - owner_name (TEXT): The name of the owner.
        - email (TEXT): The email address of the owner.
        - password (TEXT): The password of the owner.

        The PRIMARY KEY is a composite key consisting of the 'mobile_number' and
        'email' columns.

        This method commits the changes to the database and then closes the
        connection.
        """

        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users(    
                    mobile_number INTEGER,
                    owner_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL,
                    PRIMARY KEY (mobile_number, email)
                    )
                    """)
       
        conn.commit()
        conn.close()
        
    def check_user_exists(self, mobile_number, email):
        """
        Check if a user with a given mobile number and email exists in the 'users' table.

        Args:
            mobile_number (int): The mobile number of the user.
            email (str): The email address of the user.

        Returns:
            bool: True if a user with the given mobile number and email exists, False otherwise.

        This method commits the changes to the database and then closes the connection.
        """
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE mobile_number=? AND email=?", (mobile_number, email))
        result = cursor.fetchone()
        conn.close()
        return result is not None  # If 
    
    def add_user(self,mobile_number,owner_name,email,password):
        """
        Add a new user to the 'users' table in the database.

        Args:
            mobile_number (int): The mobile number of the user.
            owner_name (str): The name of the user.
            email (str): The email address of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the user is added successfully, False otherwise.

        This method first checks if a user with the same mobile number and email
        already exists in the 'users' table. If the user exists, the method prints
        a message and returns False. If the user does not exist, the method adds
        the user to the database and returns True.
        """
        conn=self.connect_db()
        cursor=conn.cursor()
        if self.check_user_exists(mobile_number, email):
            print("User with this mobile number and email already exists.")
            return  False
        else:
            cursor.execute("INSERT INTO users(mobile_number,owner_name,email,password) VALUES(?,?,?,?)",(mobile_number,owner_name,email,password))
            conn.commit()
            conn.close()
            return True
    
    def update_user(self,mobile_number,password):
        """
        Update the password of the user with the given mobile number.

        Args:
            mobile_number (int): The mobile number of the user.
            password (str): The new password of the user.

        Returns:
            None

        This method commits the changes to the database and then closes the connection.
        """
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("UPDATE users SET password=? WHERE mobile_number=?",(password,mobile_number,))
        conn.commit()
        conn.close()
        

    def show_table_structure(self,db_name, table_name):
        """
        Prints the structure of the given table in the given database.

        Args:
            db_name (str): The name of the database.
            table_name (str): The name of the table.

        Returns:
            None
        """
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        conn.close()

        print("Table Structure:")
        print("ID | Name          | Type     | NotNull | Default | PK")
        print("-" * 50)
        for col in columns:
            print(col)
            
    def view_users(self):
        
        """
        Retrieve all users from the 'users' table in the database.

        Returns:
            list: A list of tuples, where each tuple contains the mobile number, owner name, email, and password of a user.

        This method commits the changes to the database and then closes the connection.
        """
        conn = self.connect_db()  # Open connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")  # Query all rows
        rows = cursor.fetchall()
        conn.close()  # Close connection
        return rows
    
    def validation(self,mobile_number,password):
        """
        Validate the user's login credentials.

        Args:
            mobile_number (int): The mobile number of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the user is validated successfully, False otherwise.

        This method first checks if a user with the given mobile number and password
        exists in the 'users' table. If the user exists, the method returns True. If the
        user does not exist, the method returns False.
        """
        conn = self.connect_db()  # Open connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE mobile_number=? AND password=?",(mobile_number,password))  # Query all rows
        rows = cursor.fetchone()
        conn.close()  # Close connection
        if rows:
            return True
        else:
            return False
        
    def validate_emailnumber(self,email,phone_number):
        """
        Check if a user with the given email and mobile number exists in the 'users' table.

        Args:
            email (str): The email address of the user.
            phone_number (int): The mobile number of the user.

        Returns:
            bool: True if a user with the given email and mobile number exists, False otherwise.

        This method establishes a connection to the database, checks for the existence of a
        user with the specified email and mobile number, and then closes the connection.
        """
        conn = self.connect_db()  # Open connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=? AND mobile_number=?",(email,phone_number))  # Query all rows
        rows = cursor.fetchone()
        conn.close()  # Close connection
        if rows:
            return True
        else:
            return False



