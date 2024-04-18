print("Python desde cero en Español")
#--------------------------------------------------------------
print("Author @RoxDev")
print ("Puedes apoyar mis proyectos en:")

base_url = "https://paypal.me/belakiss?country.x=AR&locale.x=es_XC"
print(base_url)
#--------------------------------------------------------------
print("Operadores aritméticos: ")
#--------------------------------------------------------------

#* Operadores aritmeticos:
#* Los operadores aritméticos, son aquellos que
#* "manipulan" datos numéricos, tanto números enteros, 
#* así como números decimales también conocidos como reales. 

#* Estos operadores son los más sencillos de todos,
#* se utilizan para realizar operaciones aritméticas básicas,
#* como son: sumas, restas, multiplicaciones, divisiones, módulo
#* o residuo y exponenciales. 

#NOTE - Al igual que todos los lenguajes de programación,
#NOTE - Python también cuenta con los siguientes op arirméticos:

#NOTE - Suma (+), Resta(-), Multiplicación(*), 
#NOTE - Exponente(**), Módulo(%), División(/)

#--------------------------------------------------------------
numero_cero = 0
numero_uno =  1
numero_dos =  2
numero_tres = 3
numero_cuatro = 4
numero_cinco = 5
numero_seis = 6
numero_siete = 7
numero_ocho = 8
numero_nueve = 9
numero_diez = 10
#* SUMA
#NOTE - La suma o adición, es la reunión de dos o mas conjuntos
#NOTE - llamados "sumados" en un solo conjunto llamado "suma o total".
#NOTE - Su signo en Python es (+) y se coloca entre sumados. 

print("Suma")

resultado = numero_uno + numero_dos
print("El resultado de la suma es: " + str(resultado))
#--------------------------------------------------------------

#* RESTA
#NOTE - Es la operación contraria a la suma, y también recibe
#NOTE - el nombre de sustracción. La cuál consiste en extraer
#NOTE - o quitar de un nro mayor, otro menor. 
#NOTE - Su signo en Python es (-)

print("Resta")

resultado = numero_cuatro - numero_tres
print("El resultado de la resta es: " + str(resultado))
#--------------------------------------------------------------

#* MULTIPLICACIÓN
#NOTE - Es la operación matemática que consiste en hallar el
#NOTE - resultado de sumar un nro tantas veces como indique otro.
#NOTE - Su signo en Python es (*)

print("Multiplicación")

resultado = numero_cinco * numero_seis
print("El resultado de la multiplicación es: " + str(resultado))
#--------------------------------------------------------------

#* DIVISIÓN
#NOTE - Es una operación matemática que consiste en averiguar
#NOTE - cuántas veces un nro está contenido en otro nro.
#NOTE - Su signo en Python es (/)

print("División")

resultado= numero_seis / numero_dos
print("El resultado de la división es: " + str(resultado))
#--------------------------------------------------------------
#* EXPONENTE
#NOTE - La potenciación, es la operación matemática mediante la
#NOTE - cuál multiplicamos un número por si mismo las veces que
#NOTE - nos indique el exponente. 
#NOTE - Su respresentación en Python es (**)

print("Exponente o Potenciación")

resultado = numero_siete ** numero_ocho
print("El resultado de la potenciación es: " + str(resultado))
#--------------------------------------------------------------

#* MÓDULO
#NOTE - El módlo o resto, es la cantidad que sobra después de
#NOTE - efectuar una división, ess decir. es el valor que se 
#NOTE - obtiene cuando un nro no puede ser dividido exactamente 
#NOTE - por otro. Su signo en Python es (%)

print("Módulo")

resultado = numero_diez % numero_tres
print("El módulo o resto es: " + str(resultado))
#--------------------------------------------------------------
#* DIVISIÓN ENTERA

#NOTE - La división entera, es una operación que consiste en
#NOTE - obtener el valor entero de un nro, el cual resulte
#NOTE - de una división entre dos nros decimales o reales.abs
#NOTE - Su representación en Python es (//)

print("División entera")

resultado = numero_ocho // numero_dos
print("El resultado de la división entera es: " + str(resultado))
