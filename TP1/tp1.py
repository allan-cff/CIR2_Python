import math

def celsius_fahrenheit(celcius):
    return celcius * 9 / 5 + 32


def mention(note):
    if note >= 16:
        return 'très bien'
    elif note >= 14:
        return 'bien'
    elif note >= 12:
        return 'assez bien'
    elif note >= 10:
        return 'passable'
    else:
        return 'insuffisant'


def nombres_pairs(n):
    return list(range(0, n, 2))


def remplacer(texte, caractere, nouveau_caractere):
    nouveau = ""
    for i in range(len(texte)):
        if texte[i] == caractere:
            nouveau = nouveau + nouveau_caractere
        else:
            nouveau = nouveau + texte[i]
    return texte


def est_palindrome(mot):
    return mot[::-1] == mot


def triplets_pythagoricien(n):
    resultat = []
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                if i ** 2 + j ** 2 == k ** 2:
                    resultat.append((i, j, k))
    return resultat


def diviseurs(n):
    result = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            result.append(i)
            result.append(n//i)
    return result


def est_parfait(n):
    return 2*n == sum(diviseurs(n))


def occurrences_lettres(mot):
    result = {}
    for lettre in mot:
        if lettre in result:
            result[lettre] += 1
        else:
            result[lettre] = 1
    return result


points_lettres_1 = {
 1 : ["E", "A", "I", "N", "O", "R", "S", "T", "U", "L"],
 2 : ["D", "M", "G"],
 3 : ["B", "C", "P"],
 4 : ["F", "H", "V"],
 8 : ["J", "Q"],
 10 : ["K", "W", "X", "Y", "Z"]
}


def calculer_score(mot, points_lettres):
    result = 0
    occurences = occurrences_lettres(mot)
    for lettre in occurences.keys():
        for score in points_lettres.keys():
            if lettre in points_lettres[score]:
                result += score * occurences[lettre]
    return result


print(celsius_fahrenheit(22))
print(nombres_pairs(10))
print(remplacer("toto", "o", "i"))
print(est_palindrome("ressasser"))
print(est_palindrome("palindrome"))
print(triplets_pythagoricien(20))
print(diviseurs(60))
print(est_parfait(6))
print(est_parfait(42))
print(est_parfait(8128))
print(occurrences_lettres("ANTICONSTITUTIONNELLEMENT"))
print(occurrences_lettres("POMME"))
print(calculer_score("POMME", points_lettres_1))
print(calculer_score("JUKEBOX", points_lettres_1))