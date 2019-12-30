''' Maths Module '''
__author__ = "Matthew Byrne"
__date__ = "11/12/19"

# Import
from sympy import limit, Symbol


# functions

    ## EQUATION PARSING ##
def parseEquationIntegration(originalFunction):
    def wrapperFunc(equation, *args):    
        equation = (equation.replace(" ", "").replace("-", "+-").split("+"))
        
        for i, item in enumerate(equation):
            if "x" not in item:
                equation[i] = f"({item}*x)"

            elif "x" in item and "^" not in item:
                equation[i] = f"(({item}^2)/2)"

            else:
                exp = str(int(item[item.find("^")+1:])+1)
                item = item[:item.find("^")]
                equation[i] = f"(({item}^{exp})/{exp})"

        newEqu = "+".join(equation).replace("^", "**")

        return originalFunction(newEqu, *args)
    return wrapperFunc

def parseEquationDifferentiation(originalFunction):
    def wrapperFunc(equation, *args):    
        equation = (equation.replace(" ", "").replace("-", "+-").split("+"))

        for i, item in enumerate(equation):
            if "x" not in item:
                equation[i] = "0"

            elif "x" in item and "^" not in item:
                try:
                    equation[i] = str(int(equation[i-1]))

                except:
                    equation[i] = equation[i].replace("x", "")

            else:
                exp = item[item.find("^")+1:]
                item = item[:item.find("^")]
                try:
                    equation[i] = f"({exp}*({item}**{int(exp)-1}))"
                except:
                    equation[i] = f"({exp}*({item}**[{exp}-1]))"


        newEqu = "+".join(equation).replace("^", "**")

        return originalFunction(newEqu, *args)
    return wrapperFunc






    ## INTEGRATION ##
def definiteIntegral(originalFunction):
    @parseEquationIntegration
    def wrapperFunc(equation, start, end):
        a = equation.replace("x", str(end))
        b = equation.replace("x", str(start))
        output = eval(a) - eval(b)

        return originalFunction(output)
    return wrapperFunc

def indefiniteIntegral(originalFunction):
    @parseEquationIntegration
    def wrapperFunc(equation, *args):
        equation = equation.replace("(", " ").replace(")", " ").replace("1*", "").replace("+ -", "- ").replace("+-", "- ").replace("+0", "").replace("-0", "").replace("+ 0", "").replace("- 0", "").replace("+", "+ ").replace("* x", "x").replace("**1", "").replace("  ", " ")
        return originalFunction(equation, *args)
    return wrapperFunc






    ## Differentiation ##
def definiteDerivative(originalFunction):
    @parseEquationDifferentiation
    def wrapperFunc(equation, x, *args):
        output = eval(equation.replace("x", f"{x}"))
        return originalFunction(output, *args) 
    return wrapperFunc

def indefiniteDerivative(originalFunction):
    @parseEquationDifferentiation
    def wrapperFunc(equation, *args):
        equation = equation.replace("(", " ").replace(")", " ").replace("1*", "").replace("+ -", "- ").replace("+-", "- ").replace("+0", "").replace("-0", "").replace("+ 0", "").replace("- 0", "").replace("+", "+ ").replace("* x", "x").replace("**1 ", " ").replace("  ", " ").replace("[", "(").replace("]", ")")
        return originalFunction(equation, *args)
    return wrapperFunc



@indefiniteDerivative
def differentiate(x):
    return x

@indefiniteIntegral
def integrate(x):
    return x


''' TEST SECTION '''
if __name__ == "__main__":
    @definiteDerivative
    def Print(inp):
        return inp


    print(Print("x^5", 4))
