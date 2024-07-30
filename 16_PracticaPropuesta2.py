
#!SECTION "Práctica Propuesta 2:

#TODO - @Author RoxDev
#LINK - Github: https://github.com/RoxyDevs/PythonDesdeCeroES
#LINK - https://patreon.com/RoxFullstack?utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink
#LINK - LinkedIn: https://www.linkedin.com/in/roxdevs/
#NOTE - ===================================================================================

#!SECTION   Desarrollar un programa que solicite un número entero desde teclado al usuario, 
#!SECTION   posteriormente, el programa deberá determinar e indicar a través de un mensaje, 
#!SECTION   si el número introducido es par o impar. 
#NOTE - ===================================================================================

#!SECTION  - Requerimientos indispensables:

#!SECTION  El mensaje deberá mostrar la frase el número es par o impar, 
#!SECTION  junto con el número que el usuario introdujo desde teclado,
#!SECTION  por ejemplo:
#!SECTION              * "El número 8 es par." 
#!SECTION              * "El número 5 es impar."
#NOTE - ====================================================================================  

print("******************************************************")
print("* Programa que determina si un número es par o impar *")
print("******************************************************\n")

numero = int(input("Por favor, introduce un número entero: "))

if numero % 2 == 0:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")

