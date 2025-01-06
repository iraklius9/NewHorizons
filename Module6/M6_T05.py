def is_anagram(text1, text2):
    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()
    if len(text1) == 0 and len(text2) == 0:
        return False
    return sorted(text1) == sorted(text2)


user_text1 = input("Enter the first text: ")
user_text2 = input("Enter the second text: ")

if is_anagram(user_text1, user_text2):
    print("The texts are anagrams.")
else:
    print("The texts are not anagrams.")

