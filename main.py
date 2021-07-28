import pymysql

username = "doadmin"
password = "ypdubizi16nke1pw"
host = "codigofacilito-mysql-do-user-9539781-0.b.db.ondigitalocean.com"
port = 25060
database = "pythondb"

if __name__ == '__main__':
    
    try:
        connect = pymysql.Connect(host=host, port=port, user=username, passwd=password, db=database)

        print("Conexion realizada de forma exitosa.")
    except pymysql.err.OperationalError as err:
    #except pymysql.err.ProgrammingError as err:
        print("No fue posible realizar la conexión.")
        print(err)