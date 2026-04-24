class Programmer():
    company='Micosoft'
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer('Saheli Mondal',9999999, 700006)
print(p.name,p.salary,p.pin,p.company)
t=Programmer('Tomojit Bhattacharjee',9999999, 700006)
print(t.name,t.salary,t.pin,t.company)
