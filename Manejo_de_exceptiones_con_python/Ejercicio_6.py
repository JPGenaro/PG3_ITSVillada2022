import pymysql

conexion = pymysql.connect( host='localhost', user= 'bdi', passwd='Pepe_123456789', db='Exception')
cur = conexion.cursor()

try:
    cur.execute( "se lect nombre, apellido FROM usuarios" )
    for nombre, apellido in cur.fetchall() :
        print (nombre, apellido)
except pymysql.err.ProgrammingError as e:
    print(e, "\nError de programación...")
except pymysql.err.InternalError as e:
    print(e, "\nError interno...")
except pymysql.err.OperationalError as e:
    print(e, "\nError de operación...")
except pymysql.err.IntegrityError as e:
    print(e, "\nError de integridad...")
except pymysql.err.DataError as e:
    print(e, "\nError de datos...")
except pymysql.err.NotSupportedError as e:
    print(e, "\nError no soportado...")
except pymysql.err.DatabaseError as e:
    print(e, "\nError de base de datos...")
except Exception as e:
    print(e, "\nError desconocido...")

conexion.close()