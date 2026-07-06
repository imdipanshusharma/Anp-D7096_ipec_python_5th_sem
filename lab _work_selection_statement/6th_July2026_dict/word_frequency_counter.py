'''problem statement


Word Frequency Counter Problem Statement: Accept a
 sentence from the user and create a dictionary that
   stores the frequency of each word. Example: Input:
     python is easy and python is powerful  Output: 
     { 'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1 } 
     Additionally: • Display the most frequently occurring word. 
       • Display all words in alphabetical order'''




# Word Frequency Counter

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary
frequency = {}

# Count the frequency of each word
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Display the dictionary
print("\nWord Frequency Dictionary")
print(frequency)

# Find the most frequently occurring word
max_count = max(frequency.values())

print("\nMost Frequently Occurring Word")
for word, count in frequency.items():
    if count == max_count:
        print(word, ":", count)

# Display words in alphabetical order
print("\nWords in Alphabetical Order")
for word in sorted(frequency):
    print(word, ":", frequency[word])




    '''---------------------output---------------------
    
    
    
    
    Enter a sentence:
python is easy and python is powerful

Word Frequency Dictionary
{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}

Most Frequently Occurring Word
python : 2
is : 2

Words in Alphabetical Order
and : 1
easy : 1
is : 2
powerful : 1
python : 2'''