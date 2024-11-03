from antlr4 import ErrorNode, TerminalNode
from  compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Squeleton import *
# mientras se va creando el arbol, avanza
# para analisis semantico

# TODO ver donde cambiaria usado a true


class Escucha (compiladoresListener) :
    numTokens = 0 #tokens son las hojas
    numNodos = 0
    tabla = TablaSimbolos.get_instancia()
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("\t\tComienza la compilacion")

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("\t\tFin de la compilacion")
        # print("Se encontraron")
        # print("\tNodos: " + str(self.numNodos))
        # print("\tTokens: " + str(self.numTokens))
        print(self.tabla.__str__())
        self.tabla.mostrarVarsSinUsar()
        self.tabla.del_Contexto()
        
    
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("\t\tEnter WHILE")
        
    def exitIwhile(self, ctx: compiladoresParser.IwhileContext):
        self.tabla.add_contexto(ctx)
        print("\t\tFIN WHILE")
        # print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        # print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        print("\t\t Declaracion")
        
    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        # se solucionadoria con if anidado y llamando al buscar por separado en cada caso
        nombreVariable = ctx.getChild(1).getText()
        tipoDeDato = ctx.getChild(0).getText()
                # Si el nombre de la variable contiene un '=', tomamos solo la parte anterior
        if '=' in nombreVariable:
            nombreVariable = nombreVariable.split('=')[0].strip()  # Tomamos solo el nombre sin espacios

        variable = ID(nombreVariable, tipoDeDato)
        
        #Las busquedas si devuelven None es porque encontraron algo
        busquedaGlobal = self.tabla.buscar_global(nombreVariable)
        busquedaLocal = self.tabla.buscar_local(nombreVariable)
        
        if busquedaGlobal is None and busquedaLocal is None :
            #print('"'+nombreVariable+'"'+" no fue declarada previamente")
            self.tabla.add_identificador(variable)
        
        print("\033[1;32m" +"Nombre variable: " + nombreVariable+ "\033[0m")
        
    def enterIfor(self, ctx: compiladoresParser.IforContext):
        print("\t\tEnter FOR")
        
    def exitIfor(self, ctx: compiladoresParser.IforContext):
        self.tabla.add_contexto(ctx)
        print("\t\tFIN FOR")
        # print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        # print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterIif(self, ctx: compiladoresParser.IifContext):
        print("\t\tENTER IF")
    
    def exitIif(self, ctx: compiladoresParser.IifContext):
        self.tabla.add_contexto(ctx)
        print("\t\tEXIT IF")
        # print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        # print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterElse(self, ctx: compiladoresParser.ElseContext):
        print("\t\tENTER ELSE")
    
    def exitElse(self, ctx: compiladoresParser.ElseContext):
        self.tabla.add_contexto(ctx)
        print("\t\tEXIT del ELSE")
        # print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        # print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterFunciones(self, ctx: compiladoresParser.FuncionesContext):
        print("\t\tFUNCION")
        
    def exitFunciones(self, ctx: compiladoresParser.FuncionesContext):
        #Se agregan () para diferenciar de las variables y por si una funcion y una variable se llaman igual
        funcion = ID(ctx.getChild(1).getText()+"()", ctx.getChild(0).getText())
        self.tabla.add_identificador(funcion)
        print("\t" + ctx.getText())        
        
        
    def exitInic(self, ctx):
        nombreVariable = ctx.getChild(1).getText()
        # Si el nombre de la variable contiene un '=', extraemos solo el nombre
        if '=' in nombreVariable:
            nombreVariable = nombreVariable.split('=')[0].strip()

        # Chequear si existe en el contexto actual o global
        busquedaLocal = self.tabla.buscar_local(nombreVariable)
        busquedaGlobal = self.tabla.buscar_global(nombreVariable)
        tipoDeDato = ctx.getChild(0).getText()
        variable = ID(nombreVariable, tipoDeDato)

        # Si la variable no existe en ningún contexto, la inicializamos y agregamos
        if busquedaLocal is None and busquedaGlobal is None:
            print("\033[1;32m" +f"Se inicializó la variable '{nombreVariable}' en el contexto actual."+ "\033[0m")
            variable.set_inicializado()  # Marcar como inicializada
            self.tabla.add_identificador(variable)
        elif busquedaLocal is not None:
            print("\033[1;31m" +"ERROR SEMANTICO: La variable '" + nombreVariable + "' ya está declarada en el contexto local."+ "\033[0m")
        elif busquedaGlobal is not None:
            print("\033[1;31m" + "ERROR SEMANTICO: La variable '" + nombreVariable + "' ya está declarada en el contexto global."+ "\033[0m")

    def exitAsignacion(self, ctx):
        operacion = ctx.getChild(0).getText()
        # Verificar si el nombre de la variable de la izquierda contiene un '='
        if '=' in operacion:
            nombreVariableIzquierda = operacion.split('=')[0].strip()
            nombreVariableDerecha = operacion.split('=')[1].strip()

        busquedaLocalIzquierda = self.tabla.buscar_local(nombreVariableIzquierda)
        busquedaGlobalIzquierda = self.tabla.buscar_global(nombreVariableIzquierda)
        # Buscar la variable de la derecha en el contexto
        busquedaLocalDerecha = self.tabla.buscar_local(nombreVariableDerecha)
        busquedaGlobalDerecha = self.tabla.buscar_global(nombreVariableDerecha)
        
        # Verificar si el nombre de la variable de la derecha es un número
        if nombreVariableDerecha.isdigit():  # Si es un número
            print("\033[1;32m" +f"Se asignó el valor numérico '{nombreVariableDerecha}' a la variable '{nombreVariableIzquierda}'."+ "\033[0m")
            # Aquí no se necesita verificar si la variable izquierda está inicializada
            pass
        else:
            # Verificar que la variable de la derecha esté inicializada si existe
            if nombreVariableDerecha and (busquedaLocalDerecha is None and busquedaGlobalDerecha is None):
                print("\033[1;31m" + f"ERROR SEMANTICO: La variable '{nombreVariableDerecha}' no fue declarada previamente!"+ "\033[0m")
                return  # Salir si la variable derecha no existe
            elif nombreVariableDerecha:
                if busquedaLocalDerecha and not busquedaLocalDerecha.inicializado:
                    print("\033[1;31m" + f"ERROR SEMANTICO: La variable '{nombreVariableDerecha}' debe inicializarse antes de usarse en la asignación a '{nombreVariableIzquierda}'!"+ "\033[0m")
                    return
                elif busquedaGlobalDerecha and not busquedaGlobalDerecha.inicializado:
                    print("\033[1;31m" + f"ERROR SEMANTICO: La variable '{nombreVariableDerecha}' debe inicializarse antes de usarse en la asignación a '{nombreVariableIzquierda}'!"+ "\033[0m")
                    return
            # Verificar compatibilidad de tipos
                if busquedaLocalIzquierda:
                    tipoIzquierda = busquedaLocalIzquierda.tipoDato
                else:
                    if busquedaGlobalIzquierda is None:
                        print("\033[1;31m" + f"ERROR SEMANTICO: La variable '{nombreVariableIzquierda}' no fue declarada previamente."+ "\033[0m")
                        return
                    tipoIzquierda = busquedaGlobalIzquierda.tipoDato

                if busquedaLocalDerecha:
                    tipoDerecha = busquedaLocalDerecha.tipoDato
                else:
                    if busquedaGlobalDerecha is None:
                        print("\033[1;31m" + f"ERROR SEMANTICO: La variable '{nombreVariableDerecha}' no fue declarada previamente."+ "\033[0m")
                        return
                    tipoDerecha = busquedaGlobalDerecha.tipoDato

                # Ahora que ambas variables están verificadas, comprueba su compatibilidad
                if tipoIzquierda != tipoDerecha:
                    print("\033[1;33m" +f"Advertencia: No se puede asignar un valor de tipo '{tipoDerecha}' a una variable de tipo '{tipoIzquierda}'."+ "\033[0m")
                    return
        # Aquí ya se supone que la variable derecha está inicializada (si no es un número)
        # Puedes proceder a modificar la variable izquierda sin la verificación de inicialización
        if busquedaLocalIzquierda is not None or busquedaGlobalIzquierda is not None:
            print("\033[1;32m" +f"Se intenta modificar la variable '{nombreVariableIzquierda}' en el contexto {'local' if busquedaLocalIzquierda is not None else 'global'}."+ "\033[0m")
            if busquedaLocalIzquierda is not None:
                busquedaLocalIzquierda.set_usado()
            if busquedaGlobalIzquierda is not None:
                busquedaGlobalIzquierda.set_usado() 
        else:
            print("\033[1;31m" + f"ERROR SEMANTICO: La variable '{nombreVariableIzquierda}' no fue declarada previamente."+ "\033[0m")
            return


    def visitTerminal(self, node: TerminalNode):
        # print(" ---> Token: " + node.getText())
        self.numTokens += 1
        
    def visitErrorNode(self, node: ErrorNode):
        print("\033[1;31m" +" ERROR SINTACTICO"+ "\033[0m")
        print(node.getText())
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1
        