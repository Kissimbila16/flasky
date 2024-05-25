
import pymysql

def database_conection():
    try:
        conn = pymysql.connect(
        host='localhost',
        user='user',
        password='password',
        database='database'
        )
        conn.close()
        return True
    except pymysql.Error:
        return False

def table_user():
    if database_conection():
        conn = pymysql.connect(
        host='localhost',
        user='user',
        password='password',
        database='database'
        )

        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            number VARCHAR(20)
        )
        """

        cursor.execute(create_table_query)

        cursor.close()
        conn.close()
    else:
        print("App not connected to database")

table_user()
