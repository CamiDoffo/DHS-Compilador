from abc import ABC, abstractmethod 
# usar esto usando singleton (?

class ID(ABC):
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
    instancia = None
    
    @staticmethod
    def get_instancia():
        """
        Crea la tabla si es que no existe previamente
        """
        if TablaSimbolos.instancia == None:
            TablaSimbolos()
        return TablaSimbolos.instancia
        
    def __init__(self):
        if TablaSimbolos.instancia != None:
            raise Exception("La clase Tabla de Simbolos no puede ser instanciada mas de una vez!")
        self.contextos = []
        
    def add_contexto(self, contexto):
        """
        Agrega un nuevo contexto a la tabla de simbolos
        """
        self.contextos.append(contexto)
        
    def del_Contexto(self):
        """
        Elimina el ultimo contexto
        """
        if self.contextos is not None:
            return self.contextos.pop()
        return None
        
    def add_identificador(self, id):
        """
        Agrega un identificador al contexto actual
        """
        if self.contextos is not None:
            if self.buscar_local(id.nombre) is not None and self.buscar_global is not None: 
                #osea que no esta declarado en ninguna lado antes
                self.contextos[-1].tabla[id.nombre] = id 
            return None
            # if id.nombre in self.contextos[-1].tabla:
            #     print("---- ERROR -----")
            #     print("El identificador "+id.nombre+" ya existe en el contexto actual!")
            #     return None
            # self.contextos[-1].tabla[id.nombre] = id 
            #en el elemento que busca (segun el nombre) le asigna todo el identificador
            # lo dejo para que no me pregunten que habiamos puesto antes
        return None
    
    def buscar_local(self, nombre):
        """
        Busca en el contexto actual (para for o funcion con argumentos)
        """
        if self.contextos is not None:
            if nombre in self.contextos[-1].tabla:
                print("---- ERROR SEMANTICO -----")
                print("El identificador "+nombre+" ya existe en el contexto actual!")
                return None
            return self.contextos[-1].tabla.get(nombre, None)
        return None
            
    def buscar_global(self, nombre):
        """
        Busca el contexto globalmente (para cosas anidadas)
        """
        for contexto in reversed(self.contextos):
            if nombre in contexto.tabla:
                print("---- ERROR SEMANTICO -----")
                print("El identificador "+nombre+" ya existe en el contexto actual!")
                return None
        return contexto.tabla[nombre]
    def __repr__(self):
        return print("Tabla de Simbolos: " + self.contextos)