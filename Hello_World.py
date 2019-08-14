import time

class Robot:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print("Hello World From" + self.name  + "!")
		time.sleep(2)
		print("Goodbye cruel World! lol")
		time.sleep(1)


p1 = Robot("Python")
p1.say_hi()



