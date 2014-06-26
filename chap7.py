# Enter your answrs for chapter 7 here
# Name:


# Ex. 7.5
import math


def fact(k):
    
    if k == 0:
        return 1
    else:
        rec = fact(k-1)
        result = k * rec
        return result

def estimate_pi():

    t = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = fact(4*k) * (1103 + 26390*k)
        den = fact(k)**4 * 396**(4*k)
        term = factor * num / den
        t += term
        
        if abs(term) < 1e-15: break
        k += 1
    print k
    return 1 / t

print estimate_pi()
# How many iterations does it take to converge?
# it takes 2 iterations.