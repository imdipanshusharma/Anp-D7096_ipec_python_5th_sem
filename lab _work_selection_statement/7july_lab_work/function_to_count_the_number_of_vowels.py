'''Problem Statement 5: Vowel Counter using Function 
Write a Python program that defines a function 
count_vowels(text). 
The function should:
 • Accept a string. 
   • Count the total number of vowels (a, e, i, o, u) irrespective of case. 
      • Return the total vowel count.
          The main program should: 
          • Accept a sentence from the user. 
            • Call the function. 
              • Display the total number of vowels. 
                Sample Output Enter a sentence: Python Programming is Fun  Total Vowels: 6 '''





'''---------------------------coding---------------------------'''



# Function to count the number of vowels
def count_vowels(text):

    # Initialize vowel counter
    count = 0

    # Convert the string to lowercase
    text = text.lower()

    # Check each character in the string
    for ch in text:
        if ch in "aeiou":
            count += 1

    # Return the total number of vowels
    return count

# Main program

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Call the function
total_vowels = count_vowels(sentence)

# Display the result
print("Total Vowels:", total_vowels)



'''---------------------------output---------------------------
Enter a sentence: Enter a sentence: Python Programming is Fun


Total Vowels: 12 '''