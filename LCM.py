n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
if (n1 > n2):
    max = n1
else:
    max = n2

while(True):
    if (max % n1 == 0 and max % n2 == 0):
        print(max)
        break;
    max = max + 1