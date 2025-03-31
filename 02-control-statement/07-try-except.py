try:
    print("Try")
    r = 10 / 0
except ValueError as e:
    print("Value Error: ", e)
except ZeroDivisionError as e:
    print("Error: ", e)
else:
    print("No Error")
finally:
    print("Finally")
