import my_lib1 
#save to our_lib1

class Person(object):
	__name = ""
	__sec_name = ""
	"""docstring for Person"""
	def __init__(self, name, sec_name=""):
		self.__name = name
		self.__sec_name = sec_name 

	def set_name(self, name):
		self.__name = name
		

	def set_sec_name(self, sec_name):
		self.__sec_name = sec_name


	def get_name(self):
		return self.__name
		

	def get_sec_name(self):
		return self.__sec_name



class Teacher(Person):
	"""docstring for Teacher"""
	def __init__(self, name, sec_name):
		self.__name = name
		self.__sec_name = sec_name 

	def get_name(self):
		return self.__name
		

	def get_sec_name(self):
		return self.__sec_name
		

tech1 = Teacher("Maria", "Ivanovna")

print(tech1.get_name()+ " " + tech1.get_sec_name())

