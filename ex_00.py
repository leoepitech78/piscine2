# ex_00.py
def multiply(a, b):
    return a * b

def multiply2(num):
    return num * 2

def multiply10(num):
    return num * 10

def getSecondMax(numbers):
    if len(numbers) < 2:
        return ("The list must have at least two elements to find the second maximum.")
    
    first_max = max(numbers)
    numbers.remove(first_max)  # Remove the first maximum
    second_max = max(numbers)
    
    return second_max
