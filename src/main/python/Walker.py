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

    def etiqueta_funcion(self, identificador):
        # si el identificador existe, me devuelve la lista de etiquetas
        for id in self.funciones:
            if str(id) == str(identificador):
                return self.funciones[id]
        # si el identificador no existe, debo generar las etiquetas para la funcion
        list = []
        etiqueta1 = self.next_etiqueta(self)
        etiqueta2 = self.next_etiqueta(self)
        list.append(etiqueta1)
        list.append(etiqueta2)
        self.funciones[identificador] = list
        return list

class Walker (compiladoresVisitor):
    temporales = []
    temps = Temporales()
    labels = Etiquetas()
    isFuncion = 0
    inFuncion = 0
    
    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("=-"*20) # hace esto 20 veces
        print("--- Generado codigo intermedio ---")
        self.f = open("./output/CodigoIntermedio.txt", "w")
        
        self.visitInstrucciones(ctx.getChild(0))
        self.f.close()
        print("--- Codigo intermedio generado ---")
        
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        self.visitInstruccion(ctx.getChild(0))
        if ctx.getChild(1).getChildCount() != 0: # si hay mas de una intruccion
            self.visitInstrucciones(ctx.getChild(1))
        return
    
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        self.visitChildren(ctx)
        
    def visitAsignacionPYC(self, ctx:compiladoresParser.asignacionPYC):
        self.visitAsignacion(ctx.getChild(0))

    def visitBloqueSolo(self, ctx:compiladoresParser.BloqueSoloContext):
        self.visitInstrucciones(ctx.getChild(1))
        
    # me parece que no hace falta implementarlo
    # def visitDeclaracion(self, ctx): # devuelve el tipo de variable seguido de su id
    #     print(ctx.getChild(0).getText()+
    #           " - " + 
    #           ctx.getChild(1). getText())
    #     #return super().visitDeclaracion(ctx)
    #     return None
    
    # def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        # # ctx.getChild(0) va a ser la asignacion entera
        # print("que hay aca?? "+ctx.getChild(0).getText())
        # # return super().visitAsignacion(ctx)
        # if self.inFuncion == 1:
        #     self.f.write(ctx.getChild(0).getChild(0).getText() +
        #                  " = " + self._temporales.pop() + '\n')
        #     return
        # capaz puedo zafar de no implementar esto porque no se como separar los bools de nums
    
    def visitAsignacionBool(self, ctx:compiladoresParser.AsignacionBoolContext):
        if self.inFuncion == 1:
            self.visitExp(ctx.getChild(2))
            self.f.write(ctx.getChild(0).getText() + ' = ' +
                         self.temporales.pop() + '\n')
            return       
        self.visitExp(ctx.getChild(2))
        self.f.write(ctx.getChild(0).getText() + ' = ' +
                     self.temporales.pop() + '\n')
        return
    
    def visitOpbool(self, ctx:compiladoresParser.OpboolContext):
        self.visitFactorBool(ctx.getChild(0))
        if self.inFuncion == 0:
            if ctx.getChild(1).getChildCount() != 0:
                temporal = self.temps.next_temporal()
                self.f.write(temporal + ' = ' + self.temporales.pop() + ' ' +
                         ctx.getChild(1).getChild(0).getText() + ' ' +
                         self.visitBools(ctx.getChild(1)) + '\n')
            self.temporales.append(temporal)
            
    def visitBools(self, ctx:compiladoresParser.BoolsContext):
        self.visitFactorBool(ctx.getChild(1))
        if ctx.getChild(2).getChildCount() != 0:
            temporal = self.temps.next_temporal()
            self.f.write(temporal + ' = ' + self.temporales.pop() + ' ' +
                         ctx.getChild(2).getChild(0).getText() + ' ' +
                         self.visitOpbool(ctx.getChild(1)) + '\n')
            self.temporales.append(temporal)
            if self.isFuncion == 1:
                self.f.write('push ' + self.temporales.pop() + '\n')
        return self.temporales.pop()
            
    def visitFactorBool(self, ctx:compiladoresParser.FactorBoolContext):
        return super().visitFactorBool(ctx)       
    
    def visitAsignacionNum(self, ctx:compiladoresParser.AsignacionNumContext):
        # print("asigNum?? "+ctx.getText()) # esto entro sin que implemente asignacion...
        if self.inFuncion == 1:
            self.visitExp(ctx.getChild(2))
            self.f.write(ctx.getChild(0).getText() + ' = ' +
                         self.temporales.pop() + '\n')
            return       
        # verificacion de llamado a funcion
        if ctx.getChild(2).getChild(0).getChild(0).getChild(0).getChildCount() != 0:
            self.isFuncion = 1
            self.visitExp(ctx.getChild(2))
            self.f.write('pop ' + ctx.getChild(0).getText() + '\n')
        else:
            self.visitExp(ctx.getChild(2))
            self.f.write(ctx.getChild(0).getText() + ' = ' +
                         self.temporales.pop() + '\n')
        return
    
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        self.visitTerm(ctx.getChild(0))
        if ctx.getChild(1).getChildCount() != 0:
            temporal = self.temps.next_temporal()
            self.f.write(temporal + ' = ' + self.temporales.pop() + ' ' +
                         ctx.getChild(1).getChild(0).getText() + ' ' +
                         self.visitExpPrima(ctx.getChild(1)) + '\n')
            self.temporales.append(temporal)
            if self.isFuncion == 1:
                self.f.write('push ' + self.temporales.pop() + '\n')
        return self.temporales.pop()
    
    def visitExpPrima(self, ctx:compiladoresParser.ExpPrimaContext):
        self.visitExp(ctx.getChild(1))
        if ctx.getChild(1).getChild(1).getChildCount() != 0:
            temporal = self.temps.next_temporal()
            self.f.write(temporal + ' = ' + self.temporales.pop() + ' ' +
                         ctx.getChild(1).getChild(1).getChild(0).getText() + ' ' +
                         self.visitExp(ctx.getChild(1)) + '\n')
            self.temporales.append(temporal)
        return self.temporales.pop()
    
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        self.visitFactor(ctx.getChild(0))
        
        if ctx.getChild(1).getChildCount() != 0:
            temporal = self.temps.next_temporal()
            self.f.write(temporal + ' = ' + self.temporales.pop() + ' ' + 
                         ctx.getChild(1).getChild(0).getText() + ' ' + 
                         self.visitT(ctx.getChild(1)) + '\n')
            self.temporales.append(temporal)
            return
        if ctx.getChild(0).getChild(0).getChildCount() != 0:
            self.isFuncion = 1
    
    def visitT(self, ctx:compiladoresParser.TContext):
        self.visitFactor(ctx.getChild(1))
        
        if ctx.getChild(2).getChildCount() != 0:
            temporal = self.temps.next_temporal()
            self.f.write(temporal + ' = ' + self.temporales.pop() + ' ' +
                         ctx.getChild(2).getChild(0).getText() + ' ' +
                         self.visitT(ctx.getChild(2)) + '\n')
            self.temporales.append(temporal)
        
        return self.temporales.pop()
    
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        if ctx.getChild(0).getChildCount() != 0: # por si es funcionVar
            self.visitFuncionVar(ctx.getChild(0))
            return
        if ctx.getChildCount() == 3: # por si es PA exp PC
            self.visitExp(ctx.getChild(1))
            return
        if ctx.getChildCount() == 1:
            temporal = self.temps.next_temporal()
            self.f.write(temporal + ' = ' + ctx.getChild(0).getText() + '\n')
            self.temporales.append(temporal)
            return
        
    def visitFuncionVar(self, ctx:compiladoresParser.FuncionVarContext):
        self.visitIds(ctx.getChild(2))
        etiquetas = self.labels.etiqueta_funcion(ctx.getChild(0))
        
        self.f.write('push ' + etiquetas[1] + '\n')
        self.f.write('jmp ' + etiquetas[0] + '\n')
        self.f.write('label ' + etiquetas[1] + '\n')
        self.isFuncion = 0
    
    def visitDeffuncion(self, ctx:compiladoresParser.DeffuncionContext):
        if ctx.getChild(1).getChild(0).getText() != 'main':
            self.inFuncion = 1
            etiquetas = self.labels.etiqueta_funcion(ctx.getChild(1).getChild(0))
            self.f.write('label ' + etiquetas[0] + '\n')
            if ctx.getChild(1).getChild(2).getChildCount() != 0:
                self.visitArgumentos(ctx.getChild(1).getChild(2))
            self.f.write('pop ' + etiquetas[1] + '\n')
            self.visitInstrucciones(ctx.getChild(3))
            self.f.write('jmp ' + etiquetas[1] + '\n')
            self.inFuncion = 0
        else:
            self.visitInstrucciones(ctx.getChild(3))
        return
    
    def visitReturnfun(self, ctx:compiladoresParser.ReturnfunContext):
        if self.inFuncion == 1:
            if len(self.temporales) != 0:
                self.f.write('push ' + self.temporales.pop() + '\n')
            else:
                self.visitExp(ctx.getChild(1))
                self.f.write('push ' + self.temporales.pop() + '\n')
                
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        if ctx.getChild(0).getChildCount() != 0:
            self.visitInstruccion(ctx.getChild(0))
        else:
            self.visitInstrucciones(ctx.getChild(1))
    
    def visitIif(self, ctx:compiladoresParser.IifContext):
        self.visitCond(ctx.getChild(2))
        etiqueta1 = self.labels.next_etiqueta()
        self.f.write('ifn ' + self.temporales.pop() + 
                     ' jmp ' + etiqueta1 + '\n')
        self.visitBloque(ctx.getChild(4))
        if ctx.getChild(5) == None:
            self.f.write('label ' + etiqueta1 + '\n')
        else:
            etiqueta2 = self.labels.next_etiqueta()
            self.f.write('jmp ' + etiqueta2 + '\n')
            self.f.write('label ' + etiqueta1 + '\n')
            self.visitElse(ctx.getChild(5))
            self.f.write('label ' + etiqueta2 + '\n') 
            
    def visitElse(self, ctx:compiladoresParser.ElseContext):
        self.visitBloque(ctx.getChild(1))
    
    def visitIwhile(self, ctx:compiladoresParser.IwhileContext):
        etiqueta1 = self.labels.next_etiqueta()
        self.f.write('label ' + etiqueta1 + '\n')

        etiqueta2 = self.labels.next_etiqueta()
        self.visitCond(ctx.getChild(2))
        self.f.write('ifn ' + self.temporales.pop() +
                     ' jmp ' + etiqueta2 + '\n')
        self.visitBloque(ctx.getChild(4))
        self.f.write('jmp ' + etiqueta1 + '\n')
        self.f.write('label ' + etiqueta2 + '\n')
    
    def visitIfor(self, ctx:compiladoresParser.IforContext):
        etiqueta1 = self.labels.next_etiqueta()
        self.visitInit(ctx.getChild(2))
        self.f.write('label ' + etiqueta1 + '\n')
        
        etiqueta2 = self.labels.next_etiqueta()
        self.visitCond(ctx.getChild(4))
        self.f.write('ifn ' + self.temporales.pop() + ' jmp ' +
                     etiqueta2 + '\n')
        self.visitIter(ctx.getChild(6))
        self.visitBloque(ctx.getChild(8))
        self.f.write('jmp ' + etiqueta1 + '\n')
        self.f.write('label ' + etiqueta2 + '\n')
        
    
    
    def visitErrorNode(self, node):
        print("---- ERROR ----")
        return super().visitErrorNode(node)
    