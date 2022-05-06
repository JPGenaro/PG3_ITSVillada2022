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
except:
    print("Error de conexión...")