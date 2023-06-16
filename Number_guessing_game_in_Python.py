import math
import random

lower = int(input("Enter Lower number: "))
upper = int(input("Enter Upper number: "))

x = random.randint(lower, upper)

print("You have ", (round(math.log(upper - lower+1, 2))+1), " chances to guess!!!")

guess = 0

while(guess < (math.log(upper-lower+1, 2))):
  guess = guess + 1

  y = int(input("Enter the number: "))
  if(y > x):
    print("Your guess is high!!!")

  elif(y < x):
    print("Your guess is low!!!")
    
  elif(y == x):
    print("Your are right!!! :)")
    break

  if guess > (math.log(upper-lower+1, 2)):
    print("The number is ", x)
    print("Better luck next time! :(")