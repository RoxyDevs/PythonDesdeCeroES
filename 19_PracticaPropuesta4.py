#!SECTION "Práctica Propuesta 4:

#TODO - @Author RoxDev
#LINK - Github: https://github.com/RoxyDevs/PythonDesdeCeroES
#LINK - https://patreon.com/RoxFullstack?utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink
#LINK - LinkedIn: https://www.linkedin.com/in/roxdevs/
#NOTE - ===================================================================================

#!SECTION  Desarrollar una calculadora con las siguientes 
#!SECTION  características:

#!SECTION  1) La calculadora deberá ser capaz de calcular operaciones 
#!SECTION  de suma, resta, multiplicación, división, división entera, 
#!SECTION  exponente y módulo o resto.

#!SECTION  2) Deberá tener un menú de operaciones donde el usuario
#!SECTION  pueda elegir cual es la operación que desea ejecutar.  

#!SECTION  3) También deberá solicitar únicamente dos valores por 
#!SECTION  cada operación.  

#!SECTION  REQUERIMIENTOS INDISPENSABLES:

#!SECTION  El código de este programa deberá funcionar con una única 
#!SECTION  variable que se llamará número, es decir, no se permite
#!SECTION  la implementación de otra variable. 

print("Calculadora con una sola varibale\n")

print("*********************")
print("* Menú de opciones: *")
print("*********************")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Exponente")
print("6. Módulo o resto \n")

numero = int(input("Introduce la opción deseada: "))

if numero == 1:
    print("Elegiste suma\n")
    numero = int(input("Introduce el primer número: "))
    numero = int(input("Introduce el segundo número: "))
    print("El resultado de la suma es: ", numero)

elif numero == 2:
    print("Elegiste resta\n")
    numero = int(input("Introduce el primer número: "))
    numero -= int(input("Introduce el segundo número: "))
    print("El resultado de la resta es: ", numero)

elif numero == 3:
    print("Elegiste multiplicación\n")
    numero = int(input("Introduce el primer número: "))
    numero *= int(input("Introduce el segundo número: "))
    print("El resultado de la multiplicación es: ", numero)

elif numero == 4:
    print("Elegiste división\n")
    numero = float(input("Introduce el primer número: "))
    numero /= float(input("Introduce el segundo número: "))
    print("El resultado de la división es: ", round(numero, 2))    

elif numero == 5:
    print("Elegiste División entera\n")
    numero = int(input("Introduce el primer número: "))
    numero //= int(input("Introduce el segundo número: "))
    print("El resultado de la división entera es: ", numero)

elif numero == 6:
    print("Elegiste exponente\n")
    numero = int(input("Introduce el primer número: "))
    numero **= int(input("Introduce el segundo número: "))
    print("El resultado de la exponente es: ", numero)

elif numero == 7:
    print("Elegiste módulo o resto\n")
    numero = int(input("Introduce el primer número: "))
    numero %= int(input("Introduce el segundo número: "))
    print("El módulo o resto es: ", numero)

else: 
    print("Opción no válida")
    