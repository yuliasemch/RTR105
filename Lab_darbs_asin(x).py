# -*- coding: utf-8 -*-
from math import asin

def mans_arcsinuss(x):
    k = 0
    a = x
    S = a
    print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))

    while k < 4:
        k = k + 1
        R = x*x/((2*k)*(2*k+1))
        a = a * R
        S = S + a
        print("Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

    print("Izdruka no liet.f. Beigas!")
    return S

x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = asin (x)
print("standarta asin(%.2f) = %6.2f"%(x,y))
yy = mans_arcsinuss(x)
print("mans asin(%.2f) = %6.2f"%(x,yy))


print("          500")
print("        _______")
print("        \                  2*k+1")
print("         \         (2*k)!*x")
print("asin(x) = >      ___________________")
print("         /          k    2")
print("        /______    4*k(k!)*(2*k+1)")
print("          k=0")


print("                                2")
print("                               x")
print("rekurences reizinatajs: _______________")
print("                          k*2*(2*k+1)")
