import pymysql

try:
    conexion = pymysql.connect( host='localhost', user= 'bdi', passwd='Pepe_123456789', db='Exception')
    cur = conexion.cursor()
    cur.execute("create table if not exists usuarios (id int primary key, nombre varchar(50), apellido varchar(50))")
    print("Tabla creada")
    cur.execute("insert into usuarios (id, nombre, apellido) values (1, 'Juan', 'Perez')")
    cur.execute("insert into usuarios (id, nombre, apellido) values (2, 'Pedro', 'Mondiola')")
    cur.execute("insert into usuarios (id, nombre, apellido) values (3, 'Ana', 'Gonzalez')")
    print("Usuarios insertados\n")
    cur.execute("select * FROM usuarios" )
    for id, nombre, apellido in cur.fetchall() :
        print (id, nombre, apellido)
    cur.execute("drop table usuarios")
    conexion.close()
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