a=int(input('1 number'))
b=int(input('2 number'))
c=(input('symbol'))
if (c=='/' or c=='mod' or c=='div') and b==0:
    print('Деление на ноль')
elif c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='/':
    print(a/b)
elif c=='*':
    print(a*b)
elif c=='mod':
    print(a%b)
elif c=='pow':
    print(a**b)
elif c=='div':
    print(a//b)
else:
    print('Error')