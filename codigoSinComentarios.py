def cargar_clientes():
    try:
        clientes = {}
        with open("recursos/clientes.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
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


def cargar_precios_asientos(evento_id):
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
 
 
def guardar_factura(id_cliente, evento_id, boletas_compradas, total):
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
    indice = ord(letra.upper()) - ord('A')
    if 0 <= indice <= 19:
        return indice
    return -1
 
 
def compraBoleta(id_ingreso, numeroAsiento, letraAsiento, evento_id, mapaxEvento):
    try:
        numeroColumna = letra_a_columna(letraAsiento)
        if numeroColumna == -1:
            return mapaxEvento, False
 
        indiceFila = numeroAsiento - 1
 
        if indiceFila < 0 or indiceFila >= len(mapaxEvento):
            return mapaxEvento, False
        if numeroColumna >= len(mapaxEvento[indiceFila]):
            return mapaxEvento, False
 
        if mapaxEvento[indiceFila][numeroColumna] != "O":
            return mapaxEvento, False
 
        mapaxEvento[indiceFila][numeroColumna] = id_ingreso
 
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
 
 
try:
    id_ingreso = ""
    id_evento = ""
    nombre_cliente = ""
    clientes = {}
    eventos = []
    mensajeMenu = "\n1: Ver eventos disponibles \n2: Comprar Boletas \n3: Salir \nElija una opcion: "
    opcionMenu = 0
    evento_elegido = None
    listaLetras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
 
    print("============================================")
    print("          BIENVENIDO A EVENT.CO           ")
    print("============================================")
 
    clientes = cargar_clientes()
    eventos  = cargar_eventos()
 
    if len(clientes) == 0:
        print("No hay clientes registrados. Verifique clientes.txt")
    if len(eventos) == 0:
        print("No hay eventos disponibles. Verifique eventos.txt")
 
    while True:
        id_ingreso = input("\nIngrese su ID de cliente: ").strip()
 
        if id_ingreso not in clientes:
            print(f"Error: el ID {id_ingreso} no esta registrado.\nPor favor vuelva a ingresarlo.")
        else:
            break
 
    nombre_cliente = clientes[id_ingreso]
    print(f"\nBienvenido/a, {nombre_cliente}")
 
    while True:
        try:
            print("\n ===MENU===")
            opcionMenu = int(input(mensajeMenu))
            if not (1 <= opcionMenu <= 3):
                raise ValueError("Valor fuera de rango")
        except ValueError as ve:
            print(f"Opcion invalida: {ve}")
            continue
 
        if opcionMenu == 1:
            print("\n ====== EVENTOS DISPONIBLES ======")
            for i, evento in enumerate(eventos, start=1):
                print(f"{i}. [ {evento['id']} ] {evento['nombre']} | {evento['tipo']} | {evento['ciudad']} | {evento['fecha']} | {evento['hora']}")
            print("=================================")
 
        elif opcionMenu == 2:
            print("\n ====== EVENTOS DISPONIBLES ======")
            for i, evento in enumerate(eventos, start=1):
                print(f"{i}. [ {evento['id']} ] {evento['nombre']} | {evento['tipo']} | {evento['ciudad']} | {evento['fecha']} | {evento['hora']}")
            print("=================================")
            
            id_evento = input("\nIngrese el ID del evento: ").strip()
 
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
                        total += precio_base + servicio
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
                        total += precio_base + servicio
 
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