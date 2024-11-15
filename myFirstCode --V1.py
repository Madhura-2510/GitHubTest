import time 
import random
#App_name ="MadApp - Daily prediction"
print ("Welcome to MadApp - Daily prediction")
print ("This app gives you daily predictions about how will be your day! So, get ready ...")
time.sleep(2)

my_randomnum = random.randint(1,10)
if (my_randomnum % 3) ==0 :
  print (f"You have a wonderful day full of surprises and warm relationships. your lucky number is {my_randomnum} ")
elif (my_randomnum % 3) ==1:
  print (f"You will overcome the challenges if you stay focused.your lucky number is {my_randomnum} ")
else:
  print (f"You have great opportunities awaiting for you. your lucky number is {my_randomnum} ")
print ("Have a great day!")
