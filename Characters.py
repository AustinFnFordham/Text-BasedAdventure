import time
from datetime import date
import json

def readDescriptions():
    with open('races_desc.json') as f:
        descriptions = json.load(f)
        return descriptions

"""  helper function  """
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) <  (birthDate.month, birthDate.day)) 
    return age 


class Character:
    """
    General character class
    """
    def __init__(self, name="", age=0, race="", dexterity=5, charisma=5, strength=5, constitution=5, intelligence=5, wisdom=5, health=10, exp=1):
        self.setName()
        self.setAge()
        self.setRace()
        self.dex = dexterity
        self.cha = charisma
        self.stg = strength
        self.con = constitution
        self.int = intelligence
        self.wis = wisdom
        self.health = health
        self.exp = 1

    def __repr__(self):
        return f"{self.name}: a {self.race}"
    
    def showStats(self):
        """
        Show the character's attribute values
        """
        for property_, value in vars(self).items():
            print(property_, ": ", value)

    def setName(self):
        """
        This method prompts the user for the name, modifies the character object and assigns the given value to the property 'name'
        """
        self.name = input('What is your name Traveller? ')
        
        time.sleep(1)

    def setAge(self):
        print('Let\'s determine your age.')
        month = int(input('Month: '))
        day = int(input('Day: '))
        year = int(input('Year: '))
        self.age = calculateAge(date(year, month, day))
        
        time.sleep(1)
    
    def setRace(self):
        RACEOPTIONS = ['Human', 'Dwarf', 'Elf', 'Dragonborn', 'Tiefling', 'Half-Elf']
        # list choices as (0) Human, (1) Enhanced, etc
        choices = ', '.join([f'({i}) {race}' for i, race in enumerate(RACEOPTIONS)])
        # loop forever
        while True:
            choice = input(f'Choose a race: {choices} \n')
            choice = choice.upper()
            if choice == 'Q':
                print('Bye!')
                break
            elif not(choice.isdigit()):
                # Not a number
                print('Sorry, please choose a number')
            elif not 0 <= int(choice) <= len(RACEOPTIONS):
                # Number outside of the range of choices
                print('Sorry, please choose again')
            else:
                # The number input by the user matches the position
                # of their choice in the list of races
                selection = RACEOPTIONS[int(choice)]
                while True:
                    description = input(f'You chose {selection} - Would you like to see a description? (Y/N)\n')
                    description = description.upper()

                    if description == 'Y':
                        race_descriptions = readDescriptions()
                        print('*'*100,"\n"
                            f"Description: {race_descriptions[selection]}\n", '*'*100)
                        break

                    else:
                        print('Description: Opted Out')
                        break
                confirm = input(f'You chose {selection} - Confirm? (Y/N)\n')
                if confirm.upper() == 'Y':
                    print(f'Confirmed - you\'ve selected {selection}!')
                    break
                else:
                    print('OK, let\'s try again')
        time.sleep(1)
        self.race = selection

    def fight(self, monster):
        print(f"Let's fight!!!\n{self.name}, health: {self.health}\t{monster.race} health: {monster.health}")
        while self.health > 0 and monster.health >0:
            strike = input("What do I do: punch or kick? (P/K)\n")
            if strike.upper() == "P":
                monster.health -= 2
                print(f"{monster.race} has {monster.health} health left.")
            elif strike.upper() == "K":
                monster.health -= 5
                print(f"{monster.race} has {monster.health} health left.")
            else:
                print("You missed!")
                print(f"{monster.race} has {monster.health} health left.")
            print(f"Now it's {monster.race}'s turn")
            self.health -= 1
        if self.health == 0:
            print("You're dead. Game over")

        elif monster.health == 0:
            print(f"You defeated {monster.race}! Congratulations, you gain 10 exp!")
            self.exp += 1
            print(f"Now you have {self.exp} experience.")

class Monster:

    def __init__(self, race="Monster", attack=1, health=5):
        self.race = race
        self.attack = attack
        self.health = health

    def __repr__(self):
        return f"{self.race}! A monster with {self.attack} attack and {self.defence} defence."
        



if __name__ == "__main__":
    print("Welcome to Fantasy World 3000!")
    p1 = Character()
    p1.showStats()