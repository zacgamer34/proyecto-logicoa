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
    
#proceso
    while True:
        
        #datosLogin=input("ingrese su nombre y su id[separados por: -]\n: ")
        
        
        
        archivoUsuarios=open("recursos/clientes.txt","r")
        archivoUsuarios.readline().strip().split("|")
        
        
        print(archivoUsuarios)
        #for usuario in archivoUsuarios[0]:
            #datosLoginSeparados=datosLogin.split("-")
            #nombre=datosLoginSeparados[0]
            #if nombre==usuario:
                #for cicloID in archivoUsuarios[1]:
                    #id=datosLoginSeparados[1]
                #if id==cicloID:
                    #print(f"bienvenido:{nombre} con identificacion:{id}")
                
            
        
    


except Exception as e:
    print(F"error general del sistema->{e}")

finally:
    archivoUsuarios.close