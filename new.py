class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print('CREATED! o_o')

    def rot(self, days, temp):
        self.mold = days * temp

or1 = Orange(10, 'red')
print(or1)
print(or1.weight)
print(or1.color)
or1.weight = 333
or1.color = 'green -.-'
print(or1.weight)
print(or1.color)