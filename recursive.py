#created a function that takes one input x 
def factorial(x):
#checks if x is equal to 0 or 1    
    if x == 1 or x == 0:
        return 1  
    #recursion
    return x * factorial(x - 1)  # 

#user input
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
