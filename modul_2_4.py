numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = 0
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            is_prime = True
            break
        else:
            is_prime = False
    if is_prime == True:
        not_primes.append(i)
    else:
        primes.append(i)

print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')
