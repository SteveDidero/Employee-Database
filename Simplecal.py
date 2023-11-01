import sys

def simpleCal (x , y):
    """
    A simple calculator that takes two numbers and return the sum.

    Args:
        x: the first nummber
        y: the second number
    
    Returns:
    """
    return x + y

if __name__ == "__main__":
    print("This program takes two arguments. Both are numbers.")
    numbers = sys.argv[1:3]
    print(simpleCal(numbers[0],numbers[1]))