#!/bin/env python3
#Read integer from use 
#define a function to square n 
#define a function to add-series (n): 1+2+3+...+n
#define a function factorial (n): 1*2*3*...*n
#define a main function to run the script 

def read_n():
    return int(input("N = "))

def square(n):
    return n**2

def add(n):
    s = 0
    for e in range(1,n+1):
        s += e
    return s

def factorial(n):
    s = 1
    for e in range(1,n+1):
        s *= e
    return s

def main():
    n = read_n()
    while n != -1:
        print("Square("+str(n)+") = "+str(square(n)))
        print("Add-S("+str(n)+") = "+str(add(n)))
        print("Facorial("+str(n)+") = "+str(factorial(n)))
        n = read_n()

main()

