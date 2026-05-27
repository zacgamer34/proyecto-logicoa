# Apartado importaciones
# Apartado funciones:


# CARGA DE ARCHIVOS

# BLOQUE 1 - CARGA DE ARCHIVOS

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
                nombre     = partes[1].strip() #Manejo por listas 
                clientes[id_cliente] = nombre

        archivo.close()
        return clientes
    except FileNotFoundError as ffe:
        raise FileNotFoundError(f"Error no se encuentra el archivo clientes.txt - {ffe}")
    except Exception as e:
        raise Exception(f"Error generico en la funcion cargar_clientes - {e}")

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
                    "tipo" : partes[2].strip(),    # Manejo por diccionario
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
        raise Exception(f"Error generico en la funcion cargar_eventos - {e}")
    
#BLOQUE 2 - FUNCIONES DE VISUALIZACION

def mostrar_eventos(eventos):
        contador = 1
        print("\n ====== EVENTOS DISPONIBLES ======")
        
        for evento in eventos:
            print(f"{contador}. [ {evento["id"]} ] {evento["nombre"] } | {evento["tipo"]} | {evento["ciudad"]} | {evento["fecha"]} | {evento["hora"]}")
            contador = contador + 1
        print("=================================")
        
def cargar_precios_deporte():
    try:
        precios = []
        archivo = open("recursos/precios_evento[EVT-1001].txt", "r")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split(",")
            if len(partes) == 3:
                rango = partes[0].strip()          # ej: "1-3"
                zona  = partes[1].strip()          # ej: "VIP"
                precio = float(partes[2].strip())  # ej: 300.0

                # separar el rango "inicio-fin"
                extremos = rango.split("-")
                inicio = int(extremos[0])
                fin    = int(extremos[1])

                # asignar el mismo precio a cada fila del rango
                for num_fila in range(inicio, fin + 1):
                    precios[num_fila] = {"zona": zona, "precio": precio}
        archivo.close()
        return precios
    except FileNotFoundError as ffe:
        print(f"Error no se encontro el archivo de precios - {ffe}")

def cargar_precios_teatro():
    try:
        precios = []
        archivo = open("recursos/precios_evento[EVT-1002].txt", "r")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split(",")
            if len(partes) == 3:
                rango = partes[0].strip()          # ej: "1-3"
                zona  = partes[1].strip()          # ej: "VIP"
                precio = float(partes[2].strip())  # ej: 300.0

                # separar el rango "inicio-fin"
                extremos = rango.split("-")
                inicio = int(extremos[0])
                fin    = int(extremos[1])

                # asignar el mismo precio a cada fila del rango
                for num_fila in range(inicio, fin + 1):
                    precios[num_fila] = {"zona": zona, "precio": precio}
        archivo.close()
        return precios 
    except FileNotFoundError as ffe:
        print(f"Error no se encontro el archivo de precios - {ffe}")
        
def cargar_precios_concierto():
    try:
        precios = []
        archivo = open("recursos/precios_evento[EVT-1003].txt", "r")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split(",")
            if len(partes) == 3:
                zona         = partes[0].strip()
                cupos_totales = int(partes[1].strip())
                precio        = float(partes[2].strip())
                precios[zona] = {"cupos_totales": cupos_totales, "precio": precio}
        archivo.close()
        return precios 
    except FileNotFoundError as ffe:
        print(f"Error no se encontro el archivo de precios - {ffe}")
        
def cargar_mapa_deporte():
    try:
        mapa = []
        archivo = open("recursos/mapa_evento[EVT-1001].txt", "r")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            celdas = linea.split(",")
            fila = []
            for celda in celdas:
                fila.append(celda.strip())
            mapa.append(fila)
        archivo.close()
        return mapa
    except FileNotFoundError as ffe:
        print(f"Error no se encontro el archivo de precios - {ffe}")

def cargar_mapa_teatro():
    try:
        mapa = []
        archivo = open("recursos/mapa_evento[EVT-1002].txt", "r")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            celdas = linea.split(",")
            fila = []
            for celda in celdas:
                fila.append(celda.strip())
            mapa.append(fila)
        archivo.close()
        return mapa
    except FileNotFoundError as ffe:
        print(f"Error no se encontro el archivo de precios - {ffe}")  

def cargar_mapa_concierto():
    try:
        mapa = []
        archivo = open("recursos/mapa_evento[EVT-1003].txt", "r")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split(",")
            if len(partes) == 2:
                zona   = partes[0].strip()
                cupos  = int(partes[1].strip())
                mapa[zona] = cupos
        archivo.close()
        return mapa
    except FileNotFoundError as ffe:
        print(f"Error no se encontro el archivo de precios - {ffe}")
        
# BLOQUE 3 - GUARDAR / ACTUALIZAR ARCHIVOS
        
