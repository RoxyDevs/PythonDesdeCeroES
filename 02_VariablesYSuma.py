print("Python desde cero en Español")
#--------------------------------------------------------------
print("Author @RoxDev")
print ("Puedes apoyar mis proyectos en:")

base_url = "https://paypal.me/belakiss?country.x=AR&locale.x=es_XC"
print(base_url)
#--------------------------------------------------------------
print("Tema: Variables: ")

# ¿Qué es una variable?:
#                       Es un espacio en memoria donde se guardan
#  y recuperan los datos que utiliza un programa.
# Cada variable debe tener un nombre, con el cual se podrá 
# identificar y referirse a ella, durante el desarrollo de 
# un programa.
#                       En Python una variable no puede coincidir
# con los nombres de los comandos asignados a éste lenguaje de 
# programación, además no deberá contener espacios en blancos.
# Por ejemplo: una variable no podría llamarse "print", 
# ya que este es uno de los comandos asignados por Python 
# para imprimir o mostrar por consola.
#
# En Python hay dos tipos de variables, las mas comunes
# son: 
#     * Variables que almacenan números,
#     * Variables que almacenan texto.
#--------------------------------------------------------------

# Definición de una variable numérica (entero)
numero1 = 2
numero2 = 2.5

# Definición de una variable de texto (string)
texto1 = "Esto es un texto"
texto2 = 'Esto es otro texto'

# Imprimimos los valores de las variables
print("Número 1:", numero1)
print("Número 2:", numero2)
print("Texto 1:", texto1)
print("Texto 2:", texto2)

# Ejemplo de suma con variables numéricas
print("Esto es un ejemplo de suma: ")
numero_uno = 2
numero_dos = resultado = numero_uno + numero_dos
print(resultado)