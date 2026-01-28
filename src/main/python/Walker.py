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
        self.f = open("./output/CodigoIntermedio.txt", "w")
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
    # FUNCIONES Y VARIABLES
    # -------------------------------------------------------------------------
    def visitDeclaracionGlobal(self, ctx: compiladoresParser.DeclaracionGlobalContext):
        nombre = ctx.getChild(1).getText()
        ctx_resto = ctx.restoDeclaracion()
        primer_char = ctx_resto.start.text

        if primer_char == '(': # Función
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
        else: # Variable
            if ctx_resto.asignacionInit():
                self.visit(ctx_resto.asignacionInit())

    def visitFuncionVoid(self, ctx: compiladoresParser.FuncionVoidContext):
        nombre = ctx.getChild(1).getText()
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

    def visitAsignacionInit(self, ctx):
        nombre_var = ctx.parentCtx.parentCtx.getChild(1).getText() 
        self.visit(ctx.exp())
        self.f.write(f'{nombre_var} = {self.temporales.pop()}\n')

    # -------------------------------------------------------------------------
    # LLAMADAS Y RETORNOS
    # -------------------------------------------------------------------------
    def visitLlamadafun(self, ctx: compiladoresParser.LlamadafunContext):
         self.visit(ctx.funcionVar())

    def visitFuncionVar(self, ctx: compiladoresParser.FuncionVarContext):
        temps_antes = len(self.temporales)
        
        # Generar temporales de argumentos
        if ctx.ids(): self.visit(ctx.ids())
        
        # Extraer y hacer push
        num_args = len(self.temporales) - temps_antes
        args_para_push = []
        for _ in range(num_args):
            args_para_push.append(self.temporales.pop())

        for arg in reversed(args_para_push):
            self.f.write(f'push {arg}\n')

        # Saltos
        nombre_func = ctx.ID().getText()
        etiquetas = self.labels.etiqueta_funcion(nombre_func)
        self.f.write(f'push {etiquetas[1]}\n')
        self.f.write(f'jmp {etiquetas[0]}\n')
        self.f.write(f'label {etiquetas[1]}\n')
        
        # Simular retorno (hack para asignación)
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
        if ctx.asignacionBool(): self.visit(ctx.asignacionBool())
        elif ctx.asignacionNum(): self.visit(ctx.asignacionNum())
    
    def visitAsignacionBool(self, ctx: compiladoresParser.AsignacionBoolContext):
        self.visit(ctx.opbool())
        self.f.write(f'{ctx.ID().getText()} = {self.temporales.pop()}\n')

    def visitAsignacionNum(self, ctx: compiladoresParser.AsignacionNumContext):
        variable = ctx.ID().getText()
        self.visit(ctx.exp()) # Genera el valor o la llamada a función
        self.f.write(f'{variable} = {self.temporales.pop()}\n')

    # -------------------------------------------------------------------------
    # EXPRESIONES (Aquí estaba el error de la suma perdida)
    # -------------------------------------------------------------------------
    def visitExp(self, ctx: compiladoresParser.ExpContext):
        self.visit(ctx.term())
        # IMPORTANTE: Recorrer la lista expPrima
        for ep in ctx.expPrima():
            self.visit(ep)
            
    def visitExpPrima(self, ctx: compiladoresParser.ExpPrimaContext):
        operador = ctx.getChild(0).getText()
        self.visit(ctx.term())
        derecha = self.temporales.pop()
        izquierda = self.temporales.pop()
        temporal = self.temps.next_temporal()
        self.f.write(f'{temporal} = {izquierda} {operador} {derecha}\n')
        self.temporales.append(temporal)
    
    def visitTerm(self, ctx: compiladoresParser.TermContext):
        self.visit(ctx.factor())
        for t_ctx in ctx.t():
             self.visit(t_ctx)

    def visitT(self, ctx: compiladoresParser.TContext):
        operador = ctx.getChild(0).getText()
        self.visit(ctx.factor())
        derecha = self.temporales.pop()
        izquierda = self.temporales.pop()
        temporal = self.temps.next_temporal()
        self.f.write(f'{temporal} = {izquierda} {operador} {derecha}\n')
        self.temporales.append(temporal)
    
    def visitFactor(self, ctx: compiladoresParser.FactorContext):
        if ctx.PA():
            self.visit(ctx.exp())
        elif ctx.funcionVar():
            self.visit(ctx.funcionVar())
        else:
            temporal = self.temps.next_temporal()
            self.f.write(f'{temporal} = {ctx.getText()}\n')
            self.temporales.append(temporal)

    # -------------------------------------------------------------------------
    # CONDICIONALES Y BUCLES (Aquí faltaban los saltos ifn)
    # -------------------------------------------------------------------------
    def visitBloque(self, ctx: compiladoresParser.BloqueContext):
        if ctx.instrucciones(): self.visit(ctx.instrucciones())
        elif ctx.instruccion(): self.visit(ctx.instruccion())

    def visitIif(self, ctx: compiladoresParser.IifContext):
        self.visit(ctx.cond())
        etiqueta_else = self.labels.next_etiqueta()
        
        # IMPORTANTE: Escribir el salto
        self.f.write(f'ifn {self.temporales.pop()} jmp {etiqueta_else}\n')
        
        self.visit(ctx.bloque(0))

        if len(ctx.bloque()) > 1: # Else
            etiqueta_fin = self.labels.next_etiqueta()
            self.f.write(f'jmp {etiqueta_fin}\n')
            self.f.write(f'label {etiqueta_else}\n')
            self.visit(ctx.bloque(1))
            self.f.write(f'label {etiqueta_fin}\n')
        else:
            self.f.write(f'label {etiqueta_else}\n')
            
    def visitIwhile(self, ctx: compiladoresParser.IwhileContext):
        etiqueta_inicio = self.labels.next_etiqueta()
        etiqueta_fin = self.labels.next_etiqueta()

        self.f.write(f'label {etiqueta_inicio}\n')
        self.visit(ctx.cond())
        
        # IMPORTANTE: Escribir el salto
        self.f.write(f'ifn {self.temporales.pop()} jmp {etiqueta_fin}\n')
        
        self.visit(ctx.bloque())
        self.f.write(f'jmp {etiqueta_inicio}\n')
        self.f.write(f'label {etiqueta_fin}\n')
    
    def visitIfor(self, ctx: compiladoresParser.IforContext):
        etiqueta_inicio = self.labels.next_etiqueta()
        etiqueta_fin = self.labels.next_etiqueta()
        
        self.visit(ctx.init())
        self.f.write(f'label {etiqueta_inicio}\n')
        self.visit(ctx.cond())
        self.f.write(f'ifn {self.temporales.pop()} jmp {etiqueta_fin}\n')
        self.visit(ctx.bloque())
        self.visit(ctx.iter())
        self.f.write(f'jmp {etiqueta_inicio}\n')
        self.f.write(f'label {etiqueta_fin}\n')
    
    def visitIter(self, ctx: compiladoresParser.IterContext):
         var = ctx.ID(0).getText()
         # Obtenemos op y num manualmente porque la visita puede ser compleja
         op = ctx.iteracion().getChild(0).getText() # +
         num = ctx.iteracion().NUMERO().getText()   # 1
         
         temporal = self.temps.next_temporal()
         self.f.write(f'{temporal} = {var} {op} {num}\n')
         self.f.write(f'{var} = {temporal}\n')

    # -------------------------------------------------------------------------
    # CONDICIONES Y OPERADORES
    # -------------------------------------------------------------------------
    def visitCond(self, ctx):
        if ctx.opcomp(): self.visit(ctx.opcomp())
        elif ctx.opbool(): self.visit(ctx.opbool())
        
    def visitOpcomp(self, ctx):
        left = ctx.ID().getText()
        operator = ctx.getChild(1).getText()
        self.visit(ctx.factor())
        right = self.temporales.pop()
        
        temp = self.temps.next_temporal()
        self.f.write(f"{temp} = {left} {operator} {right}\n")
        self.temporales.append(temp)

    def visitOpbool(self, ctx: compiladoresParser.OpboolContext):
        if ctx.getChildCount() == 1: self.visit(ctx.getChild(0))
        else: pass # Implementar recursión de AND/OR si es necesario

    def visitFactorBool(self, ctx):
        temp = self.temps.next_temporal()
        val = 1 if ctx.TRUE() else 0
        self.f.write(f'{temp} = {val}\n')
        self.temporales.append(temp)

    def visitErrorNode(self, node):
        print("---- ERROR WALKER ----")
        return super().visitErrorNode(node)