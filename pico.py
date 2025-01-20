from machine import Pin
from utime import sleep
 
relay1=Pin(16,Pin.OUT)
relay2=Pin(17,Pin.OUT)
relay1.value(1)
relay2.value(1)

'''
while True:
    relay1.value(0)
    sleep(0.2)
    relay1.value(1)
    sleep(0.1)
'''


while True:
    order=int(input())
    if(order==1):
        relay1.value(0) #on
        relay2.value(1) #off
        sleep(5)
        relay1.value(1)
        relay2.value(1)
        
    elif(order==2):
        relay2.value(0) #on
        relay1.value(1) #off
        sleep(5)
        relay1.value(1)
        relay2.value(1)
        
    else:
        relay1.value(1)
        relay2.value(1)
        #sleep(1-0.1*ndown[i])
        #sleep(1-0.1*ndown[i])
    
    