class Employee():
    def __init__(self):
        print('Constructor of Employee')
    a=99
class Show(Employee):
    def __init__(self):
        super().__init__()
        print('Constructor of Show')
    b=100
class Register(Show,Employee):
    def __init__(self):
        super().__init__()
        print('Constructor of Register')
    c=110

s=Employee()
print(s.a)
t=Show()
print(t.b)
r=Register()
print(r.a,r.b,r.c)