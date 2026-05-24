# Apartado importaciones
# Apartado funciones

# CARGA DE ARCHIVOS

def cargar_clientes():
    try:
        clientes = {}
        
        archivo = open("recursos/clientes.txt", "r")
        for linea in archivo:
            linea = linea.strip()
            if linea == "": continue      # saltar lineas vacias
            partes = linea.split(",")
            if len(partes) == 2:
                id_cliente = partes[0].strip()
                nombre     = partes[1].strip()
                clientes[id_cliente] = nombre

        archivo.close()
        return clientes
    except FileNotFoundError as ffe:
        raise FileNotFoundError(f"Error no se encuentra el archivo clientes.txt - {ffe}")
    except Exception as e:
        raise Exception(f"Error generico en la funcion division - {e}")

def cargar_eventos():
    try:
        eventos = []
        
        archivo = open("recursos/eventos.txt", "r")
        for linea in archivo:
            linea == linea.strip()
            if linea == "": continue
            partes = linea.split(",")
            if len(partes) == 6:
                evento = {
                    "id" : partes[0].strip(),
                    "nombre" : partes[1].strip(),
                    "tipo" : partes[2].strip(),
                    "ciudad" : partes[3].strip(),
                    "fecha" : partes[4].strip(),
                    "hora" : partes[5].strip()
                }
                eventos.append(evento)
        archivo.close()
        return eventos
    except FileNotFoundError as ffe:
        raise FileNotFoundError(f"Error no se encuentra el archivo clientes.txt - {ffe}")            
    except Exception as e:
        raise Exception(f"Error generico en la funcion division - {e}")
    
# LO QUE SE VA A VISUALIZAR

def mostrar_eventos(eventos):
        contador = 1
        print("\n ====== EVENTOS DISPONIBLES ======")
        
        for evento in eventos:
            print(f"{contador}. [ {evento["id"]} ] {evento["nombre"] } | {evento["tipo"]} | {evento["ciudad"]} | {evento["fecha"]} | {evento["hora"]}")
            contador = contador + 1
        print("=================================")
    
# Apartado principal
try:
    #datos de entrada
    id_ingreso = ""
    id_evento = ""
    #datos de salida
    nombre_cliente = ""
    #variables adicionales
    clientes = ""
    eventos = ""
    mensajeMenu = "\n====== MENU ======\n1: Ver eventos disponibles \n2: Comprar Boletas \n3: Salir \nElija una opcion: "
    opcionMenu = 0
    evento_elegido = ""
    
    # Proceso
    print("============================================")
    print("   BIENVENIDO AL SISTEMA DE VENTA BOLETAS  ")
    print("============================================")

    # Cargar datos al arrancar
    clientes = cargar_clientes()
    eventos  = cargar_eventos()
        
    # Verificacion si hay informacion en los documentos
    if len(clientes) == 0:
        print("No hay clientes registrados. Verifique clientes.txt")
        
    if len(eventos) == 0:
        print("No hay eventos disponibles. Verifique eventos.txt")
        
    # LOGIN
        
    id_ingreso = input("\nIngrese su ID de cliente: ").strip()
        
    if id_ingreso not in clientes:
        print("Error: el ID " + id_ingreso + "no esta registrado.")
        
    nombre_cliente = clientes[id_ingreso]
    print("\nBienvenido/a, " + nombre_cliente)
    
    while True:
        try:
            
            opcionMenu = int(input(mensajeMenu))
            if not (1 <= opcionMenu <= 4): 
                raise ValueError("Valor fuera de rango")
        except ValueError as ve:
            print(f"Opcion invalida: {ve}")
            continue

        if opcionMenu == 1:
            # Mostrar eventos 
            mostrar_eventos(eventos)
        
        elif opcionMenu == 2:
            # Comprar boletas 
            mostrar_eventos(eventos)
            id_evento = input("\nIngrese el ID del evento: ").strip()
            
            # Buscar el evento en la lista 
            for evento in eventos:
                if evento["id"] == id_evento:
                    evento_elegido = evento
                    print(f"Eventos: {evento_elegido["nombre"] (evento_elegido["tipo"])}")
                    break
                else:
                    print(f"ERROR: No se encontro el evento con ID {id_evento}")
                    continue
            
            # redirigir segun el tipo de evento
            tipo = evento_elegido["tipo"]
            if tipo == "Teatro" or tipo == "Deporte":
                pass
            elif tipo == "Concierto":
                pass
            else:
                print("ERROR: Tipo de evento desconocido: " + tipo)
        
        
        elif opcionMenu == 3:
            # Finalizar
            break
        

    #Cerrar documentos
    clientes.close()
    eventos.close()
        
except Exception as e:
    print(f"Error generico -> {e}")
else:
    print("Ejecución exitosa")
finally:
    print("Fin del programa")