import pymysql

username = "doadmin"
password = "ypdubizi16nke1pw"
host = "codigofacilito-mysql-do-user-9539781-0.b.db.ondigitalocean.com"
port = 25060
database = "pythondb"

DROP_TABLE_USERS = """DROP TABLE IF EXISTS users
"""

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

if __name__ == '__main__':
    
    try:
        connect = pymysql.Connect(host=host, port=port, user=username, passwd=password, db=database)

        cursor = connect.cursor()

        cursor.execute(DROP_TABLE_USERS)
        cursor.execute(USERS_TABLE)

    except pymysql.err.OperationalError as err:
    #except pymysql.err.ProgrammingError as err:
        print("No fue posible realizar la conexión.")
        print(err)

    finally:
        cursor.close()
        connect.close()

        print('Conexión finalizada de forma exitosa.')