def check_if_palindromes(word):
    return word == word[::-1]

usr_word = input('Podaj słowo: ')
print(check_if_palindromes(usr_word.lower()))
