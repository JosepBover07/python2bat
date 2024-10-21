# pensar palabra
# escribir _ _ _ _ _ _
# pedir letra
# buscar si está en la palabra
    # SI -> escribir la letra en la palabra
        # mirar si hemos acertado -> fin
    # NO -> quitar intentos-1
        # mirar si hemos perdido -> fin

palabraSecreta = "gato"

letrasCorrectas = []
letrasIncorrectas = []

seguirJugando = True
while seguirJugando == True: 
    for letra in palabraSecreta: 
        if letra in letrasCorrectas:
            print(letra,end="")
        else:
            print('_',end="")

    letraPedida = input("Dime una letra\n")

    if letraPedida in palabraSecreta:
        letrasCorrectas.append(letraPedida)
    else:
        letrasIncorrectas.append(letraPedida)

    print(f"correctas: {letrasCorrectas}")
    print(f"incorrectas: {letrasIncorrectas}")

    if set(letrasCorrectas) == set(palabraSecreta):
        seguirJugando = False
        print("Has ganado!")
    
    if len(letrasIncorrectas) == 6:
        seguirJugando = False
        print("Has perdido!")