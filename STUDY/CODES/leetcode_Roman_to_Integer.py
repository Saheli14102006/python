def romanToInt(s):
    I='I'
    V='V'
    X='X'
    L='L'
    C='C'
    D='D'
    M='M'
    for i in s:
        if i==I or i==V or i==X or i==L or i==C or i==D or i==M:
            I = 1
            V = 5
            X = 10
            L = 50
            C = 100
            D = 500
            M = 1000

            pass
        # print(i)

s=input('Enter')
romanToInt(s)



        