num = 1
while num < 20:
	print(num)
	num += 1

command = ''
while command.lower() != 'exit': # El ciclo while no termina hasta que no se ingrese 'exit'
	command = input('$ ')
	print(command)

while True: #ciclo infinito
	command = input('$ ')
	print(command)
	if command.lower() == 'exit':
		break # Recomendable siempre que se trabaja con ciclos infinitos