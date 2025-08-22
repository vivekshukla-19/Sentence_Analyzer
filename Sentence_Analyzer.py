sentence = input("Enter the sentence: ")        # take the input from the userr

vowels = consonants = digits = spaces = special_chars = 0

for i in sentence:
    if i.lower() in 'aeiou':          # character ko lowercase banata hai (upper case ko ignore karne ke liye)
        vowels +=1
    elif i.isalpha():                 # Ye check karta hai ki character alphabet hai ya nahi
        consonants +=1
    elif i.isdigit():                 # Ye check karta hai ki character digit (0-9) hai ya nahi
        digits +=1
    elif i.isspace():                 # Ye check karta hai ki character space hai ya nahi
        spaces +=1           
    else :                            # Agar above koi bhi condition match nahi karti, to wo special character hoga
        special_chars +=1


# use of f string in print statements

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special Characters: {special_chars}")            
