def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    while n != 0:
        if n % 2 == 1:
            n = n * 3 + 1
        else:
            n = n / 2
    return n


print(syracuse(3))