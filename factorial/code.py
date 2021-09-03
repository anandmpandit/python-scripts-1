num = 4
factorial = 1

if num <0:
    print("Not Possible")
elif num == 0:
    print(factorial)
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("factorial")