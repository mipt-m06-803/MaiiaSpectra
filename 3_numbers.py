a=int(input())
b=int(input())
c=int(input())
D=(b**2 - 4*a*c)**0.5
if (b**2 - 4*a*c)<0:
    print('нет корней')
else :
    x1=(-b+D)/(2*a)
    x2=(-b-D)/(2*a)
    if x1==x2 :
        print(x1)
    elif x1 > x2:
        print(x2, x1)
    else :
        print(x1, x2)
