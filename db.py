import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'atiku',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS user(
        ID INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255),
        dob VARCHAR(255),
        email VARCHAR(255),
        address VARCHAR(255),
        phone INT,
        city VARCHAR(255),
        gender VARCHAR(255),
        PRIMARY KEY(ID)
    )
    """
)
