import math;

print("===============")
print("Palindrome Test")
print("===============")
stringInput = input("Enter a string: ")

stringLen = len(stringInput)
midpoint = math.ceil(stringLen/2) - 1
palindrome = 0;

for i in range(0, len(stringInput)):
    if stringInput[i] != stringInput[stringLen - i - 1]:
        break
    elif (i == midpoint):
        palindrome = 1;
        break

if (palindrome == 1):
    print("Yes palindrome")
else:
    print("Not a palindrome")
