import re
import nltk
from nltk import Prover9
from nltk.sem import Expression

from characters import Character

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('tkinter')
nltk.download('treebank')

def string_to_prover9(sentence):


    withoutEnumerations = re.sub(",|and ", "", sentence)
    x = re.split("\s", withoutEnumerations)

    if len(x) < 4:
        return "invalid sentence: too short"

    if not re.search("Crewmate[1-9]", x[0]):
        return "Error: Invalid Crewmate name: " + x[0] + " (must be Crewmate1, Crewmate2, etc.)"

    if x[1] != "is":
        return "incorrect sentence structure: " + x[1] + " (must be 'is')"

    if x[2] != "in":
        return "incorrect sentence structure: " + x[2] + " (must be 'in')"

    if not re.search("Reactor|OTwo|Weapons|Navigation|Admin|Electrical|Storage|Security|Medbay|Cafeteria", x[3]):
        return "Error: Invalid room name"

    if not re.search("with|alone", x[4]):
        return "Error: Invalid sentence structure: " + x[4] + " (must be with or alone)"

    if x[4] == "with":
        for i in range(5, len(x)):
            if not re.search("Crewmate[1-9]", x[i]):
                return "Error: Invalid Crewmate name: " + x[i] + " (must be Crewmate1, Crewmate2, etc.)"

    statement = x[3].lower() + "(%s)" % x[0].lower()

    if x[4] == "with":
        for i in range(5, len(x)):
            statement += " & " + x[3].lower() + "(%s)" % x[i].lower()

    statement += " -> " + "p%s" % x[0][8]

    # print(statement)

    return statement

def generateBaseAssumptions(n):
    baseAssumptions = []

    rooms = ["Reactor", "OTwo", "Weapons", "Navigation", "Admin", "Electrical", "Storage", "Security", "Medbay", "Cafeteria"]

    for i in range(0, len(rooms) - 1):
        st = rooms[i].lower() + "(x) -> "
        for j in range(i+1, len(rooms)):
            st += "-" + rooms[j].lower() + "(x) & "
        st = st[:-3]
        baseAssumptions.append(st)
    return baseAssumptions


def generatePositionalAssumptions(characters):
    assumptions = []
    for i in range(0, len(characters)):
        st = "%s" %characters[i].position.lower() + "(crewmate%d)" % (i + 1)
        assumptions.append(st)
    return assumptions



def generateAllAsumptions(n, characters):
    allAssumptions = []
    allAssumptions += generateBaseAssumptions(n)
    allAssumptions += generatePositionalAssumptions(characters)
    for character in characters:
        allAssumptions += [string_to_prover9(character.statement)]
    return allAssumptions

def solve(characters, n):

    assumptions = generateAllAsumptions(n, characters)

    prover9Assumptions = []
    for assumption in assumptions:
        prover9Assumptions += [Expression.fromstring(assumption)]

    impostors = []

    for i in range(1, n + 1):
        g = Expression.fromstring("p%d" % i)
        if not (Prover9().prove(g, prover9Assumptions)):
            impostors += [i]

    return impostors
def create_file(allAssumptions):
    f = open("assumptions.txt", "w")
    for assumption in allAssumptions:
        f.write(assumption + "\n")
    f.close()