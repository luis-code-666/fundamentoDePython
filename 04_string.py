name = "Luis"
last_name = "Banda"
print(name)
print(last_name)
# aqui se concatenara las dos variables 

full_name = name + last_name
print(full_name)


# aca se puede ver cuando se usa comilla doble y cuando la simple
qoute ="i'm luis"
print(qoute)

qoute2 ='She said "Hello"'
print(qoute2)

template = "Hola mi nombre es " + name + " y mi apellido es " + last_name
print(template)

template = "Hola, mi nombre es {} y  mi apellido es {}".format(name, last_name)
print(template)