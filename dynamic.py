#import Adafruit_BBIO.GPIO as g
import sys
import time as t
dp=0
max1=5

def upward(dp,tp):
   for i in range(tp+1):
      pin="P9_"+str(11+dp+i)
      print "Floor No: "+str(dp+i)
      #g.setup(pin,g.OUT)
      #g.output(pin,g.HIGH)
      t.sleep(1)
      #g.setup(pin,g.OUT)
      #g.output(pin,g.LOW)
   #g.setup(pin,g.OUT)
   #g.output(pin,g.HIGH)
   print "Reached To Floor"
   t.sleep(3)
   #g.setup(pin,g.OUT)
   #g.output(pin,g.LOW)

def downword(dp,tp):
   for i in range(tp+1):
      pin="P9_"+str(11+dp-i)
      #g.setup(pin,g.OUT)
      #g.output(pin,g.HIGH)
      print "Floor No: "+str(dp-i)
      t.sleep(1)
      #g.setup(pin,g.OUT)
      #g.output(pin,g.LOW)
   #g.setup(pin,g.OUT)
   #g.output(pin,g.HIGH)
   print "Reached To Floor"
   t.sleep(3)
   #g.setup(pin,g.OUT)
   #g.output(pin,g.LOW)

while 1:
  choice=map(int,raw_input("Enter your choice:"))

  if(dp<=(max1/2)):
   for item in choice:
       item=int(item)
   choice.sort()
   print choice
   length=len(choice)
   for j in range(0,length):

      if(choice[j]>max1):
        print "MAXIMUM FLOOR REACHED"

      elif(choice[j]==dp):
        print "You are at same floor"

      elif(choice[j]>dp & choice[j]<=max1):
        tp=choice[j]-dp
        upward(dp,tp)
        dp=choice[j]

      elif (choice[j]<dp):
        tp=dp-choice[j]
        downword(dp,tp)
        dp=choice[j]

  else:
    for item in choice:
        item=int(item)
    choice.sort(reverse=True)
    print choice
    length=len(choice)
    for j in range(0,length):

      if(choice[j]>max):
        print "WRONG INPUT...!"

      elif(choice[j]==dp):
        print "You are at same floor"

      elif(choice[j]>dp):
        tp=choice[j]-dp
        upward(dp,tp)
        dp=choice[j]

      elif (choice[j]<dp | choice[j]<=max):
        tp=dp-choice[j]
        downword(dp,tp)
        dp=choice[j]
g.cleanup()
