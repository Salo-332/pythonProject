def sum(a, b):
    return a + b


a, sign, b = input().split()

if sign == "+":
    print(sum(int(a), int(b)))