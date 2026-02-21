from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser

class Temporales:
    def __init__(self):
        self.counter = 0
    def next_temporal(self):
        temporal = f'temp{self.counter}'
        self.counter += 1
        return temporal

class Etiquetas:
    funciones = dict()
    counter = 0

    def next_etiqueta(self):
        etiqueta = f'label{self.counter}'
        self.counter += 1
        return etiqueta

    def etiqueta_funcion(self, identificador:str):
        if identificador in self.funciones:
            return self.funciones[identificador]
        
        list = []
        etiqueta1 = self.next_etiqueta() # Etiqueta inicio
        etiqueta2 = self.next_etiqueta() # Etiqueta retorno/fin
        list.append(etiqueta1)
        list.append(etiqueta2)
        self.funciones[identificador] = list
        return list

class Walker(compiladoresVisitor):
    def __init__(self):
        self.temporales = []
        self.temps = Temporales()
        self.labels = Etiquetas()
        self.isFuncion = 0
        self.inFuncion = 0
        self.f = None

    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("=-"*20)
        print("--- Generando codigo intermedio ---")
        self.f = open("./output/CodigoIntermedio_Puro.txt", "w")
        self.visit(ctx.instrucciones())
        self.f.close()
        print("\033[1;32m"+"--- Codigo intermedio generado ---"+"\033[0m")
        
    def visitInstrucciones(self, ctx: compiladoresParser.InstruccionesContext):
        for instruccion in ctx.instruccion():
            self.visit(instruccion)
    
    def visitInstruccion(self, ctx: compiladoresParser.InstruccionContext):
        if ctx.declaracionGlobal(): self.visit(ctx.declaracionGlobal())
        elif ctx.funcionVoid():     self.visit(ctx.funcionVoid())
        elif ctx.iwhile():          self.visit(ctx.iwhile())
        elif ctx.ifor():            self.visit(ctx.ifor())
        elif ctx.iif():             self.visit(ctx.iif())
        elif ctx.asignacionPYC():   self.visit(ctx.asignacionPYC())
        elif ctx.returnfun():       self.visit(ctx.returnfun())
        elif ctx.bloque():          self.visit(ctx.bloque())
        elif ctx.llamadafun():      self.visit(ctx.llamadafun())

    # -------------------------------------------------------------------------
    # FUNCIONES Y VARIABLES GLOBALES
    # -------------------------------------------------------------------------
    def visitDeclaracionGlobal(self, ctx: compiladoresParser.DeclaracionGlobalContext):
        nombre = ctx.getChild(1).getText()
        ctx_resto = ctx.restoDeclaracion()
        primer_char = ctx_resto.start.text

        if primer_char == '(': # Función o Prototipo
            if ctx_resto.bloque() is not None: 
                if nombre != 'main':
                    self.inFuncion = 1
                    etiquetas = self.labels.etiqueta_funcion(nombre)
                    self.f.write(f'label {etiquetas[0]}\n')
                    self.f.write(f'pop {etiquetas[1]}\n')
                    self.visit(ctx_resto.bloque())
                    self.f.write(f'jmp {etiquetas[1]}\n')
                    self.inFuncion = 0
                else:
                    self.visit(ctx_resto.bloque())
            else:
                pass # Es un prototipo
        else: # Variable (ej: int a = 1, b = 2;)
            if ctx_resto.exp():
                self.visit(ctx_resto.exp())
                self.f.write(f'{nombre} = {self.temporales.pop()}\n')
            
            for dec in ctx_resto.decItem():
                self.visit(dec)

    def visitDecItem(self, ctx: compiladoresParser.DecItemContext):
        if ctx.exp():
            nombre = ctx.ID().getText()
            self.visit(ctx.exp())
            self.f.write(f'{nombre} = {self.temporales.pop()}\n')

    def visitFuncionVoid(self, ctx: compiladoresParser.FuncionVoidContext):
        nombre = ctx.getChild(1).getText()
        if ctx.bloque() is not None:
            if nombre != 'main':
                self.inFuncion = 1
                etiquetas = self.labels.etiqueta_funcion(nombre)
                self.f.write(f'label {etiquetas[0]}\n')
                self.f.write(f'pop {etiquetas[1]}\n')
                self.visit(ctx.bloque())
                self.f.write(f'jmp {etiquetas[1]}\n')
                self.inFuncion = 0
            else:
                self.visit(ctx.bloque())

    # -------------------------------------------------------------------------
    # LLAMADAS Y RETORNOS
    # -------------------------------------------------------------------------
    def visitLlamadafun(self, ctx: compiladoresParser.LlamadafunContext):
         self.visit(ctx.funcionVar())

    def visitFuncionVar(self, ctx: compiladoresParser.FuncionVarContext):
        temps_antes = len(self.temporales)
        
        if ctx.ids(): self.visit(ctx.ids())
        
        num_args = len(self.temporales) - temps_antes
        args_para_push = []
        for _ in range(num_args):
            args_para_push.append(self.temporales.pop())

        for arg in reversed(args_para_push):
            self.f.write(f'push {arg}\n')

        nombre_func = ctx.ID().getText()
        etiquetas = self.labels.etiqueta_funcion(nombre_func)
        self.f.write(f'push {etiquetas[1]}\n')
        self.f.write(f'jmp {etiquetas[0]}\n')
        self.f.write(f'label {etiquetas[1]}\n')
        
        temp_ret = self.temps.next_temporal()
        self.f.write(f'pop {temp_ret}\n') 
        self.temporales.append(temp_ret)
        self.isFuncion = 0

    def visitReturnfun(self, ctx: compiladoresParser.ReturnfunContext):
        if self.inFuncion == 1:
            if ctx.exp():
                self.visit(ctx.exp())
                self.f.write(f'push {self.temporales.pop()}\n')

    # -------------------------------------------------------------------------
    # ASIGNACIONES
    # -------------------------------------------------------------------------
    def visitAsignacionPYC(self, ctx: compiladoresParser.AsignacionPYCContext):
        self.visit(ctx.asignacion())

    def visitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        variable = ctx.ID().getText()
        self.visit(ctx.exp()) 
        self.f.write(f'{variable} = {self.temporales.pop()}\n')

    # -------------------------------------------------------------------------
    # CONDICIONALES Y BUCLES
    # -------------------------------------------------------------------------
    def visitBloque(self, ctx: compiladoresParser.BloqueContext):
        if ctx.instrucciones(): self.visit(ctx.instrucciones())

    def visitInstruccionOBloque(self, ctx: compiladoresParser.InstruccionOBloqueContext):
        if ctx.bloque(): self.visit(ctx.bloque())
        elif ctx.instruccion(): self.visit(ctx.instruccion())

    def visitIif(self, ctx: compiladoresParser.IifContext):
        self.visit(ctx.exp())
        etiqueta_else = self.labels.next_etiqueta()
        
        self.f.write(f'ifn {self.temporales.pop()} jmp {etiqueta_else}\n')
        
        self.visit(ctx.instruccionOBloque(0))

        if len(ctx.instruccionOBloque()) > 1: # Else
            etiqueta_fin = self.labels.next_etiqueta()
            self.f.write(f'jmp {etiqueta_fin}\n')
            self.f.write(f'label {etiqueta_else}\n')
            self.visit(ctx.instruccionOBloque(1))
            self.f.write(f'label {etiqueta_fin}\n')
        else:
            self.f.write(f'label {etiqueta_else}\n')
            
    def visitIwhile(self, ctx: compiladoresParser.IwhileContext):
        etiqueta_inicio = self.labels.next_etiqueta()
        etiqueta_fin = self.labels.next_etiqueta()

        self.f.write(f'label {etiqueta_inicio}\n')
        self.visit(ctx.exp())
        
        self.f.write(f'ifn {self.temporales.pop()} jmp {etiqueta_fin}\n')
        
        self.visit(ctx.instruccionOBloque())
        self.f.write(f'jmp {etiqueta_inicio}\n')
        self.f.write(f'label {etiqueta_fin}\n')
    
    def visitIfor(self, ctx: compiladoresParser.IforContext):
        etiqueta_inicio = self.labels.next_etiqueta()
        etiqueta_fin = self.labels.next_etiqueta()
        
        self.visit(ctx.decItem())
        self.f.write(f'label {etiqueta_inicio}\n')
        self.visit(ctx.exp())
        self.f.write(f'ifn {self.temporales.pop()} jmp {etiqueta_fin}\n')
        self.visit(ctx.instruccionOBloque())
        self.visit(ctx.asignacion())
        self.f.write(f'jmp {etiqueta_inicio}\n')
        self.f.write(f'label {etiqueta_fin}\n')

    # -------------------------------------------------------------------------
    # LA SÚPER EXPRESIÓN UNIFICADA (Matemáticas, Lógica y Comparaciones)
    # -------------------------------------------------------------------------
    def visitExp(self, ctx: compiladoresParser.ExpContext):
        # Si tiene 3 hijos, es una operación (ej: exp + exp, exp > exp, exp && exp)
        if ctx.getChildCount() == 3:
            self.visit(ctx.getChild(0)) 
            self.visit(ctx.getChild(2)) 
            
            derecha = self.temporales.pop()
            izquierda = self.temporales.pop()
            
            operador = ctx.getChild(1).getText()
            
            temporal = self.temps.next_temporal()
            self.f.write(f'{temporal} = {izquierda} {operador} {derecha}\n')
            self.temporales.append(temporal)
            
        # Si solo tiene 1 hijo, es un Factor (bajó por la regla sin operar)
        else:
            self.visit(ctx.factor())

    def visitFactor(self, ctx: compiladoresParser.FactorContext):
        # Maneja los literales booleanos directamente
        if ctx.TRUE():
            temp = self.temps.next_temporal()
            self.f.write(f'{temp} = 1\n')
            self.temporales.append(temp)
        elif ctx.FALSE():
            temp = self.temps.next_temporal()
            self.f.write(f'{temp} = 0\n')
            self.temporales.append(temp)
        # Maneja las llamadas a funciones
        elif ctx.funcionVar():
            self.visit(ctx.funcionVar())
        # Maneja los paréntesis (ej: (a + b) )
        elif ctx.PA():
            self.visit(ctx.exp())
        # Maneja variables y números puros
        else:
            temporal = self.temps.next_temporal()
            self.f.write(f'{temporal} = {ctx.getText()}\n')
            self.temporales.append(temporal)