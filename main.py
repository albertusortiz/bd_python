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

users = [
    ("user1", "password", "user1@gmail.com"),
    ("user2", "password", "user2@gmail.com"),
    ("user3", "password", "user3@gmail.com"),
    ("user4", "password", "user4@gmail.com"),
    ("user5", "password", "user5@gmail.com"),
]

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

            # Insertando valores con Placeholders
            query = "INSERT INTO users(username, password, email) VALUES (%s, %s, %s)"

            #for user in users:
            #    cursor.execute(query, user)

            cursor.executemany(query, users)

            # Insertando valores con valores directos
            #query = "INSERT INTO users(username, password, email) VALUES('albertusortiz','password','alberto@gmail.com')"

            # Insertando valores con metodo format
            #query = "INSERT INTO users(username, password, email) VALUES('{}', '{}', '{}')".format("user1","password","user1@gmail.com")

            # Insertando valores con metodo format string
            #username = "user2"
            #password = "password"
            #email = "user2@gmail.com"
            #query = f"INSERT INTO users(username, password, email) VALUES('{username}','{password}','{email}')"

            #cursor.execute(query)
            
            connect.commit() # Persistir todos los cambios realizados hasta el momento.

    except pymysql.err.OperationalError as err:
    #except pymysql.err.ProgrammingError as err:
        print("No fue posible realizar la conexión.")
        print(err)

    finally:
        connect.close()

        print('Conexión finalizada de forma exitosa.')