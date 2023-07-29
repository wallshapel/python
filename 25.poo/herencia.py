##########################################################
class Vehicle():
    def __init__(self, trade_mark, model):
        self.__trade_mark = trade_mark
        self.__model = model
        self.__state = False
        self.__acelerate = False
        self.__stop = False
    # Métodos
    def on(self):
        self.__state = True
    def acelerate(self):
        self.__acelerate = True
    def curb(self): # frenar
        self.__stop = True
    def show(self):
        print('Trade mark: ', self.__trade_mark, '\nModel: ', self.__model, '\nState: ', self.__state, '\nAcelerating: ', self.__acelerate, '\nCurbing: ', self.__stop)
##########################################################
class Electric_Vehicle():
	def __init__(self):
		self.__state = 0
		self.__charging = False
	def charge(self):
		self.__charging = True
##########################################################
class Moto(Vehicle): # Herencia simple
    pass
##########################################################
class Electric_Bicycle(Vehicle, Electric_Vehicle): # Herencia múltiple
	pass
##########################################################
myMoto = Moto('Honda', 'CBR')
myMoto.show()
bycicle = Electric_Bicycle('Scott', 'Spark RC') # Al haber puesto de primero a la clase 'Vehicle' en el orden de herencia mútiple, se toma el constructor de esta clase por encima del constructor de Electric_Vehicle
# Sin embargo y para este caso, si se hubiera puesto de primero a la clase Electric_Vehicle en el orden de la herencia múltiple, entonces luego no se puede acceder al método show que requiere que se pasen argumentos al constructor, pero la clase Electric_Vehicle no recible parámetros, lo constituiría en un Error
bycicle.show()
