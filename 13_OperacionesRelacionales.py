#NOTE - Las sentencias condicionales anidadas, se presentan 
#NOTE - cuando por el camino de verdadero o falso de una 
#NOTE -  sentencia condicional hay otra sentencia condicional.

#NOTE - Cuando trabajamos sentencias condicionales simples,
#NOTE - compuestas o múltiples, podemos colocar dentro de la/s 
#NOTE - instrucción/es a ejecutar de cada una de estas sentencias,
#NOTE - otra sentencia condicional. 

print("Introduce dos números a comparar:\n")

num_uno = int(input("Introduce el primer número: "))
num_dos = int(input("Introduce el segundo número: "))

print("\n Los números a comparar son: ", num_uno, " y ", num_dos, "\n")

if num_uno == num_dos:
    print("Es igual...")
if num_uno != num_dos:
    print("Es diferente...")
if  num_uno < num_dos:
    print(" Es menor...")
if num_uno > num_dos:
    print(" Es mayor...")
if num_uno <= num_dos:
    print("Es menor o igual...")
if num_uno >= num_dos:
    print("Es mayor o igual...")
