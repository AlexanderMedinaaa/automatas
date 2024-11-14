from PythonToJavaListener import PythonToJavaListener
from PythonToJavaParser import PythonToJavaParser

class PythonToJavaConverter(PythonToJavaListener):
    def __init__(self):
        self.codigo_java = ""
        self.codigo_funciones = ""

    def enterProg_main(self, ctx: PythonToJavaParser.Prog_mainContext):
        # Clase principal y el main
        self.codigo_java += "public class Main {\\n"
        self.codigo_java += "    public static void main(String[] args) {\\n"

    def exitProg_main(self, ctx: PythonToJavaParser.Prog_mainContext):
        # Funciones fuera del main
        self.codigo_java += "    }\\n"
        self.codigo_java += self.codigo_funciones
        self.codigo_java += "}\\n"

        # Imprimir el código completo de Java generado
        print("Código en Java generado:")
        print(self.codigo_java)

    def enterDefine_funcion(self, ctx: PythonToJavaParser.Define_funcionContext):
        # Definir las funciones fuera del método main
        nombre_funcion = ctx.NOMBRE().getText()
        parametros = ', '.join([f"int {param.getText()}" for param in ctx.parametros().NOMBRE()])
        self.codigo_funciones += f"    public static int {nombre_funcion}({parametros}) " + "{\\n"
        print(f"Función '{nombre_funcion}' detectada con parámetros: {parametros}")

    def exitDefine_funcion(self, ctx: PythonToJavaParser.Define_funcionContext):
        # Cerrar la definición de la función
        self.codigo_funciones += "    }\\n"
        print(f"Función '{ctx.NOMBRE().getText()}' cerrada.")

    def enterAsignacion_var(self, ctx: PythonToJavaParser.Asignacion_varContext):
        nombre_variable = ctx.NOMBRE().getText()
        expresion = ctx.expresion().getText()
        self.codigo_funciones += f"        int {nombre_variable} = {expresion};\\n"
        print(f"Asignación detectada: {nombre_variable} = {expresion}")

    def enterRetorno(self, ctx: PythonToJavaParser.RetornoContext):
        expresion = ctx.expresion().getText()
        self.codigo_funciones += f"        return {expresion};\\n"
        print(f"Sentencia de retorno detectada: return {expresion}")

    def enterImprimir(self, ctx: PythonToJavaParser.ImprimirContext):
        # Captura el texto completo de la expresión dentro del print
        expresion_texto = ctx.getText().replace("print(", "").rstrip(")")

        # Construye la instrucción println en Java con el texto capturado
        self.codigo_java += f"        System.out.println({expresion_texto}));\\n"
        print(f"Sentencia de impresión detectada: print({expresion_texto})")
