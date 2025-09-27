for num in range(1, 10):
    print("*")

for num1 in range(-10, 1):
    for num2 in range(-num1):
        print("*", end= " ")
    print("*")

"""
*
**
***
****
*****
****
***
**
*

"""

for num in range(1, 10):
    for num2 in range(num):
        print("*", end= " ")
    print("*")

for num1 in range(-10, 1):
    for num2 in range(-num1):
        print("*", end= " ")
    print("*")

"""
*
**
***
****
*****
****
***
**
*

"""
