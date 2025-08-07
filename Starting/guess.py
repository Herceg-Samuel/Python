#guessing game

secret = 5
limit = 3
count = 0

while count < limit:
    guess = int(input("Guess :"))
    print(input)
    count += 1

    if guess == secret:
        print("Correct!!")
        break

else:
    print("You lost!")

