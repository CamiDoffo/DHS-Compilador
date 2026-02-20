import sys
import shutil  # <--- IMPORTANTE: Importar shutil
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha
from Walker import Walker
from Optimizador import Optimizador

def main(argv):
    archivo = "input/prueba_final.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo, encoding='utf-8')
    lexer = compiladoresLexer(input) 
    stream = CommonTokenStream(lexer) 
    parser = compiladoresParser(stream) 
    escucha = Escucha()
    parser.addParseListener(escucha)
    tree = parser.programa() 

    if not escucha.error:
        # 1. Generar Código Intermedio (Primera vez)
        caminante = Walker()
        caminante.visit(tree)
        
        print("\033[1;36m" + "--- Iniciando Optimización Iterativa (3 Pasadas) ---" + "\033[0m")
        
        # 2. Bucle de Optimización
        for i in range(3):
            print(f" -> Ejecutando Pasada {i+1}...")
            
            optimizador = Optimizador()
            
            # REINICIO FORZADO DE ARCHIVOS: 
            # forzamos que los abra de nuevo para leer la versión actualizada.
            optimizador.src = open("./output/CodigoIntermedio.txt", "r")
            optimizador.dest = open("./output/CodigoIntermedioOptimizado.txt", "w")
            
            # Ejecutar lógica
            optimizador.optimizarCodigoIntermedio()
            
            # CERRAR ARCHIVOS:
            # Es vital cerrarlos antes de copiar para asegurar que se guardó todo.
            optimizador.src.close()
            optimizador.dest.close()
            
            # COPIAR SALIDA A ENTRADA:
            # El archivo 'Optimizado' ahora pasa a ser el 'Normal' para la siguiente vuelta.
            if i < 2: # No es necesario copiar en la última vuelta, pero mal no hace.
                shutil.copyfile("./output/CodigoIntermedioOptimizado.txt", "./output/CodigoIntermedio.txt")
        
        print("\033[1;32m" + "--- Optimización Finalizada con Éxito ---" + "\033[0m")
        
    else:
        print("\033[1;31m"+"Ocurrio un error. No se genero codigo intermedio"+"\033[0m")
    

if __name__ == '__main__':
    main(sys.argv)