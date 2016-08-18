class Student(object):
	"""This is a representation of a Student
	checking system determining whether he/she failed his/her exam
	and what grade he/she scored
	"""
	def __init__(self, name, marks, subjects):
		self.name = name
		self.marks = marks
		self.subjects = subjects
	def grades(self):
		grade = ""
		mean = self.marks/ self.subjects
		if mean in range(80, 101):
			grade += "A" 
		if mean in range(70, 80):
			grade += "B"
		if mean in range(50, 70):
			grade += "C"
		elif mean in range(0, 50):
			grade += "Fail"
		return grade
	def prnt_rslts(self):
		print "%s scored %d marks which was a %s!" %(self.name, self.marks, self.grades() )
mary = Student("Mary Wangechi", 300, 5)
john = Student("John Juma", 400, 5)
anthony = Student("Anthony Duba", 200, 5)
mary.prnt_rslts()
john.prnt_rslts()
anthony.prnt_rslts()
		
"""
Here is the output:
++++++++++++++++++++++++++++++++++++++++++++++
Mary Wangechi scored 300 marks which was a C!
John Juma scored 400 marks which was a A!
Anthony Duba scored 200 marks which was a Fail!
++++++++++++++++++++++++++++++++++++++++++++++
"""

