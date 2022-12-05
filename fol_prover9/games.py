import re
import random

from playsound import playsound

from characters import Character
from folProver9 import solve

rooms = ["Reactor", "OTwo", "Weapons", "Navigation", "Admin", "Electrical", "Storage", "Security", "Medbay", "Cafeteria", "LowerEngine", "UpperEngine", "Communications", "Shields"]

roomAdjacencyCrewmates = {
    "Reactor": ["Security", "UpperEngine", "LowerEngine"],
    "Security": ["Reactor", "UpperEngine", "LowerEngine"],
    "UpperEngine": ["Reactor", "Security", "LowerEngine", "Cafeteria", "Medbay"],
    "LowerEngine": ["Reactor", "Security", "UpperEngine", "Storage", "Electrical"],
    "Storage": ["LowerEngine", "Electrical", "Admin", "Cafeteria", "Communications", "Shields"],
    "Medbay": ["UpperEngine", "Cafeteria"],
    "Electrical": ["Storage", "LowerEngine"],
    "Admin": ["Storage", "Cafeteria"],
    "Cafeteria": ["UpperEngine", "Storage", "Weapons", "Admin", "Medbay"],
    "Communications": ["Storage", "Shields"],
    "Weapons": ["Cafeteria", "OTwo", "Shields", "Navigation"],
    "OTwo": ["Weapons", "Navigation", "Shields"],
    "Shields": ["Storage", "Communications", "OTwo", "Navigation", "Weapons"],
    "Navigation": ["Weapons", "OTwo", "Shields"]
}

roomAdjacencyImpostors = {
    "Reactor": ["Security", "UpperEngine", "LowerEngine"],
    "Security": ["Reactor", "UpperEngine", "LowerEngine", "Electrical"],
    "UpperEngine": ["Reactor", "Security", "LowerEngine", "Cafeteria", "Medbay", "Weapons"],
    "LowerEngine": ["Reactor", "Security", "UpperEngine", "Storage", "Electrical", "Shields"],
    "Storage": ["LowerEngine", "Electrical", "Admin", "Cafeteria", "Communications", "Shields"],
    "Medbay": ["UpperEngine", "Cafeteria"],
    "Electrical": ["Storage", "LowerEngine", "Security"],
    "Admin": ["Storage", "Cafeteria", "Navigation"],
    "Cafeteria": ["UpperEngine", "Storage", "Weapons", "Admin", "Medbay"],
    "Communications": ["Storage", "Shields"],
    "Weapons": ["Cafeteria", "OTwo", "Shields", "Navigation", "UpperEngine"],
    "OTwo": ["Weapons", "Navigation", "Shields"],
    "Shields": ["Storage", "Communications", "OTwo", "Navigation", "Weapons", "LowerEngine"],
    "Navigation": ["Weapons", "OTwo", "Shields", "Admin"]
}

def loadGameDate(n):

    f = open("games%s.in" % n)
    x = f.read()
    lines = x.splitlines()
    nr = int(lines[0])

    crewmates = []

    for i in range(1, nr + 1):
        atributes = re.split("!", lines[i])
        # print(lines[i], atributes)
        crewmates += [Character(atributes[0], atributes[1], atributes[1], atributes[2], atributes[3] == "Sus", atributes[4] == "Alive", i)]

    f.close()

    return (nr, crewmates)

def lies():
    randomValue = random.randint(0, 100)
    if randomValue < 75:
        return False
    else:
        return True
