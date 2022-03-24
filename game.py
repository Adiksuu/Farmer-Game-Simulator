# ------------------ ( COLORAMA IMPORT - MODULES ) -----------------

import colorama
from colorama import Fore
colorama.init

import time

import random

# ------------------ (       ANY VARIABLES      ) ------------------

carrot = 0
carrot_name = 'bananas'
carrot_name_level = 1
carrot_name_cost = 500
cash = 0

carrot_barn = 0
barn_storage = 30
barn_open = False

bp_multi = 1
bp_multi_up = bp_multi + 1

bag_capility = 15
carrot_grow = 1
bag_capility_upgrade = 35
carrot_grow_upgrade = 2
bag_capility_cost = 50
carrot_grow_cost = 75

farmer = 0
farmer_up = 0.25
farmer_cost = 750
farmer_lvl = 0
farmer_counter = 0

ver_info_settings = 'True'

game_start = True
game_menu = True

free_money = False
free_money_2 = False
free_money_3 = False
free_money_4 = False
free_bag = False

house_selected = False
house_level = 1
house_level_max = 5
house_level_next = 2
house_cost = 3000

energy = 60
max_energy = 100
house_energy = 10
house_energy_next = 20
energy_remover = 1

day_time = 0
night = False

# ------------------ (     GAME START - WHILE    ) -----------------

while game_start == True:

    print('')
    print(Fore.LIGHTGREEN_EX + ' ---=( ' + Fore.GREEN + 'FARMER GAME v1.7 - Barn Update ' + Fore.LIGHTGREEN_EX + ')=---')
    print('')

    game_menu = True

