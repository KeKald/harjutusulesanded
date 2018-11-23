from math import sqrt

class ruutvorrand:

    def __init__(self, a, b ,c):

        self.a = a
        self.b = b
        self.c = c

        self.x1 = self.solve_x1()
        self.x2 = self.solve_x2()

    def solve_x1(self):

        calc_4ac = 4 * self.a * self.c
        
        _sqrt = sqrt(self.b**2 - calc_4ac)

        x1 = (-self.b + _sqrt) / (2 * self.a)

        return x1

    def solve_x2(self):
        calc_4ac = 4 * self.a * self.c
        
        _sqrt = sqrt(self.b**2 - calc_4ac)

        x2 = (-self.b - _sqrt) / (2 * self.a)
        
        return x2

if __name__ == "__main__":
    a1 = ruutvorrand(2, 32, 4)

print(a1.x1, a1.x2)