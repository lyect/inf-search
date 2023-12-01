from flask_sqlalchemy import SQLAlchemy

class MyDatabase(SQLAlchemy):

	def __init__(self, username, password, address, name):

		super().__init__()

		self.__username = username
		self.__password = password
		self.__address = address
		self.__name = name

	def getURI(self):
		return "mysql://" +  self.__username + ":" + self.__password + "@" + self.__address + "/" + self.__name

db = MyDatabase("lyect", "12345678", "localhost", "InfSearchPythonDatabase")