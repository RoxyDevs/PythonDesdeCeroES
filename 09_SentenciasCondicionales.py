print("Python desde cero en Español")
#--------------------------------------------------------------
print("Author @RoxDev")
print ("Puedes apoyar mis proyectos en:")

base_url = "https://paypal.me/belakiss?country.x=AR&locale.x=es_XC"
print(base_url)
#--------------------------------------------------------------
print("Sentencias condicionales: ")
#--------------------------------------------------------------
#* Una sentencia condicional, es una intruccion o grupo de 
#* intrucciones, que se ejecutan cuando a un programa se le
#* establece una condición lógica. Al cumplirse dicha condición,
#* el programa ejecuta la instrucción que ha sido asignada a 
#* esta condición.

#NOTE - Las sentencias condicionales, nos ayudan a controlar la
#NOTE - toma de decisiones dentro de un programa, haciendo uso 
#NOTE - de la lógica. De esta manera, las sentencias condicionales
#NOTE - comprueban, si una condición es verdadera o falsa y con 
#NOTE - base a eso lleva a cabo una acción. En Python, la sintaxis
#NOTE - de las sentencias condicionales son las siguientes:
#*      SENTECIAS CONDICIONALES SIMPLES:
#*       if Condicion logica : 
#*       <-TAB-> intrucción 1  (debe ir con una tabulación)     
#*       <-TAB-> intrucción 2
#*       <-TAB-> intrucción 3
#--------------------------------------------------------------
"""  
                            INICIO
                              |
<-_____FALSO_____________<-CONDICIÓN->_______VERDADERO____->
|                                                          |
|                                                          |
|                                                     INTRUCCIÓN  
|                                                          |
|___->_______________________________________________<-____|
                              |
                             FIN 
                             
Ejemplo: 

1- (Comparación Verdadera):

num_uno = 5
if num_uno == 5 :
    print("El nro es cinco")
print ("Fin.")
--------------------------------------------------------------

2- (Comparación Falsa):

num_dos =10
if num_dos == 5:
    print("El nro es cinco")
print("Fin.")
"""
#--------------------------------------------------------------

print("Sistema para calcular el promedio de un alumno.")
nombre = input("Para comenzar, ¿cuál es tu nombre?: ")
apellido = input("Cuál es tu apellido?: ")
matematica = int(input(nombre + " ¿Cuál es tu calificación en matemáticas?: "))
quimica = int(input(nombre + "¿Cuál es tu nota de química?: "))
biologia = int(input(nombre +"¿Cuál es tu calificación en Biología?: "))

promedio = (matematica + quimica + biologia) / 3

if promedio >= 7 :
    print("¡Felicidades, ha aprobado! " + nombre + " " + apellido + "." + " Su promedio es: ", promedio)
print("El alumno no ha aprobado. Su promedio es: ", promedio)




    


