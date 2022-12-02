palabra_secreta = "ivana"
intentos = 6
linea_verificada = []


print("'Bienvenido al wordle tortura de ivana'")

while intentos > 0:
    intentos = intentos-1
    palabra_ingresada = input("ingrese su palabra ")
    lista_palabras = []

    # verificamos la cantidad de letras

    while len(palabra_ingresada) != len(palabra_secreta):
        print("la palabra debe ser de 5 letras")
        print(f" Te quedan {intentos} intentos")
        palabra_ingresada = input("ingrese de vuelta la palabra ")

    # verificas las letras

    for posicion in range(5):
        if palabra_ingresada[posicion] == palabra_secreta[posicion]:
            lista_palabras.append("[" + palabra_ingresada[posicion] + "]")
        elif palabra_ingresada[posicion] in palabra_secreta:
            lista_palabras.append("(" + palabra_ingresada[posicion] + ")")
        else:
            lista_palabras.append(palabra_ingresada[posicion])

        if posicion == 4:
            linea_verificada.append(lista_palabras)

    # imprimimos cada palabra

    for iterador in range(len(linea_verificada)):
        print(linea_verificada[iterador])

    if palabra_ingresada == palabra_secreta:
        print("Felicidades!! acertaste")
        break

    elif intentos == 0:
        print("Perdiste :( ")
    print(f" Te quedan {intentos} intentos")