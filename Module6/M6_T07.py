def is_hidden(word, text):
    index = 0
    for char in word:
        index = text.find(char, index)
        if index == -1:
            return False
        index += 1
    return True


print(is_hidden("dog", "vcxzgxduybfdsobywuefas"))
print(is_hidden("dog", "vcxzxduybfdsobywuefgas"))
