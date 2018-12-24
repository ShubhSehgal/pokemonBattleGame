import random


class PokemonMove:
    def __init__(self, name, codeName, damage, heal, moveType):
        self.name = name
        self.codeName = codeName
        self.damage = damage
        self.heal = heal
        self.moveType = moveType

flamethrower = PokemonMove("Flamethrower", "flamethrower", 6, 0, "fire")
tackle = PokemonMove("Tackle", "tackle", 5, 0, "normal")
fireblast = PokemonMove("Fire Blast", "fireblast", 7, 0, "fire")
dragonclaw = PokemonMove("Dragon Claw", "dragonclaw", 5, 0, "dragon")
solarbeam = PokemonMove("Solarbeam", "solarbeam", 7, 0, "grass")
leechseed = PokemonMove("Leech Seed", "leechseed", 5, 30, "grass")
razorleaf = PokemonMove("Razor Leaf", "razorleaf", 6, 0, "grass")
earthquake = PokemonMove("Earthquake", "earthquake", 6, 0, "ground")
hydropump = PokemonMove("Hydropump", "hydropump", 7, 0, "water")
icebeam = PokemonMove("Ice Beam", "icebeam", 5, 0, "ice")
bubbleblast = PokemonMove("Bubble Blast", "bubbleblast", 5, 0, "water")
dragonsmash = PokemonMove("Dragon Smash", "dragonsmash", 7, 0, "dragon")
rocksmash = PokemonMove("Rock Smash", "rocksmash", 6, 0, "rock")


class Pokemon:
    def __init__(self, name, type, hp, attack, defense, speed, move1, move2, move3, move4):
        self.name = name
        self.type = type
        self.hp = hp
        self. attack = attack
        self.defense = defense
        self.speed = speed
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4


charizard = Pokemon("Charizard", "fire", 150, 9, 7, 7, flamethrower, tackle, fireblast, dragonclaw)
venusaur = Pokemon("Venusaur", "grass", 150, 8, 8, 5, solarbeam, leechseed, razorleaf, earthquake)
blastoise = Pokemon("Blastoise", "water", 150, 7, 9, 6, hydropump, icebeam, bubbleblast, tackle)
garchomp = Pokemon("Garchomp", "dragon", 150, 9, 8, 9, dragonsmash, earthquake, rocksmash, flamethrower)

charizardcomp = Pokemon("Charizard", "fire", 150, 9, 7, 7, flamethrower, tackle, fireblast, dragonclaw)
venusaurcomp = Pokemon("Venusaur", "grass", 150, 8, 8, 5, solarbeam, leechseed, razorleaf, earthquake)
blastoisecomp = Pokemon("Blastoise", "water", 150, 7, 9, 6, hydropump, icebeam, bubbleblast, tackle)
garchompcomp = Pokemon("Garchomp", "dragon", 150, 9, 8, 9, dragonsmash, earthquake, rocksmash, flamethrower)


def chooseComputerPokemon():
    randNum = random.randint(1, 4)

    if randNum == 1:
        computerPokemon = charizardcomp
        return computerPokemon

    elif randNum == 2:
        computerPokemon = venusaurcomp
        return computerPokemon

    elif randNum == 3:
        computerPokemon = blastoisecomp
        return computerPokemon

    elif randNum == 4:
        computerPokemon = garchompcomp
        return computerPokemon


def computerFight(computerPokemon):
    randNum = random.randint(1, 9)

    if randNum < 3:
        computerMove = computerPokemon.move1
        return computerMove

    elif randNum < 5:
        computerMove = computerPokemon.move2
        return computerMove

    elif randNum < 7:
        computerMove = computerPokemon.move3
        return computerMove

    elif randNum <= 9:
        computerMove = computerPokemon.move4
        return computerMove


