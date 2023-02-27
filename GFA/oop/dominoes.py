from domino import Domino


def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2, 4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()
# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...

snakeDomino = [dominoes[2]]

for s_domino in snakeDomino:
    for domino in dominoes:
        if s_domino.values[1] == domino.values[0]:
            snakeDomino.append(domino)
            dominoes.remove(domino)

snakeDomino.remove(snakeDomino[len(snakeDomino) - 1])

print(snakeDomino)