
# (a)
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

a = [200, 400]
for i in a:
    leap = is_leap(i)
    print (leap)

# (b)
def days_in_month (month, year):
    if month < 1 or month > 12:
        return None
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in (4, 6, 9 ,11):
        return 30
    return 31

print (f"Feb 2024: {days_in_month(2, 2024)} | "
       f"Feb 2026: {days_in_month(2, 2026)} | "
       f" Apr: {days_in_month(4, 2026)} | "
       f"Month 13: {days_in_month(13, 2026)}")

# (c) check leap year
for y in (1900, 2000, 2024, 2026):
    print (y, "Leap" if is_leap(y) else "Not leap")

# (d) count leap year
count = 0
for y in range (2000, 2101):
    if is_leap(y):
        count += 1

print(f"Leap years from 2000 to 2100: {count}")