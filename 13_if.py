if True:
    print("deberia ejecutarse")

if False:
    print("Nunca se ejecuta")

pet = input(' Cual es tu mascota favorita? ')
if pet == 'perro':
    print("genial tienes buenos gusto")
elif pet == 'gato':
    print("espero tengas suerte")
elif pet == 'pez':
    print("eres lo maximo")
else:
    print("no tienes ninguna mascota interesante")

'''
    
stock = int(input('Digite el stock => '))

if stock >= 100 and stock <=1000:
    print("el stock es correcto")
else:
    print("el stock es incorrecto")
'''
###################################
#################################### si un numero es par o impar

numero = int(input('Digite un numero '))

if numero % 2 == 0:
    print('Es par! ')
else:
    print('Es impar! ')

