
def digit_sum (n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def revers_number (n):
    revers = 0
    while n > 0:
        revers = revers * 10 + n % 10
        n //= 10
    return revers

def is_palindrome (n):
    return n == revers_number(n)

# (a) Test the three functions with 2026, 12321 and 9875

for t in (2026, 12321, 9875):
    print (f"{t}: Digit sum = {digit_sum(t)}, Reversed = {revers_number(t)}, Palindrome = {is_palindrome(t)}")

# (b) Count how many palindromes there are from 10 to 999.

count = 0
for i in range (10, 1000):
    if is_palindrome(i):
        count += 1

print (f"Palindromes from 10 to 999: {count}")