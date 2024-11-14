import antlr4
from PythonToJavaLexer import PythonToJavaLexer
from PythonToJavaParser import PythonToJavaParser
from PythonToJavaConverter import PythonToJavaConverter

# creador: Alexander medina Noble
# Grupo: I7B



def convertir_py_a_java(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        codigo_python = archivo.read()

    flujo_entrada = antlr4.InputStream(codigo_python)
    lexer = PythonToJavaLexer(flujo_entrada)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = PythonToJavaParser(token_stream)
    arbol = parser.prog_main()

    convertidor = PythonToJavaConverter()
    walker = antlr4.ParseTreeWalker()
    walker.walk(convertidor, arbol)

    codigo_java = convertidor.codigo_java
    return codigo_java


# Lee el archivo con la función en Python y tradúcelo a Java
ruta_archivo = 'prueba.txt'
codigo_java = convertir_py_a_java(ruta_archivo)

# Guarda el código traducido a Java en un archivo de salida
with open('FuncionTraducida.java', 'w') as archivo_salida:
    archivo_salida.write(codigo_java)

print("La conversión a código Java se ha completado y se ha guardado en 'FuncionTraducida.java'.")
"""

# Modifications for `prueba.txt`
modified_prueba_txt = """
def calculo_simple(x, y, z):
    resultado = x + y * z
    return resultado

print(calculo_simple(10, 5, 1))
"""