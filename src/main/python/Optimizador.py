import re

class Optimizador:
    def __init__(self):
        self.src = None
        self.dest = None
        self.variables = dict()

    def optimizarCodigoIntermedio(self):
        print("=-"*20)
        print('--- Comenzando optimizacion ---')
        
        self.src.seek(0)
        
        for linea in self.src:
            linea = linea.strip()
            if not linea: continue
            
            partes = linea.split()
            opcode = partes[0]

            # 1. LABELS (Puntos de entrada)
            if opcode == 'label':
                # ¡CRÍTICO! Al entrar a una etiqueta (bucle o función), 
                # no sabemos el estado de las variables, así que borramos la memoria.
                self.variables.clear() 
                self.dest.write(linea + '\n')

            # 2. JUMPS INCONDICIONALES
            elif opcode == 'jmp':
                self.dest.write(linea + '\n')

            # 3. POP (Invalida constantes)
            elif opcode == 'pop':
                var_destino = partes[1]
                if var_destino in self.variables:
                    del self.variables[var_destino]
                self.dest.write(linea + '\n')

            # 4. PUSH (Propagación)
            elif opcode == 'push':
                arg = partes[1]
                if arg in self.variables:
                    arg = self.variables[arg]
                self.dest.write(f"push {arg}\n")

            # 5. IFN (CORREGIDO: ifn 0 -> jmp / ifn 1 -> nada)
            elif opcode == 'ifn':
                condicion = partes[1]
                label = partes[3]

                if condicion in self.variables:
                    condicion = self.variables[condicion]

                # --- LÓGICA CORREGIDA ---
                # 'ifn X' significa 'Jump if Not True' (Salta si es Falso/0)
                
                # Caso A: La condición es 0 (FALSO) -> DEBE SALTAR SIEMPRE
                if condicion == '0':
                    self.dest.write(f"jmp {label}\n")
                    
                # Caso B: La condición es distinta de 0 (VERDADERO) -> NUNCA SALTA
                # Borramos la línea porque el flujo sigue recto.
                elif condicion.replace('.','',1).isdigit() and float(condicion) != 0:
                    continue 
                    
                # Caso C: Variable desconocida -> Escribimos la instrucción normal
                else:
                    self.dest.write(f"ifn {condicion} jmp {label}\n")

            # 6. ASIGNACIONES
            elif '=' in linea:
                lado_izq = partes[0]
                lado_der_str = linea.split('=', 1)[1].strip()
                
                # Reemplazo de variables en la derecha
                tokens_der = re.split(r'(\+|-|\*|/|%|>|<|==|>=|<=)', lado_der_str)
                nuevo_lado_der = []
                
                for token in tokens_der:
                    token = token.strip()
                    if not token: continue
                    if token in self.variables:
                        nuevo_lado_der.append(str(self.variables[token]))
                    else:
                        nuevo_lado_der.append(token)
                
                lado_der_procesado = " ".join(nuevo_lado_der)

                # Intentar resolver matemáticas
                valor_final = lado_der_procesado
                es_constante = False

                if re.match(r'^[0-9+\-*/%(). <>=]+$', lado_der_procesado):
                    try:
                        resultado = eval(lado_der_procesado)
                        if isinstance(resultado, bool):
                            resultado = 1 if resultado else 0
                        valor_final = str(resultado)
                        es_constante = True
                    except:
                        pass

                # Guardar conocimiento
                if es_constante:
                    self.variables[lado_izq] = valor_final
                else:
                    if lado_izq in self.variables:
                        del self.variables[lado_izq]

                # Escritura inteligente
                if es_constante and lado_izq.startswith('temp'):
                    continue # Propagamos temporales constantes
                else:
                    self.dest.write(f"{lado_izq} = {valor_final}\n")

            else:
                self.dest.write(linea + '\n')

        print('Todas las variables han sido procesadas')
        print("\033[1;32m"+'--- Optimizacion completada ---'+"\033[0m")