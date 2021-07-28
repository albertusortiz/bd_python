import pymysql

from decouple import config

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

if __name__ == '__main__':
    
    try:
        connect = pymysql.Connect(host=config('HOST_DB'),
                                port=int(config('PORT_DB')),
                                user=config('USERNAME_DB'),
                                passwd=config('PASSWORD_DB'),
                                db=config('DATABASE'))

        with connect.cursor() as cursor:
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)

            query = "INSERT INTO users(username, password, email) VALUES (%s, %s, %s)"
            values = ("albertusortiz", "password123", "alberto.ortiz.vargas@gmail.com")

            cursor.execute(query, values)
            connect.commit() # Persistir todos los cambios realizados hasta el momento.

    except pymysql.err.OperationalError as err:
    #except pymysql.err.ProgrammingError as err:
        print("No fue posible realizar la conexión.")
        print(err)

    finally:
        connect.close()

        print('Conexión finalizada de forma exitosa.')