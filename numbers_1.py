#created a variable called number which got its input from the user
number = int(input("Enter a number: "))
#used % and an if statemtn to find if the remainder of the number that the user provided is equal to  0
if number % 2 == 0:
  print("It's an even number")
else:
   print("It's an odd number")
