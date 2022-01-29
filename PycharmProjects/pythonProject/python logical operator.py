# logical operator

a = 20


if a%4 == 0 and a%3 ==0:  # logical and operation
 print("divided by both 4 and 3")

if a%4 ==0 or a%3 ==0:    # logical or operation
    print("either divided by 4 or 3")

if not (a%4 == 0 or a%3 == 0):   # logical not operation
    print("neither divided by 4 nor 3")
