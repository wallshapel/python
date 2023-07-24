name = 'String forma 1' # string forma 1
name2 = "String forma 2" # string froma 2, no hay diferencia con la forma 1

description = """
	Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código, se utiliza para desarrollar aplicaciones de todo tipo, ejemplos: Instagram, Netflix, Spotify, Panda3D, entre otros
""" # Se usan las triples comillas para textos grandes

print(name, name2, description) # Forma de imprimir varias variables a la vez

print(len(name)) # 'len' devuelve la longitud de la cadena name. 14

print(name[1]) # Devuelve el segundo caracter de la cadena. 't'

print(name[0:8]) # Devuelve los primeros 7 caracteres de la cadena. 'String f'

print(name[9:]) # Devuelve desde el caracter 10 hasta el final de la cadena. 'rma 1'

print(name[:8]) # Devuelve desde el comienzo, hasta el caracter 7  de la cadena. 'String f'

print(name[:]) # Devuelve la cadena completa

names = 'Legato Camilo'
surnames = 'Bluesummers Martínez'

full_name = names + ' ' + surnames # Con el signo + concatenamos textos y variables
print(full_name) # Devuelve Legato Camilo Bluesummers Martínez

full_name2 = f"{names} {surnames}" # Otra forma de concatenar
print(full_name2) # Devuelve Legato Camilo Bluesummers Martínez

print(f"{names[1]} {2 + 5}") # Devuelve el segundo carcter de la cadena 'names' y el resultado de la operación 2 + 5. 'e 7'