def userEffectiveness(userMove, computerPokemon):

    if userMove.moveType == "fire":

        if computerPokemon.type == "dragon" or "fire" or "water" or "ground":
            damage = userMove.damage / 2
            return damage

        elif computerPokemon.type == "grass" or "ice":
            damage = userMove.damage * 2
            return damage

        else:
            damage = userMove.damage
            return damage

    elif userMove.moveType == "normal":
        damage = userMove.damage
        return damage

    elif userMove.moveType == "dragon":

        if computerPokemon.type == "dragon":
            damage = userMove.damage * 2
            return damage

        else:
            damage = userMove.damage
            return damage

    elif userMove.moveType == "grass":

        if computerPokemon.type == "grass" or "fire" or "rock" or "ground" or "dragon":
            damage = userMove.damage / 2
            return damage

        elif computerPokemon.type == "water" or "ground" or "rock":
            damage = userMove.damage * 2
            return damage

        else:
            damage = userMove.damage
            return damage

    elif userMove.moveType == "ground":

        if computerPokemon.type == "grass":
            damage = userMove.damage / 2
            return damage

        elif computerPokemon.type == "fire" or "rock":
            damage = userMove.damage * 2
            return damage

        else:
            damage = userMove.damage
            return damage

    elif userMove.moveType == "water":

        if computerPokemon.type == "water" or "grass" or "dragon":
            damage = userMove.damage / 2
            return damage

        elif computerPokemon.type == "fire" or "ground" or "rock":
            damage = userMove.damage * 2
            return damage

        else:
            damage = userMove.damage
            return damage

    elif userMove.moveType == "rock":

        if computerPokemon.type == "ground":
            damage = userMove.damage / 2
            return damage

        elif computerPokemon.type == "fire" or "ice":
            damage = userMove.damage * 2
            return damage

        else:
            damage = userMove.damage
            return damage

    elif userMove.moveType == "ice":

        if computerPokemon.type == "fire" or "water" or "ice":
            damage = userMove.damage / 2
            return damage

        elif computerPokemon.type == "grass" or "ground" or "dragon":
            damage = userMove.damage * 2
            return damage

    else:
        damage = userMove.damage
        return damage

def computerEffectiveness(computerMove, userPokemon):

    if computerMove.moveType == "fire":

        if userPokemon.type == "dragon" or "fire" or "water" or "ground":
            damage = computerMove.damage / 2
            return damage

        elif userPokemon.type == "grass" or "ice":
            damage = computerMove.damage * 2
            return damage

        else:
            damage = computerMove.damage
            return damage

    elif computerMove.moveType == "normal":
        damage = computerMove.damage
        return damage

    elif computerMove.moveType == "dragon":

        if userPokemon.type == "dragon":
            damage = computerMove.damage * 2
            return damage

        else:
            damage = computerMove.damage
            return damage

    elif computerMove.moveType == "grass":

        if userPokemon.type == "grass" or "fire" or "rock" or "ground" or "dragon":
            damage = computerMove.damage / 2
            return damage

        elif userPokemon.type == "water" or "ground" or "rock":
            damage = computerMove.damage * 2
            return damage

        else:
            damage = computerMove.damage
            return damage

    elif computerMove.moveType == "ground":

        if userPokemon.type == "grass":
            damage = computerMove.damage / 2
            return damage

        elif userPokemon.type == "fire" or "rock":
            damage = computerMove.damage * 2
            return damage

        else:
            damage = computerMove.damage
            return damage

    elif computerMove.moveType == "water":

        if userPokemon.type == "water" or "grass" or "dragon":
            damage = computerMove.damage / 2
            return damage

        elif userPokemon.type == "fire" or "ground" or "rock":
            damage = computerMove.damage * 2
            return damage

        else:
            damage = computerMove.damage
            return damage

    elif computerMove.moveType == "rock":

        if userPokemon.type == "ground":
            damage = computerMove.damage / 2
            return damage

        elif userPokemon.type == "fire" or "ice":
            damage = computerMove.damage * 2
            return damage

        else:
            damage = computerMove.damage
            return damage

    elif computerMove.moveType == "ice":

        if userPokemon.type == "fire" or "water" or "ice":
            damage = computerMove.damage / 2
            return damage

        elif userPokemon.type == "grass" or "ground" or "dragon":
            damage = computerMove.damage * 2
            return damage

    else:
        damage = computerMove.damage
        return damage

