PI = 3.14  # PI is a "constant" in our module


def square(side):
    # Calculate area of square.
    return side * side


def rectangle(length, width):
    # Calculate area of rectangle.
    return length * width


def circle(radius):
    # Calculate area of circle.
    return PI * radius**2


if __name__ == "__main__":
    # __name__ variable indentifies the file that is running
    # it's value is "__main__" when module is executed as a script directly
    print("Area of square:", square(4))
    print("Area of rectangle:", rectangle(6, 2))
    print("Area of circle:", circle(8))
