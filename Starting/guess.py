#guessing game

secret = 5
limit = 3
count = 0

def sec(secret):
    sec = print(input("Enter secret number: ")).append(secret)
    return sec

while count < limit:
    guess = int(input("Guess :"))
    print(input)
    count += 1

    if guess == secret:
        print("Correct!!")
        break

else:
    print("You lost!")

