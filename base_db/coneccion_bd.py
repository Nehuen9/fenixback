import mysql.connector

coneccion = mysql.connector.connect(user = 'root',
                                    password='',
                                    host='127.0.0.1'
                                    database='fenixdb')

cursor = conexion.cursor()


config_dev = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'fenixdb',
}

config_prod = {
  'user': 'Diego11',
  'password': 'fenix2024@',
  'host': 'Diego11.mysql.pythonanywhere-services.com',
  'database': 'Diego
}

conexion = mysql.connector.connect(**config_dev) 

print(coneccion)
