name = "Luis"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))


print("luis" + "banda")
print(12 +12)
print("luis" + "12")

age = 12
print("Mi edad es " + str(age))
print(f"Mi edad es {age}")

age = input('Escribe tu edad => ')
print(type(age))
age = int(age)
age += 12
print(f"tTu edad es 10 anios sera {age}")

print("*****" * 7)

name = 'luis'
print(name)
age = '30'
print(age)
total = 10 + int(age)
template = f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años"
print(template)