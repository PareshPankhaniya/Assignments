What relationship is appropriate for Student and Person?

class EmployeeData:

    def __init__(self, sal=0, age=0):
        self.sal = sal
        self.age = age

    def getData(self):
        print("{0}+{1}j".format(self.sal,self.age))