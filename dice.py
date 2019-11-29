import random, sys, time

RANGE = [1, 2, 3, 4, 5, 6]
WIN = []
LOSE = []
print('Roling dice simulator.')
time.sleep(0.9)
print('Type "ctrl+c" for exit.')
time.sleep(0.5)

while True:
    try:
        choice = input('Choice a number from 1 to 6: ')
        if int(choice) not in RANGE:
            print('Error!')
            time.sleep(2)
            print(f'Your choice is {choice}, and this is wrong.')
        else:
            rand_number = random.randint(1, 6)
            print(f'Your choice is {choice}. \nGood luck!')
            for i in range(1, 11):
                sys.stdout.write(f"\r{i}")
                sys.stdout.flush()
                time.sleep(0.5)
            if rand_number == int(choice):
                print(f'\nThe dice number is {rand_number}, and your choice is {choice}.')
                time.sleep(1)
                print('Congratulations!!!!')
                time.sleep(1)
                WIN.append([rand_number, int(choice)])
            else:
                print(f'\nThe dice number is {rand_number}, and your choice is {choice}.')
                time.sleep(1)
                print('Try again =/')
                time.sleep(1)
                LOSE.append([rand_number, int(choice)])
    except KeyboardInterrupt:
        exit()
    except Exception:
        print('Type a number!')
        time.sleep(0.5)