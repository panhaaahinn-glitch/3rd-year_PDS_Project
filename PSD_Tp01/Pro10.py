
# (a) Prime number function
def is_prime(n):
    if n <= 1:
        return False
        
    primes = (2, 3, 5, 7, 11, 13, 17, 19)
    if n in primes:
        return True
        
    for i in primes:
        if n % i == 0:
            return False
            
    return True

# (b) Print all prime below 50, and count prime below 100
print("Primes Below 50 : ")
for n in range(1, 50): 
    if is_prime(n):
        print(n, end=" ") 
print ()

# Count prime below 100
count = 0
for i in range(1, 101): 
    if is_prime(i):
        count += 1

print (f"Count Prime number between 1 - 100: {count}")

#Goldbach function
def goldbach(n): 
    for p in range(2, n): 
        q = n - p 
        if is_prime(p) and is_prime(q): 
            return p, q
    return None 

# (c) Pairs for 4, 6, ..., 30
for n in range(4, 31, 2):
    p, q = goldbach(n)
    print(f"{n} = {p} + {q}")

# (d) Check every even number from 4 to 10000, stopping at the first failure
holds = True
for n in range(4, 10001, 2):
    if goldbach(n) is None:
        holds = False
        break
print(f"Goldbach holds for every even number from 4 to 10000: {holds}")