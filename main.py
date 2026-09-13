base = int(input('Enter base number:'))
exponent = int(input('Enter the exponent:'))

result = 1

for i in range (1, exponent + 1 ):
    result = result * base
    print("step", i , ": result =", result)
