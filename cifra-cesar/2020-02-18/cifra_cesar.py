class PalavraNaoPalavra(Exception):
    message = 'Isso não é uma palavra!'


def cifrar_palavra(palavra, rotacao=3):
    try:
        palavra_cifrada = ""
        for letra in palavra:
            palavra_cifrada += cifrar_letra(letra, rotacao)

        return palavra_cifrada
    except ValueError:
        raise PalavraNaoPalavra()


def cifrar_letra(letra, rotacao=3):
    if letra == " ":
        return " "
    if letra.isupper():
        alfabeto = pegar_alfabeto()
    else:
        alfabeto = pegar_alfabeto().lower()
    index_da_letra = alfabeto.index(letra)
    index_da_cifra = index_da_letra + rotacao
    if index_da_cifra > 25:
        index_da_cifra = index_da_cifra % 26
    letra_cifrada = alfabeto[index_da_cifra]
    return letra_cifrada

def pegar_alfabeto():
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
