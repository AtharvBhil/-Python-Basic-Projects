def analyze_string(s):
    # Check if string is empty
    if len(s) == 0:
        print("String is empty.")
        return
    # Print length
    print("Length:", len(s))
    # Print reverse string
    print("Reverse:", s[::-1])
    # Count vowels
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    print("Number of vowels:", count)
    # Print character with positive and negative index
    print("\nCharacter Positions:")
    for i in range(len(s)):
        print("Character:", s[i], "Positive Index:", i, "Negative Index:", i-len(s))
text = input("Enter a string: ")
analyze_string(text)