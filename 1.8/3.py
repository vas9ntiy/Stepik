a=int(input('Time to sleep in minutes'))
b=int(input('What hour is it now?'))
c=int(input('What minute is it now?'))
d=b*60+c
print((d+a)//60)
print((d+a)%60)

#d - start point of time
#print((d+a)//60) - (start point + time of sleeping)in minutes//60
#print((d+a)%60)