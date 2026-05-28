# ============================================================
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
            linea = linea.strip()
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
        print(f"{contador}. [ {evento['id']} ] {evento['nombre']} | {evento['tipo']} | {evento['ciudad']} | {evento['fecha']} | {evento['hora']}")
        contador = contador + 1
    print("=================================")
        
def cargar_precios_deporte():
    try:
        precios = {}
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
        return {}
    except Exception as e:
        print(f"Error general en cargar_precios_deporte - {e}")
        return {}

def cargar_precios_teatro():
    try:
        precios = {}
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
        return {}
    except Exception as e:
        print(f"Error general en cargar_precios_teatro - {e}")
        return {}
        
def cargar_precios_concierto():
    try:
        precios = {}
        archivo = open("recursos/precios_eventos[EVT-1003].txt", "r")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split(",")
            if len(partes) == 4:
                rango         = partes[0].strip()   # ej: "1-5"
                zona          = partes[1].strip()    # ej: "VIP"
                cupos_totales = int(partes[2].strip())
                precio        = float(partes[3].strip())
                precios[zona] = {"cupos_totales": cupos_totales, "precio": precio, "rango": rango}
        archivo.close()
        return precios 
    except FileNotFoundError as ffe:
        print(f"Error no se encontro el archivo de precios - {ffe}")
        return {}
    except Exception as e:
        print(f"Error general en cargar_precios_concierto - {e}")
        return {}
        
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
        return []
    except Exception as e:
        print(f"Error general en cargar_mapa_deporte - {e}")
        return []

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
        return []
    except Exception as e:
        print(f"Error general en cargar_mapa_teatro - {e}")
        return []

def cargar_mapa_concierto():
    """
    Carga el mapa de concierto como cupos por zona.
    Usa el archivo de precios para determinar las zonas y sus cupos disponibles.
    """
    try:
        mapa = {}
        precios = cargar_precios_concierto()
        for zona, info in precios.items():
            mapa[zona] = info["cupos_totales"]
        return mapa
    except Exception as e:
        print(f"Error general en cargar_mapa_concierto - {e}")
        return {}
        
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
        
def compraBoleta(id_ingreso, numeroAsiento, letraAsiento, evento_id, mapa):
    """
    Función para registrar la compra de una boleta en el mapa de asientos.
    """
    try:
        # Convertir la letra a número de columna (A-T = 0-19)
        letras_validas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                          "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
        
        if letraAsiento in letras_validas:
            numeroColumna = letras_validas.index(letraAsiento)
        else:
            return mapa, False
        
        # Ajustar índice (python es 0-based)
        indiceFila = numeroAsiento - 1
        
        # Verificar límites
        if indiceFila < 0 or indiceFila >= len(mapa):
            return mapa, False
        if numeroColumna < 0 or numeroColumna >= len(mapa[indiceFila]):
            return mapa, False
        
        # Verificar si el asiento ya está ocupado (O = libre, X = ocupado)
        if mapa[indiceFila][numeroColumna] != "O":
            return mapa, False
        
        # Marcar el asiento como ocupado
        mapa[indiceFila][numeroColumna] = "X"
        
        # Guardar el mapa en el archivo
        nombre_archivo = f"recursos/mapa_evento[{evento_id}].txt"
        
        archivo = open(nombre_archivo, "w")
        for fila in mapa:
            archivo.write(",".join(fila) + "\n")
        archivo.close()
        
        return mapa, True
        
    except IndexError as Ie:
        return mapa, False
    except Exception as e:
        raise Exception(f"Error en la funcion compraBoleta: {e}")
# BLOQUE 4 - CONTEO DE BOLETAS YA COMPRADAS POR CLIENTE
# BLOQUE 5 - COMPRA TEATRO / DEPORTE
# BLOQUE 6 - COMPRA CONCIERTO        
# BLOQUE 7 - MODULO DE REPORTES (ADMINISTRADOR)

