for a in range(1,21):
    if a%3 == 0 and a%5 != 0:
        print('Fizz')
    elif a%5 == 0 and a%3 != 0:
        print('Buzz')
    elif a%3 == 0 and a%5 == 0:
        print('FizzBuzz')
    else:
        print(a)
