from Characters import Character, Monster


class Dungeon:
    """
    Place where adventures take place! Dungeons contain many monsters and puzzles.
    """

    def __init__(self, name="Dungeon", monsters=None, puzzles=None):
        self.name=name
        self.monsters=monsters
        self.puzzles=puzzles

    def __repr__(self):
        """
        Add plural endings to monsters and create a description of the dungeon monsters awaiting for you inside.
        """
        plurals = ["".join((monster,"s")) for monster in set(self.monsters)]
        monsters_string = ", ".join(plurals[:-1])
        return f"You're in the {self.name}. Watch out for {monsters_string} and {plurals[-1]}!"

    def explore(self, player):
        want_to_fight = input(f"{player.name}! Welcome to the {self.name}! Would you like to fight a monster? (Y/N)\n")

        if want_to_fight.upper() == "Y":
            choices = ', '.join([f'({i}) {monster}' for i, monster in enumerate(self.monsters)])

            monster_choice = input(f"Which monster would you like to fight?\n{choices}\n")
            race = self.monsters[int(monster_choice)]
            confirm_choice = input(f"You want to fight a {race}? That's very brave of you. Please confirm (Y/N)")
            if confirm_choice.upper() == "Y":
                monster = Monster(race=race)
                player.fight(monster)
            elif confirm_choice.upper() == "N":
                "Get the hell out of here you coward!!!"
        
        want_a_puzzle = input("Would you like to solve a puzzle and gain some experience and wisdom? (Y/N)\n")
        if want_a_puzzle.upper() == "Y":
            print("Well I don't have any puzzles for you yet.")

        print("Well, goodbye then.")

if __name__ == "__main__":
    p1 = Character()
    cave = Dungeon(name="Cave", monsters=["Zombie", "Vampire", "Dragon"])
    cave.explore(p1)
