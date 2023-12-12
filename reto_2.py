# Agregar la letra G al final de la lista.
# Reemplazar la letra en la posición 0 con la letra Z.
# Eliminar la letra C de la lista.
# Imprimir la lista resultante al revés.
# Input: ["A", "B", "C", "D", "E", "F"]
# Output: ["G", "F", "E", "D", "B", "Z"]

letters = ["A", "B", "C", "D", "E", "F"]
letters.append('G')
letters[0] = 'Z'
letters.remove('C')
letters.reverse()
print(letters)
