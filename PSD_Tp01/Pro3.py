
def celsius_to_fahrenheit (c, round_to = 1):
    value = c * 9/5 + 32
    return round (value, round_to)

def fahrenheit_to_celsuis (f, round_to = 1):
    value = (f - 32) * 5/9
    return round (value, round_to)

# (a)
print ("\n(a) -- Celsius to Fahrenheit\n")
for c in range (0, 101, 20):
    f = celsius_to_fahrenheit(c)

    print (f"{c}\t==>\t{f}")

# (b)
print ("\n(b) -- Convert 98.6F to C\n")
temp_F = 98.6
temp_C = fahrenheit_to_celsuis(temp_F)

print (f"Convert {temp_F} F to Celsisus equal {temp_C}")

# (c)
print ("\n(c) -- Turn 37C to F and back again\n")
f = celsius_to_fahrenheit(37)
c = fahrenheit_to_celsuis(f)

print (f"37C to F equal {f} and {f} to C equal {c}")

# (d)
print ("\n(d) -- Call one function with round to 3\n")
r = celsius_to_fahrenheit(23.42, round_to = 3)

print (f"{r}\n")