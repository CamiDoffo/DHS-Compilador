import sys
import shutil  # <--- IMPORTANTE: Importar shutil
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha 
from Walker import Walker
from Optimizador import Optimizador

def main(argv):
    archivo = "input/opal.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    
    input_stream = FileStream(archivo, encoding='utf-8')
    lexer = compiladoresLexer(input_stream) 
    stream = CommonTokenStream(lexer) 
    parser = compiladoresParser(stream) 
    
    escucha = Escucha()
    parser.addParseListener(escucha)
    
    # Genera el árbol de sintaxis
    tree = parser.programa() 

    # TEMPORAL: Como no hay Escucha, forzamos el paso a True
    hay_errores_semanticos = escucha.error

    if not hay_errores_semanticos:
        print("=-"*20)
        print("\033[1;36m" + "--- Iniciando Generación de Código Intermedio ---" + "\033[0m")
        
        try:
            # 1. Generar Código Intermedio
            caminante = Walker()
            caminante.visit(tree)
            
            # Copiamos el código puro al archivo de trabajo del Optimizador
            shutil.copyfile("./output/CodigoIntermedio_Puro.txt", "./output/CodigoIntermedio.txt")
            
            print("\033[1;36m" + "--- Iniciando Optimización Iterativa (3 Pasadas) ---" + "\033[0m")
            
            # 2. Bucle de Optimización
            for i in range(3):
                print(f" -> Ejecutando Pasada {i+1}...")
                
                optimizador = Optimizador()
                
                # REINICIO FORZADO DE ARCHIVOS
                optimizador.src = open("./output/CodigoIntermedio.txt", "r")
                optimizador.dest = open("./output/CodigoIntermedioOptimizado.txt", "w")
                
                # Ejecutar lógica
                optimizador.optimizarCodigoIntermedio()
                
                # CERRAR ARCHIVOS
                optimizador.src.close()
                optimizador.dest.close()
                
                # COPIAR SALIDA A ENTRADA
                if i < 2: 
                    shutil.copyfile("./output/CodigoIntermedioOptimizado.txt", "./output/CodigoIntermedio.txt")
            
            print("\033[1;32m" + "--- Optimización Finalizada con Éxito ---" + "\033[0m")
            
        except Exception as e:
            print(f"\033[1;31mError fatal en el Walker/Optimizador: {e}\033[0m")
            # Esto imprime la línea exacta del error si algo falla
            import traceback
            traceback.print_exc()
            
    else:
        print("\033[1;31m"+"Ocurrio un error semantico. No se genero codigo intermedio"+"\033[0m")

if __name__ == '__main__':
    main(sys.argv)