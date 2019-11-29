import random, sys, time

RANGE = [1, 2, 3, 4, 5, 6]
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
            print('Your choice is %s, and this is wrong.' % (choice))
        else:
            rand_number = random.randint(1, 6)
            print('Your choice is %s. \nGood luck!' % (choice))
            for i in range(1, 11):
                sys.stdout.write("\r%s" % (i))
                sys.stdout.flush()
                time.sleep(0.5)
            if rand_number == int(choice):
                print('\nThe dice number is %s, and your choice is %s.' % (rand_number, choice))
                time.sleep(1)
                print('Congratulations!!!!')
                time.sleep(1)
            else:
                print('\nThe dice number is %s, and your choice is %s.' % (rand_number, choice))
                time.sleep(1)
                print('Try again =/')
                time.sleep(1)
    except KeyboardInterrupt:
        exit()
    except Exception:
        print('Type a number!')
        time.sleep(0.5)