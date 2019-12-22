from DiceRoll import diceRoll, EnemydiceRoll


weapondmg = 5
enemyweapondmg = 3
charhealth = 15
enemyhealth = 15
enemyAC = 11
charAC = 10

def characterdmg():
    enemyhealth = 15
    if diceRoll.d20(diceRoll) >= enemyAC:
        enemyhealth -= weapondmg
        print(f'The Enemies health is now {enemyhealth}!')
    else:
        print('You missed!')

def crit():
    if diceRoll.d20(diceRoll) == 20:
        return enemyweapondmg * 2

def enemydmg():
    charhealth = 15

    if EnemydiceRoll.d20(EnemydiceRoll) >= charAC:
        charhealth -= enemyweapondmg
        print(f'You\'re health is now {charhealth}! Be careful!')
        return charhealth
    else:
        charhealth
        print(f"They missed! Your health is {charhealth}!")

def healthBar():
    if charhealth == 0:
        quit()
charhealth = 15
enemyhealth = 15
while charhealth > 0 and enemyhealth > 0:
    input('Attack!')
    if diceRoll.d20(diceRoll) <= enemyAC:
        print('You missed!')
    else:
        enemyhealth -= weapondmg
        print(f'The Enemies health is now {enemyhealth}!')

    if EnemydiceRoll.d20(EnemydiceRoll) <= charAC:

        print(f"They missed! Your health is {charhealth}")
    else:
        charhealth -= enemyweapondmg
        print(f'You\'re health is now {charhealth}!')

    if charhealth == 0:
        print("You died!!")

    if enemyhealth == 0:
        print('You won!!')
