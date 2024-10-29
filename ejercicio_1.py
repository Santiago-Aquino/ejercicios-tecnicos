# 1
# Desarrollar una función que reciba una palabra y devuelva True en caso de ser un
# palíndromo y False en caso de no serlo.

def is_palindrome(word):
    modified_word = word.strip().lower()

    char_list = list(modified_word)
    char_list.reverse()
    reverse_word = ''.join(char_list)

    return modified_word == reverse_word

print(is_palindrome('neuquen'))
print(is_palindrome('ciudad'))