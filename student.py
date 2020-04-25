class student:
	
	def __init__(self, code, name, age, gender, carreer):
		self.code = code
		self.name = name
		self.age = age
		self.gender = gender
		self.carreer = carreer

	def set_age(self,age):
		self.age = age

	def set_gender(self,gender):
		self.gender = gender

	def set_carreer(self,carreer):
		self.carreer = carreer
	
	def get_age(self):
		return ("edad: " + self.age)
		