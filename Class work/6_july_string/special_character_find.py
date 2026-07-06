# WAP to count the number of special characters in a given sentence

sentence = input("Enter a sentence: ")

special = 0

# Traverse each character of the sentence
for ch in sentence:

    # Check if the character is NOT a letter, digit, or space
    if not ((ch >= 'A' and ch <= 'Z') or
            (ch >= 'a' and ch <= 'z') or
            (ch >= '0' and ch <= '9') or
            ch == ' '):
        special += 1

# Display the result
print("Number of Special Characters =", special)

