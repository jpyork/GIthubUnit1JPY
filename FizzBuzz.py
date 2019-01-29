print ("Welcome to Jonathan's FizzBuzz Program")

x = 1

for x in range(101):
        if x==0:
            continue
        if (x%5 == 0) and (x%3 ==0):
            print("FizzBuzz")
        elif (x%3) == 0: print("Fizz")
        elif (x%5) == 0: print("Buzz")
        else: print(x)
