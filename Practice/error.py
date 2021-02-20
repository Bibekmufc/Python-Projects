
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You cant divide by zero. Don't bother."


print(divide(2,0))