def moveCrewmates(crewmates, n):

    #if an impostor is with someone, they kill them
    crews = []
    for crewmate in crewmates:
        if crewmate.isImpostor:
            for crewmate2 in crewmates:
                if crewmate2.position == crewmate.position and crewmate2.alive and crewmate2.isImpostor == False:
                    crews += [crewmate2]
            print(len(crews))
            if len(crews) > 0:
                crewmateKilled = random.choice(crews)
                crewmateKilled.alive = False
                print("Crewmate killed in %s" % crewmate.position)
                playsound("/home/stoian/Home/AI/MoagUs/fol_prover9/Impostor Kill.mp3")

    #move characters
    for crewmate in crewmates:
        if crewmate.alive:
            if crewmate.isImpostor:
                # print(roomAdjacencyImpostors[crewmate.position], len(roomAdjacencyImpostors[crewmate.position]))
                randomRoom = random.choice(roomAdjacencyImpostors[crewmate.position] + [crewmate.position])
                # print(randomRoom)
            else:
                # print(roomAdjacencyCrewmates[crewmate.position], len(roomAdjacencyCrewmates[crewmate.position]))
                randomRoom = random.choice(roomAdjacencyCrewmates[crewmate.position] + [crewmate.position])
                # print(randomRoom)
            crewmate.lastPosition = crewmate.position
            crewmate.position = randomRoom

    crewInRoom = {
        "Reactor": [],
        "OTwo": [],
        "Weapons": [],
        "Navigation": [],
        "Admin": [],
        "Electrical": [],
        "Storage": [],
        "Security": [],
        "Medbay": [],
        "Cafeteria": [],
        "LowerEngine": [],
        "UpperEngine": [],
        "Communications": [],
        "Shields": []
    }

    for crewmate in crewmates:
        if crewmate.alive:
            crewInRoom[crewmate.position] += [crewmate]

    for crewmate in crewmates:
        if crewmate.alive:
            if crewmate.isImpostor == False:
                crewmate.statement = "Crewmate%d is in %s"%(crewmate.index, crewmate.position)
                if len(crewInRoom[crewmate.position]) > 1:
                    crewmate.statement += " with "
                    for crewmate2 in crewInRoom[crewmate.position]:
                        if crewmate2 != crewmate:
                            crewmate.statement += "Crewmate%d, "%crewmate2.index
                    crewmate.statement = crewmate.statement[:-2]
                else:
                    crewmate.statement += " alone"
            else:
                if not lies():
                    crewmate.statement = "Crewmate%d is in %s"%(crewmate.index, crewmate.position)
                    if len(crewInRoom[crewmate.position]) > 1:
                        crewmate.statement += " with "
                        for crewmate2 in crewInRoom[crewmate.position]:
                            if crewmate2 != crewmate:
                                crewmate.statement += "Crewmate%d, "%crewmate2.index
                        crewmate.statement = crewmate.statement[:-2]
                    else:
                        crewmate.statement += " alone"
                else:
                    print("Impostor lied")
                    crewmate.statement = "Crewmate%d is in %s"%(crewmate.index, crewmate.position)
                    if len(crewInRoom[crewmate.position]) > 1:
                        crewmate.statement += " alone"
                    else:
                        nrOfCrewmates = random.randint(2, n+1) - 1
                        randomValue = random.sample(range(1, n+1), nrOfCrewmates)
                        crewmate.statement += " with "
                        for i in range(nrOfCrewmates):
                            crewmate.statement += "Crewmate%d, "%randomValue[i]
                        crewmate.statement = crewmate.statement[:-2]

    return crewmates

def crewmatesDead(crewmates):

    numberOfDead = 0

    for crewmate in crewmates:
        if not crewmate.alive:
            numberOfDead += 1

    return numberOfDead


sus = []
def findImpostor(crewmates, n, round):
    if round < n / 2 and crewmatesDead(crewmates) == n - 2:
        return False

    susThisRound = solve(crewmates, n)
    for val in susThisRound:
        if crewmates[val - 1] in sus:
            sus.append(crewmates[val])

    threshold = round + 2 * crewmatesDead(crewmates)
    randomValue = random.randint(20, 85)

    if randomValue < threshold:
        print(randomValue, threshold)
        return True

    return False

def killImpostor(crewmates, n):
    for crewmate in crewmates:
        if crewmate.isImpostor:
            crewmate.alive = False