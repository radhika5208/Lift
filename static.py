#import Adafruit_BBIO_GPIO as g
import sys
import time
dp=0
while 1:
  choice=map(int,raw_input("Enter your choice:"))
 
  if(choice[0]==dp):
    print "You are at same floor"
  if(choice[0]>dp):
    tp=choice[0]-dp
    for i in range(tp+1):
      pin="P8_"+str(7+dp+i)
      #g.setup(pin,#g.OUT)
      #g.output(pin,#g.HIGH)
      time.sleep(1)
      #g.setup(pin,#g.OUT)
      #g.output(pin,#g.LOW)
    dp=choice[0]
    print "Reached to floor"
  elif (choice[0]<dp):
    tp=dp-choice[0]
    for i in range(tp+1):
      pin="P8_"+str(7+dp-i)
      #g.setup(pin,#g.OUT)
      #g.output(pin,#g.HIGH)
      time.sleep(1)
      #g.setup(pin,#g.OUT)
      #g.output(pin,#g.LOW)
    dp=choice[0]
    print "Reached to floor"
#g.cleanup()
