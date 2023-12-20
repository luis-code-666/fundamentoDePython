import random

opciones = ["piedra", "papel", "tijera"]

rondas = 1
count_usuario = 0
count_computadora = 0

while True:
    
    print("x" * 10)
    print("Ronda ", rondas)
    print("x" * 10)
    rondas += 1
    
    usuario_minuscula = input('Introduce piedra, papel o tijera => ')
    usuario = usuario_minuscula.lower()

    #computadora = 'tijera'

    computadora = random.choice(opciones)

    print('usuario eligio => ', usuario)
    print('computadora eligio => ', computadora)

    # Ejemplo de uso
    #elemento_seleccionado = seleccionar_elemento()
    #print("Elemento seleccionado:", elemento_seleccionado)


    if (usuario == computadora):
        print('Empate!')

    elif usuario == 'piedra':
        if computadora == 'tijera':
            print('piedra gana a tijera ')
            print('gano usuario ')
            count_usuario += 1
        else:
            print('papel gana a piedra ')
            print('gano computadora ')
            count_computadora += 1
    elif usuario == 'papel':
        if computadora == 'piedra':
            print('papel gana a piedra ')
            print('gano usuario ')
            count_usuario += 1
        else:
            print('tijera gana a papel ')
            print('gano computadora ')
            count_computadora += 1
    elif usuario == 'tijera':
        if computadora == 'papel':
            print('tijera gana a papel ')
            print('gano usuario ')
            count_usuario += 1
        else:
            print('piedra gana a tijera ')
            print('gano computadora ')
            count_computadora += 1
    
    if count_usuario == 2:
        print('Gano Usuario', count_usuario)
        break
    if count_computadora == 2:
        print('Gano Computadora', count_computadora)
        break