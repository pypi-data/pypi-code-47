#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
"""
_________                                                   ______              
__  ____/_____________________________________  ________ ______  /______________
_  /    __  ___/  __ \_  ___/_  ___/_  __ \  / / /_  __ `__ \_  __ \  _ \_  ___/
/ /___  _  /   / /_/ /(__  )_(__  )_  / / / /_/ /_  / / / / /  /_/ /  __/  /    
\____/  /_/    \____//____/ /____/ /_/ /_/\__,_/ /_/ /_/ /_//_.___/\___//_/     
                                                                                
A collection of functions which may be of use when solving crossnumber puzzles.
Author: Adam Vellender
dev@vellender.com
"""

def binomial(x, y):
    """Binomial coefficients"""
    from math import factorial as fac
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom

def isAnagram(m,n):
    """Takes two numbers (or words) as inputs, returns True only if they're anagrams"""
    if sorted(str(m))==sorted(str(n)):
        return True
    else:
        return False
    
def digitSum(n):
    """Digit sum"""
    return sum([int(a) for a in str(n)])    
  
def digitProduct(n):
    """Digit product"""
    a = 1
    for b in str(n):
        a = a * int(b)
    return a

def primes(n):
    """Primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return tuple([2] + [i for i in range(3,n,2) if sieve[i]])

def pol(n):
    """Primes of length n."""
    return tuple(filter(lambda x: x>=10**(int(n)-1), primes(10**n)))

def sol(n):
    """Squares of length n."""
    import numpy as np
    return [a**2 for a in range(int(np.ceil(np.sqrt(10**(n-1)))),int(np.ceil(np.sqrt(10**n))))]

def rev(n):
    """Reverse an integer"""
    return int(str(n)[::-1])

tri=tuple(binomial(n+1,2) for n in range(1,1000))
tri2=tuple(filter(lambda x: 9<x<100,tri))
tri3=tuple(filter(lambda x: 99<x<1000,tri))

def nthDigit(n,d):
    """d-th Digit of an integer n"""
    return int(str(n)[d-1])

def isCosy(n):
    """A ‘cosy’ number's largest digit is the sum of the two smaller ones and allows the case where the largest digit is repeatede.g. 990"""
    if sorted([int(a) for a in str(n)])[len(str(n))-1]==sum(sorted([int(a) for a in str(n)])[:-1]):#Allows any number of digits, not just 3.
        return True
    else:
        return False
    
def isFriendly(n):
    """A ‘friendly’ number is divisible by its digit sum"""
    if n%digitSum(n)==0:
        return True
    else:
        return False