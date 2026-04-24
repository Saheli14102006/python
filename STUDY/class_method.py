class sample():
    a=8
    @classmethod
    def show(cls):
        print(f'The class attribute of a is {cls.a}')

b=sample()
b.a= 88

b.show()