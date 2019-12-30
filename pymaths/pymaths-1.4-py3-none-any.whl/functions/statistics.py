'''
STATISTICS
'''

__author__ = "Matthew Byrne"
__date__ = "11/12/19"

# Import
from math import sqrt
from pymaths.functions.pure import sigma, factorial

# Functions

## MEAN ##
def mean(Set):
    return sum(Set)/len(Set)

## ST DEVIATION ##
def stdev(Set):
    variation = (sigma(Set, "x**2")/len(Set))-mean(Set)
    return sqrt(variation)

## COMBINATIONS ##
def C(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

## PERMUTATIONS ##
def P(n, r):
    return factorial(n)/factorial(n-r)

## BINOMIAL DISTRIBUTION ##
class B: 
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def P(self, X):
        return round(C(self.n, X) * (self.p**X) * ((1-self.p)**(self.n-X)), 5)

    def greaterP(self, X):
        total = 0
        for i in range(X+1, self.n+1):
            total += self.P(i)

        return total

    def greaterEquP(self, X):
        total = 0
        for i in range(X, self.n+1):
            total += self.P(i)

        return total

    def lesserP(self, X):
        total = 0
        for i in range(0, self.X):
            total += self.P(i)

        return total

    def lesserEquP(self, X):
        total = 0
        for i in range(0, self.X+1):
            total += self.P(i)

        return total






## TESTING ##
if __name__ == "__main__":
    a = B(10, 1/24) # on a calculator this would normally be this
    print(a.P(6)) # it's essentially 0