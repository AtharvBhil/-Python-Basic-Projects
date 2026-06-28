import math
try:
    sentence = input("Enter a sentence: ")
    # Convert sentence into words
    words = sentence.split()
    # Store unique words
    unique_words = set(words)
    # Print sorted words
    print("Unique Words:")
    for word in sorted(unique_words):
        print(word)
    # Calculate power
    print("Power:", math.pow(len(unique_words), 2))
except Exception as e:
    print("Error:", e)