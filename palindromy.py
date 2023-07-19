def check_if_palindromes(word):
    return word.lower() == word[::-1].lower()

usr_word = input('Podaj słowo: ')
print(check_if_palindromes(usr_word))
