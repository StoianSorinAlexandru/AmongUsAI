import re
from characters import Character

def loadGameDate(n):

    f = open("games%s.in" % n)
    x = f.read()
    lines = x.splitlines()
    nr = int(lines[0])

    crewmates = []

    for i in range(1, nr + 1):
        atributes = re.split("!", lines[i])
        # print(lines[i], atributes)
        crewmates += [Character(atributes[0], atributes[1], atributes[2], atributes[3] == "Sus", atributes[4] == "Alive")]

    f.close()

    return (nr, crewmates)

