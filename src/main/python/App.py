import sys
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
    input = FileStream(archivo)
    lexer = compiladoresLexer(input) #cuando encuentra algo parecido a una regla, devuelve un token
    stream = CommonTokenStream(lexer) #acumula esos tokens
    parser = compiladoresParser(stream) #pide mas tokens, hasta que termine o encuentre un error
    escucha = Escucha()
    parser.addParseListener(escucha)
    tree = parser.programa() #con el arbol vamos a crear el codigo intermedio
    # print(tree.toStringTree(recog=parser))
    # si hay algun error, debera detenerse la ejecucion y no se construira el codigo intermedio
    if not escucha.error:
        caminante = Walker()
        caminante.visit(tree)
        optimizador = Optimizador()
        optimizador.optimizarCodigoIntermedio()
    else:
        print("\033[1;31m"+"Ocurrio un error. No se genero codigo intermedio"+"\033[0m")
    

if __name__ == '__main__':
    main(sys.argv)