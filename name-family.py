
#This was done pair programming there were no more computers, Camerons
#computer was not working. Cameron made some changes after a computer was available
#Cameron Alexander and Brian TRINH

class Student:
		
	courseMarks={}
	name= ""
	avg = 0
	def __init__(self, name, family):
		self.name = name
		self.family = family 
			
	def addCourseMark(self, course, mark):
		self.courseMarks[course] = mark
		print("Added course mark")
		return
		
	def average(self):
		sum = 0
		count = 0
		for key,value in self.courseMarks.items():
			print(key,value)
			sum = sum + int(value)
			count = count + 1
			
		average = sum/count	
		return average

obj1 = Student("brian","trinh")
obj1.addCourseMark("Cmput4102341","45")
obj1.addCourseMark("Cmput410234341","90")
obj1.addCourseMark("Cmput41021","90")
print(obj1.average())


	
