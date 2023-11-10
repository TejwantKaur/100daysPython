scores = {
    "panner": 34,
    "abd":54,
    "har":99,
    "tej":91,
    "khushi":89
}

grades = {}

for i in scores:
    marks = scores[i]

    if marks > 90:
        grades[i] = "Outstanding"
    elif marks > 80:
        grades[i] = "Exceeds Expectations"
    elif marks>70:
        grades[i] = "Acceptable"
    else:
        grades[i] = 'Fail'

print (grades)