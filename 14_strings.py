text = 'Ella sabe programar en Python'

'''
IN es para verificar si exite esa palabra en un texto 
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
    print('Elegiste bien!!')
else:
    print('Tambien elegita bien!!')
'''
size = len(text)
print(size)

print(text)
print(text.upper()) #coloca en mayusculas todo 
print(text.lower()) #coloca en minususculas todo el texto 
print(text.count('a')) #cuenta las letras que mencina uno

print(text.swapcase()) # transforma las mayusculas en minusculas y viceverza de un texto 
print(text.startswith('Ella')) # si comienza en esa palabra pero tiene que estar bien escrito tal cual como dice
print(text.endswith('Rust')) # si termina en esa palabra pero tiene que estar bien escrito tal cual como dice
print(text.replace('Python', 'Go')) # remplaza una palabra por otra 

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize()) #lo coloca en mayuscula la primera letra de un texto 
print(text_2.title()) #lo coloca en mayuscula la ultima palabra en primero en letra mayuscula
print(text_2.isdigit()) # esto nos dice si el texto es un digito
print("988".isdigit()) # esto nos dice si el texto es un digito

