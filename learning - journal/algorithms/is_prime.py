def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n%2 == 0 : return False
    for x in range(3, int(n**0.5) + 1):
        if n%x == 0: return False
    else:
        return True

print(is_prime(2))   # True
print(is_prime(3))   # True
print(is_prime(4))   # False
print(is_prime(17))  # True
print(is_prime(1))   # False
print(is_prime(0))   # False