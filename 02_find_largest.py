# Question:
# You have 5 numbers. How would you find the largest?

numbers = [10, 25, 7, 42, 18]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number:", largest)
