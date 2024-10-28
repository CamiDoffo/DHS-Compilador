from enum import Enum
from abc import abstractclass, abstractmethod
# usar esto usando singleton (?

class ID(abstractclass):
    @abstractmethod
    def __init__(self, nombre, tipoDato, inicializado=False, usado=False):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.inicializado = inicializado
        self.usado = usado
    
    def set_inicializado(self):
        self.inicializado = True
    def set_usado(self):
        self.usado = True
    
class Variable(ID):
    def __repr__(self):
        return print("Variable: "+self.tipoDato+" "+self.nombre+": "+self.inicializado+", "+self.usado)
class Funcion(ID):
    def __init__(self, nombre, tipoDato, args=None, inicializado=False, usado=False):
        super().__init__(nombre, tipoDato, inicializado, usado) #tipoDatoReturn
        if args is not None:
            self.args = args
        else:
            self.args = []
    def __repr__(self):
        return print("Funcion: "+self.tipoDato+" "+self.nombre+": "+self.inicializado+", "+self.usado)

class Contexto:
    """
    Contexto son las anidaciones
    """
    def __init__(self):
        # Diccionario con nombre como clave y la instancia de ID (Variable o Funcion) como valor
        self.tabla = {}
    def __repr__(self):
        return print("Contexto: "+ self.tabla)
    
class TablaSimbolos:
    """
    Dict<String, ID> tabla ==> es un diccionario porque el string 
                                osea el nombre del objeto será la referencia 
                                a la informacion guardada en el tipo ID
    """
    def __init__(self):
        self.contextos = []
        
    def add_contexto(self, contexto):
        self.contextos.append(contexto)
    def del_Contexto(self):
        """
        Elimina el ultimo contexto
        """
        if self.contextos is not None:
            return self.contextos.pop()
        return None
        
    def add_identificador(self, id):
        if self.contextos is not None:
            self.contextos[-1].tabla[id.nombre] = id
        return None
    def buscar_local(self, nombre):
        """
        Busca en el contexto actual (para for o funcion con argumentos)
        """
        if self.contextos is not None:
            return self.contextos[-1].tabla.get(nombre, None)
        return None
            
    def buscar_global(self, nombre):
        """
        Busca el contexto globalmente (para cosas anidadas)
        """
        for contexto in reversed(self.contextos):
            for nom in contexto.tabla:
                if nom == nombre:
                    return contexto.tabla[nombre]
        return None
    def __repr__(self):
        return print("Tabla de Simbolos: " + self.contextos)