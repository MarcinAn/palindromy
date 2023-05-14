def check_if_palindromes(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False

usr_word = input('Podaj słowo: ')
print(check_if_palindromes(usr_word))