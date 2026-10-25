# PART B
def safe_int(text):
    try:
        return int(float(text.strip()))
    except (ValueError, OverflowError, AttributeError):
        return None


for sample in ["42", "-8", "3.9", "abc", ""]:
    print(f"{sample} -> {safe_int(sample)}")

# PART C
first = safe_int(input("\nEnter the first number: "))
second = safe_int(input("\nEnter the second number: "))

if first is None or second is None:
    print("\nSorry, one of the values is not a number. Please try again.")
else:
    print("\nThe sum is:", first + second)