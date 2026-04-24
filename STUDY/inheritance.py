class Employee():
    company='ITC'
    name='Saheli Mondal'
    designation='Software Engineer'
    salary=9999999999
    def show(self):
        print(f'The name of the Employee is {self.name} and the salary is {self.salary}.')

class Programmer(Employee):
    company='ITC Infotech'
    language='C,Python'
    def showLanguage(self):
        print(f'The name is {self.name} and she is good with {self.language} language.')

class designation(Programmer):
    def role(self):
        print(f'The designation of {self.name} is {self.designation} in {self.company} company. Her speciality is she is good with {self.language}.')
    
a= Employee()
b= Programmer()
c= designation()
# print(a.company,b.company)
c.show()
c.showLanguage()
c.role()
