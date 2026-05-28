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
            if linea == "": continue
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
        raise Exception(f"Error generico en la funcion cargar_eventos - {e}")
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
                rango = partes[0].strip()
                zona  = partes[1].strip()
                precio = float(partes[2].strip())
                extremos = rango.split("-")
                inicio = int(extremos[0])
                fin    = int(extremos[1])
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
                rango = partes[0].strip()
                zona  = partes[1].strip()
                precio = float(partes[2].strip())
                extremos = rango.split("-")
                inicio = int(extremos[0])
                fin    = int(extremos[1])
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
                rango         = partes[0].strip()
                zona          = partes[1].strip()
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
