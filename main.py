import random

x = random.randint(0, 9)
turn_counter = 1
guess = int()

while guess != x:
    while True:
        try:
            guess = int(input('spróbuj odgadnąć liczbę z zakresu 0 - 9\n'))
            break
        except ValueError:
            print('tylko liczby całkowite')
    if guess < 0 or guess > 9:
        print('to liczba spoza zakresu')
        continue
    elif guess > x:
        print('to nie ta liczba, ta liczba jest mniejsza')
        turn_counter += 1
    elif guess < x:
        print('to nie ta liczba, ta liczba jest większa')
        turn_counter += 1
if guess == x:
    print('Gratulacje! Udało ci się za ' + str(turn_counter) + ' razem')
