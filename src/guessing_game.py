print("Think of a number between 1 and 100and I will guess it.")
print("You have to tell me if my guess is greater, less than or equal to your number")

correct = False

top = 100
bottom = 1

while not correct:
    guess = (top + bottom) // 2

    print(f"I am guessing it is {guess}")

    result = input("Less, Greater, or Equal?").lower()
    result = result[0]

    if result == 'l':
        top = guess - 1
    elif result == 'g':
        bottom = guess + 1
    elif result == 'e':
        correct = True
    else:
        print("Please enter valid option")

    if top == bottom:
        guess = top
        correct = True

print (f'\nIt is {guess}\n')