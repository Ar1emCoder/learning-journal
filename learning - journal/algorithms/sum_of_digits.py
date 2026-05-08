def sum_of_digits(n):
    tmp = 0
    while n > 0:
        # tmp = 0
        tmp +=  n%10
        n //= 10
    return tmp

print(sum_of_digits(456))