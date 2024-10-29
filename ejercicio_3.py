# 3
# Desarrollar una función que reciba un texto e invierta el orden de las palabras siendo la
# última palabra la primera y la primera la última, debe devolver el texto invertido


def invert_word(text):
    word_list = text.split(' ')
    word_list.reverse()
    return ' '.join(word_list)

print(invert_word('resolviendo prueba tecnica'))