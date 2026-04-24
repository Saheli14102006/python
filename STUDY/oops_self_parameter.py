class Employee:
    # name='Saheli'
    language='Py' #language is a class attribute and also the salary
    salary=99999999

    def getinfo(self):
        print(f'Salary = {self.salary}\nLanguage = {self.language}')

    @staticmethod     #we don't want any object inside the function because of that it's under staticmethod
    def greet():
        print('Good Evening')

Saheli=Employee()
Saheli.language='C'
Saheli.name='Saheli Mondal' #name is the instance atrribute because it is belong to the object named 'Saheli'
# print(Saheli.name,Saheli.language,Saheli.salary)

Saheli.getinfo()  #this syntax converts itself into 'Employee.getinfo(Saheli)' 
Saheli.greet()