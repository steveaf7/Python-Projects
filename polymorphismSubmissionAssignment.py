

#creates the class called Person
class Person:
    fname = ''
    lname = ''
    height = 0
    weight = 0
    age = 0
    address = ''
    income = 75000
    #function for calculating and printing taxes based on income 
    def calcTaxes(self):
        taxes = self.income * .20
        print("Your total taxes for this year are {}".format(taxes))
        

#creates the child class

class Student(Person):
    studentId = ''
    graduateYear = ''
    income = 40000
    tuition = 8000
    #changes the cal taxes to represent student taxes at a different rate
    def calcTaxes(self):
        taxes = (self.income - self.tuition) * .10
        print("Your total taxes for this year are {}".format(taxes))


class Teacher(Person):
    employeeId = ''
    hireDate = ''
    income = 60000
    #teachers get a different tax rate
    def calcTaxes(self):
        taxes = self.income * .15
        print("Your total taxes for this year are {}".format(taxes))

if __name__ == "__main__":
    student = Student()#initializes a Student class as the object student 
    student.calcTaxes()# calls the calctaxes function for the student object
    teacher = Teacher()# initialies a teacher object with the properties of the teacher class
                       # and inherits properties from the parent class 
    teacher.calcTaxes()#calls the calc taxes funtion for the teacher object
    student2 = Student()
    student2.income = 60000
    student2.calcTaxes()
