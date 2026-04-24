class Employee():
    a=99
    def ok(self):
        print('hey')
class Show(Employee):
    b=100
    def greet(self):
        super().ok()
        print('hello!!')
class Register(Show):
    c=110

s=Employee()
print(s.a)
t=Show()
print(t.a,t.b)
r=Register()
print(r.a,r.b,r.c)
t.greet()
