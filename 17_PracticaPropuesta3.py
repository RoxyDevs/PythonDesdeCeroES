

#!SECTION "Práctica Propuesta 3:

#TODO - @Author RoxDev
#LINK - Github: https://github.com/RoxyDevs/PythonDesdeCeroES
#LINK - https://patreon.com/RoxFullstack?utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink
#LINK - LinkedIn: https://www.linkedin.com/in/roxdevs/
#NOTE - ===================================================================================

#!SECTION   Desarrollar un programa que solicite tres números entero desde teclado al usuario, 
#!SECTION   posteriormente, el programa deberá determinar e indicar a través de un mensaje, 
#!SECTION   cuál de los tres números es el más grande. 
#NOTE - ===================================================================================

#!SECTION  - Requerimientos indispensables:

#!SECTION  El mensaje deberá mostrarel número que resultó ser el más grande de los tres, 
#!SECTION  por ejemplo:
#!SECTION              * "El número 10 es el más grande de los tres." 

#NOTE - ====================================================================================  

print("***************************************************************")
print("* Programa que determina cuál es el número mar grande o mayor *")
print("***************************************************************\n")

num_uno = int(input("Introduce el primer número: "))
num_dos = int(input("Introduce el seguro número: "))
num_tres = int(input("Introduce el tercer número: "))

if num_uno > num_dos and num_uno > num_tres:
    print("El número ", num_uno, " es el número más grande de los tres.")
else:
    if num_dos > num_tres: 
        print("El número ", num_dos, "es el número más grande de los tres.")
    else:
        print("El número ", num_dos, "es el número más grande de los tres.")
    