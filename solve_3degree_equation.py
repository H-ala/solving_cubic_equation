import numpy as np
import math

def get_equation():
    a = float(input('Enter a:'))
    b = float(input('Enter b:'))
    c = float(input('Enter c:'))
    d = float(input('Enter d:'))
    return a, b, c, d


def normalize_equation(a, b, c, d):
    p=b/a
    q=c/a
    r=d/a
    a=1
    return p, q, r

def EliminateـtheـQuadraticـTerm(p, q, r):
    m = q - (p**2 / 3)
    n = (2*(p**3))/27 - (p*q/3)+r
    return m, n

def computing_delta(n, m):
    delta = (n/2)**2 + (m/3)**3
    return delta, m, n

def solving(delta, m, n):
    if delta >= 0:
        u = np.cbrt(-n/2 + np.sqrt(delta))
        v = np.cbrt(-n/2 - np.sqrt(delta))

        w = -1/2 + np.sqrt(3)/2j
        w2 = -1/2 - np.sqrt(3)/2j

        y1 = u + v
        y2 = w*u + w2*v
        y3 = w2*u + w*v
    else:
        cos_value = (-n/2)/np.sqrt(-m**3/27)
        theta = math.acos(cos_value)
        y1 = 2*np.sqrt(-m/3)*math.cos(theta/3)
        y2 = 2*np.sqrt(-m/3)*math.cos((theta-2*math.pi)/3)
        y3 = 2*np.sqrt(-m/3)*math.cos((theta-4*math.pi)/3)
    return y1, y2, y3

def solved(y1, y2, y3, p) :
    j=0
    for i in [y1,y2,y3]:
        x = i-p/3
        j+=1
        print(f'x_{j} is {x}')

def solve():
    a, b, c, d = get_equation()
    if a!=1:
        p, q, r = normalize_equation(a, b, c, d)
    else:
        p, q, r = b, c, d
    m, n = EliminateـtheـQuadraticـTerm(p, q, r)
    delta, m, n = computing_delta(n, m)
    print (delta, m, n)
    y1, y2, y3 = solving(delta, m, n)
    solved(y1, y2, y3, p)


solve()