import random

usuario = input('Introduce piedra, papel o tijera ')
#computadora = 'tijera'

def seleccionar_elemento():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

computadora = seleccionar_elemento()


# Ejemplo de uso
#elemento_seleccionado = seleccionar_elemento()
#print("Elemento seleccionado:", elemento_seleccionado)


if (usuario == computadora):
    print('Empate!')

elif usuario == 'piedra':
    if computadora == 'tijera':
        print('piedra gana a tijera ')
        print('gano usuario ')
    else:
        print('papel gana a piedra ')
        print('gano computadora ')
elif usuario == 'papel':
    if computadora == 'piedra':
        print('papel gana a piedra ')
        print('gano usuario ')
    else:
        print('tijera gana a papel ')
        print('gano computadora ')
elif usuario == 'tijera':
    if computadora == 'papel':
        print('tijera gana a papel ')
        print('gano usuario ')
    else:
        print('piedra gana a tijera ')
        print('gano computadora ')