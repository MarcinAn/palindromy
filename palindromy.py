def check_if_palindromes(word):
    word= word.lower()
    return word == word[::-1]

usr_word = input('Podaj słowo: ')
print(check_if_palindromes(usr_word))
