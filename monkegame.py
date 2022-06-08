# Modules:
import random, time, threading
# Define the variables:

# Supplies:
leather = 0
leaves = 0
wood = 0
metal = 0
stone = 0
bones = 0
strings = 0
meat = 0

# Weapon variables:
spear = 0
sword = 0
axe = 1
daggers = 0
bow = 0
pickaxes = 1
# Other:
fires = 0
health = 100
hunger = 100
timesmined = 0
bananasfound = 0
animalskilled = 0
# Define hungerloss function:
def hungerloss():
    # Globalize the hunger variable:
    global hunger
    # While loop:
    while True:
        # Remove 3 from hunger variable:
        hunger -= 3.0
        # Wait for 10 seconds:
        time.sleep(10)
# Define the thread target:
x = threading.Thread(target=hungerloss)
# Start threading:
x.start()

print("You are a monke. What would you like to do?")
# Define main function:
def main():
    # Globalize variables:
    global health
    global hunger
    global fires
    global meat
    global spear
    global sword
    global bow
    global axe
    global daggers
    global pickaxes
    global animalskilled
    global strings
    global wood
    global stone
    global metal
    global bones
    global leather
    global leaves
    global timesmined
    global bananasfound

    # If user has mined 10 times:
    if timesmined == 10:
        print('//Oops! Your pickaxe broke! Time to craft a new one!//')
        pickaxes -= 1
        timesmined = 0
        # Wait for 4 seconds:
        time.sleep(4)
        print('\n' * 30)
        
    # If user hits 0% hunger:
    while hunger <= 0:
        print('\n' * 5)
        print('//You died due to hunger!//')
        # Wait for 5 seconds:
        time.sleep(5)
        # Exit the program:
        exit()

    # If user hits 0% health:
    while health <= 0:
        print('\n' * 5)
        print('//You died due to low health!//')
        # Wait for 5 seconds:
        time.sleep(5)
        # Exit the program:
        break

    # If user has more than 100 health:
    if health > 100:
        # Re-define health variable to 100:
        health = 100
    
    # If user has more than 100 hunger:
    if hunger > 100:
        # Re-define hunger variable to 100:
        hunger = 100

    # Print out health and hunger status:
    print(f'Health: {health}')
    print(f'Hunger: {hunger}')
    print()
    print('1. Start a fire (you can also extinguish it)')
    print('2. Craft something')
    print('3. Hunt down animals')
    print('4. Get supplies')
    print('5. Eat')
    print('6. Inventory')
    # Input field:
    entry = input('>>> ').lower()

    # If input is start a fire:
    if entry in ('1.', '1', 'start a fire'):
        # If user has started 0 fires:
        if fires == 0:
            # If user doesn't have 8 wood or 4 leaves:
            if wood < 8 or leaves < 4:
                print('You need 8 wood and 4 leaves to start a fire!')
                # Wait for 3 seconds:
                time.sleep(3)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if user has 8 wood and 4 leaves:
            else:
                print('You have started a fire.')
                # Remove 8 from wood variable:
                wood -= 8
                # Remove 4 from leaves variable:
                leaves -= 4
                # Add 1 to fires variable:
                fires += 1
                # Wait for 3 seconds:
                time.sleep(3)
                print('\n' * 3)
                # Call the main function:
                main()
        # Else if user has already started a fire:
        else:
            print('You already have a fire burning! Extinguishing current one.')
            # Remove 1 from fires variable:
            fires -= 1
            # Wait for 3 seconds:
            time.sleep(3)
            print('\n' * 30)
            # Call the main function:
            main()

        
    # Else if input is craft something:
    elif entry in ('2.', '2', 'craft something'):
        print('\n' * 3)
        print('Weapons: \n\n')
        print('1. Spear')
        print('2. Sword')
        print('3. Axe')
        print('4. Daggers')
        print('5. Bow')
        print('Other: \n\n')
        print('6. Homemade bandages')
        # Input field:
        craftentry = input('What would you like to craft?: ').lower()
        # If user wants to craft a spear:
        if craftentry in ('1.', '1', 'spear'):
            # If user doesn't have 3 wood:
            if wood < 3:
                print('You need 3 wood to craft a spear!')
                # Wait for 3 seconds:
                time.sleep(3)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if user has 3 wood:
            else:
                # Input field:
                confirm = input('Craft a spear out of 3 wood? (Y/N): ').lower()
                # If user doesn't want to craft a spear:
                if confirm not in 'y':
                    # Wait for 3 seconds:
                    time.sleep(3)
                    print('\n' * 5)
                    # Call the main function:
                    main()
                # Else if the user wants to craft a spear:
                else:
                    print('You have crafted a spear.')
                    # Remove 3 from wood variable:
                    wood -= 3
                    # Add 1 to spear variable:
                    spear += 1
                    # Wait for 3 seconds:
                    time.sleep(3)
                    print('\n' * 5)
                    # Call the main function:
                    main()

        # Elif user wants to craft a sword:
        elif craftentry in ('2.', '2', 'sword'):
            # If user already has a sword:
            if sword >= 1:
                print('You already have a sword!')
                # Wait for 3 seconds:
                time.sleep(3)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if the user doesn't have a sword:
            else:
                # If user doesn't have 5 metal:
                if metal < 5:
                    print('You need 5 metal to craft a sword!')
                    # Wait for 3 seconds:
                    time.sleep(3)
                    print('\n' * 30)
                    # Call the main function:
                    main()
                # Else if the user has 5 metal:
                else:
                    # Input field:
                    confirm = input('Craft a sword with 5 metal? (Y/N):').lower()
                    # If user doesn't want to craft a sword:
                    if confirm not in 'y':
                        # Wait for 3 seconds:
                        time.sleep(3)
                        print('\n' * 5)
                        # Call the main function:
                        main()
                    # Else if the user wants to craft a sword:
                    else:
                        print('You have crafted a sword.')
                        # Add 1 to sword variable:
                        sword += 1
                        # Remove 5 from metal variable:
                        metal -= 5
                        # Wait for 3 seconds:
                        time.sleep(3)
                        print('\n' * 30)
                        # Call the main function:
                        main()

        # Else if the user wants to craft an axe:
        elif craftentry in ('3.', '3', 'axe'):
            # If user already has an axe:
            if axe >= 1:
                print('You already have an axe!')
                # Wait for 3 seconds:
                time.sleep(3)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if the user doesn't have an axe:
            else:
                # If user doesn't have 6 wood:
                if wood < 6:
                    print('You need 6 wood to craft an axe!')
                    # Wait for 3 seconds:
                    time.sleep(3)
                    print('\n' * 30)
                    # Call the main function:
                    main()
                # Else if the user has 6 wood:
                else:
                    # Input field:
                    confirm = input('Craft an axe with 6 wood? (Y/N):').lower()
                    # If the user doesn't want to craft an axe:
                    if confirm not in 'y':
                        # Wait for 3 seconds:
                        time.sleep(3)
                        print('\n' * 5)
                        # Call the main function:
                        main()
                    # Else if the user wants to craft an axe:
                    else:
                        print('You have crafted an axe.')
                        # Add 1 to axe variable:
                        axe += 1
                        # Remove 6 from wood variable:
                        wood -= 6
                        # Wait for 3 seconds:
                        time.sleep(30)
                        print('\n' * 5)
                        # Call the main function:
                        main()

        # Else if the user wants to craft daggers:
        elif craftentry in ('4.', '4', 'daggers'):
            # If the user already has daggers:
            if daggers >= 1:
                print('You already have daggers!')
                # Wait for 3 seconds:
                time.sleep(3)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if the user doesn't have daggers:
            else:
                # If user doesn't have 3 metal or 2 bones:
                if metal < 3 or bones < 2:
                    print('You need 3 metal and 2 bones to craft daggers!')
                    # Wait for 3 seconds:
                    time.sleep(3)
                    print('\n' * 30)
                    # Call the main function:
                    main()
                # Else if the user has 3 metal and 2 bones:
                else:
                    # Input field:
                    confirm = input('Craft daggers with 3 metal and 2 bones? (Y/N):').lower()
                    # If user doesn't want to craft daggers:
                    if confirm not in 'y':
                        # Wait for 3 seconds:
                        time.sleep(3)
                        print('\n' * 5)
                        # Call the main function:
                        main()
                    # Else if the user wants to craft daggers:
                    else:
                        print('You have crafted daggers.')
                        # Add 1 to daggers variable:
                        daggers += 1
                        # Remove 1 from metal variable:
                        metal -= 3
                        # Remove 1 from bones variable:
                        bones -= 2
                        # Wait for 3 seconds:
                        time.sleep(3)
                        print('\n' * 30)
                        # Call the main function:
                        main()

        # Elif user wants to craft a bow:
        elif craftentry in ('5.', '5', 'bow'):
            # If user already has a bow:
            if bow >= 1:
                print('You already have a bow!')
                # Wait for 3 seconds:
                time.sleep(3)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if the user doesn't have a bow:
            else:
                # If user doesn't have 3 wood or 2 strings:
                if wood < 3 or strings < 2:
                    print('You need 3 wood and 2 strings to craft a bow!')
                    # Wait for 3 seconds:
                    time.sleep(3)
                    print('\n' * 30)
                    # Call the main function:
                    main()
                # Else if the user has 3 wood and 2 strings:
                else:
                    # Input field:
                    confirm = input('Craft a bow with 3 wood and 2 strings? (Y/N):').lower()
                    # If the user doesn't want to craft a bow:
                    if confirm not in 'y':
                        # Wait for 3 seconds:
                        time.sleep(3)
                        print('\n' * 5)
                        # Call the main function:
                        main()
                    # Else if the user wants to craft a bow:
                    else:
                        print('You have crafted a bow.')
                        # Add 1 to bow variable:
                        bow += 1
                        # Remove 3 from wood variable:
                        wood -= 3
                        # Remove 2 from strings variable:
                        strings -= 2
                        # Wait for 3 seconds:
                        time.sleep(3)
                        print('\n' * 30)
                        # Call the main function:
                        main()
        elif craftentry in ('6', '6.', 'homemade bandages', 'bandages'):
            # If user doesn't have 5 leaves or 5 strings:
            if leaves < 5 or strings < 5:
                print('You need 5 leaves and 5 strings to craft a bandage!')
                # Wait for 3 seconds:
                time.sleep(3)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if the user has 5 leaves and 5 strings:
            else:
                # Input field:
                confirm = input('Craft a bandage with 5 wood and 5 strings? (Y/N):').lower()
                # If the user doesn't want to craft a bandage:
                if confirm not in 'y':
                    # Wait for 3 seconds:
                    time.sleep(3)
                    print('\n' * 5)
                    # Call the main function:
                    main()
                # Else if the user wants to craft a bandage:
                else:
                    print('You have crafted a bandage and used it.')
                    # Remove 5 from leaves variable:
                    leaves -= 5
                    # Remove 5 from strings variable:
                    strings -= 5
                    # Add 20 to health variable:
                    health += 20
                    # Wait for 3 seconds:
                    time.sleep(3)
                    print('\n' * 30)
                    # Call the main function:
                    main()
        else:
            print('\n' * 30)
            # Call the main function:
            main()

    # Else if entry is hunt down animals:
    elif entry in ('3.', '3', 'hunt down animals'):
        print('\n' * 3)
        # Input field:
        confirm = input('Hunt down an animal? (Y/N): ').lower()
        # If user doesn't want to hunt down animals:
        if confirm not in 'y':
            # Wait for 3 seconds:
            time.sleep(3)
            print('\n' * 30)
            # Call the main function:
            main()
        # Else if the user wants to hunt down animals:
        else:
            # Variables that contain the random func.:
            animalchoice = random.choice(['cow', 'sheep', 'pig', 'chicken', 'lion', 'nothing'])
            healthlost = random.randrange(1, 30)
            meatgained = random.randrange(1, 10)
            leathergained = random.randrange(1, 5)
            # Else if user didn't get to hunt down any animals:
            if animalchoice == 'nothing':
                print(f"You didn't find any animals to hunt!")
                # Wait for 4 seconds:
                time.sleep(4)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else:
            else:
                print(f'You put down a {animalchoice}! You gained {meatgained} meat, {leathergained} leather and lost {healthlost} health.')
                # Add 1 to animalskilled variable:
                animalskilled += 1
                # Add (meatgained) to meat variable:
                meat += meatgained
                leather += leathergained
                if meat > 30:
                    meat = 30
                if leather > 30:
                    leather = 30
                # Remove (healthlost) from health variable:
                health -= healthlost
                # Wait for 5 seconds:
                time.sleep(5)
                print('\n' * 30)
                # Call the main function:
                main()


    elif entry in ('4', '4.', 'get supplies'):
        print('Materials: \n\n')
        print('1. Trees')
        print('2. Stone')
        print('3. Metal')
        print('4. String')
        print('Other: \n\n')
        print('5. Homemade bandages')
        # Input field:
        supplyentry = input('What would you like to harvest?: ').lower()
        # If user wants to take down trees:
        if supplyentry in ('1.', '1', 'trees'):
            # Define variables:
            woodamount = random.randrange(0,10)
            leavesamount = random.randrange(1,4)
            bananachance = random.randrange(0,20)
            # If user didn't find any trees: 
            if woodamount == 0:
                print("You didn't find any trees!")
                # Wait for 4 seconds:
                time.sleep(4)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if the user found trees:
            else:
                # If user found a banana from the tree:
                if bananachance == 17:
                    print('You found a banana! 15+ health')
                    # Add 15 to health variable:
                    health += 15
                    # Add 1 to bananasfound variable:
                    bananasfound += 1
                print(f'You brought trees down with an axe and got {woodamount} wood and {leavesamount} leaves!')
                # Add (woodamount) to wood variable:
                wood += woodamount
                # Add (leaves) to leavesamount variable:
                leaves += leavesamount
                if wood > 30:
                    wood = 30
                if leaves > 30:
                    leaves = 30
                # Wait for 5 seconds:
                time.sleep(5)
                print('\n' * 30)
                # Call the main function:
                main()

        # Else if user wants to obtain stone:
        elif supplyentry in ('2.', '2', 'stone'):
            # Define the variable:
            stoneamount = random.randrange(0,7)
            # If user didn't get to obtain any stone:
            if stoneamount == 0:
                print("You didn't get to obtain any stone!")
                # Wait for 4 seconds:
                time.sleep(4)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if the user got to obtain stone:
            else:
                print(f'You obtained {stoneamount} stone!')
                # Add (stoneamount) to stone variable
                stone += stoneamount
                timesmined += 1
                if stone > 30:
                    stone = 30
                # Wait for 5 seconds:
                time.sleep(5)
                print('\n' * 30)
                # Call the main function:
                main()

        # Else if the user wants to obtain metal:
        elif supplyentry in ('3', '3.', 'metal'):
            # Define variable:
            metalamount = random.randrange(0,5)
            # If user didn't find any metal:
            if metalamount == 0:
                print("You didn't find any metal from mining!")
                # Wait for 4 seconds:
                time.sleep(4)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if the user found metal:
            else:
                print(f'You mined and got {metalamount} metal!')
                # Add (metalamount) to metal variable:
                metal += metalamount
                timesmined += 1
                if metal > 30:
                    metal = 30
                # Wait for 5 seconds:
                time.sleep(5)
                print('\n' * 30)
                # Call the main function:
                main()
            
        # Else if the user wants to obtain string:
        elif supplyentry in ('4', '4.', 'string'):
            # Define variable:
            stringamount = random.randrange(0,3)
            # If user didn't find any strings:
            if stringamount == 0:
                print("You didn't find any strings!")
                # Wait for 4 seconds:
                time.sleep(4)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if the user found strings:
            else:
                print(f'You found cobwebs and obtained {stringamount} strings!')
                # Add (stringamount) to strings variable:
                strings += stringamount
                if strings > 30:
                    strings = 30
                # Wait for 5 seconds:
                time.sleep(5)
                print('\n' * 30)
                # Call the main function:
                main()
        
        else:
            print('\n' * 30)
            # Call the main function:
            main()
    # Else if input is eat:
    elif entry in ('5', '5.', 'eat'):
        def eat():
            global hunger
            global meat
            # If user has fewer than 3 meat:
            if meat < 3:
                print("You need 3 meat to eat! Get some by hunting animals.")
                # Wait for 3 seconds:
                time.sleep(3)
                print('\n' * 30)
                # Call the main function:
                main()
            # Else if user has meat to eat:
            else:
                # If user has no fires currently burning:
                if fires == 0:
                    print("You need to start a fire first to be able to eat meat!")
                    # Wait for 3 seconds:
                    time.sleep(3)
                    print('\n' * 30)
                    # Call the main function:
                    main()
                # Else if user has fires currently burning:
                else:
                    # Define the variable for random number:
                    hungeramount = random.randint(0,20)
                    if (int(hungeramount) + int(hunger)) > 100 or hungeramount == 0:
                        eat()
                    else:
                        print(f'You ate meat and gained {hungeramount}% hunger.')
                        # Add (hungeramount) to hunger variable:
                        hunger += hungeramount
                        meat -= 3
                        # Wait for 4 seconds:
                        time.sleep(4)
                        print('\n' * 30)
                        # Call the main function:
                        main()
        eat()

    # Else if input is inventory:
    elif entry in ('6', '6.', 'inventory'):
        # Display the whole inventory:
        print('\n' * 5)
        print('Inventory')
        print('---------')
        print('Materials:')
        print(f'Wood: {wood}  Metal: {metal}')
        print(f'Stone: {stone}  Bones: {bones}')
        print(f'Strings: {strings}  Leather: {leather}')
        print(f'Leaves: {leaves}')
        print('')
        print('Weapons:')
        print(f'Axes: {axe}  Spears: {spear}')
        print(f'Swords: {sword}  Daggers: {daggers}')
        print(f'Bows: {bow}  Pickaxes: {pickaxes}')
        print('Other:')
        print('')
        print(f'Animals killed: {animalskilled}  Meat: {meat}')
        print(f'Fires burning: {fires}  Daggers: {daggers}')
        print(f'Bananas found: {bananasfound}')
        print()
        input('Type anything to go back: ')
        print('\n' * 5)
        # Call the main function:
        main()
    # Else if the user typed in something else out of choices:
    else:
        print('\n' * 30)
        # Call the main function:
        main()

# Call the main function:
main()