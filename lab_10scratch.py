class Student():
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.courses = []

    def __str__(self):
        return self.name

    def add_courses(self, courses):
        return self.courses.extend(courses) #takes a list of courses and adds it to list of courses that the student is taking

derrick = Student('Derrick', 'User Experience') #don't need to include self here because it's already included
#print(derrick)
# outputs: <__main__.Student object at 0x10cd1bb50>
# # just tells you that inside of the main module, there is a Student object
# but it doesn't tell you anything else (name or major)
# this is why you call __str__() method to get more info (liines 7-8)
derrick.add_courses(['SI 501', 'SI 506', 'SI 582', 'SI 588'])
print(derrick)
print(derrick.courses)

