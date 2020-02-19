from cifra_cesar import cifrar_letra, cifrar_palavra, PalavraNaoPalavra
import pytest

@pytest.mark.parametrize('letra,letra_cifrada', [
    ('a', 'd'),
    ('b', 'e'),
    ('c', 'f')
])
def test_letra_minuscula(letra, letra_cifrada):
    assert cifrar_letra(letra) == letra_cifrada

@pytest.mark.parametrize('letra,letra_cifrada', [
    ('A', 'D'),
    ('B', 'E'),
    ('C', 'F')
])
def test_letra_maiscula(letra, letra_cifrada):
    assert cifrar_letra(letra) == letra_cifrada

def test_space():
    assert cifrar_letra(' ') == ' '


def test_alfabeto_4_primeiras_letras():
    assert cifrar_palavra('abcd') == 'defg'

def test_alfabeto_cifrado():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfabeto_cifrado = 'DEFGHIJKLMNOPQRSTUVWXYZABC'
    assert cifrar_palavra(alfabeto) == alfabeto_cifrado

def test_palavra_capitalizada():
    assert cifrar_palavra('Rafael') == 'Udidho'

def test_frase_com_espaco():
    frase = 'a ligeira raposa marrom saltou sobre o cachorro cansado'
    cifrado = 'd oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr'
    assert cifrar_palavra(frase) == cifrado

def test_letra_a_rot_4():
    assert cifrar_letra('a', rotacao=4) == 'e'

def test_palavra_cifrada_rot_4():
    assert cifrar_palavra('ABCDEF', 4) == 'EFGHIJ'

def test_letra_a_rot_26():
    assert cifrar_letra('A', 26) == 'A'

def test_letra_a_rot_53():
    assert cifrar_letra('A', 53) == 'B'

def test_palavra_cifrada_rot_53():
    assert cifrar_palavra('ABCDEF', 53) == 'BCDEFG'

@pytest.mark.parametrize('nao_letra', ['@', '!', '2', ']', '%'])
def test_letra_nao_letra(nao_letra):
    with pytest.raises(ValueError):
        cifrar_letra(nao_letra)

@pytest.mark.parametrize('nao_palavra', ['@@@@', '!!!!', '2222', ']]]', '%%'])
def test_palavra_nao_palavra(nao_palavra):
    with pytest.raises(PalavraNaoPalavra):
        cifrar_palavra(nao_palavra)
