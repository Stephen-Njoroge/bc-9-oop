
map_ = {
    'KE': 'Kenya',
    'NG': 'Nigeria',
    'UG': 'Uganda',
    'TZ': 'Tanzania'
}

class Student(object): #inheritance
    count = 0 # class variable
    class_attendance = {} # dictionary to track class attendance -> key = date, value = list of students 
    def __init__(self, fname, lname, cc='KE'):
        # generate sequential unique ID
        Student.count += 1
        self.id = Student.count # fake private
        self.fname = fname
        self.lname = lname
        self.country = map_[cc]

    def attend_class(self, **kwargs):
    	'''
        default values:
            loc = 'Hogwarts'
            date = current_date
            teacher = 'Alex'
        '''

    	if 'date' in kwargs.keys():
    		date = kwargs['date']
    	else:
    		date = "18/08/2016"

    	if not kwargs['loc']:
    		loc = 'Hogwarts'
    	else:
    		loc = kwargs['loc']

    	if not kwargs['teacher']:
    		teacher = 'Alex'
    	else:
    		teacher = kwargs['teacher']

    	full_name = self.fname + " " + self.lname
    	if date in Student.class_attendance.keys():
    		if full_name not in Student.class_attendance[date]:
    			Student.class_attendance[date].append(self.fname + " " + self.lname)
    	else:
    		Student.class_attendance[date] = [full_name]

        # return [date, loc, teacher]


    @staticmethod
    def get_attendance(date):
    	return Student.class_attendance[date]
    	if date in Student.class_attendance.keys():
    		print(Student.class_attendance['date'].values())
    	else:
    		print("no records!")




















