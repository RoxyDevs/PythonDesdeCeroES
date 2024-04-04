print("Python desde cero en Español")
#--------------------------------------------------------------
print("Author @RoxDev")
print ("Puedes apoyar mis proyectos en:")

base_url = "https://paypal.me/belakiss?country.x=AR&locale.x=es_XC"
print(base_url)
#--------------------------------------------------------------
print("Tema: Manipulación de cadenas de caracteres: ")
#--------------------------------------------------------------

#* Cadenas de caracteres:
#* Strings, es una serie de caracteres compuestas por letra,
#* números, signos y símbolos, que dentro de sus funciones, 
#* destaca la interacción de un programa con el usurario.
#* Dentro de las cuales se encuentran:

#* La asignación: Consiste en asignar una cadena de caracteres
#* a otra. 
#* Por el cual se utiliza el operador + y/o - 

#! Por ejemplo:
 
mensaje = "Hola"
mensaje +=" "
mensaje += "Programador, soy RoxDev. "
print(mensaje) 
#--------------------------------------------------------------

#* La concatenación: Es unir dos cadenas o más, para formar una
#* cadena de mayor tamaño. Por es necesario utilizar el operador +

#! Por ejemplo:

mensaje ="Hola"
espacio =" "
nombre ="RoxDev"

print("Concatenación: ")
print(mensaje + espacio + nombre)

#* Concatenación en una suma:
numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es:" + resultado)
#--------------------------------------------------------------

#* La búsqueda: Consiste en localizar dentro de una cadena, una
#* subcadena más pequeña a un carácter. Para lo cual es necesario
#* utilizar el método "find".

#! Por ejemplo:

mensaje = "Hola Programador"
buscar_subcadena = mensaje.find("Programador")
print(buscar_subcadena)
#-------------------------------------------------------------

#* La extracción: Se trata de sacar fuera de una cadena,
#* una porción de la misma según su posición dentro de ella.
#*  Para ello es necesario la posición a extraer [1:8]

#! Por ejemplo: 

mensaje= "Hola Programador/a"
extraer_subcadena= mensaje[1:8]
print(extraer_subcadena)
#--------------------------------------------------------------

#* La comparación: Se utiliza para comparar dos cadenas de caracteres.
#* Para ello se utiliza el operador ==

#! Por ejemplo:

mensaje_uno= "Hola"
mensaje_dos= "Hola"

mensaje_uno==mensaje_dos
