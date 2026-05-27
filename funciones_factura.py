#apartado import
#apartado funciones
def cancelarCompra(id : int, avion):
    try:

        

        
        for fila in range(len(avion)):
            for columna in range(len(avion[fila])):
                if avion[fila][columna].find(id) != -1:
                    avion[fila][columna] = ""
                    return  avion

        return False, avion

    except Exception as e:
        raise Exception(f"Error en la funcion retirarVehiculo: {e}")



def compraBoleta(id:int, numeroAsiento:int,letraAsiento: str, avion):
    try:

        for fila in range(len(avion)):
            numeroAsiento-=1
            numeroColumna=0
            
            for columna in range(len(avion[numeroAsiento])):
                if letraAsiento == "A":
                        numeroColumna=0
                elif letraAsiento=="B":
                        numeroColumna=1
                elif letraAsiento =="C":
                        numeroColumna=2
                elif letraAsiento=="D":
                        numeroColumna=3
                
                if len(avion[numeroAsiento][numeroColumna]) == 0:
                        avion[numeroAsiento][numeroColumna] = id
                        return avion, True

        return avion, False

    except Exception as e:
        raise Exception(f"Error en la funcion ingresoVehiculo: {e}")




def crearAvion(fila : int , columna : int):
    try:

        celda = []

        avion = []

        for i in range(fila):
            
            for j in range(columna):
                celda.append("")
            
            avion.append(celda)

            celda = []

        return avion

    except Exception as e:
        raise Exception(f"Error en la funcion crearParqueadero: {e}")
#apartado principal
try: 
#datos entrada 
    cantidadAsientos=0
    
    idAsiento=0

#datos de salida
# Datos Salida
    avion = crearAvion(fila=7, columna=4)
    seleccion_asientos = False
    
#variables adicionales
    id=0
    mensajeMenu = "\n1: comprar boletas  \n2: cancelar reservas \n3: Visualizar estado del avion \n4: Salir \n: "
    opcionMenu = 0
    listaLetras=["A","B","C","D"]
    asientoSeparado=""
    numeroAsiento=0
    letraAsiento=""
    ySeparado=""
#proceso

    while True:
        try:
            opcionMenu = int(input(mensajeMenu))
            if not (1 <= opcionMenu <= 4): raise ValueError("Valor fuera de rango")
        except ValueError as ve:
            print(f"Opcion invalida: {ve}")
            continue
        if opcionMenu == 1:
            id+=1
            
            print("asientos disponibles")
            print("\n ======== \n")

            for fila in range(len(avion)):
                for columna in range(len(avion[fila])):
                    print(avion[fila][columna], end=" | ")
                print()

            print("\n ========")

            print(f"\nsu id en esta compra es: {id}\n")
            
            while True:
                try:
                    cantidadAsientos=int(input("ingrese la cantidad de asientos a seleccionar \n| solo se le permite seleciionar 4 asientos|\n:"))
                
                    if not (1 <= cantidadAsientos <= 4): raise ValueError("supero el limite establecido de 4 asietos")
                    else:break
                except ValueError as ve:
                    print(f"dato invalido: {ve}")
                    continue
                
            while True:
                try:
                    idAsiento=input(f"ingrese que asientos desea\n|selecionar asi Numero-LetraIDentificadora|\n|despues de selecionar uno serpar la selecion con (,)|\nletras->{listaLetras}\nnumeros[1-7]\n:").upper()
                    asientoSeparado=idAsiento.split(",")
                    if not(len(asientoSeparado)==cantidadAsientos): raise ValueError("los asientos selecionado no concuerdan con la cantidad dada anterior mente")
                    else:break
                except ValueError as ve:
                    print(f"dato invalido: {ve}")
                    continue
        
            for y in asientoSeparado:
                ySeparado=y.replace("",",").split(",")
            
                numeroAsiento=ySeparado[1]
                numeroAsiento=int(numeroAsiento)
                letraAsiento=ySeparado[2]
            
            
                avion,seleccion_asientos=compraBoleta(id,numeroAsiento,letraAsiento,avion)
                if seleccion_asientos == True: print("reserva exitosa")
                else: print("asiento ocupado porfavor elija otro")
            
        
        elif opcionMenu == 2:
        
            while True:
                seleccionID= input("Ingrese la placa del vehiculo: ")

                if seleccionID!=id: print("Placa invalida")
                else: break
            
            avion= cancelarCompra(id, avion=avion)

            if  seleccion_asientos == False: print("id no encontrado no encontrado")
            else: print("cancelado con exitos")
        
        
        elif opcionMenu==3:
            print("\n ======== \n")

            for fila in range(len(avion)):
                for columna in range(len(avion[fila])):
                    print(avion[fila][columna], end=" | ")
                print()

            print("\n ========")
                
        elif opcionMenu==4:
            break
            



except ValueError as ve:
    print(f"Error de valor -> {ve}")
except TypeError as te:
    print(f"Error de tipos de datos -> {te}")
except Exception as e:
    print(f"Error generico -> {e}")
else:
    print("Ejecución exitosa")
finally:
    print("Fin del programa")