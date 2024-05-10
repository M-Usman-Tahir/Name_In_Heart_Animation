import numpy as np

class AlphabetsGraphics():
    def __init__(self):
        self.__alphas = {"A": self.__A, "B": self.__B, "C":self.__C, "D": self.__D, "E": self.__E, "F": self.__F, "G": self.__G, "H": self.__H, "I": self.__I, "J": self.__J, "K": self.__K, "L": self.__L, "M": self.__M, "N": self.__N, "O": self.__O, "P": self.__P, "Q": self.__Q, "R": self.__R, "S": self.__S, "T": self.__T, "U": self.__U, "V": self.__V, "W": self.__W, "X": self.__X, "Y": self.__Y, "Z": self.__Z}

    def __Map(self, f, l): return np.array(list(map(f, l)))
    def  __line(self, x): return 0*x

    def get(self, alpha : str):
        return lambda x : self.__Translate(self.__alphas[alpha.upper()](x))

    def __Translate(self, c):
        x, y = [], []
        for i in c:
            x += list(i[0]) + [np.nan]
            y += list(i[1]) + [np.nan]
        return np.array(x), np.array(y)

    def __A(self, x):
        def a(x): return np.sin(x*np.pi)
        def a2(x): return 0*x+0.5 if (x > 0.17) & (0.83 > x) else np.nan
        return [(x, a(x)), (x, self.__Map(a2, x))]

    def __B(self, x):
        def b(x): return abs(np.sin(x*np.pi*2))
        return [(self.__line(x), x), (b(x), x)]

    def __C(self, x):
        def c(x): return -np.sin(x*np.pi)
        return [(c(x)+1, x)]

    def __D(self, x):
        def d(x): return np.sin(x*np.pi)
        return [(self.__line(x), x), (d(x), x)]

    def __E(self, x):
        return [(x, self.__line(x)), (x*0.75, self.__line(x)+.5), (x, self.__line(x)+1), (self.__line(x), x)]

    def __F(self, x):
        return [(x*0.75, self.__line(x)+.5), (x, self.__line(x)+1), (self.__line(x), x)]

    def __G(self, x):
        def g(x): return -np.sin(x*np.pi)
        return [(g(x)+1, x), (x[len(x)//2:], self.__line(x[len(x)//2:])+.5), (self.__line(x[:len(x)//2])+1, x[:len(x)//2])]

    def __H(self, x):
        return [(x, self.__line(x)+.5), (self.__line(x), x), (self.__line(x)+1, x)]

    def __I(self, x):
        def i(x): return 0*x if (x > 0.18) & (0.82 > x) else np.nan
        return [(x, self.__Map(i, x)), (x, self.__Map(i, x)+1), (self.__line(x)+0.5, x)]

    def __J(self, x):
        joint = int(len(x)/8.4)
        def u(x): return abs((x-0.5)**3)*0.9
        return [(x, self.__line(x)+1), (x/2, u(x)), (self.__line(x[joint:])+0.5, x[joint:])]

    def __K(self, x):
        return [(self.__line(x), x), (x, x*.5+.5), (-x+1, x*.5)]

    def __L(self, x):
        return [(x, self.__line(x)), (self.__line(x), x)]

    def __M(self, x):
        def m(x): return abs(np.sin(x*np.pi*2))
        return [(x, m(x))]

    def __N(self, x):
        def n(x): return .5+.5*np.sin(x*np.pi *
                                      2) if x >= (1/4) and 3/4 >= x else np.nan
        return [(self.__line(x), x), ((x-1/4)*2, self.__Map(n, x)), (self.__line(x)+1, x)]

    def __O(self, x):
        k = 0.5
        h = 0.5
        r = 0.5
        def o(x): return k + np.sqrt(r**2-(x-h)**2)
        return [(x, o(x)), (x, -o(x)+1)]

    def __P(self, x):
        def p(x): return abs(np.sin(x*np.pi*2))
        return [(self.__line(x), x), (p(x[len(x)//2:]), x[len(x)//2:])]

    def __Q(self, x):
        k = 0.5
        h = 0.5
        r = 0.5
        def o(x): return k + np.sqrt(r**2-(x-h)**2)
        return [(x, o(x)), (x, -o(x)+1), (-x[:len(x)//3]+1, x[:len(x)//3])]

    def __R(self, x):
        def r(x): return abs(np.sin(x*np.pi*2))
        return [(self.__line(x), x), (r(x[len(x)//2:]), x[len(x)//2:]), (-x+1, x*.5)]

    def __S(self, x):
        def s(x): return -np.cos(x*np.pi*2.7+0.4)/2 + .5
        return [(s(x), x)]

    def __T(self, x):
        return [(x, self.__line(x)+1), (self.__line(x)+0.5, x)]

    def __U(self, x):
        joint = int(len(x)/8.4)
        def u(x): return abs((x-0.5)**3)*0.9
        return [(x, u(x)), (self.__line(x[joint:]), x[joint:]), (self.__line(x[joint:])+1, x[joint:])]

    def __V(self, x):
        def v(x): return np.cos(x*np.pi*2)
        return [(x, .5+v(x)*.5)]

    def __W(self, x):
        def w(x): return abs(np.sin(x*np.pi*2))
        return [(x, -w(x)+1)]

    def __X(self, x):
        return [(x, x), (-x+1, x)]

    def __Y(self, x):
        return [(x, x), (-x[len(x)//2:]+1, x[len(x)//2:])]

    def __Z(self, x):
        return [(x, self.__line(x)), (x, x), (x, self.__line(x)+1)]
