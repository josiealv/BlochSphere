from qutip.states import basis

ALPHA_STR = "alpha"
BETA_STR = "beta"

ENTER_REAL_NUM = "Enter a real number (i.e. int) for "
ENTER_REAL_PART_STR = "Enter real part of "
ENTER_IMAGINARY_PART_STR = "Enter imaginary part of "
ENTER_Y_N = "Enter 'y' or 'n'\n"


def getQuantumStates(numQuantumStates):
    complex_array = []
    for i in range (0, numQuantumStates):
        print(f"Inputs for Quantum State #{i+1}:\n")
        alphaState = 0
        betaState = 0
        complexAlpha = input("Is alpha a complex number? " + ENTER_Y_N)
        if (complexAlpha == 'y'):
            alphaState = __getComplex(ALPHA_STR)
        else:
            alphaState = __getReal(ALPHA_STR)

        complexBeta = input("Is beta a complex number? " + ENTER_Y_N)
        if (complexBeta == 'y'):
            betaState = __getComplex(BETA_STR)
        else:
            betaState = __getReal(BETA_STR)
        
        print(f"alpha: {alphaState} and beta: {betaState}\n")
        complex_array.append((alphaState * basis(2, 0)) + (betaState * basis(2, 1)))

    return complex_array

def __getComplex(val):
    try: 
     return complex(float(input(ENTER_REAL_PART_STR + val + ':\n')), 
                   float(input(ENTER_IMAGINARY_PART_STR + val + ':\n')))
    except(ValueError, RuntimeError):
        print(f"Error occurred when inputting: {val}! Making {val} 1...")
        return complex(1)    

def __getReal(val):
    try:
        real = int(input(ENTER_REAL_NUM + val + ':\n'))
        if(real == 0):
            return complex()
        return complex(real, 0)
    except(ValueError, RuntimeError):
        print(f"Error occurred when inputting: {val}! Making {val} 1...")
        return complex(1)  
        