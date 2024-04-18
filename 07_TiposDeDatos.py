print("Python desde cero en Español")
#--------------------------------------------------------------
print("Author @RoxDev")
print ("Puedes apoyar mis proyectos en:")

base_url = "https://paypal.me/belakiss?country.x=AR&locale.x=es_XC"
print(base_url)
#--------------------------------------------------------------
print("Tipos de datos: ")
#--------------------------------------------------------------
#NOTE - En programación, un tipo de dato, es un atributo de los datos 
#NOTE - que indica a la computadora y al programador, sobre
#NOTE - la clase de datos que se va a manejar: 

#*      1) Enteros y Largos

""" 
    Los números enteros, son aquellos que no tienen decimales,
    tanto positivos como negativos. En Python se pueden representar 
    mediante el tipo int (entero) o el tipo long (largo)
"""

numero = 15
print("El valor es: " + numero, type(numero))
 
#--------------------------------------------------------------

#* 2) Flotantes o Reales
"""
    Los nros flotantes o reales, son los que tienen decimales,
    tantos positivos como negativos. En Python se expresan mediante 
    el tipo float (flotante)
 """
 
numero_flotante = 15.5
print("El número florante es: " + numero_flotante, type(numero_flotante))
 #--------------------------------------------------------------

#*3) Números Complejos
""" 
    Los nros complejos son aquellos que tienen una parte real y
    una parte imaginaria. La mayor parte de lenguajes de programación
    carecen de este tipo, aunque sea muy utilizado por ingenieros
    y científicos en general. En Python se expresa mediante el
    tipo complex. 
"""
numero_complejo = 5 + 6j
print("El nro complejo es:" + numero_complejo, type(numero_complejo))
#--------------------------------------------------------------

#* Cadenas
"""
Las cadenas o también conocidas como Strings, mismas que ya hemos 
estudiado anteriormente, no son mas que texto encerrado entre
comillas simples ('cadena') o dobles ("cadena"). También es posible 
encerrar una cadena entre triples comillas (simples o dobles)

De esta forma podremos escribir el texto en carias líneas,
y al imprimir la cadena, se representan los saltos de línea
que introdujimos sin tener que recurrir al carácter \n. 
"""
nombre = "RoxDev"
print("La cadena es : "+ nombre, type(nombre))
#--------------------------------------------------------------

#* Booleanos
"""
   El tipo Booleano, sólo puede tener dos valores: True(cierto) 
   y False(Falso). Estos valores son especialmente importantes
   para las expresiones condicionales y los bucles, mismos que 
   ya estudiaremos en videos posteriores. En Python se expresan 
   mediante el tipo bool.        
"""
verdadero_falso = 3 == 3
print("El booleano es : "+ verdadero_falso, type(verdadero_falso))
#--------------------------------------------------------------

