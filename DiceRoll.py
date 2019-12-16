import random

#player diceRoll
class diceRoll:

    def d3(self):
        threeSided = random.randint(1, 3)
        print(f'You rolled: {threeSided}!')

    def d4(self):
        fourSided = random.randint(1, 4)
        print(f'You rolled: {fourSided}!')

    def d6(self):
        sixSided = random.randint(1, 6)
        print(f'You rolled: {sixSided}!')

    def d8(self):
        eightSided = random.randint(1, 8)
        if eightSided == 8:
            print(f'{eightSided}! You did max damage!')
        else:
            print(f'You rolled: {eightSided}!')

    def d10(self):
        tenSided = random.randint(1, 10)
        if tenSided == 10:
            print(f'{tenSided}! You did max damage!')
        else:
            print(f'You rolled: {tenSided}!')

    def d12(self):
        twelveSided = random.randint(1, 12)
        if twelveSided == 12:
            print(f'{twelveSided}! You did max damage!')
        else:
            print(f'You rolled: {twelveSided}!')

    def d20(self):
        twentySided = random.randint(1, 20)
        if twentySided == 1:
            print(f'{twentySided}! You rolled a critical miss!')
        elif twentySided == 20:
            print(f'{twentySided} You rolled a critical hit! ')
        else:
            print(f'You rolled: {twentySided}!')
        return twentySided

    def d20_RAW(self):
        twentySided = random.randint(1, 20)
        print(twentySided)
        return twentySided


class EnemydiceRoll:

    def d3(self):
        threeSided = random.randint(1, 3)
        print(f'The enemy rolled: {threeSided}!')

    def d4(self):
        fourSided = random.randint(1, 4)
        print(f'The enemy rolled: {fourSided}!')

    def d6(self):
        sixSided = random.randint(1, 6)
        print(f'The enemy rolled: {sixSided}!')

    def d8(self):
        eightSided = random.randint(1, 8)
        if eightSided == 8:
            print(f'{eightSided}! You did max damage!')
        else:
            print(f'The enemy rolled: {eightSided}!')

    def d10(self):
        tenSided = random.randint(1, 10)
        if tenSided == 10:
            print(f'{tenSided}! The enemy did max damage!')
        else:
            print(f'You rolled: {tenSided}!')

    def d12(self):
        twelveSided = random.randint(1, 12)
        if twelveSided == 12:
            print(f'{twelveSided}! The enemy did max damage!')
        else:
            print(f'You rolled: {twelveSided}!')

    def d20(self):
        twentySided = random.randint(1, 20)
        if twentySided == 1:
            print(f'{twentySided}! The enemy rolled a critical miss!')
        elif twentySided == 20:
            print(f'{twentySided} The enemy rolled a critical hit! ')
        else:
            print(f'The enemy rolled: {twentySided}!')
        return twentySided

    def d20_RAW(self):
        twentySided = random.randint(1, 20)
        print(twentySided)
        return twentySided