def main():

    print("\nWelcome to Pokemon Battle Simulator. Here are the rules. To input, make sure you type in your desired option, or the number corresponding to your desired option. When typing, if there is a space inbetween the words making up the option, combine them.\n For example, the option (3) Fire Blast should be inputed as either fireblast or 3.\n\n Now, let's begin!")
    choice = (input("\nChoose your Pokemon. (1) Charizard, (2) Venusaur, (3) Blastoise or (4) Garchomp. Type name as written.")).lower()

    validInput = 0
    while validInput == 0:

        if choice == "charizard" or choice == "1":
            userPokemon = charizard
            validInput = 1

        elif choice == "venusaur" or choice == "2":
            userPokemon = venusaur
            validInput = 1

        elif choice == "blastoise" or choice == "3":
            userPokemon = blastoise
            validInput = 1

        elif choice == "garchomp" or choice == "4":
            userPokemon = garchomp
            validInput = 1

        else:
            choice = (input("\nSorry, that was not a valid input. Try again.\n\nChoose your Pokemon. (1) Charizard, (2) Venusaur, (3) Blastoise or (4) Garchomp. Type name as written.")).lower()

    print("\nYou chose " + userPokemon.name + ".")

    computerPokemon = chooseComputerPokemon()
    print("The computer chose " + computerPokemon.name + ".")

    print("\n" + userPokemon.name + " HP: " + str(userPokemon.hp))
    print(computerPokemon.name + " HP: " + str(computerPokemon.hp))

    while userPokemon.hp > 0 and computerPokemon.hp > 0:

        moveChoice = (input("\nWhat move should " + userPokemon.name + " do? (1) " + userPokemon.move1.name + ", (2) " + userPokemon.move2.name + ", (3) " + userPokemon.move3.name + " or (4) " + userPokemon.move4.name + ".")).lower()

        computerMove = computerFight(computerPokemon)

        userMove = 0

        validInput2 = 0
        while validInput2 == 0:
            if moveChoice == userPokemon.move1.codeName or moveChoice == "1":
                userMove = userPokemon.move1
                validInput2 = 1

            elif moveChoice == userPokemon.move2.codeName or moveChoice == "2":
                userMove = userPokemon.move2
                validInput2 = 1

            elif moveChoice == userPokemon.move3.codeName or moveChoice == "3":
                userMove = userPokemon.move3
                validInput2 = 1

            elif moveChoice == userPokemon.move4.codeName or moveChoice == "4":
                userMove = userPokemon.move4
                validInput2 = 1

            else:
                moveChoice = (input(
                    "\nWe're gonna be here all night if you can't input the move properly buddy. What move should " + userPokemon.name + " do? (1) " + userPokemon.move1.name + ", (2) " + userPokemon.move2.name + ", (3) " + userPokemon.move3.name + " or (4) " + userPokemon.move4.name + ".")).lower()

        winner = "nobody"
        if userPokemon.speed >= computerPokemon.speed:

            computerPokemon.hp -= userEffectiveness(userMove, computerPokemon) * userPokemon.attack - (2 * computerPokemon.defense)
            userPokemon.hp += userMove.heal
            print(userPokemon.name + " used " + userMove.name)

            if computerPokemon.hp <= 0:
                winner = "user"
                computerPokemon.hp = 0

            else:

                userPokemon.hp -= computerEffectiveness(computerMove, userPokemon) * computerPokemon.attack - (2 * userPokemon.defense)
                computerPokemon.hp += computerMove.heal
                print(computerPokemon.name + " used " + computerMove.name)

            if userPokemon.hp <= 0:
                winner = "computer"
                userPokemon.hp = 0

            print(userPokemon.name + " HP: " + str(userPokemon.hp))
            print(computerPokemon.name + " HP: " + str(computerPokemon.hp))

        elif userPokemon.speed < computerPokemon.speed:

            userPokemon.hp -= computerEffectiveness(computerMove, userPokemon) * computerPokemon.attack - (2 * userPokemon.defense)
            computerPokemon.hp += computerMove.heal
            print(computerPokemon.name + " used " + computerMove.name)

            if userPokemon.hp <= 0:
                winner = "computer"
                userPokemon.hp = 0

            else:

                computerPokemon.hp -= userEffectiveness(userMove, computerPokemon) * userPokemon.attack - (2 * computerPokemon.defense)
                userPokemon.hp += userMove.heal
                print(userPokemon.name + " used " + userMove.name)

            if computerPokemon.hp <= 0:
                winner = "user"
                computerPokemon.hp = 0

            print(userPokemon.name + " HP: " + str(userPokemon.hp))
            print(computerPokemon.name + " HP: " + str(computerPokemon.hp))

    if winner == "computer":
        print(userPokemon.name + " fainted! Computer wins!")

    elif winner == "user":
        print(computerPokemon.name + " fainted! You win!")

main()
