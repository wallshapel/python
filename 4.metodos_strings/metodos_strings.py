animal = 'chanchito feliz'
print(animal.upper()) # Convierte la cadena en mayúscula

animal = 'Chanchito Feliz'
print(animal.lower()) # Convierte la cadena en minúscula

animal = 'chanchito FeLiz'
print(animal.capitalize()) # Convierte solo la primera letra de la cadena en mayúscula, el resto queda en minúscula

animal = 'chanchIto fEliZ'
print(animal.title()) # Convierte en mayúscula la letra inicial de cada palabra. El resto queda en minúscula

animal = '    chanchito feliz   '
print(animal.strip()) # Remueve los espacios en blanco de la izquierda y derecha de la cadena

print(animal.strip().capitalize()) # Siempre que se quiera usar un método de strings que convierta al primer o último caracter de la cadena en algo, debería usarse strip() para eliminar los espacios en blanco

animal = '    chanchito feliz     '
print(animal.lstrip()) # Quita los espacios en blanco solo de la izquierda

animal = '    chanchito feliz     '
print(animal.rstrip()) # Quita los espacios en blanco solo de la derecha

animal = 'chanchito feliz'
print(animal.find('i')) # Busca la cadena 'it' dentro de la cadena. Si lo encuentra devuelve el índice donde se ubica y por donde comienza por primera vez. Devuelve -1 en caso contrario. Es sensible a mayúsculas y minúsculas

print(animal.replace('chan', 'Chon')) # Busca la coincidencia 'chan' en la cadena, y la reemplaza por 'Chon'

print('chi' in animal) # Busca la cadena 'chi' dentro de la cadena y devuelve True o False dependiendo de si lo encuentra o no
print('chi' not in animal) # Hace lo mismo que la instrucción anterior, pero al revés