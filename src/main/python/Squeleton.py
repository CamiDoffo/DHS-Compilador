from abc import abstractmethod, ABC
import inspect

class ID(ABC):
    args = []
    @abstractmethod
    def __init__(self, nombre, tipoDato, inicializado=False, usado=False, declarado=True):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.inicializado = inicializado
        self.usado = usado
        self.declarado = declarado
    def get_tipoDato(self):
        return str(self.tipoDato)
    
    def set_inicializado(self, valor=True):
        self.inicializado = valor

    def set_usado(self):
        self.usado = True
    
    def __str__(self):
        return self.tipoDato+" "+self.nombre+": Inicializado? "+str(self.inicializado)+", Usado? "+str(self.usado)

class Variable(ID):
    def __init__(self, nombre, tipoDato, inicializado=False, usado=False, declarado=True):
        super().__init__(nombre, tipoDato, inicializado, usado, declarado)  
    def __str__(self):
        return "Variable: "+super().__str__()

class Funcion(ID):
    args = []
    def __init__(self, nombre, tipoDato, inicializado=False, usado=False, declarado=True):
        super().__init__(nombre, tipoDato, inicializado, usado, declarado)

    def set_args(self, args):
        self.args = args  
    def __str__(self):
        return "Función: "+super().__str__()
          
class Contexto:
    """
    Contexto son las anidaciones
    """
    ids = dict()
    nombreContexto=""
    def __init__(self, nombreContexto):
        # Diccionario con nombre como clave y la instancia de ID (Variable o Funcion) como valor
        self.ids = dict()
        self.nombreContexto = nombreContexto
        
    def agregarID(self, id):
        self.ids[id.nombre] = id 
        
    def __str__(self):
        # Crear una representación en cadena para todos los IDs en el contexto
        ids_repr = ""
        if self.ids == dict():
            ids_repr = "Sin contexto."
        else:
            for id in self.ids.values():
                ids_repr += id.__str__() + "\n"
        return "Contexto "+self.nombreContexto+": \n"+ ids_repr

class Contexto:
    def __init__(self, nombre=""):
        self.nombre = nombre
        self.ids = {}

    def agregarID(self, id):
        self.ids[id.nombre] = id

class TablaSimbolos:
    __instance = None

    def __init__(self):
        self.contextos = []

    @staticmethod
    def get_instancia():
        if TablaSimbolos.__instance is None:
            TablaSimbolos.__instance = TablaSimbolos()
        return TablaSimbolos.__instance

    def add_contexto(self, nombre=""):
        nuevo = Contexto(nombre)
        self.contextos.append(nuevo)

    def del_Contexto(self):
        if len(self.contextos) > 0:
            return self.contextos.pop()
        return None

    def add_identificador(self, id):
        if self.contextos:
            self.contextos[-1].ids[id.nombre] = id

    def buscar_local(self, nombre):
        """Busca SOLO en el contexto actual (tope de la pila)."""
        if not self.contextos:
            return None
        if nombre in self.contextos[-1].ids:
            return self.contextos[-1].ids[nombre]
        return None

    # --- ESTA ES LA FUNCIÓN QUE TE FALTA CORREGIR ---
    def buscar_global(self, nombre):
        """
        Busca en CUALQUIER contexto, empezando por el actual y bajando hasta el global.
        Usamos 'reversed' para ir del tope (local) hacia la base (global).
        """
        for ctx in reversed(self.contextos):
            if nombre in ctx.ids:
                return ctx.ids[nombre]
        return None
    # ------------------------------------------------

    def mostrarVarsSinUsar(self):
        print("\nVariables sin usar:")
        for ctx in self.contextos:
            for id_obj in ctx.ids.values():
                # Verificamos si tiene atributo 'usado' y si es falso
                if hasattr(id_obj, 'usado') and not id_obj.usado:
                     print(f"{type(id_obj).__name__} {id_obj.nombre}: Inicializado? {getattr(id_obj, 'inicializado', False)}, Usado? False")