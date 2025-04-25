#Created a function that takes the word to be reversed
def reverse_string(x):
    #We create an empty string called reversed_str to store the reversed version of x as we build it.
    reversed_str = ""
    #We initialize a variable y to the index of the last character in the string.
    y = len(x) - 1

    while y >= 0:
        #this adds the character at position y of x to the end of reversed_str.
        reversed_str += x[y]
        y -= 1

    return reversed_str

# Example
text = input("Type in text to be reversed: ")
print(reverse_string(text))  # Output of the reversed word
