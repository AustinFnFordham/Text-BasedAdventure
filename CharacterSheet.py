import time
from datetime import date

def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) <  (birthDate.month, birthDate.day)) 
    return age 


class Character:

    def __init__(self, name="", age=0):
        """
        Initialize a character object and prompt the user for the name, age and race.
        """
        self.charName()
        print(f'Hello {self.name}! Welcome to Fantasy World 3000!')
        self.charAge()
        print(f'Your Birthday: {self.age}\n(The year has been modified to match the setting of the game)')


    def charName(self):
        """
        This method prompts the user for the name, modifies the character object and assigns the given value to the property 'name'
        """
        self.name = input('What is your name Traveller? ')
        time.sleep(1)
    
    def charAge(self):
        print('Let\'s determine your age.')
        month = int(input('Month: '))
        day = int(input('Day: '))
        year = int(input('Year: '))
        self.age = calculateAge(date(year, month, day))
        
        # birth = f'Your Birthday: {month}/{day}/{year}\n'
        time.sleep(1)

    RACEOPTIONS = ['Human', 'Dwarf', 'Elf', 'Dragonborn', 'Tiefling', 'Half-Elf']

    RACEDESCRIPTOR = {0 : """

+1 Extra Feat, +2 to any attribute, or +1 to any choice of 2 attribute
Bipedal. 
Medium Humanoids. 

    """,
                      1 : """

+2 , +1 Extra Augment, +1 to any attribute or +1 Extra Feat/Skill.
Bipedal.
Small Humanoids. 

                      """,
                      2 : """

+2 Constitution[placeholder],+2 Skills , and +1 Extra Feat/Skill or +1 to any attribute
Bipedal.
Tall Humanoids.

                      """,
                      3 : """

+2 Strength[placeholder], +1 to any attribute, and +1 to A/C[placeholder]
Bipedal Dragon-Folk
                      """,
                      4 : """

+2 Intelligence[placeholder], +2 to any attribute, +1 Skills, or +1 Extra Feat
Bipedal(Generally).
Medium Humanoids.


                      """,
                      5 : """

+1 Wisdom, +1 to anyattribute, and +1 Extra Feat
Bipedal Half-Humanoid.

                      """}


    def chooseRace(self):
        # list choices as (0) Human, (1) Enhanced, etc
        choices = ', '.join([f'({i}) {race}' for i, race in enumerate(self.RACEOPTIONS)])
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
            elif not 0 <= int(choice) <= len(self.RACEOPTIONS):
                # Number outside of the range of choices
                print('Sorry, please choose again')
            else:
                # The number input by the user matches the position
                # of their choice in the list of races
                selection = self.RACEOPTIONS[int(choice)]
                while True:
                    description = input(f'You chose {selection} - Would you like to see a description? (Y/N)\n')
                    description = description.upper()

                    if description == 'Y':
                        print('*'*100,
                            f"""
                            Description:
    {self.RACEDESCRIPTOR[int(choice)]}
""", '*'*100
                        )
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
        return

#testing to see if it works

# Character.charName(Character)
# Character.charAge(Character)
# Character.chooseRace(Character)
if __name__ == "__main__":
    p1 = Character()