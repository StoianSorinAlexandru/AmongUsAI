import time

from playsound import playsound

from characters import Character
from folProver9 import solve, create_file, generateAllAsumptions
from games import loadGameDate, moveCrewmates, findImpostor

sentence1 = "Crewmate1 is in OTwo with Crewmate5"
sentence2 = "Crewmate2 is in Cafeteria with Crewmate4"
sentence3 = "Crewmate3 is in Admin alone"
sentence4 = "Crewmate4 is in Cafeteria with Crewmate2"
sentence5 = "Crewmate5 is in OTwo with Crewmate1"
sentence6 = "Crewmate6 is in Electrical alone"


character1 = Character("red", "OTwo", "OTwo", sentence1, False, True, 1)
character2 = Character("blue", "Cafeteria", "Cafeteria", sentence2, False, True, 2)
character3 = Character("green", "Admin", "Admin", sentence3, False, True, 3)
character4 = Character("pink", "Cafeteria", "Cafeteria", sentence4, False, True, 4)
character5 = Character("orange", "OTwo", "OTwo", sentence5, False, True, 5)
character6 = Character("yellow", "Electrical", "Electrical", sentence6, True, True, 6)

c = [character1, character2, character3, character4, character5, character6]

(n, crewmates) = loadGameDate(0)

# for crewmate in c:
#     print(crewmate.tostring())



print("The impostors are:", solve(crewmates, n))

# crewmates = moveCrewmates(crewmates, n)
create_file(generateAllAsumptions(n, crewmates))
#
# for crewmate in crewmates:
#     print(crewmate.tostring())
#
# print("\n")
#
# crewmates = moveCrewmates(crewmates, n)
#
# for crewmate in crewmates:
#     print(crewmate.tostring())
# print("\n")

def areAllDead(crewmates):
    for crewmate in crewmates:
        if crewmate.alive and not crewmate.isImpostor:
            return False
    return True

round = 0
impostorsFound = False

while(areAllDead(crewmates) == False and impostorsFound == False):

    print("Round: ", round)
    sus = solve(crewmates, n)
    if len(sus) != 0:
        playsound("/home/stoian/Home/AI/MoagUs/fol_prover9/Among Us Role Sound Effect.mp3")
    print("The impostors are:", solve(crewmates, n))

    for crewmate in crewmates:
        print(crewmate.tostring())
    crewmates = moveCrewmates(crewmates, n)

    impostorsFound = findImpostor(crewmates, n, round)

    round += 1
    time.sleep(1)

if areAllDead(crewmates):
    print("The impostors won")

else:
    print("The crewmates won")