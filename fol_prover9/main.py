
from characters import Character
from folProver9 import solve, create_file, generateAllAsumptions
from games import loadGameDate

sentence1 = "Crewmate1 is in OTwo with Crewmate5"
sentence2 = "Crewmate2 is in Cafeteria with Crewmate4"
sentence3 = "Crewmate3 is in Admin alone"
sentence4 = "Crewmate4 is in Cafeteria with Crewmate2"
sentence5 = "Crewmate5 is in OTwo with Crewmate1"
sentence6 = "Crewmate6 is in Electrical with Crewmate2"


character1 = Character("red", "OTwo", sentence1, False)
character2 = Character("blue", "Cafeteria", sentence2, False)
character3 = Character("green", "Admin", sentence3, False)
character4 = Character("pink", "Cafeteria", sentence4, False)
character5 = Character("orange", "OTwo", sentence5, False)
character6 = Character("yellow", "Electrical", sentence6, True)

c = [character1, character2, character3, character4, character5, character6]
# create_file(generateAllAsumptions(6, c))

(n, crewmates) = loadGameDate(0)

for crewmate in crewmates:
    print(crewmate.tostring())



print("The impostors are:", solve(crewmates, n))
