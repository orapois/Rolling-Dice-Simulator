import random, sys, time, os
RANGE = [1, 2, 3, 4, 5, 6]
WIN = []
LOSE = []
print('Roling dice simulator.')
time.sleep(0.9)
print('Type "ctrl+c" for exit.')
time.sleep(0.5)

def update_file():
    if file_exists():
        date = time.asctime(time.localtime(time.time()))
        win = f'{date} {WIN}/n'
        lose = f'{date} {LOSE}'
        write_file(win)
        write_file(lose)

def file_exists():
    if os.path.exists("score.txt"):
        return True
    else:
        open("score.txt", "x")
        return True

def write_file(x):
    f = open("score.txt", "a")
    f.write(x)

def view_score():
    print('Win')
    for i in WIN:
        print(f'CPU {i[0]}, You {i[1]}')
    print('Lose')
    for i in LOSE:
        print(f'CPU {i[0]}, You {i[1]}')

def verify_lists():
    if len(WIN) > 0 or len(LOSE) > 0:
        return True
    else:
        return False

while True:
    try:
        if verify_lists():
            score = input('type to view score or 2 for try again: ')
            if score == '1':
                view_score()
                choice = input('Choice a number from 1 to 6: ')
        else:
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
