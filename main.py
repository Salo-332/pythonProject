import os
a = int(input())
b = int(input())
def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def product(a, b):
    return a * b
def delenie(a, b):
    return a / b

a, sign, b = input().split()

if sign == "+":
    print(sum(int(a), int(b)))
if sign == "-":
    print(difference(int(a), int(b)))
if sign == "*":
    print(product(int(a), int(b)))
if sign == "/":
    print(delenie(int(a), int(b)))
else:
    print("Моя твою не понимать")