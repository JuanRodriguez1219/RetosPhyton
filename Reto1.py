instructores=[]
seguir="s" 
def agregar():
    instructores.append(input("Escriba el nombre del instructor que va a agregar \n"))
def listar():
    for i,e in enumerate(instructores):
           print("En la posición ",i," se encuentra ",e)
def modificar():
    for i,e in enumerate(instructores):
        print("En la posición ",i," se encuentra ",e)
    a=int(input("Ingresa la posición del instructor que deseas modificar\n"))
    instructores[a]=input("Ingrese el nombre del instructor\n")
def borrar():
    for i,e in enumerate(instructores):
        print("En la posición ",i," se encuentra ",e)
    p=int(input("Escriba la posicion del instructor que desea borrar: \n")) 
    del instructores[p]
def buscar():
    nombre=input("Ingrese el nombre del instructor que desea buscar: ")
    nombre = nombre.lower()
    encontrado = False
    for nombre1 in instructores:
        nombre1 = nombre1.lower()
        if nombre1 == nombre:
            encontrado = True
            break
    if encontrado:
        print(f"El intructor {nombre}, fue encontrado en la lista.")
    else:
        print(f"El instructor {nombre}, no fue encontrado en la lista.")
def organizar():
    instructores.sort()
    for i,e in enumerate(instructores):
        print("En la posición ",i," se encuentra ",e)
        

while seguir=="s" or "S":
    menu=int(input("Ingrese la opción que va a ejecutar \n1. Insertar nombre de instructor \n2.Listar los instructores \n3.Modificar algún instructor \n4.Borrar un elemento de la lista \n5.Buscar instructor \n6.Ordenar la lista de forma ascendente \n"))
    if menu==1:
        agregar()
    elif menu==2:
        listar()
    elif menu==3:
        modificar()
    elif menu==4:
        
        borrar()
    elif menu==5:
        buscar() 
    elif menu==6:
        organizar()
    else:
        print("Opción Erronea")
    seguir=input("Escriba s o S para seguir en su lista \n")