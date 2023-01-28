n = int(input("Enter the number of rows: "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
start = 0

for i in range(1, n+1):
    for j in range(i):
        print(alphabet[start], end="")
        start += 1
        if start == 26:
            start = 0
    print()
