# WAP to count the number of uppercase and lowercase characters
# in a given sentence without using library functions

sentence = input("Enter a sentence: ")

upper = 0
lower = 0

# Traverse each character of the sentence
for x in sentence:

    # Check for uppercase letters (A-Z)
    if x >= 'A' and x <= 'Z':
        upper += 1

    # Check for lowercase letters (a-z)
    elif x >= 'a' and x <= 'z':
        lower += 1

# Display the counts of uppercase and lowercase characters
print("Number of uppercase characters:", upper)
print("Number of lowercase characters:", lower)


'''output
Enter a sentence: a FOX JUMp over the Dog 
Number of uppercase characters: 7
Number of lowercase characters: 11 '''