def guardar_factura(id_cliente, evento_id, boletas_compradas, total):
    try:
        nombre_archivo = "factura_" + id_cliente + "_" + evento_id + ".txt"
        
        archivo = open(nombre_archivo, "w")
        archivo.write("==============================\n")
        archivo.write("  FACTURA DE COMPRA\n")
        archivo.write("==============================\n")
        archivo.write("Cliente : " + id_cliente + "\n")
        archivo.write("Evento  : " + evento_id  + "\n")
        archivo.write("------------------------------\n")

        for boleta in boletas_compradas:
            archivo.write("Silla/Zona : " + boleta["silla"]        + "\n")
            archivo.write("Zona       : " + boleta["zona"]         + "\n")
            archivo.write("Costo base : $" + str(boleta["base"])   + "\n")
            archivo.write("Servicio 8%: $" + str(boleta["servicio"]) + "\n")
            archivo.write("------------------------------\n")

        archivo.write("TOTAL      : $" + str(round(total, 2)) + "\n")
        archivo.write("==============================\n")
        archivo.close()
        print(f"\nFactura guardada en: {nombre_archivo}")
    except Exception as error:
        print("ERROR al guardar la factura: " + str(error))
        
# BLOQUE 4 - CONTEO DE BOLETAS YA COMPRADAS POR CLIENTE
# BLOQUE 5 - COMPRA TEATRO / DEPORTE
# BLOQUE 6 - COMPRA CONCIERTO        
# BLOQUE 7 - MODULO DE REPORTES (ADMINISTRADOR)

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
    mensajeMenu = "\n1: Ver eventos disponibles \n2: Comprar Boletas \n3: Salir \nElija una opcion: "
    opcionMenu = 0
    evento_elegido = ""
    mensajeBienvenida=""
    mapaxEvento=""
    seleccionAsientos=""
    listaLetras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
    cantidadSillas=""
    id_silla=""
    # Proceso
    mensajeBienvenida+="============================================"
    mensajeBienvenida+="\n          BIENVENIDO A EVENT.CO           "
    mensajeBienvenida +="\n============================================"
    
    print(mensajeBienvenida)

    # Cargar datos al arrancar
    clientes = cargar_clientes()
    eventos  = cargar_eventos()
        
    # Verificacion si hay informacion en los documentos
    if len(clientes) == 0:
        print("No hay clientes registrados. Verifique clientes.txt")
        
    if len(eventos) == 0:
        print("No hay eventos disponibles. Verifique eventos.txt")
        
    # LOGIN
    while True:
    
            id_ingreso = input("\nIngrese su ID de cliente: ").strip()

            if id_ingreso not in clientes:
                print("Error: el ID " + id_ingreso + "no esta registrado. \n porfavor vuelva a ingresarlo")
                
            else:
                break
            nombre_cliente = clientes[id_ingreso]
            print("\nBienvenido/a, " + nombre_cliente)

            
    while True:
        try:
            print("\n ===MENU=== \n")
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
                if tipo== "Teatro":
                    print("asientos disponibles en teatro ")
                    mapaxEvento=cargar_mapa_teatro()
                    print(mapaxEvento)
                    
                    print("\n| x = ocupado|| 0= libre|\n")
                    
                elif tipo=="Deporte":
                    print("asientos disponibles en Deporte")
                    mapaxEvento=cargar_mapa_deporte()
                    print(mapaxEvento)
                    print("\n| x = ocupado|| 0= libre|\n")
                
                
            elif tipo == "Concierto":
                print("asientos disponibles en Concierto")
                mapaxEvento=cargar_precios_concierto()
                print(mapaxEvento)
                print("\n| x = ocupado|----| 0= libre|\n")
                #entrada del dato selecion de sillas
                while True:
                    try:
                        cantidadSillas=int(input("ingrese la cantidad de sillas que desea escojer"))
                        if not(cantidadSillas>0): raise TypeError("numero ingresado invalido")
                        else:break
                    except TypeError as Te:
                        print(f"error en los datos   -> {Te}")
                        continue
                #validacion de la cantidad de asintos
                while True:
                    try:
                        id_silla=idAsiento=input(f"ingrese que asientos desea\n|selecionar asi Numero-LetraIDentificadora|\n|despues de selecionar uno serpar la selecion con (,)|\nletras->{listaLetras}\nnumeros[1-10]\n:").upper()
                        asientoSeparado=idAsiento.split(",")
                        if not(len(asientoSeparado)==cantidadSillas): raise ValueError("los asientos selecionado no concuerdan con la cantidad dada anterior mente")
                        else:break
                    except ValueError as ve:
                        print(f"dato invalido: {ve}")
                        continue
            else:
                print("ERROR: Tipo de evento desconocido: " + tipo)
        
        
        elif opcionMenu == 3:
            # Finalizar
            break
        

    #Cerrar documentos
    clientes.close()
    eventos.close()

except TypeError as Te:
    print(f"error en los datos   -> {Te}")
except Exception as e:
    print(f"Error generico -> {e}")
else:
    print("Ejecución exitosa")
finally:
    print("Fin del programa")