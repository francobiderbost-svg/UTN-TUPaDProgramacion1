#Ejercicio 1 "CAJA DEL KIOSCO"

nombre = input("nombre del cliente: ").strip()

while nombre == "" or not nombre.isalpha():
    print("error: ingresa un nombre valido por favor")
    nombre = input("nombre del cliente: ").strip()

cantidad_str = input("por favor ingrese la cantidad de productos: ").strip()

while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("error: ingresa un numero entero positivo mayor a 0")
    cantidad_str = input("por favor ingrese la cantidad de productos: ").strip()

cantidad_int = int(cantidad_str)

total_sin_descuento = 0

total_con_descuento = 0.0

for i in range(1, cantidad_int+1):
    precio_str = input(f"producto {i} - precio: ").strip()

    while not precio_str.isdigit() or int(precio_str) == 0:
        
        print("error: el precio debe ser un numero entero positivo")
        
        precio_str = input(f"producto {i} - precio: ").strip()

    precio_int = int(precio_str)


    descuento = input("descuento (S/N): ").strip().lower()

    while descuento != "s" and descuento != "n":
        print("error: ingrese S para si, N para no")
        descuento = input("descuento (S/N): ").strip().lower()

    total_sin_descuento += precio_int
  
    if descuento == "s":
        precio_final = precio_int * 0.9
    else:
        precio_final = precio_int

    total_con_descuento += precio_final


ahorro = total_sin_descuento - total_con_descuento
promedio_producto = total_con_descuento / cantidad_int
print(f"cliente: {nombre}")
print(f"cantidad de productos {cantidad_int}")
print(f"total sin descuento: {total_sin_descuento}")
print(f"total con descuento: {total_con_descuento:.2f}")
print(f"cantidad ahorrada: {ahorro}")
print(f"promedio por producto {promedio_producto}")


#Ejercicio 2 “Acceso al Campus y Menú Seguro” ##############################

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0

while intentos < 3:
    usuario = input("Ingrese usuario: ")
    clave = input("Ingrese clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso correcto")
        break
    else:
        print("Datos incorrectos")
        intentos += 1

if intentos == 3:
    print("Cuenta bloqueada")
else:
    opcion = ""

    while opcion != "4":
        print("\nMENU")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mensaje motivacional")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if not opcion.isdigit():
            print("Error: debe ingresar un número")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: opción inválida")
            continue

        elif opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            nueva = input("Ingrese nueva clave: ")
            confirmacion = input("Confirme la clave: ")

            if nueva == confirmacion:
                clave_correcta = nueva
                print("Clave actualizada correctamente")
            else:
                print("Las claves no coinciden")

        elif opcion == 3:
            print("¡Seguí aprendiendo, vas por buen camino!")

        elif opcion == 4:
            print("Saliendo del sistema...")


#Ejercicio 3 “Agenda de Turnos con Nombres (sin listas)” ####################

# Turnos Lunes (4)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Turnos Martes (3)
martes1 = ""
martes2 = ""
martes3 = ""

# 1. Nombre del operador
operador = input("Ingrese nombre del operador: ")

while not operador.isalpha():
    print("Error: solo letras")
    operador = input("Ingrese nombre del operador: ")

# 2. Menú
opcion = ""

