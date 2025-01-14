import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="test"
)

mycursor = mydb.cursor()

q = input("enter a num: ")
if not q.isidentifier():
    print("Invalid table name. Please use a valid identifier.")
else:
    # Create the SQL statement using an f-string
    sql = f"""
    CREATE TABLE `{q}` (
        id INT AUTO_INCREMENT,
        name VARCHAR(255),
        PRIMARY KEY (id)
    );
    """
                     
                 
