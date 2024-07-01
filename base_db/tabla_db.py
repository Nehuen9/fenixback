

class Tabla:
  #creacion de tabla
  def __init__(self, nombre, apellido, telefono, mail, usuario, password):
    self.tabla = nombre
    self.apellido = apellido
    self.telefono = telefono
    self.mail = mail
    self.usuario = usuario
    self.password = password



# CRUD
def crear_nombre():
  
  pass

def crear_usuario(self, usuario ):
  self.usuario = usuario
  if usuario != usuario:
    print ("usuario creado correctamente!")
  else:
    print("usuario ya existente!, pruebe con otro nombre!")


def guardar_db(self):
    campos_q = str(self.campos[1:]).replace("'", "`")
    values_q = f"({'%s, ' * (len(self.campos)-2)} %s)"
    consulta = (f"INSERT INTO {self.tabla} {campos_q} "
                f"VALUES {values_q};")
    datos = tuple(vars(self).values())
    rta_db = self.__conectar(consulta, datos)
    
    if rta_db:
        return 'Creación exitosa.'
    
    return 'No se pudo crear el registro.'


def password():
  
  pass