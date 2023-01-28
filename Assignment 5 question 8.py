numbers = []
for i in range(10):
    numbers.append(int(input("Enter an integer: ")))

positive_numbers = []
negative_numbers = []
odd_numbers = []
even_numbers = []
occurrences = {}

for num in numbers:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1

print("Positive numbers: ", positive_numbers)
print("Negative numbers: ", negative_numbers)
print("Odd numbers: ", odd_numbers)
print("Even numbers: ", even_numbers)
print("Number of occurrences of each number: ", occurrences)
