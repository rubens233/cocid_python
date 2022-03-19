from persistencia.repositorio_persona import RepositorioPersona
from persistencia.repositorio_empleado import RepositorioEmpleado


def eliminar_persona(curp):    
    return RepositorioPersona().eliminar(curp) 

def insertar_persona(persona):    
    return RepositorioPersona().insertar(persona)    

def consultar_persona():    
    return RepositorioPersona().consultar()    