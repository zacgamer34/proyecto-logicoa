#apartado importaciones
#apartado funciones
#apartado principal
try:
#datos de entrada
    archivoUsuarios=""
    archivoEventos=""
    archivoMapa=""
    archivoPrecios=""
    datosLogin=""
#datos de salida
#variables adicionales
    datosLoginSeparados=""
    id=""
    nombre=""
    usuariosSeparados=""
    contenido_clientes=""
#proceso
    while True:
        
        datosLogin=input("ingrese su nombre y su id[separados por: |]\n: ")
        
        
        
        archivoUsuarios=open("recursos/clientes.txt", "r")
        
        contenido_clientes=archivoUsuarios.readline()
        
        
        
        for usuario in archivoUsuarios:
            
            datosLoginSeparados=datosLogin.strip().split("|")
            nombre=datosLoginSeparados[0]
            if nombre==usuario:
                for cicloID in archivoUsuarios[1]:
                    id=datosLoginSeparados[1]
                if id==cicloID:
                    print(f"bienvenido:{nombre} con identificacion:{id}")
                
            
        
    
    archivoUsuarios.close()

except Exception as e:
    print(F"error general del sistema->{e}")

finally:
    archivoUsuarios.close