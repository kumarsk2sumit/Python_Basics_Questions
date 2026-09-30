maths = 45
english = 65
science = 48
hindi = 32
sst = 45

average_marks = (maths + english + science + hindi + sst) / 5

if average_marks >= 90:
    print(f"Grade: A | Percentage: {average_marks}%")
elif average_marks >= 80:
    print(f"Grade: B | Percentage: {average_marks}%")
elif average_marks >= 70:
    print(f"Grade: C | Percentage: {average_marks}%")
else:
    print(f"Grade: D | Percentage: {average_marks}%")
