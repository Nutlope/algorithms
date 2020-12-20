class Student: 
    def __init__(self, firstName, lastName, year):
        self.firstName = firstName
        self.lastName = lastName
        self.year = year
        self.late = 0
    
    def fullName(self):
        return self.firstName + " " + self.lastName
    
    def addLates(self):
        self.late+=1
        return 'You have been late {lates} times'.format(lates = self.late)

firstStudent = Student("Hassan", "El Mghari", 5)
firstStudent.addLates()
firstStudent.addLates()
firstStudent.addLates()
firstStudent.addLates()
print(firstStudent.addLates())