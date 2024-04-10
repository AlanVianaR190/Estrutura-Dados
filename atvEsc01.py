#função
def media(lista):
    '''
    Metodo que calcula a media
    :param lista: uma lista com notas com valores reais
    :return: a media
    '''
    media = sum(lista) / len(lista)
    return f"{media:.1f}"


#programa
notas = list((6, 7, 6.5, 4.8, 8))

#chamada função
print(media(notas))