while opcion != "5":
    print("\nMENU")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione opción: ")

    # Validar opción
    if not opcion.isdigit():
        print("Error: ingrese un número")
        
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Opción inválida")
        
        continue

    
    # OPCIÓN 1: RESERVAR
    
    if opcion == 1:
        dia = input("Ingrese día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error")
            dia = input("Ingrese día (1=Lunes, 2=Martes): ")

        dia = int(dia)

        nombre = input("Nombre del paciente: ")
        while not nombre.isalpha():
            print("Error: solo letras")
            nombre = input("Nombre del paciente: ")

        if dia == 1:
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Paciente ya tiene turno")
            elif lunes1 == "":
                lunes1 = nombre
                print("Turno asignado")
            elif lunes2 == "":
                lunes2 = nombre
                print("Turno asignado")
            elif lunes3 == "":
                lunes3 = nombre
                print("Turno asignado")
            elif lunes4 == "":
                lunes4 = nombre
                print("Turno asignado")
            else:
                print("No hay turnos disponibles")

        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Paciente ya tiene turno")
            elif martes1 == "":
                martes1 = nombre
                print("Turno asignado")
            elif martes2 == "":
                martes2 = nombre
                print("Turno asignado")
            elif martes3 == "":
                martes3 = nombre
                print("Turno asignado")
            else:
                print("No hay turnos disponibles")

    
    
    
    elif opcion == 2:
        dia = input("Ingrese día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error")
            dia = input("Ingrese día (1=Lunes, 2=Martes): ")

        dia = int(dia)

        nombre = input("Nombre del paciente: ")
        while not nombre.isalpha():
            print("Error: solo letras")
            nombre = input("Nombre del paciente: ")

        if dia == 1:
            if nombre == lunes1:
                lunes1 = ""
                print("Turno cancelado")
            elif nombre == lunes2:
                lunes2 = ""
                print("Turno cancelado")
            elif nombre == lunes3:
                lunes3 = ""
                print("Turno cancelado")
            elif nombre == lunes4:
                lunes4 = ""
                print("Turno cancelado")
            else:
                print("Paciente no encontrado")

        else:
            if nombre == martes1:
                martes1 = ""
                print("Turno cancelado")
            elif nombre == martes2:
                martes2 = ""
                print("Turno cancelado")
            elif nombre == martes3:
                martes3 = ""
                print("Turno cancelado")
            else:
                print("Paciente no encontrado")

    
    
    
    elif opcion == 3:
        dia = input("Ingrese día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error")
            dia = input("Ingrese día (1=Lunes, 2=Martes): ")

        dia = int(dia)

        if dia == 1:
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    
    
    
    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print("Lunes:", ocupados_lunes, "ocupados,", 4 - ocupados_lunes, "libres")
        print("Martes:", ocupados_martes, "ocupados,", 3 - ocupados_martes, "libres")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Hay empate")

    
    
    
    elif opcion == 5:
        print("Sistema cerrado")


    #Ejercicio 4 ##################

    energia = 100
    tiempo = 12
    cerraduras_abiertas = 0
    alarma = False
    codigo_parcial = ""
    veces_forzado = 0


    nombre = ""
    while nombre == "" or not nombre.isalpha():
        nombre = input("Ingresá tu nombre: ")
        if not nombre.isalpha():
            print("Solo letras.")


    while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

    
        print(f"Energía: {energia}")
        print(f"Tiempo: {tiempo}")
        print(f"Cerraduras: {cerraduras_abiertas}/3")
        if alarma:
            print("ALARMA ACTIVADA")

    
        print("1. Forzar cerradura")
        print("2. Hackear panel")
        print("3. Descansar")

    opcion = ""
while not opcion.isdigit() or opcion not in ("1", "2", "3"):
                opcion = input("Elegí una opción: ")
if opcion not in ("1", "2", "3"):
                print("Opción inválida")

    
elif opcion == "1":
                energia -= 20
                tiempo -= 2
                veces_forzado += 1
if veces_forzado == 3:
                alarma = True
                print("¡La cerradura se trabó! Alarma activada.")
else:
        if energia < 40:
                numero = ""
                while not numero.isdigit() or numero not in ("1", "2", "3"):
                    numero = input("Elegí un número del 1 al 3: ")
                if numero == "3":
                    alarma = True
                else:
                    cerraduras_abiertas += 1
                    print("¡Cerradura abierta!")
        else:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

    
if opcion == "2":
    energia -= 10
tiempo -= 3
veces_forzado = 0
for i in range(4):
            print(f"Hackeando... paso {i + 1}/4")
            codigo_parcial = codigo_parcial + "A"
if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            print("¡Cerradura abierta!")

    
elif opcion == "3":
        veces_forzado = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10


if cerraduras_abiertas == 3:
    print("victoria")
elif energia <= 0 or tiempo <= 0:
    print("derrota")
elif alarma and tiempo <= 3:
    print("derrota por bloqueo")


    
    #Ejercicio 5 ################

vida_gladiador = 100 
vida_enemigo = 100 
pociones = 3 
daño_base_ataque_pesado = 15
daño_base_del_enemigo = 12 
turno_Gladiador = True 

nombre_gladiador = input("por favor ingresa tu nombre: ")
while not nombre_gladiador.isalpha():
     print("error: solo se permiten letras")
     nombre_gladiador = input("por favor ingresa tu nombre: ")

while vida_gladiador > 0 and vida_enemigo > 0:

    
    print(f"{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = ""
    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        opcion = input("Elegí una opción: ")
        if opcion not in ("1", "2", "3"):
            print("Error: ingresá un número válido.")

if opcion == "1":
        if vida_enemigo < 20:
            daño = daño_base_ataque_pesado * 1.5
            vida_enemigo -= daño
        else:
            daño = daño_base_ataque_pesado
            vida_enemigo -= daño
        print(f"¡Atacaste al enemigo por {daño} puntos de daño!")

    
elif opcion == "2":
        print("¡Iniciás una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("Golpe conectado por 5 de daño")

    
elif opcion == "3":
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
        else:
            print("¡No quedan pociones!")

    
        vida_gladiador -= 12
        print("¡El enemigo te atacó por 12 puntos de daño!")


if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")