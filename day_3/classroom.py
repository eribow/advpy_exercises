class Person:
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def printFullName(self):
        print(self.firstName  + " " + self.lastName)


class Student(Person):
    def __init__(self, fn, ln, subject):
        super(Student, self).__init__(fn, ln)
        self.subject = subject

    def printStudent(self):
        print(self.firstName +  " " + self.lastName + ", " + self.subject)


class Teacher(Person):
    def __init__(self, fn, ln, course):
        super(Teacher, self).__init__(fn, ln)
        self.course = course

    def printTeacher(self):
        print(self.firstName +  " " + self.lastName + ", teaches \"" + self.course + "\"")
