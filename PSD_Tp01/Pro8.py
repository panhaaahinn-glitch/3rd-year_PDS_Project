
# (a) Descibe data
def describe (*numbers, decimals = 2, label = 'Data'):
    if not numbers:
        print (f"{label}: not number")
        return None
    count = len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    mean = sum(numbers) / count

    print (f"{label}: n = {count} "
           f"min = {minimum} "
           f"max = {maximum} "
           f"mean = {mean:.{decimals}f} ")

    return count, minimum, maximum, round(mean, decimals)

describe(12, 7, 30, 4)
describe(3.14159, 2.71828, decimals=3, label="Constants")
describe()

# (b) 
def make_tag(text, **style):
    attributes = " ".join(
        f'{key} = "{value}"' for key, value in style.items()
    )
    return f"<span {attributes}>{text}</span>"

print(make_tag("Hello", color="red", size=14))

# (c) Write two lamda
square = lambda x: x ** 2
is_adult = lambda age: age >= 18
print(square(9), is_adult(17), is_adult(21))