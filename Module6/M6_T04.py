def is_palindrome(text):
    text = text.lower().replace(' ', '')
    return text == text[::-1]


text = input('Enter some text: ')
if is_palindrome(text):
    print('The text is a palindrome.')
else:
    print('The text is not a palindrome.')
