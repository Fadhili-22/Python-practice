#created a function that takes one input x
def sum_of_digits(x):
    total = 0
    while x > 0:
        digit = x  % 10        # Get the last digit
        total += digit        # Add it to total
        x = x // 10           # Remove the last digit
    return total

num = int(input('Enter number: '))
print("Sum of digits of", num, "is", sum_of_digits(num))
