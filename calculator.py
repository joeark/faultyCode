# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    # Bug: This is incorrectly doing addition instead of subtraction
    return a + b

if __name__ == "__main__":
    x = 10
    y = 5

    print("Addition:", add(x, y))         # Expected: 15
    print("Subtraction:", subtract(x, y)) # Expected: 5 but will return 15 due to the bug
