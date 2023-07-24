gas = True
on = True

if gas and on: # devuelve True
	print('You can continue')
else:
	print('You cannot continue')

gas = False
on = True

if gas and on: # Devuelve False
	print('You can continue')
else:
	print('You cannot continue')

gas = False
on = True

if gas or on: # Devuelve True
	print('You can continue')
else:
	print('You cannot continue')

gas = False
on = False

if gas or on: # Devuelve False
	print('You can continue')
else:
	print('You cannot continue')

gas = False
on = False

if gas or not on: # 'not' aplica para 'on', es decir tomará el valor contrario de 'on'. 'on' tiene False, por lo tanto lo tomará como True. Por lo tanto la operación completa devolverá True
	print('You can continue')
else:
	print('You cannot continue')


age = 25
if 15 <= age < 50:
	print('You can enter the pool')
else:
	print('You cannot enter the pool')