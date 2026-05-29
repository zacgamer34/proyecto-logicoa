# Apartado importaciones
# Apartado funciones:
# BLOQUE 1 - CARGA DE ARCHIVOS
def cargar_clientes():
    """Carga el archivo de clientes y retorna un diccionario {id: nombre}."""
    try:
        clientes = {}
        with open("recursos/clientes.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue  # saltar lineas vacias
                partes = linea.split(",")
                if len(partes) == 2:
                    id_cliente = partes[0].strip()
                    nombre     = partes[1].strip()
                    clientes[id_cliente] = nombre
        return clientes
    except FileNotFoundError as ffe:
        raise FileNotFoundError(f"Error no se encuentra el archivo clientes.txt - {ffe}")
    except Exception as e:
        raise Exception(f"Error generico en la funcion cargar_clientes - {e}")

def cargar_eventos():
    """Carga el archivo de eventos y retorna una lista de diccionarios."""
    try:
        eventos = []
        with open("recursos/eventos.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split(",")
                if len(partes) == 6:
                    evento = {
                        "id"     : partes[0].strip(),
                        "nombre" : partes[1].strip(),
                        "tipo"   : partes[2].strip(),
                        "ciudad" : partes[3].strip(),
                        "fecha"  : partes[4].strip(),
                        "hora"   : partes[5].strip()
                    }
                    eventos.append(evento)
        return eventos
    except FileNotFoundError as ffe:
        raise FileNotFoundError(f"Error no se encuentra el archivo eventos.txt - {ffe}")
    except Exception as e:
        raise Exception(f"Error generico en la funcion cargar_eventos - {e}")

def cargar_admis():
    try:
        admins = {}
        with open("recursos/admines.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue  # saltar lineas vacias
                partes = linea.split(",")
                if len(partes) == 2:
                    id_admin = partes[0].strip()
                    nombre_admin = partes[1].strip()
                    admins[id_admin] = nombre_admin
        return admins
    except FileNotFoundError as ffe:
        raise FileNotFoundError(f"Error no se encuentra el archivo clientes.txt - {ffe}")
    except Exception as e:
        raise Exception(f"Error generico en la funcion cargar_clientes - {e}")
# BLOQUE 2 - FUNCIONES DE VISUALIZACION
def mostrar_eventos(eventos):
    """Muestra la lista de eventos disponibles con formato."""
    print("\n ====== EVENTOS DISPONIBLES ======")
    for i, evento in enumerate(eventos, start=1):
        print(f"{i}. [ {evento['id']} ] {evento['nombre']} | {evento['tipo']} | {evento['ciudad']} | {evento['fecha']} | {evento['hora']}")
    print("=================================")

def cargar_precios_asientos(evento_id):
    """
    Carga precios para eventos tipo Deporte o Teatro.
    Retorna un diccionario {num_fila: {"zona": str, "precio": float}}.
    """
    try:
        precios = {}
        with open(f"recursos/precios_evento[{evento_id}].txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split(",")
                if len(partes) == 3:
                    rango  = partes[0].strip()
                    zona   = partes[1].strip()
                    precio = float(partes[2].strip())

                    extremos = rango.split("-")
                    inicio = int(extremos[0])
                    fin    = int(extremos[1])

                    for num_fila in range(inicio, fin + 1):
                        precios[num_fila] = {"zona": zona, "precio": precio}
        return precios
    except FileNotFoundError as ffe:
        print(f"Error no se encontro el archivo de precios - {ffe}")
        return {}
    except Exception as e:
        print(f"Error general en cargar_precios_asientos - {e}")
        return {}

def cargar_precios_concierto():
    """
    Carga precios para evento tipo Concierto.
    Retorna un diccionario {zona: {"cupos_totales": int, "precio": float}}.
    Archivo: precios_eventos[EVT-1003].txt con formato: rango,zona,cupos,precio
    """
    try:
        precios = {}
        with open("recursos/precios_eventos[EVT-1003].txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split(",")
                if len(partes) == 4:
                    zona          = partes[1].strip()
                    cupos_totales = int(partes[2].strip())
                    precio        = float(partes[3].strip())
                    precios[zona] = {"cupos_totales": cupos_totales, "precio": precio}
        return precios
    except FileNotFoundError as ffe:
        print(f"Error no se encontro el archivo de precios - {ffe}")
        return {}
    except Exception as e:
        print(f"Error general en cargar_precios_concierto - {e}")
        return {}

def cargar_mapa_asientos(evento_id):
    """
    Carga el mapa de asientos para eventos tipo Deporte o Teatro.
    Retorna una lista de listas (matriz).
    """
    try:
        mapa = []
        with open(f"recursos/mapa_evento[{evento_id}].txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
                celdas = linea.split(",")
                fila = [celda.strip() for celda in celdas]
                mapa.append(fila)
        return mapa
    except FileNotFoundError as ffe:
        print(f"Error no se encontro el archivo del mapa - {ffe}")
        return []
    except Exception as e:
        print(f"Error general en cargar_mapa_asientos - {e}")
        return []

def cargar_mapa_concierto():
    """
    Carga el mapa de zonas para evento tipo Concierto.
    Retorna un diccionario {zona: cupos_disponibles}.
    """
    try:
        mapa = {}
        with open("recursos/mapa_evento[EVT-1003].txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split(",")
                if len(partes) == 2:
                    zona  = partes[0].strip()
                    cupos = int(partes[1].strip())
                    mapa[zona] = cupos
        return mapa
    except FileNotFoundError as ffe:
        print(f"Error no se encontro el archivo del mapa de concierto - {ffe}")
        return {}
    except Exception as e:
        print(f"Error general en cargar_mapa_concierto - {e}")
        return {}
    
# BLOQUE 3 - GUARDAR / ACTUALIZAR ARCHIVOS
def guardar_factura(id_cliente, evento_id, boletas_compradas, total):
    """Genera y guarda un archivo de factura con los detalles de la compra."""
    try:
        nombre_archivo = f"factura_{id_cliente}_{evento_id}.txt"
        with open(nombre_archivo, "w") as archivo:
            archivo.write("==============================\n")
            archivo.write("  FACTURA DE COMPRA\n")
            archivo.write("==============================\n")
            archivo.write(f"Cliente : {id_cliente}\n")
            archivo.write(f"Evento  : {evento_id}\n")
            archivo.write("------------------------------\n")

            for boleta in boletas_compradas:
                archivo.write(f"Silla/Zona : {boleta['silla']}\n")
                archivo.write(f"Zona       : {boleta['zona']}\n")
                archivo.write(f"Costo base : ${boleta['base']}\n")
                archivo.write(f"Servicio 8%: ${boleta['servicio']}\n")
                archivo.write("------------------------------\n")

            archivo.write(f"TOTAL      : ${round(total, 2)}\n")
            archivo.write("==============================\n")

        print(f"\nFactura guardada en: {nombre_archivo}")
    except Exception as error:
        print(f"ERROR al guardar la factura: {error}")

def letra_a_columna(letra):
    """
    Convierte una letra (A-T) a su indice de columna (0-19).
    Retorna -1 si la letra no es valida.
    """
    indice = ord(letra.upper()) - ord('A')
    if 0 <= indice <= 19:
        return indice
    return -1


def compraBoleta(id_ingreso, numeroAsiento, letraAsiento, evento_id, mapaxEvento):
    """
    Registra la compra de una boleta en el mapa de asientos.
    Retorna (mapa_actualizado, exito: bool).
    """
    try:
        numeroColumna = letra_a_columna(letraAsiento)
        if numeroColumna == -1:
            return mapaxEvento, False

        # Ajustar indice (python es 0-based)
        indiceFila = numeroAsiento - 1

        # Validar que los indices esten dentro del rango
        if indiceFila < 0 or indiceFila >= len(mapaxEvento):
            return mapaxEvento, False
        if numeroColumna >= len(mapaxEvento[indiceFila]):
            return mapaxEvento, False

        # Verificar si el asiento ya esta ocupado (el mapa usa "O" para libre)
        if mapaxEvento[indiceFila][numeroColumna] != "O":
            return mapaxEvento, False

        # Marcar el asiento con el ID del cliente
        mapaxEvento[indiceFila][numeroColumna] = id_ingreso

        # Guardar el mapa en el archivo
        nombre_archivo = f"recursos/mapa_evento[{evento_id}].txt"
        with open(nombre_archivo, "w") as archivo:
            for fila in mapaxEvento:
                archivo.write(",".join(fila) + "\n")

        return mapaxEvento, True

    except IndexError:
        return mapaxEvento, False
    except Exception as e:
        raise Exception(f"Error en la funcion compraBoleta: {e}")


def compra_concierto(zona, cantidad, mapa_concierto, evento_id):
    """
    Registra la compra de entradas de concierto por zona.
    Retorna (mapa_actualizado, exito: bool).
    """
    try:
        if zona not in mapa_concierto:
            print(f"ERROR: La zona '{zona}' no existe.")
            return mapa_concierto, False

        cupos_disponibles = mapa_concierto[zona]
        if cantidad > cupos_disponibles:
            print(f"ERROR: Solo hay {cupos_disponibles} cupos disponibles en la zona {zona}.")
            return mapa_concierto, False
        mapa_concierto[zona] = cupos_disponibles - cantidad
        with open(f"recursos/mapa_evento[{evento_id}].txt", "w") as archivo:
            for z, c in mapa_concierto.items():
                archivo.write(f"{z},{c}\n")

        return mapa_concierto, True

    except Exception as e:
        raise Exception(f"Error en la funcion compra_concierto: {e}")

def parsear_asiento(texto):
    texto = texto.strip()

    
    if "-" in texto:
        partes = texto.split("-")
        if len(partes) == 2:
            numero = int(partes[0].strip())
            letra  = partes[1].strip().upper()
            if len(letra) == 1 and letra.isalpha():
                return numero, letra

    numero_str = ""
    letra = ""
    for char in texto:
        if char.isdigit():
            numero_str += char
        elif char.isalpha() and letra == "":
            letra = char.upper()

    if numero_str and letra:
        return int(numero_str), letra

    raise ValueError(f"Formato de asiento invalido: '{texto}'. Use formato: 3A o 3-A")


def mostrar_mapa_asientos(mapaxEvento, listaLetras):
    num_columnas = len(mapaxEvento[0]) if mapaxEvento else 0
    letras_header = listaLetras[:num_columnas]

    print("\n    " + "  ".join(letras_header))
    print("   " + "---" * num_columnas)
    for i, fila in enumerate(mapaxEvento, start=1):
        celdas = []
        for celda in fila:
            if celda == "O":
                celdas.append("O")
            else:
                celdas.append("X")
        print(f"{i:2d}| " + "  ".join(celdas))

    print("\n| O = libre | X = ocupado |")



# BLOQUE 4 - MODULO DE REPORTES (ADMINISTRADOR)

#funciones apoyadas con ia herramienta(blackbox)
def calcular_datos_reporte(evento_id, tipo_evento):
    """
    Calcula los datos necesarios para un reporte de ventas de un evento específico.
    
    Args:
        evento_id (str): Identificador único del evento.
        tipo_evento (str): Tipo de evento ('Teatro', 'Deporte' o 'Concierto').
    
    Returns:
        dict: Diccionario con los datos del reporte o lanza una excepción si hay errores.
    """
    datos_reporte = {
        "evento_id": evento_id,
        "tipo_evento": tipo_evento,
        "total_asientos": 0,
        "asientos_vendidos": 0,
        "asientos_disponibles": 0,
        "porcentaje_occupacion": 0.0,
        "ingresos_totales": 0.0,
        "detalle_por_zona": {}
    }
    
    try:
        if tipo_evento in ("Teatro", "Deporte"):
            # Cargar mapa de asientos para Teatro/Deporte
            mapa = cargar_mapa_asientos(evento_id)
            precios = cargar_precios_asientos(evento_id)
            
            if not mapa:
                raise ValueError(f"No se pudo cargar el mapa para el evento {evento_id}")
            
            # Calcular totales
            total_asientos = 0
            asientos_vendidos = 0
            ingresos_totales = 0.0
            detalle_por_zona = {}
            
            for indice_fila, fila in enumerate(mapa):
                for indice_columna, estado_asiento in enumerate(fila):
                    numero_fila = indice_fila + 1
                    total_asientos += 1
                    
                    # Verificar si el asiento está ocupado (no es "O")
                    if estado_asiento != "O":
                        asientos_vendidos += 1
                        
                        # Obtener precio de la zona
                        precio_zona = 0.0
                        nombre_zona = "General"
                        
                        if numero_fila in precios:
                            precio_zona = precios[numero_fila]["precio"]
                            nombre_zona = precios[numero_fila]["zona"]
                        
                        # Calcular ingreso con cargo de servicio (8%)
                        precio_base = precio_zona
                        cargo_servicio = round(precio_base * 0.08, 2)
                        ingreso_total_asiento = precio_base + cargo_servicio
                        
                        ingresos_totales += ingreso_total_asiento
                        
                        # Agregar al detalle por zona
                        if nombre_zona not in detalle_por_zona:
                            detalle_por_zona[nombre_zona] = {
                                "vendidos": 0,
                                "ingresos": 0.0
                            }
                        
                        detalle_por_zona[nombre_zona]["vendidos"] += 1
                        detalle_por_zona[nombre_zona]["ingresos"] += ingreso_total_asiento
            
            datos_reporte["total_asientos"] = total_asientos
            datos_reporte["asientos_vendidos"] = asientos_vendidos
            datos_reporte["asientos_disponibles"] = total_asientos - asientos_vendidos
            datos_reporte["porcentaje_occupacion"] = round((asientos_vendidos / total_asientos) * 100, 2) if total_asientos > 0 else 0.0
            datos_reporte["ingresos_totales"] = round(ingresos_totales, 2)
            datos_reporte["detalle_por_zona"] = detalle_por_zona
            
        elif tipo_evento == "Concierto":
            # Cargar mapa de zonas para Concierto
            mapa_zonas = cargar_mapa_concierto()
            precios_zonas = cargar_precios_concierto()
            
            if not mapa_zonas:
                raise ValueError(f"No se pudo cargar el mapa de zonas para el evento {evento_id}")
            
            # Calcular totales遍历zonas
            total_cupos = 0
            asientos_vendidos = 0
            ingresos_totales = 0.0
            detalle_por_zona = {}
            
            for zona, cupos_disponibles in mapa_zonas.items():
                total_cupos += cupos_disponibles
            
            # Calcular vendidos restando disponibles de totales conocidos
            for zona, cupos_disponibles in mapa_zonas.items():
                if zona in precios_zonas:
                    precio_unitario = precios_zonas[zona]["precio"]
                    cupos_totales_zona = precios_zonas[zona]["cupos_totales"]
                    vendidos_zona = cupos_totales_zona - cupos_disponibles
                    
                    asientos_vendidos += vendidos_zona
                    
                    # Calcular ingresos
                    precio_base = precio_unitario * vendidos_zona
                    cargo_servicio = round(precio_base * 0.08, 2)
                    ingreso_zona = precio_base + cargo_servicio
                    
                    ingresos_totales += ingreso_zona
                    
                    # Detalle por zona
                    detalle_por_zona[zona] = {
                        "vendidos": vendidos_zona,
                        "ingresos": round(ingreso_zona, 2)
                    }
            total_asientos = asientos_vendidos + sum(mapa_zonas.values())
            
            datos_reporte["total_asientos"] = total_asientos
            datos_reporte["asientos_vendidos"] = asientos_vendidos
            datos_reporte["asientos_disponibles"] = sum(mapa_zonas.values())
            datos_reporte["porcentaje_occupacion"] = round((asientos_vendidos / total_asientos) * 100, 2) if total_asientos > 0 else 0.0
            datos_reporte["ingresos_totales"] = round(ingresos_totales, 2)
            datos_reporte["detalle_por_zona"] = detalle_por_zona
            
        else:
            raise ValueError(f"Tipo de evento desconocido: {tipo_evento}")
        return datos_reporte
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Archivo no encontrado al generar reporte: {e}")
    except Exception as e:
        raise Exception(f"Error al calcular datos del reporte: {e}")

def guardar_reporte_ventas(datos_reporte, evento_id):
    """
    Guarda los datos del reporte de ventas en un archivo de texto.
    Args:
        datos_reporte (dict): Diccionario con los datos del reporte.
        evento_id (str): Identificador del evento.
    Returns:
        str: Ruta del archivo donde se guardó el reporte.
    """
    try:
        nombre_archivo = f"reporte_ventas_{evento_id}.txt"
        
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("=" * 50 + "\n")
            archivo.write("       REPORTE DE VENTAS - EVENT.CO\n")
            archivo.write("=" * 50 + "\n\n")
            
            archivo.write(f"ID Evento     : {datos_reporte['evento_id']}\n")
            archivo.write(f"Tipo Evento   : {datos_reporte['tipo_evento']}\n")
            archivo.write("-" * 50 + "\n\n")
            
            archivo.write("--- RESUMEN GENERAL ---\n")
            archivo.write(f"Total de asientos      : {datos_reporte['total_asientos']}\n")
            archivo.write(f"Asientos vendidos      : {datos_reporte['asientos_vendidos']}\n")
            archivo.write(f"Asientos disponibles   : {datos_reporte['asientos_disponibles']}\n")
            archivo.write(f"Porcentaje ocupación   : {datos_reporte['porcentaje_occupacion']}%\n")
            archivo.write(f"Ingresos totales       : ${datos_reporte['ingresos_totales']:.2f}\n")
            archivo.write("\n")
            
            if datos_reporte["detalle_por_zona"]:
                archivo.write("--- DETALLE POR ZONA ---\n")
                for zona, info in datos_reporte["detalle_por_zona"].items():
                    archivo.write(f"\nZona: {zona}\n")
                    archivo.write(f"  Vendidos : {info['vendidos']}\n")
                    archivo.write(f"  Ingresos : ${info['ingresos']:.2f}\n")
            
            archivo.write("\n" + "=" * 50 + "\n")
            archivo.write("        FIN DEL REPORTE\n")
            archivo.write("=" * 50 + "\n")
        
        return nombre_archivo
        
    except Exception as e:
        raise Exception(f"Error al guardar el reporte de ventas: {e}")
# Apartado principal
try:
    # datos de entrada
    id_ingreso = ""
    id_evento = ""
    # datos de salida
    nombre_cliente = ""
    # variables adicionales
    clientes = {}
    eventos = []
    mensajeMenu = "\n1: Ver eventos disponibles \n2: Comprar Boletas \n3: Salir \nElija una opcion: "
    opcionMenu = 0
    evento_elegido = None
    listaLetras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
    precio_base=0.0
    boletas_compradas=[]
    todos_exitosos=True
    zona_elegida=""
    admins={}
    mensajeMenuAdmin="\n1:generar informe de ventas \n2: Salir \nElija una opcion: "
    admin_nombre=""
    id_evento_reporte=""
    admin_nombre=""
    zona_nombre=""
    zona=""
    zonas_lista=""
    mapaxEvento=""
    precio_zona=""
    precios_evento=""
    archivo_reporte=""
    mensaje_reporte=""
    mensajeBienvenida=""
    sillaSeperada=[]
    total=0.0
    # Proceso
    mensajeBienvenida+="============================================"
    mensajeBienvenida+="          BIENVENIDO A EVENT.CO           "
    mensajeBienvenida+="============================================"
    print(mensajeBienvenida)

    # Cargar datos al arrancar
    clientes = cargar_clientes()
    eventos  = cargar_eventos()
    admins   = cargar_admis()

    if len(clientes) == 0:
        print("No hay clientes registrados. Verifique clientes.txt")
    elif len(eventos) == 0:
        print("No hay eventos disponibles. Verifique eventos.txt")
    elif len(admins)==0:
        print("No hay eventos disponibles. Verifique admines.txt")
    # LOGIN
    while True:
        
        id_ingreso = input("\nIngrese su ID de cliente o admin: ").strip()
        if (id_ingreso not in clientes) and (id_ingreso not in admins) :
            print(f"Error: el ID {id_ingreso} no esta registrado.\nPor favor vuelva a ingresarlo.")
        
        else:
            break
        
    if id_ingreso in admins:
        admin_nombre=admins[id_ingreso]
        print(f"\nBienvenido adimistrador/a,{admin_nombre}")
        while True:
            
            try:
                print("\n ===panel de administrador=== \n")
                opcionPanel = int(input(mensajeMenuAdmin))
                if not (1 <= opcionPanel <= 2):
                    raise ValueError("Valor fuera de rango")
            except ValueError as ve:
                print(f"Opcion invalida: {ve}")
                continue

            if opcionPanel == 1:
            # Solicitar ID del evento para el reporte
                mostrar_eventos(eventos)
                id_evento_reporte= input("\nIngrese el ID del evento para generar el reporte: ").strip()
            # Buscar evento seleccionado
                evento_seleccionado = None
                for evento in eventos:
                    if evento["id"] == id_evento_reporte:
                        evento_seleccionado = evento
                        break
                if evento_seleccionado is None:
                    print(f"ERROR: No se encontró el evento con ID {id_evento_reporte}")
                else:
                    # Generar datos del reporte
                    datos_reporte = calcular_datos_reporte(
                        evento_seleccionado["id"],
                        evento_seleccionado["tipo"]
                        )
                    # Guardar reporte en archivo
                    archivo_reporte = guardar_reporte_ventas(datos_reporte, evento_seleccionado["id"])
                
            elif opcionPanel==2:
                break
            
    nombre_cliente = clientes[id_ingreso]
    print(f"\nBienvenido/a, {nombre_cliente}")
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

            
            tipo = evento_elegido["tipo"]

            if tipo == "Teatro" or tipo == "Deporte":
                
                print(f"\nAsientos disponibles en {tipo}")
                mapaxEvento = cargar_mapa_asientos(id_evento)
                precios_evento = cargar_precios_asientos(id_evento)
                if not mapaxEvento:
                    print("ERROR: No se pudo cargar el mapa de asientos.")
                    continue
                mostrar_mapa_asientos(mapaxEvento, listaLetras)
                cantidadSillas = 0
                while True:
                    try:
                        cantidadSillas = int(input("\nIngrese la cantidad de asientos que desea comprar [limite de 5 por compra]: "))
                        if not (1 <= cantidadSillas <= 5):
                            raise ValueError("La cantidad debe ser entre 1 y 5")
                        else:
                            break
                    except ValueError as ve:
                        print(f"Error en los datos: {ve}")
                        continue
                sillaSeperada = []
                while True:
                    try:
                        id_silla = input(
                            f"\nIngrese los asientos que desea comprar\n"
                            f"| Formato: NumeroLetra (ej: 3A) o Numero-Letra (ej: 3-A) |\n"
                            f"| Separe con coma si son varios (ej: 3A,5B,7C) |\n"
                            f"Letras disponibles-> {listaLetras[:len(mapaxEvento[0]) if mapaxEvento else 0]}\n"
                            f"Filas [1-{len(mapaxEvento)}]\n: "
                        ).upper()
                        sillaSeperada = id_silla.split(",")
                        if len(sillaSeperada) != cantidadSillas:
                            raise ValueError("La cantidad de asientos seleccionados no coincide con la cantidad ingresada")
                        
                        for s in sillaSeperada:
                            parsear_asiento(s)
                        break
                    except ValueError as ve:
                        print(f"Dato invalido: {ve}")
                        continue
                boletas_compradas = []
                total = 0.0
                todos_exitosos = True
                for asiento_str in sillaSeperada:
                    numeroAsiento, letraAsiento = parsear_asiento(asiento_str)
                    mapaxEvento, exito = compraBoleta(id_ingreso, numeroAsiento, letraAsiento, id_evento, mapaxEvento)
                    if exito:
                        precio_base = 0.0
                        zona_nombre = "Desconocida"
                        if numeroAsiento in precios_evento:
                            precio_base = precios_evento[numeroAsiento]["precio"]
                            zona_nombre = precios_evento[numeroAsiento]["zona"]
                        servicio = round(precio_base * 0.08, 2)
                        boleta = {
                            "silla"   : f"{numeroAsiento}{letraAsiento}",
                            "zona"    : zona_nombre,
                            "base"    : precio_base,
                            "servicio": servicio
                        }
                        boletas_compradas.append(boleta)
                        total = precio_base + servicio
                        print(f"  -> Asiento {numeroAsiento}{letraAsiento} reservado con exito (Zona: {zona_nombre}, Precio: ${precio_base})")
                    else:
                        print(f"  -> Asiento {numeroAsiento}{letraAsiento} NO disponible (ocupado o invalido)")
                        todos_exitosos = False
                if boletas_compradas:
                    print(f"\n--- Resumen de compra ---")
                    print(f"Asientos comprados: {len(boletas_compradas)}")
                    print(f"Total: ${round(total, 2)}")
                    guardar_factura(id_ingreso, id_evento, boletas_compradas, total)
                else:
                    print("\nNo se pudo completar ninguna compra.")

            elif tipo == "Concierto":
                print("\nEntradas disponibles para Concierto")
                mapaxEvento = cargar_mapa_concierto()
                precios_evento = cargar_precios_concierto()
                if not mapaxEvento:
                    print("ERROR: No se pudo cargar las zonas del concierto.")
                    continue
                print("\nZonas disponibles:")
                zonas_lista = list(mapaxEvento.keys())
                for i, zona in enumerate(zonas_lista, start=1):
                    cupos = mapaxEvento[zona]
                    precio_zona = precios_evento[zona]["precio"] if zona in precios_evento else 0
                    print(f"  {i}. {zona}: {cupos} cupos disponibles - Precio: ${precio_zona:.2f}")
                zona_elegida = ""
                while True:
                    zona_elegida = input("\nIngrese el nombre de la zona (ej: VIP, General): ").strip()
                    if zona_elegida in mapaxEvento:
                        break
                    else:
                        print(f"Zona '{zona_elegida}' no existe. Las zonas son: {zonas_lista}")
                cantidadEntradas = 0
                while True:
                    try:
                        cantidadEntradas = int(input(f"Ingrese la cantidad de entradas para zona {zona_elegida} [limite de 5]: "))
                        if not (1 <= cantidadEntradas <= 5):
                            raise ValueError("La cantidad debe ser entre 1 y 5")
                        if cantidadEntradas > mapaxEvento[zona_elegida]:
                            raise ValueError(f"Solo hay {mapaxEvento[zona_elegida]} cupos disponibles")
                        break
                    except ValueError as ve:
                        print(f"Error en los datos: {ve}")
                        continue
                mapaxEvento, exito = compra_concierto(zona_elegida, cantidadEntradas, mapaxEvento, id_evento)
                
                if exito:
                    precio_base = 0.0
                    if zona_elegida in precios_evento:
                        precio_base = precios_evento[zona_elegida]["precio"]
                    boletas_compradas = []
                    total = 0.0
                    for i in range(cantidadEntradas):
                        servicio = round(precio_base * 0.08, 2)
                        boleta = {
                            "silla"   : f"{zona_elegida}-{i+1}",
                            "zona"    : zona_elegida,
                            "base"    : precio_base,
                            "servicio": servicio
                        }
                        boletas_compradas.append(boleta)
                        total = precio_base + servicio
                    print(f"\n--- Resumen de compra ---")
                    print(f"Zona: {zona_elegida}")
                    print(f"Entradas: {cantidadEntradas}")
                    print(f"Total: ${round(total, 2)}")
                    guardar_factura(id_ingreso, id_evento, boletas_compradas, total)
                else:
                    print("\nNo se pudo completar la compra.")

            else:
                print("ERROR: Tipo de evento desconocido: " + tipo)

        elif opcionMenu == 3:

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