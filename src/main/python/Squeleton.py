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
    def __init__(self, nombre, tipoDato):
        self.nombre = nombre
        self.tipoDato = tipoDato
    def __repr__(self):
        return "Variable: "+self.tipoDato+" "+self.nombre+": "+self.inicializado+", "+self.usado
class Funcion(ID):
    def __init__(self, nombre, tipoDato, args=None):
        super().__init__(nombre, tipoDato) #tipoDatoReturn
        if args is not None:
            self.args = args
        else:
            self.args = []
    def __repr__(self):
        args_repr = ", ".join([repr(arg) for arg in self.args])
        return "Funcion: "+self.tipoDato+" "+self.nombre+"("+args_repr+"): Inicializado: "+self.inicializado+", Usado: "+self.usado

class Contexto:
    """
    Contexto son las anidaciones
    """
    def __init__(self):
        # Diccionario con nombre como clave y la instancia de ID (Variable o Funcion) como valor
        self.ids = dict()

    def agregarID(self, id):
        self.ids[id.nombre] = id 
    def __repr__(self):
        # Crear una representación en cadena para todos los IDs en el contexto
        ids_repr = "\n".join([repr(id) for id in self.ids.values()])
        print("caca2")
        return "Contexto: "+ ids_repr

class TablaSimbolos:
    """
    Dict<String, ID> tabla ==> es un diccionario porque el string 
                                osea el nombre del objeto será la referencia 
                                a la informacion guardada en el tipo ID
    """
    instancia = None
    contextos = []
    
    @staticmethod
    def get_instancia():
        """
        Crea la tabla si es que no existe previamente
        """
        if TablaSimbolos.instancia is None:
            TablaSimbolos.instancia = TablaSimbolos()
        return TablaSimbolos.instancia
        
    def __init__(self):
        if TablaSimbolos.instancia is not None:
            raise Exception("La clase Tabla de Simbolos no puede ser instanciada mas de una vez!")
        self.contextos = []
        #self.contextos.append(Contexto())#para mi no va aca esto
        TablaSimbolos.instancia = self
        
    def add_contexto(self, contexto):
        """
        Agrega un nuevo contexto a la tabla de simbolos
        """
        print("Agregando contexto ......")
        print(self.__repr__())
        #print("Instancia: "+ self.get_instancia().getText())
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
        TODO ver si esto en serio sirve
        porque si hago una asignacion despues de inicializarla
        esto no lo va a tomar como bien
        capaz solo dejar en contexto
        """
        if self.contextos is not None:
            if self.buscar_local(id.nombre) is not None and self.buscar_global is not None: 
                #osea que no esta declarado en ninguna lado antes
                self.contextos[-1].tabla[id.nombre] = id 
            return None
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
        #print("Instancia: "+ self.instancia.getText())
        return "Tabla de Simbolos: " + self.contextos.__repr__()