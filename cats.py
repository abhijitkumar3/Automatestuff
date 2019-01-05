while True:
    try:
        print('how many cats do you have?')
        numcats = input()
        if int(numcats) >= 4:
            print('that is a lot of a cats')
        elif int(numcats) == 3:
            print('wow, I have 3 cats too')
        else:
            print('I definitely have more cats than you')
    except ValueError:
            print('Error, please only enter integer values')
