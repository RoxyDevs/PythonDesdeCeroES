print(" ")
print("Python desde cero en Español")
print(" ")
#--------------------------------------------------------------
print("Author @RoxDev")
print(" ")
print ("Puedes apoyar mis proyectos en:")

base_url = "https://paypal.me/belakiss?country.x=AR&locale.x=es_XC"
print(base_url)
print(" ")
#--------------------------------------------------------------
print("Sentencias condicionales múltiples): ")
print(" ")
#--------------------------------------------------------------
#NOTE - Las sentencias condicionales anidadas, se presentan
#NOTE - cuando por el cambio de verdadero o falso de una
#NOTE - sentencia condicional hay otra sentencia condicional.

#NOTE - Es decir, cuando trabajamos con sentencias condicionales
#NOTE - simples, compuestas o múltiples, podemos colocar dentro
#NOTE - de la instrucción/es a ejecutar de cada una de estas 
#NOTE - sentencias, otra sentencia condicional.
#NOTE - En conclusión, las sentencias condicionales anidadas
#NOTE - consisten en tener una instrucción condicional dentro
#NOTE - de otra y dependiendo de si la condición de la primera
#NOTE - sentencia condicional se cumple o no se cumple, se
#NOTE - ejecutará otra sentencia condicional.

#NOTE - De esta manera, tendremos una condición dentro de otra
#NOTE - condición, ampliando la cantidad de opcioness para que
#NOTE - nuestros programas puedan resolver un problema, sin 
#NOTE - importar la cantidad de situaciones que se presenten.
#--------------------------------------------------------------
#NOTE - \n es salto de línea

print("=========")
print("Conversor")
print("=========\n")

print("Menú de opciones: \n")
print("Presiona 1 para convertir de número a palabra.")
print("Presiona 2 para convertir de palabra a número. \n")

opcion = int(input("Cual es la opción deseada?: "))
if opcion == 1:
    print("\n Conversor de número a palabra. \n")
    opcion_uno=int(input("¿Cuál es el nro que deseas convertir a palabra: "))
    if opcion_uno ==1:
        print("El nro es 'UNO'.")
    elif opcion_uno ==2:
        print("El nro es 'DOS'")
    elif opcion_uno ==3:
        print("El nro es 'TRES'") 
    elif opcion_uno ==4:
        print("El nro es 'CUATRO'")
    elif opcion_uno ==5:
        print("El nro es 'CINCO'")
    else:
        print("El nro seleccionado no está regisrado. ")    
elif opcion ==2:
    print("\n Conversor de palabra a número. \n")
    opcion_dos = input("¿Cuál es la palabra que deseas convertir a nro?: ")
    
    if opcion_dos == "uno":
        print("El nro es '1'")
    elif opcion_dos == "dos":
        print("El nro es '2'")
    elif opcion_dos == "tres":
        print("El nro es '3'")
    elif opcion_dos == "cuatro":
        print("El nro es '4'")
    elif opcion_dos == "cinco":
        print("El nro es '5'") 
    else: 
        print("El nro seleccionado no está registrado. ")       
else:
    print("\n La opción no es válida. \n")
print("Fin.")



