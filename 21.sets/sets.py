# set en python significa grupo o colección

set1 = { 1, 1, 2, 2, 3, 4 }
print(set1) # Devuelve 1, 2, 3, 4. los elementos repetidos son excluidos

set1.add(5) # Agrega 5 al final del set. si el elemento a agregar ya existe, no lo agrega
print(set1) # Devuelve 1, 2, 3, 4, 5

set2 ={ 3, 4, 6, 7, 8, 9 }

# Operadores con sets
print(set1 | set2) # Hace una unión del set1 y el set2
print(set1 & set2) # Realiza una interesección entre ambos sets. 3, 4
print(set1 - set2) # Devuelve solo los elementos del sey1 y quita los elementos que haya en común entre el set1 y el set2
print(set1 ^ set2) # Devuelve los elementos de ambos sets, menos los que estén repetidos

# No podemos acceder a los índices de los sets, pero si podemos buscar un elemento
if 5 in set1:
	print('found')
