import sys

def simpleCal (x , y):
    """
    A simple calculator that takes two numbers and return the product.

    Args:
        x (int): the first number
        y (int): the second number
    
    Returns:
        (int): The product of both numbers
    """
    
    return x * y

if __name__ == "__main__":
    print("This program takes two arguments. Both are integers.")
    numbers = sys.argv[1:3]
    print(simpleCal(numbers[0],numbers[1]))
