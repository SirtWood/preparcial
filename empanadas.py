""" 1- Permitir que un admin ingrese una empanada, para ingresarlo se debe tener en cuenta que tiene id, nombre, precio, popularidad, fecha de vencimiento. """

""" 2- Mostrar todas las empanadas registradas. """

""" 3- Permitir que el usuario busque las empanadas por ID. """

""" 4- Editar una empanada por ID, editar precio. """
""" 5- Eliminar una empanada por ID """
""" 6- Si preciono 0 que termine el programa. """

empanadas = []
opcion = 1

while (opcion != 1):
    print("---Empanadas Iguanodrillo---")
    print("---Opcion 1 = Ingresar una empanada---")
    print("---Opcion 2 = Mostrar las empanadas---")
    print("---Opcion 3 = Buscar una empanada---")
    print("---Opcion 4 = Editar una empanada---")
    print("---Opcion 5 = Eliminar una empanada---")
    print("---Opcion 0 = Salir---")
    opcion = int(input("Ingrese opcion: "))
    if(opcion == 1):
        empanada = {}
        empanada['id'] = int(input("Ingrese id de la empanada: "))
        empanada['nombre'] = input("Ingrese nombre de la empanada: ")
        empanada['valor'] = float(input("Ingrese valor de la empanada: "))
        empanada['popularidad'] = int(input("Ingrese popularidad de la empanada: "))
        empanada['fechaVencimiento'] = input("Ingrese popularidad de la empanada: ")
        empanadas.append(empanada)
        print("Empanada registrada.")

    elif(opcion == 2):
        for empanada in empanadas:
            print(empanada)
    elif(opcion == 3):
        buscarEmp = int(input("Ingrese id de empanada a buscar: "))
        for empanada in empanadas:
            if (empanada['id'] == buscarEmp):
                print(f"Empanada {empanada}")
        print('No se encontró la empanada.')
    elif(opcion == 4):
        buscarEmp = int(input("Ingrese id de empanada a buscar: "))
        for empanada in empanadas:
            if (empanada['id'] == buscarEmp):
                print(f"El valor actual de la empanada es: {empanada['precio']}")
                precioNuevo=float(input("Digita nuevo precio: "))
                empanada["precio"]=precioNuevo
        print("No se encontró la empanada")
    elif(opcion == 5):
        buscarEmp = int(input("Ingrese id de empanada a buscar: "))
        for empanada in empanadas:
            if (empanada['id'] == buscarEmp):
                empanadas.remove(empanada['id'])
                print(f"La empanada fue eliminada exitosamente")
        print("No se encontró la empanada")
    elif(opcion == 0):
        break
    else:
        print("opción invalida.")
    