# ------------------ (     GAME MENU - WHILE     ) -----------------

    while game_menu == True:

        if day_time >= 24:
            night = True
            day_time = 24
        else:
            night = False

        if night == True:
            if energy <= 25:
                carrot = 0
                carrot_name = 'bananas'
                carrot_name_level = 1
                carrot_name_cost = 500
                cash = 0

                bp_multi = 1
                bp_multi_up = bp_multi + 1

                bag_capility = 15
                carrot_grow = 1
                bag_capility_upgrade = 35
                carrot_grow_upgrade = 2
                bag_capility_cost = 50
                carrot_grow_cost = 75

                farmer = 0
                farmer_up = 0.25
                farmer_cost = 750
                farmer_lvl = 0
                farmer_counter = 0

                ver_info_settings = 'True'

                game_start = True
                game_menu = True

                free_money = False
                free_money_2 = False
                free_money_3 = False
                free_money_4 = False
                free_bag = False

                house_selected = False
                house_level = 1
                house_level_max = 5
                house_level_next = 2
                house_cost = 3000

                energy = 100
                max_energy = 100
                house_energy = 10
                house_energy_next = 20
                energy_remover = 1

                day_time = 0
                night = False
                print(Fore.LIGHTRED_EX + '>>> ' + Fore.RED + "You die, because night came and you didn't have enough energy. You lost all!")
            print(Fore.RED + '>>> ' + Fore.LIGHTRED_EX + 'The night has come!')
        else:
            night = False    

        if house_level == 1:
            house_energy = 10
            house_cost = 3000
            house_energy_next = 20
            house_level_next = 2
        elif house_level == 2:
            house_energy = 20
            house_cost = 7500
            house_energy_next = 25
            house_level_next = 3
        elif house_level == 3:
            house_energy = 25
            house_cost = 12500
            house_energy_next = 30
            house_level_next = 4
        elif house_level == 4:
            house_energy = 30
            house_cost = 17500
            house_energy_next = '35'
            house_level_next = '5'
        elif house_level == 5:
            house_energy = 35
            house_cost = 'MAX UPGRADE LEVEL'
            house_energy_next = 'MAX UPGRADE LEVEL'
            house_level_next = 'MAX UPGRADE LEVEL'

        if carrot_name_level == 1:
            carrot_name = 'carrots'
            cnn = 'melons'
        elif carrot_name_level == 2:
            carrot_name = 'melons'
            cnn = 'tomatos'
            bp_multi = 2
            bp_multi_up = bp_multi + 1
        elif carrot_name_level == 3:
            carrot_name = 'tomatos'
            cnn = 'potatoes'
            bp_multi = 3
            bp_multi_up = bp_multi + 1
        elif carrot_name_level == 4:
            carrot_name = 'potatoes'
            cnn = 'pumpkins'
            bp_multi = 4
            bp_multi_up = bp_multi + 1
        elif carrot_name_level == 5:
            carrot_name = 'pumpkins'
            cnn = 'beans'
            bp_multi = 5
            bp_multi_up = bp_multi + 1
        elif carrot_name_level == 6:
            carrot_name = 'beans'
            cnn = 'pees'
            bp_multi = 6
            bp_multi_up = bp_multi + 1
        elif carrot_name_level == 7:
            carrot_name = 'pees'
            cnn = 'MAX UPGRADE LEVEL'
            bp_multi = 7
            bp_multi_up = bp_multi + 1
            if bp_multi_up == 8:
                bp_multi_up = 7
            carrot_name_cost = 'MAX UPGRADE LEVEL'

        if energy <= 0:
            energy = 0

        print('')
        print(Fore.BLUE + '---=( ' + Fore.LIGHTBLUE_EX + 'SELECT OPTION ' + Fore.BLUE + ')=---')
        print('')
        print(Fore.CYAN + '1. ' + Fore.LIGHTCYAN_EX + 'Make a ' + str(carrot_name))
        print(Fore.CYAN + '2. ' + Fore.LIGHTCYAN_EX + 'Sell a ' + str(carrot_name))
        print(Fore.CYAN + '3. ' + Fore.LIGHTCYAN_EX + 'Upgrades')
        print(Fore.CYAN + '4. ' + Fore.LIGHTCYAN_EX + 'Settings')
        print(Fore.CYAN + '5. ' + Fore.LIGHTCYAN_EX + 'Farmer Machine')
        print(Fore.CYAN + '6. ' + Fore.LIGHTCYAN_EX + 'Quit game')
        print(Fore.CYAN + '7. ' + Fore.LIGHTCYAN_EX + 'Enter Code')
        print(Fore.CYAN + '8. ' + Fore.LIGHTCYAN_EX + 'Go home')
        print(Fore.CYAN + '9. ' + Fore.LIGHTCYAN_EX + 'Go barn')
        print('')

        selected_option = input(Fore.BLUE + '>>> ' + Fore.LIGHTBLUE_EX + 'SELECTED OPTION: ')

