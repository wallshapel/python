def divide(n1, n2):
	try:
		return n1 / n2
	except ZeroDivisionError: # ZeroDivisionError es el nombre del error que arroja python al intentar dividir por cero. 
		print('You can\'t to divide by zero')
		return 'wrong operation'

while True:
	try:
		n1 = float(input('Enter a number: '))
		n2 = float(input('Enter an other number: '))
		break
	except ValueError: # Si no se especifica un tipo de excepcion en except, entonces se considera excepción general, para cualquier tipo de error
		print('Invalid number')
	finally:
		print('This will run whether or not there are errors') # Esto siempre se ejecutara se hayan producido o no errores

print(divide(n1, n2))


# Excepciones personalizadas
def check_age(age):
	if age < 0:
		# 'raise' nos permite capturar el error
		# Podemos usar TypeError o cualquiera de los tipos de errores de la biblioteca de python. Inluso crear nuestra propia clase de error
		raise TypeError('Negative ages are not allowed')

try:
	print(check_age(-18))
except TypeError as NegativeError:
	print(NegativeError) # Esto hará que se imprime el mensaje capturado con 'raise'

print('more code...')