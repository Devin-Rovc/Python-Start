total = 0

for i in range(3):
    while True:
        try:
            num = int(input("Enter an integer: "))
            total += num
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

print("The sum of the three integers is:", total)