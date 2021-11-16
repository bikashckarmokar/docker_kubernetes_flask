from random import randint

min_number = int(input("Enter the minimum number: "))
max_number = int(input("Enter the maximum number: "))

if (max_number < min_number):
    print("Invalid input - shutting down..")

else:
    rnd_number = randint(min_number, max_number)
    print("The random number is: ", rnd_number)