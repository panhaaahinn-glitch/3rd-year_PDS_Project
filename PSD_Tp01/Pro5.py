
# (a)

def letter_grade(score):
    if score < 0 or score > 100:
        return ("Invalid")
    elif score >= 97:
        return ("A+")
    elif score > 90:
            return ("A")
    elif score >= 80:
            return ("B")
    elif score >= 70:
            return ("C")
    elif score >= 60:
            return ("D")
    else:
        return ("F")


for i in [99, 90, 85.5, 72, 60, 59, -5, 101]:
    print(i, "->", letter_grade(i))

# (b) Why must the test for A+ come before the test for A? What happens if you swap them?
# Because if the Condition A true other condition wont run even if your score 100.