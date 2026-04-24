class Employee:
    # name='Saheli'
    language='Py' #language is a class attribute and also the salary
    salary=99999999

    def __init__(self,name,language,salary):  #It's a Dunder Method and only init func is automatically called. The function with double underscore is called Dunder
        self.name=name
        self.language=language
        self.salary=salary
        print('I am creating an object')


    def getinfo(self):
        print(f'Salary = {self.salary}\nLanguage = {self.language}')

    @staticmethod     #we don't want any object inside the function because of that it's under staticmethod
    def greet(self):
        print('Good Evening')

Saheli=Employee('Saheli Mondal','C',999999999)
# Saheli.name='Saheli Mondal'
print(Saheli.name,Saheli.salary,Saheli.language)

# Tomojit=Employee()