# ============================================================
# Apartado principal
try:
    #datos de entrada
    id_ingreso = ""
    id_evento = ""
    #datos de salida
    nombre_cliente = ""
    #variables adicionales
    clientes = {}
    eventos = []
    mensajeMenu = "\n1: Ver eventos disponibles \n2: Comprar Boletas \n3: Salir \nElija una opcion: "
    opcionMenu = 0
    evento_elegido = None
    mensajeBienvenida=""
    mapaxEvento=[]
    seleccionAsientos=""
    listaLetras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
    cantidadSillas=0
    id_silla=""
    boletas_compradas = []
    total = 0.0
    sillaSeperada=""
    
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
            print("Error: el ID " + id_ingreso + " no esta registrado. \n porfavor vuelva a ingresarlo")
                
        else:
            break
            
    nombre_cliente = clientes[id_ingreso]
    print("\nBienvenido/a, " + nombre_cliente)

            
    while True:
        try:
            print("\n ===MENU=== \n")
            opcionMenu = int(input(mensajeMenu))
            if not (1 <= opcionMenu <= 3): 
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
            evento_elegido = None
            for evento in eventos:
                if evento["id"] == id_evento:
                    evento_elegido = evento
                    break
            
            if evento_elegido is None:
                print(f"ERROR: No se encontro el evento con ID {id_evento}")
                continue
            
            
            print(f"Evento: {evento_elegido['nombre']} ({evento_elegido['tipo']})")
            
            # redirigir segun el tipo de evento
            tipo = evento_elegido["tipo"]
            # Reiniciar boletas y total para cada compra
            boletas_compradas = []
            total = 0.0
            
            if tipo == "Teatro" or tipo == "Deporte":
                if tipo == "Teatro":
                    print("Asientos disponibles en Teatro")
                    mapaxEvento = cargar_mapa_teatro()
                    precios_evento = cargar_precios_teatro()
                    
                elif tipo == "Deporte":
                    print("Asientos disponibles en Deporte")
                    mapaxEvento = cargar_mapa_deporte()
                    precios_evento = cargar_precios_deporte()
                
                # Mostrar el mapa con encabezado de letras
                print("\nMapa de asientos (X = ocupado, O = libre):")
                print("     " + "  ".join(listaLetras))
                num_fila = 1
                for fila in mapaxEvento:
                    print(f"{num_fila:2d}   " + "  ".join(fila))
                    num_fila += 1
                    
                print("\n| X = ocupado | O = libre|")
                
                # Entrada de la cantidad de sillas
                while True:
                    try:
                        cantidadSillas = int(input("\nIngrese la cantidad de asientos que desea comprar: "))
                        if cantidadSillas <= 0:
                            raise ValueError("Debe ser mayor a 0")
                        else:
                            break
                    except ValueError as ve:
                        print(f"Error en los datos: {ve}")
                        continue
                
                # Selección de asientos
                num_filas_mapa = len(mapaxEvento)
                while True:
                    try:
                        id_silla = input(f"Ingrese que asientos desea comprar\n|Selecione asi Numero-LetraIdentificadora|\n|Despues de selecionar uno separe la seleccion con (,)|\nLetras->{listaLetras}\nNumeros[1-{num_filas_mapa}]\n:").upper()
                        sillaSeperada = id_silla.split(",")
                        
                        if len(sillaSeperada) != cantidadSillas:
                            raise ValueError("La cantidad de asientos seleccionados no coincide con la cantidad ingresada anteriormente")
                        
                        # Validar formato y rango de asientos
                        for asiento in sillaSeperada:
                            asiento = asiento.strip()
                            if "-" not in asiento:
                                raise ValueError(f"Formato inválido: '{asiento}' debe ser Numero-Letra")
                            partes = asiento.split("-")
                            if len(partes) != 2:
                                raise ValueError(f"Formato inválido: '{asiento}'")
                            try:
                                num = int(partes[0].strip())
                                letra = partes[1].strip()
                                if num < 1 or num > num_filas_mapa:
                                    raise ValueError(f"Número de asiento {num} fuera de rango [1-{num_filas_mapa}]")
                                if letra not in listaLetras:
                                    raise ValueError(f"Letra '{letra}' inválida")
                            except ValueError as e:
                                if "invalid literal" in str(e):
                                    raise ValueError(f"Número inválido en '{asiento}'")
                                raise
                        
                        break
                    except ValueError as ve:
                        print(f"Dato invalido: {ve}")
                        continue
                
                # Procesar los asientos seleccionados
                
                for y in sillaSeperada:
                    ySeparado = y.strip().split("-")
            
                    numeroAsiento = int(ySeparado[0].strip())
                    letraAsiento = ySeparado[1].strip()
            
                    mapaxEvento, seleccion_asientos = compraBoleta(id_ingreso, numeroAsiento, letraAsiento, id_evento, mapaxEvento)
                    if seleccion_asientos == True:
                        print("Compra exitosa del asiento " + letraAsiento + str(numeroAsiento))
                        # Calcular precio según la fila
                        if numeroAsiento in precios_evento:
                            info_precio = precios_evento[numeroAsiento]
                            base = info_precio["precio"]
                            servicio = base * 0.08
                            boletas_compradas.append({
                                "silla": str(numeroAsiento) + "-" + letraAsiento,
                                "zona": info_precio["zona"],
                                "base": base,
                                "servicio": servicio
                            })
                            total += base + servicio
                        else:
                            print(f"Advertencia: No se encontró precio para la fila {numeroAsiento}")
                    
                    else:
                        print("Error: El asiento " + letraAsiento + str(numeroAsiento) + " ya esta ocupado o no existe. Por favor seleccione otro asiento.")
                
                # Generar factura para Teatro/Deporte
                if boletas_compradas:
                    print(f"\nTotal a pagar: ${round(total, 2)}")
                    guardar_factura(id_ingreso, id_evento, boletas_compradas, total)
                
                    
                
            elif tipo == "Concierto":
                print("Asientos disponibles en Concierto")
                mapaxEvento = cargar_mapa_concierto()
                precios_evento = cargar_precios_concierto()
                
                print("\nZonas disponibles:")
                for zona, cupos in mapaxEvento.items():
                    precio_zona = precios_evento[zona]["precio"] if zona in precios_evento else 0
                    print(f"  {zona}: {cupos} cupos disponibles - Precio: ${precio_zona:.2f}")
                
                print("\n| x = ocupado | 0 = libre|")
                
                
                # Entrada del dato selecion de sillas
                while True:
                    try:
                        cantidadSillas = int(input("Ingrese la cantidad de entradas que desea comprar: "))
                        if cantidadSillas <= 0:
                            raise ValueError("Debe ser mayor a 0")
                        else:
                            break
                    except ValueError as ve:
                        print(f"Error en los datos: {ve}")
                        continue
                
                while True:
                    try:
                        id_silla = input(f"Ingrese que zonas desea comprar\n|Ingrese el nombre de la zona|\n|Despues de selecionar una separe la seleccion con (,)|\nZonas disponibles: {list(mapaxEvento.keys())}\n:").upper()
                        sillaSeperada = id_silla.split(",")
                        
                        if len(sillaSeperada) != cantidadSillas:
                            raise ValueError("La cantidad de zonas seleccionadas no coincide con la cantidad ingresada anteriormente")
                        
                        # Validar que las zonas existan y tengan cupos disponibles
                        for zona in sillaSeperada:
                            zona = zona.strip()
                            if zona not in mapaxEvento:
                                raise ValueError(f"Zona '{zona}' no encontrada")
                            if mapaxEvento[zona] <= 0:
                                raise ValueError(f"Zona '{zona}' está llena")
                        
                        break
                    except ValueError as ve:
                        print(f"Dato invalido: {ve}")
                        continue
                
                # Procesar compra de entradas de concierto
                boletas_compradas = []
                for zona in sillaSeperada:
                    zona = zona.strip()
                    if mapaxEvento[zona] > 0:
                        mapaxEvento[zona] -= 1
                        precio_zona = precios_evento[zona]["precio"] if zona in precios_evento else 0
                        base = precio_zona
                        servicio = base * 0.08
                        boletas_compradas.append({
                            "silla": zona,
                            "zona": zona,
                            "base": base,
                            "servicio": servicio
                        })
                        total += base + servicio
                        print(f"Entrada comprada para la zona {zona} - Precio: ${precio_zona:.2f}")
                    else:
                        print(f"Error: Zona {zona} sin cupos disponibles")
                
                # Guardar el mapa actualizado
                nombre_archivo = f"recursos/mapa_evento[{id_evento}].txt"
                try:
                    with open(nombre_archivo, "w") as archivo:
                        for zona, cupos in mapaxEvento.items():
                            archivo.write(f"{zona},{cupos}\n")
                except Exception as e:
                    print(f"Error al guardar el mapa: {e}")
                
                # Generar factura
                if boletas_compradas:
                    guardar_factura(id_ingreso, id_evento, boletas_compradas, total)
                
                
            else:
                print("ERROR: Tipo de evento desconocido: " + tipo)
        
        
        elif opcionMenu == 3:
            # Finalizar
            print("\nGracias por usar EVENT.CO. Hasta luego!")
            break
        
        else:
            print("Opcion invalida. Por favor seleccione 1, 2 o 3.")

except TypeError as Te:
    print(f"Error en los datos: {Te}")
except FileNotFoundError as ffe:
    print(f"Error de archivo no encontrado: {ffe}")
except Exception as e:
    print(f"Error generico: {e}")
else:
    print("\nEjecucion exitosa")
finally:
    print("Fin del programa")