from student import Student

# Create at least 10 students

s1 = Student('Kevin', 'Chiteri')
s2 = Student('Allan', 'M.', 'UG')
s3 = Student('Test','K','KE')
s4 = Student('Rama', "K", 'TZ')
s5 = Student("John", "Morgin", "UG")
s6 = Student("Juma", "Morgin", "UG")
s7 = Student("Moris", "Morgin", "UG")
s8 = Student("Juma", "Chege", "UG")
s9 = Student("Eliud", "Kamau", "UG")
s10 = Student("Juma", "Waithera", "UG")
s1.attend_class(loc='Andela',teacher='Alex', date='18/09/2016')
s2.attend_class(loc='Andela',teacher='Alex', date='18/09/2016')
s3.attend_class(loc='Andela',teacher='Alex', date='19/09/2016')
s4.attend_class(loc='Andela',teacher='Alex', date='19/09/2016')
s5.attend_class(loc='Andela',teacher='Alex', date='19/09/2016')
print(Student.get_attendance('18/09/2016'))
print(Student.get_attendance('19/09/2016'))

# You should be able to print the list of
# students who attend class on particular day