# ------------------ (     GAME MENU - IF'S     ) -----------------

        if selected_option == '1':
            if energy <= 0:
                print(Fore.RED + ">>> You can't work! Don't have energy!")
            else:
                if carrot < bag_capility:
                    carrot = carrot + carrot_grow
                    energy = energy - energy_remover
                    day_time = day_time + 1
                    if carrot == bag_capility:
                        print('')
                        if carrot_barn != barn_storage:
                            if barn_storage > carrot:
                                print(Fore.LIGHTMAGENTA_EX + '>>> ' + Fore.MAGENTA + 'Your bag is full!' + Fore.LIGHTMAGENTA_EX + ' Your ' + str(carrot_name) + ' was automatically moved to the barn!')
                                carrot_barn = carrot_barn + carrot
                                carrot = carrot - bag_capility
                            else:
                                print(Fore.RED + '>>> ' + Fore.LIGHTRED_EX + 'Your barn storage is too small!')
                        elif carrot_barn >= barn_storage:
                            print('')
                            print(Fore.RED + '>>>' + Fore.LIGHTRED_EX + ' Your barn is full! Upgrade your barn!')
                            carrot_barn = barn_storage
                    print('')
                    if carrot > bag_capility:
                        carrot = bag_capility
                    print(Fore.CYAN + 'You have: ' + str(carrot) + ' / ' + str(bag_capility) + Fore.BLUE + ' ' + str(carrot_name))
                elif carrot >= bag_capility:
                    print('')
                    if carrot_barn != barn_storage:
                        if barn_storage > carrot:
                            print(Fore.LIGHTMAGENTA_EX + '>>> ' + Fore.MAGENTA + 'Your bag is full!' + Fore.LIGHTMAGENTA_EX + ' Your ' + str(carrot_name) + ' was automatically moved to the barn!')
                            carrot_barn = carrot_barn + carrot
                            carrot = carrot - bag_capility
                        else:
                            print(Fore.RED + '>>> ' + Fore.LIGHTRED_EX + 'Your barn storage is too small!')
                    elif carrot_barn >= barn_storage:
                        print(Fore.RED + '>>>' + Fore.LIGHTRED_EX + ' Your barn is full! Upgrade your barn!')
                        carrot_barn = barn_storage

        elif selected_option == '2':
            if carrot > 0:
                print('')
                print(Fore.MAGENTA + '---=( ' + Fore.LIGHTMAGENTA_EX + 'Selled!' + Fore.MAGENTA + ' )=---')
                print('')
                print(Fore.MAGENTA + '>>> ' + Fore.LIGHTMAGENTA_EX + 'You sold: ' +
                      str(carrot) + Fore.MAGENTA + ' (x' + str(bp_multi) + ') Carrots')
                cash = cash + carrot * bp_multi
                carrot = carrot - carrot
                print(Fore.MAGENTA + '>>> ' + Fore.LIGHTMAGENTA_EX + 'You has: ' + str(cash) + Fore.MAGENTA + ' Cash')
                print('')
                print(Fore.MAGENTA + '---=( ' + Fore.LIGHTMAGENTA_EX + 'Selled!' + Fore.MAGENTA + ' )=---')
            elif carrot == 0:
                print('')
                print(Fore.MAGENTA + '---=( ' + Fore.LIGHTMAGENTA_EX + 'Selled!' + Fore.MAGENTA + ' )=---')
                print('')
                print(Fore.MAGENTA + '>>> ' + Fore.LIGHTMAGENTA_EX + "You don't have any " + str(carrot_name) + ' ' + Fore.MAGENTA + str(carrot) + ' / ' + str(bag_capility))
                print(Fore.MAGENTA + '>>> ' + Fore.LIGHTMAGENTA_EX + 'You has: ' + str(cash) + Fore.MAGENTA + ' Cash')
                print('')
                print(Fore.MAGENTA + '---=( ' + Fore.LIGHTMAGENTA_EX + 'Selled!' + Fore.MAGENTA + ' )=---')

        elif selected_option == '9':
            barn_open = True
            while barn_open == True:
                print('')
                print(Fore.LIGHTBLUE_EX + '>>>' + Fore.BLUE + ' Your Barn' + Fore.LIGHTBLUE_EX + ' <<<')
                print('')
                print(Fore.CYAN + '>>>' + Fore.BLUE + ' You have a ' + str(carrot_barn)  + ' / ' + str(barn_storage) + ' ' + str(carrot_name) + ' In Barn' + Fore.CYAN + ' Select "1" to get this ' + str(carrot_name) + '.')
                print(Fore.CYAN + '1. ' + Fore.BLUE + 'Take my ' + str(carrot_name))
                print('')
                barn_selected = input(Fore.CYAN + 'Selected option: ')

                if barn_selected == '1':
                    if bag_capility >= carrot_barn:
                        if carrot_barn != 0:
                            if carrot == 0:
                                carrot = carrot + carrot_barn
                                carrot_barn = 0
                                print('')
                                print(Fore.CYAN + '>>> ' + Fore.BLUE + 'Moved a carrot from barn to your inventory!')
                            else:
                                print('')
                                print(Fore.RED + '>>> ' + Fore.LIGHTRED_EX + 'You must has a 0 ' + str(carrot_name) + ' to move this!')
                        else:
                            print(Fore.RED + "You can't move a 0 " + str(carrot_name))
                    elif bag_capility < carrot_barn:
                        print(Fore.RED + '>>> ' + Fore.LIGHTRED_EX + 'Your bag is too small!')

                else:
                    barn_open = False

        elif selected_option == '3':
            print('')
            print(Fore.LIGHTCYAN_EX + '---=( ' + Fore.CYAN + 'UPGRADES' + Fore.LIGHTCYAN_EX + ' )=---')
            print('')
            print(Fore.LIGHTGREEN_EX + '>>> ' + Fore.GREEN + '1.' + Fore.LIGHTGREEN_EX + ' Upgrade a bag.' + Fore.GREEN + ' You have now: ' + str(bag_capility) + ' capitality.' + Fore.LIGHTGREEN_EX + ' After upgrade: ' + Fore.GREEN + str(bag_capility) + ' --> ' + str(bag_capility_upgrade) + ' capitality.' + Fore.LIGHTGREEN_EX + ' Upgrade cost: ' + str(bag_capility_cost))

            print(Fore.LIGHTGREEN_EX + '>>> ' + Fore.GREEN + '2.' + Fore.LIGHTGREEN_EX + ' Upgrade a ' + str(carrot_name) + '.' + Fore.GREEN + ' You have now: ' + str(carrot_grow) + ' per click.' + Fore.LIGHTGREEN_EX + ' After upgrade: ' + Fore.GREEN + str(carrot_grow) + ' --> ' + str(carrot_grow_upgrade) + ' per click.'
            + Fore.LIGHTGREEN_EX + ' Upgrade cost: ' + str(carrot_grow_cost))

            print(Fore.LIGHTGREEN_EX + '>>> ' + Fore.GREEN + '3.' + Fore.LIGHTGREEN_EX + ' Rebirth.' + Fore.GREEN + ' You has: ' + str(bp_multi) + ' rebirths.' + Fore.LIGHTGREEN_EX + ' After rebirth: ' + Fore.GREEN + str(carrot_name) + ' (x' + str(bp_multi) + ')' + ' --> ' + str(cnn) + ' (x' + str(bp_multi_up) + ') per sell.' + Fore.LIGHTGREEN_EX + ' Upgrade cost: ' + str(carrot_name_cost))

            print(Fore.LIGHTGREEN_EX + '>>> ' + Fore.GREEN + '4.' + Fore.LIGHTGREEN_EX + ' Auto farmer' + Fore.GREEN + ' You has: ' + str(farmer) + '/s.' + Fore.LIGHTGREEN_EX + ' After upgrade: ' + Fore.GREEN + str(farmer) + ' --> ' + str(farmer_up) + '/s.' + Fore.LIGHTGREEN_EX + ' Upgrade cost: ' + str(farmer_cost))

            print(Fore.LIGHTGREEN_EX + '>>> ' + Fore.GREEN + '5.' + Fore.LIGHTGREEN_EX + ' Upgrade a house' + Fore.GREEN + ' You have now: ' + str(house_level) + ' level.' + Fore.LIGHTGREEN_EX + ' After upgrade: ' + Fore.GREEN + str(house_level) + ' (' + str(house_energy) + ' energy per sleep) level' + ' --> ' + str(house_level_next) + ' (' + str(house_energy_next) + ' energy per sleep) level.' + Fore.LIGHTGREEN_EX + ' Upgrade cost: ' + str(house_cost))

            print('')

            upgrade_selected = input(Fore.CYAN + 'Upgrade selected: ')

            if upgrade_selected == '1':
                if cash >= bag_capility_cost:
                    bag_capility = bag_capility_upgrade
                    bag_capility_upgrade = bag_capility_upgrade * 2
                    cash = cash - bag_capility_cost
                    bag_capility_cost = bag_capility_cost * 2
                else:
                    print('')
                    print(Fore.RED + "You don't have " + str(bag_capility_cost) + ' cash!' + Fore.LIGHTRED_EX + ' You have: ' + str(cash) + ' / ' + str(bag_capility_cost) + ' cash')

            elif upgrade_selected == '2':
                if cash >= carrot_grow_cost:
                    carrot_grow = carrot_grow_upgrade
                    carrot_grow_upgrade = carrot_grow_upgrade * 2
                    cash = cash - carrot_grow_cost
                    carrot_grow_cost = carrot_grow_cost * 2
                else:
                    print('')
                    print(Fore.RED + "You don't have " + str(carrot_grow_cost) + ' cash!' + Fore.LIGHTRED_EX + ' You have: ' + str(cash) + ' / ' + str(carrot_grow_cost) + ' cash')

            elif upgrade_selected == '5':
                if house_level != 5:
                    if cash >= house_cost:
                        house_level = house_level + 1
                        cash = cash - house_cost
                    else:
                        print('')
                        print(Fore.RED + "You don't have " + str(house_cost) + ' cash!' + Fore.LIGHTRED_EX + ' You have: ' + str(cash) + ' / ' + str(house_cost) + ' cash')
                else:
                    print('')
                    print(Fore.LIGHTRED_EX + '>>> ' + Fore.RED + 'You have a max level of house!')

            elif upgrade_selected == '3':
                if carrot_name != 'pees':
                    if cash >= carrot_name_cost:
                        carrot_name_level = carrot_name_level + 1
                        carrot_name_cost = carrot_name_cost * 5
                        cash = cash - carrot_name_cost
                        print('')
                        print(Fore.LIGHTRED_EX + '---=' + Fore.RED + ' ( REBIRTH ) ' + Fore.LIGHTRED_EX + '=---')
                        print('')
                        print(Fore.RED + '>>>' + Fore.LIGHTRED_EX + ' You have: ' + Fore.LIGHTMAGENTA_EX + str(carrot_name_level) + Fore.LIGHTRED_EX + ' rebirths.')
                        print('')
                        print(Fore.LIGHTRED_EX + '---=' + Fore.RED + ' ( REBIRTH ) ' + Fore.LIGHTRED_EX + '=---')
                    else:
                        print('')
                        print(Fore.RED + "You don't have " + str(carrot_name_cost) + ' cash!' + Fore.LIGHTRED_EX + ' You have: ' + str(cash) + ' / ' + str(carrot_name_cost) + ' cash')

                else:
                    print('')
                    print(Fore.RED + '>>> You have a max level of this item name!')

            elif upgrade_selected == '4':
                if cash >= farmer_cost:
                    farmer = farmer_up
                    cash = cash - farmer_cost
                    farmer_cost = farmer_cost * 2
                    farmer_up = farmer_up + 0.25
                    farmer_lvl = farmer_lvl + 1
                else:
                    print('')
                    print(Fore.RED + "You don't have " + str(farmer_cost) + ' cash!' + Fore.LIGHTRED_EX + ' You have: ' + str(cash) + ' / ' + str(farmer_cost) + ' cash')

            else:
                print('')

        elif selected_option == '4':
            print('')
            print(Fore.YELLOW + '---=( SETTINGS )=---')
            print('')
            print(Fore.RED + '>>> COMMING SOON...')
            print('')
            print(Fore.YELLOW + '---=( SETTINGS )=---')


        elif selected_option == '5':
            if energy <= 0:
                print(Fore.RED + ">>> You can't work! Don't have energy!")
            else:
                if farmer_lvl >= 1:
                    print('')
                    farmer_select = input(Fore.GREEN + 'You want to use farmer? (yes or no) ')
                    if farmer_select == 'yes':
                        farmer_counter_loop = input(Fore.BLUE + 'Earning for (10s / 30s / 60s): ')
                        farmer_counter = 0
                        
                        if farmer_counter_loop == '10s':
                            while farmer_counter != 10:
                                if energy <= 0:
                                    print(Fore.RED + ">>> You can't work! Don't have energy!")
                                    break
                                else:
                                    cash = cash + farmer
                                    farmer_counter = farmer_counter + 1
                                    farmer_left = 10 - farmer_counter
                                    print('')
                                    print(Fore.LIGHTBLUE_EX + 'You earn ' + str(farmer) + ' cash !' + Fore.CYAN + ' You has: ' + str(cash) + ' cash. Left: ' + str(farmer_left) + ' seconds!')
                                    energy = energy - energy_remover * 2
                                    day_time = day_time + 0.5
                                    time.sleep(1)

                        elif farmer_counter_loop == '30s':
                            while farmer_counter != 30:
                                if energy <= 0:
                                    print(Fore.RED + ">>> You can't work! Don't have energy!")
                                    break
                                else:
                                    cash = cash + farmer
                                    farmer_counter = farmer_counter + 1
                                    farmer_left = 30 - farmer_counter
                                    print('')
                                    print(Fore.LIGHTBLUE_EX + 'You earn ' + str(farmer) + ' cash !' + Fore.CYAN + ' You has: ' + str(cash) + ' cash. Left: ' + str(farmer_left) + ' seconds!')
                                    energy = energy - energy_remover * 2
                                    day_time = day_time + 0.5
                                    time.sleep(1)

                        elif farmer_counter_loop == '60s':
                            while farmer_counter != 60:
                                if energy <= 0:
                                    print(Fore.RED + ">>> You can't work! Don't have energy!")
                                    break
                                else:
                                    cash = cash + farmer
                                    farmer_counter = farmer_counter + 1
                                    farmer_left = 60 - farmer_counter
                                    print('')
                                    print(Fore.LIGHTBLUE_EX + 'You earn ' + str(farmer) + ' cash !' + Fore.CYAN + ' You has: ' + str(cash) + ' cash. Left: ' + str(farmer_left) + ' seconds!')
                                    energy = energy - energy_remover * 2
                                    day_time = day_time + 0.5
                                    time.sleep(1)

                        else:
                            print('')
                            print(Fore.RED + '>>> Incorrect number! Automatically selected 10s!')
                            print('')
                            while farmer_counter != 10:
                                if energy <= 0:
                                    print(Fore.RED + ">>> You can't work! Don't have energy!")
                                    break
                                else:
                                    cash = cash + farmer
                                    farmer_counter = farmer_counter + 1
                                    farmer_left = 10 - farmer_counter
                                    print('')
                                    print(Fore.LIGHTBLUE_EX + 'You earn ' + str(farmer) + ' cash !' + Fore.CYAN + ' You has: ' + str(cash) + ' cash. Left: ' + str(farmer_left) + ' seconds!')
                                    energy = energy - energy_remover * 2
                                    day_time = day_time + 0.5
                                    time.sleep(1)

                    else:
                        print('')
                else:
                    print('')
                    print(Fore.RED + ">>> You don't have farmer! Buy it on upgrade!")

        elif selected_option == '6':
            print('')
            print(Fore.MAGENTA + 'Leaving...' + Fore.WHITE)
            print('')
            game_start = False
            game_menu = False

        elif selected_option == '8':
            house_selected = True
            while house_selected == True:
                print('')
                print(Fore.GREEN + '#' * 19)
                print(Fore.LIGHTGREEN_EX + '  HOUSE & PROFILE')
                print(Fore.GREEN + '#' * 19)
                print('')
                print(Fore.LIGHTBLUE_EX + '1. ' + Fore.BLUE + 'My Profile')
                print(Fore.LIGHTBLUE_EX + '2. ' + Fore.BLUE + 'Go Sleep')
                print(Fore.LIGHTBLUE_EX + '3. ' + Fore.BLUE + 'Quit Home')
                print('')
                house_function = input(Fore.BLUE + '>>> ' + Fore.LIGHTBLUE_EX + 'SELECTED OPTION: ')

                if house_function == '1':
                    print('')
                    print(Fore.YELLOW + '---=( PROFILE )=---')
                    print('')
                    print(Fore.CYAN + '>>>' + Fore.LIGHTBLUE_EX + ' You has: ' + str(cash) + Fore.BLUE + ' cash. ')
                    print(Fore.CYAN + '>>>' + Fore.LIGHTBLUE_EX + ' The time is now: ' + str(day_time) + ' / 24h ')
                    print(Fore.CYAN + '>>>' + Fore.LIGHTBLUE_EX + ' You has: ' + str(carrot) + ' / ' + str(bag_capility) + Fore.BLUE + ' capitality.')
                    print(Fore.CYAN + '>>>' + Fore.LIGHTBLUE_EX + ' Your energy: ' + str(energy) + ' / ' + str(max_energy) + Fore.BLUE + ' energy.')
                    print('')
                    print(Fore.YELLOW + '---=( PROFILE )=---')

                elif house_function == '2':
                    if house_level == 1:
                        if energy < max_energy:
                            if energy <= 80:
                                if day_time >= 6:
                                    energy = energy + house_energy
                                    day_time = day_time - 6
                                    print('')
                                    print(Fore.MAGENTA + 'You were a sleep, you regained ' + Fore.LIGHTMAGENTA_EX + str(house_energy))
                                else:
                                    print(Fore.RED + 'It must be after 6:00 to go to bed')
                            else:
                                print('')
                                print(Fore.RED + '>>> You must has 80 energy or lower')
                        else:
                            print('')
                            print(Fore.RED + '>>> You have a max energy!')

                elif house_function == '3':
                    house_selected = False
                    print(Fore.RED + '>>> Leaving home...')

        elif selected_option == '7':
            print('')        
            typed_code = input(Fore.LIGHTGREEN_EX + 'Code: ' + Fore.GREEN)  

            if typed_code == 'Free C2sh':
                if free_money == False:
                    cash = cash + 250
                    free_money = True
                    print(Fore.GREEN + 'Added 250cash!')

                else:
                    print('')
                    print(Fore.RED + 'This code already used!')

            elif typed_code == 'Uk4aine':
                if free_money_2 == False:
                    cash = cash + 500
                    free_money_2 = True
                    print(Fore.GREEN + 'Added 500cash!')

                else:
                    print('')
                    print(Fore.RED + 'This code already used!')

            elif typed_code == 'Farm3r':
                if free_money_3 == False:
                    carrot_grow = carrot_grow_upgrade
                    carrot_grow_upgrade = carrot_grow_upgrade * 2
                    carrot_grow_cost = carrot_grow_cost * 2
                    free_money_3 = True
                    print(Fore.GREEN + 'Free Carrot Upgrade arrived!')

                else:
                    print('')
                    print(Fore.RED + 'This code already used!')

            elif typed_code == 'Spr1ng':
                if free_money_4 == False:
                    cash = cash + 500
                    free_money_4 = True
                    print(Fore.GREEN + 'Added 500cash!')
                else:
                    print('')
                    print(Fore.RED + 'This code already used!')

            elif typed_code == 'Bag4free':
                if free_bag == False:
                    if bag_capility < 560:
                        bag_capility = bag_capility_upgrade
                        bag_capility_upgrade = bag_capility_upgrade * 2
                        bag_capility_cost = bag_capility_cost * 2
                        free_bag = True
                        print(Fore.GREEN + 'Free Bag Upgrade arrived!')
                    else:
                        print(Fore.RED + 'This code is active if you bag upgrade smaller than 5')

                else:
                    print('')
                    print(Fore.RED + 'This code already used!')

            else:
                print(Fore.RED + 'Incorrect code!')

        else:
            print('')
            print(Fore.LIGHTRED_EX + '---=(' + Fore.RED + ' ERROR - INCORRECT OPTION! ' + Fore.LIGHTRED_EX + ')=---')