a=int(input('1'))
if 0<=a<=2000:
    if a%20==0 or a%20==5 or a%20==6 or a%20==7 or a%20==8 or a%20==9 or a%20==10 or a%20==15 or a%20==16 or a%20==17 or a%20==18 or a%20==19 or a%100==11 or a%100==12 or a%100==13 or a%100==14:
        print(str(a)+' программистов')
    elif a%20==1 or a%100==31 or a%100==51 or a%100==71 or a%100==91:
        print(str(a)+' программист')
    else :
        print(str(a) + ' программистa')