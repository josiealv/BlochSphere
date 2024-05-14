
class Coefficients:
    # def __init__(self, filename):
    #     self._value = load_from_file(filename)

    # @classmethod
    # def from_somewhere(cls, somename):
    #     obj = cls.__new__(cls)  # Does not call __init__
    #     super(MyClass, obj).__init__()  # Don't forget to call any polymorphic base class initializers
    #     obj._value = load_from_somewhere(somename)
    #     return obj
    
    def __init__(self, alpha:complex, beta:complex):
        self.alpha = alpha
        self.beta = beta

    def setWithReals(self, alpha, beta):
        self.alpha = complex(alpha)
        self.beta = complex(beta)
    
    def setWithComplexParams(self, alphaReal: float, alphaImag: float, betaReal: float, betaImag: float):
        self.alpha = complex(alphaReal, alphaImag)
        self.beta = complex(betaReal, betaImag)