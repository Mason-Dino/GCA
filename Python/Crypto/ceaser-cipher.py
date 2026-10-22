import random

message = input("")
print(message)

result = ""

shift = 3

for letter in message:
    if letter.isalpha():
        if letter.islower():
            base = ord('a')
        else:
            base = ord('A')

        newLetter = chr((ord(letter) - base + shift) % 26 + base)
        result += newLetter
    else:
        result += letter

print(f"Result Message: {result}\n\n")

for s in range(0, 26):
    hack = ""

    for letter in result:
        if letter.isalpha():
            if letter.islower():
                base = ord('a')
            else:
                base = ord('A')

            newLetter = chr((ord(letter) - base - s) % 26 + base)
            hack += newLetter
        else:
            hack += letter

    print(f"Shift {s}: {hack}")