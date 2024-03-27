import math

a=input()
b=input()
c=input()

def fun(a, b, c):
    d=b*b-4*a*c
    if d>=0:
        print((math.sqrt(d)-b)/2*a,(-math.sqrt(d)-b)/2*a)
    elif d==0:
        print("중근을 갖습니다.")
    elif d<0:
        print("근이 존재하지 않습니다.")

fun(a, b, c)