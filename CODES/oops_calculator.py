class Calculator():
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f'The Square of {n} is {self.n*self.n}')
    def cube(self):
        print(f'The Cube of {n} is {self.n*self.n*self.n}')
    def square_root(self):
        print(f'The Squareroot of {n} is {self.n**1/2}')

n=int(input('Enter a number'))
a=Calculator(n)
a.square()
a.cube()
a.square_root()