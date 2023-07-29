class Car(): # Definición de la clase

	# Constructor
	def __init__(self, chasis_height, chasis_width, wheels, state):
		self.__chasis_height = chasis_height # Los '__' antes del nombre de la propiedad equivale al private de otros lenguajes
		self.__chasis_width = chasis_width
		self.__wheels = wheels
		self.__state = state
	
	# Métodos
	def on(self): # 'self' equivale al this de otros lenguajes. En python toca ponerlo como primer argumento obligatoriamente
		self.__state = True
	def off(self):
		self.__state = False
	def get_chasis_height(self):
		return self.__chasis_height
	def get_chasis_width(self):
		return self.__chasis_width
	def get_wheels(self):
		return self.__wheels
	def get_state(self):
		return self.__state

my_car = Car(250, 120, 4, False) # Creamos una nueva instanciamos de la clase 'Car'. A diferencia de otros lenguajes, no se usa el operador 'new'

print(my_car.get_chasis_height()) # Devuelve 250
my_car.on() # Encedemos el carro
print(my_car.get_state()) # Devuelve True porque el carro está en marcha
my_car.off() # Apagamos el carro
print(my_car.get_state()) # Devuelve False porque el carro está apagado