class sample():
    a=8
    
    @classmethod
    def show(cls):
        print(f'The class attribute of a is {cls.a}')
        
    @property
    def name(self):
        return f'{self.fname} {self.lname}'
    
    @name.setter
    def name(self,value):
        self.fname= value.split(" ")[0]
        self.lname= value.split(" ")[1]

b=sample()
b.a= 88

b.name=input('Enter name')
print(b.fname,b.lname)

b.show()