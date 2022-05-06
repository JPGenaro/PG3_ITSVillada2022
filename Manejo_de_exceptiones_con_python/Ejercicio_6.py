import pymysql

conexion = pymysql.connect( host='localhost', user= 'bdi', passwd='Pepe_123456789', db='Exception')
cur = conexion.cursor()

try:
    cur.execute( "se lect nombre, apellido FROM usuarios" )
    for nombre, apellido in cur.fetchall() :
        print (nombre, apellido)
except pymysql.err.ProgrammingError:
    print("Error de programación...")
    conexion.close()
except pymysql.err.InternalError:
    print("Error interno...")
except pymysql.err.OperationalError:
    print("Error de operación...")
except pymysql.err.IntegrityError:
    print("Error de integridad...")
except pymysql.err.DataError:
    print("Error de datos...")
except pymysql.err.NotSupportedError:
    print("Error no soportado...")
except pymysql.err.DatabaseError:
    print("Error de base de datos...")
except:
    print("Error de conexión...")