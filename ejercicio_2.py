# 2
# Desarrollar una función que reciba un texto e identifique que todos los paréntesis estén
# balanceados (chequear que siempre que se abra un paréntesis este se cierre), devolver
# True caso que así sea, False caso contrario

def check_parenthesis(text):
    char_list = list(text)
    parenthesis = filter(lambda word: word == '(' or word == ')', char_list)

    parenthesis_list = list(parenthesis)
    parenthesis_string = ''.join(parenthesis_list)

    while '()' in parenthesis_string:
        parenthesis_string = parenthesis_string.replace('()', '')

    return parenthesis_string == ''

print(check_parenthesis('(())()'))
print(check_parenthesis('())'))