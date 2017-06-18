import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down = GPIO.PUD_UP)

f = open("/home/pi/test.txt", "r")
count=f.readline()
f.close()
c = int(count)

f = open("/home/pi/test.txt", "w")

while True:
    time.sleep(0.2)
    if(GPIO.input(40) == 0):
        c+=1
        print (c)
        f.seek(0)
        f.truncate()    
        f.write(str(c))
        f.flush()
        time.sleep(0.1)
        while GPIO.input(40) == 0:
            pass
    
f.close()
GPIO.cleanup()



