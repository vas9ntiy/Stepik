A=int(input('min'))
B=int(input('max'))
H=int(input('your time'))

if H<A:
    print ('Недосып')
elif H>B:
    print ('Пересып')
else:
    print ('Это нормально')