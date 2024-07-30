
#TODO - Propuesta Práctica Nro1:

# @Author RoxDev

#LINK - https://github.com/RoxyDevs/PythonDesdeCeroES/upload/main

#LINK - LinkedIn: https://www.linkedin.com/in/roxdevs/

#LINK - FigJam: https://www.figma.com/board/a3fJ6zMLzY6AdiAaBybRz0/Vacaciones-Rappi?node-id=0-1&t=pgHIyHzgV8Ejdi5V-0


#!SECTION           La compañía multinacional Rappi, solicita un sistema que determine  
#!SECTION           los días de vacaciones a los que tiene derecho un trabajador,  
#!SECTION           tomando en cuenta las siguientes características:

#!SECTION           Existen tres departamentos dentro de la compañía con sus 
#!SECTION           respectivas claves:

#!SECTION           Departamento de atención al cliente: (Clave 1)
#!SECTION           Departamento de logística: (Clave 2)
#!SECTION           Gerencia: (Clave 3)

#!SECTION ----------------------------------------------------------------------------
#!SECTION           ||TRABAJADORES CON CLAVE 1 (Atención al cliente)||
#!SECTION ----------------------------------------------------------------------------
#!SECTION          -Con 1 año de servicio, reciben 6 días de vacaciones.
#!SECTION          -Con 2 a 6 años de servicio, reciben 14 días de vacaciones.
#!SECTION          -A partir de 7 años de servicio, reciben 20 días de vacaciones. 

#!SECTION ----------------------------------------------------------------------------
#!SECTION          ||TRABAJADORES CON CLAVE 2 (Logística)||
#!SECTION ----------------------------------------------------------------------------
#!SECTION          -Con 1 año de servicio, reciben 7 días de vacaciones. 
#!SECTION          -Con 2 a 6 años de servicio, reciben 15 días de vacaciones. 
#!SECTION          -A partir de 7 años de servicio, 22 días de vacaciones.

#!SECTION ----------------------------------------------------------------------------
#!SECTION          ||TRABAJADORES CON CLAVE 3 (Gerencia)||
#!SECTION ---------------------------------------------------------------------------- 
#!SECTION          -Con 1 año de servicio, reciben 10 días de vacaciones. 
#!SECTION          -Con 2 a 6 años de servicio reciben 20 días de vacaciones. 
#!SECTION          -A partir de los 7 años de servicio, reciben 30 días de vacaciones. 
#!SECTION ----------------------------------------------------------------------------

#NOTE - ==============================================================================
#NOTE - Requirimientos indispensables:
#NOTE - ==============================================================================

#NOTE - El sistema debe solicitar eñ "Nombre", "Clave del departamento" y 
#NOTE - "Antigüedad" del trabajador desde el teclado. 
#NOTE - Posteriormente el programa debe mostrar un mensaje en pantalla, que contenga
#NOTE - el nombre del trabajador y los días de vacaciones que tiene derecho. 
#NOTE - ==============================================================================
🤖: I noticed a couple of indentation errors in your code. The `elif` statements under `clave_departamento == 2` are not properly indented. Here's the corrected code:

```python
print("*******************************************")
print("****Sistema de control vacacional Rappi****")
print("******************************************* \n")

nombre_empleado = input("Por favor, introduce el nombre del empleado: ")
clave_departamento = int(input("Por favor, introduce la clave del departamento: "))
antiguedad_empleado = float(input("Por favor, introduce los años laborados del empleado: "))

if clave_departamento == 1:
    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("El empleado", nombre_empleado, "tiene derecho a 6 días de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado", nombre_empleado, "tiene derecho a 14 días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado, "tiene derecho a 20 días de vacaciones.")
    else:
        print("El empleado", nombre_empleado, "aún NO tiene derecho a vacaciones.")

elif clave_departamento == 2:
    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("El empleado", nombre_empleado, "tiene derecho a 7 días de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado", nombre_empleado, "tiene derecho a 15 días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado, "tiene derecho a 22 días de vacaciones.")
    else:
        print("El empleado", nombre_empleado, "aún NO tiene derecho a vacaciones.")

elif clave_departamento == 3: 
    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("El empleado", nombre_empleado, "tiene derecho a 10 días de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado", nombre_empleado, "tiene derecho a 20 días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado, "tiene derecho a 30 días de vacaciones.")
    else:
        print("El empleado", nombre_empleado, "aún NO tiene derecho a vacaciones.")
