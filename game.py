# ------------------ ( COLORAMA IMPORT - MODULES ) -----------------

from asyncore import loop
import colorama
from colorama import Fore
colorama.init

import time

# ------------------ (       ANY VARIABLES      ) ------------------

carrot = 0
carrot_name = 'banan'
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

ver_info_settings = True

game_start = True
game_menu = True

free_money = False
free_money_2 = False
free_bag = False

# ------------------ (     GAME START - WHILE    ) -----------------

while game_start == True:
    print('')
    print(Fore.LIGHTGREEN_EX + ' ---=( ' + Fore.GREEN + 'FARMER GAME v1.4 ' + Fore.LIGHTGREEN_EX + ')=---')
    print(Fore.LIGHTGREEN_EX + '---=( ' + Fore.GREEN + 'FULL ACCESS VERSION ' + Fore.LIGHTGREEN_EX + ')=---')
    print(Fore.LIGHTGREEN_EX + ' ---=( ' + Fore.GREEN + 'FARMER GAME v1.4 ' + Fore.LIGHTGREEN_EX + ')=---')
    print('')

    game_menu = True

# ------------------ (     GAME MENU - WHILE     ) -----------------
    
    while game_menu == True:

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
        print('')

        selected_option = input(Fore.BLUE + '>>> ' + Fore.LIGHTBLUE_EX + 'SELECTED OPTION: ')

# ------------------ (     GAME MENU - IF'S     ) -----------------

        if selected_option == '1':
            if carrot < bag_capility:
                carrot = carrot + carrot_grow
                if carrot == bag_capility:
                    print('')
                    print(Fore.LIGHTMAGENTA_EX + '>>> ' + Fore.MAGENTA + 'Bag is full! You have ' + Fore.LIGHTBLUE_EX + str(bag_capility) + Fore.MAGENTA + ' ' + str(carrot_name) + Fore.LIGHTMAGENTA_EX + ' Sell ' + str(carrot_name) + '!')
                print('')
                if carrot > bag_capility:
                    carrot = bag_capility
                print(Fore.CYAN + 'You have: ' + str(carrot) + ' / ' + str(bag_capility) + Fore.BLUE + ' ' + str(carrot_name))
            elif carrot >= bag_capility:
                print('')
                print(Fore.LIGHTMAGENTA_EX + '>>> ' + Fore.MAGENTA + 'Bag is full! You have ' + Fore.LIGHTBLUE_EX + str(bag_capility) + Fore.MAGENTA + ' ' + str(carrot_name) + Fore.LIGHTMAGENTA_EX + ' Sell ' + str(carrot_name))

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
        elif selected_option == '3':
            print('')
            print(Fore.LIGHTCYAN_EX + '---=( ' + Fore.CYAN + 'UPGRADES' + Fore.LIGHTCYAN_EX + ' )=---')
            print('')
            print(Fore.LIGHTGREEN_EX + '>>> ' + Fore.GREEN + '1.' + Fore.LIGHTGREEN_EX + ' Upgrade a bag.' + Fore.GREEN + ' You have now: ' + str(bag_capility) + ' capitality.' + Fore.LIGHTGREEN_EX + ' After upgrade: ' + Fore.GREEN + str(bag_capility) + ' --> ' + str(bag_capility_upgrade) + ' capitality.' + Fore.LIGHTGREEN_EX + ' Upgrade cost: ' + str(bag_capility_cost))

            print(Fore.LIGHTGREEN_EX + '>>> ' + Fore.GREEN + '2.' + Fore.LIGHTGREEN_EX + ' Upgrade a ' + str(carrot_name) + '.' + Fore.GREEN + ' You have now: ' + str(carrot_grow) + ' per click.' + Fore.LIGHTGREEN_EX + ' After upgrade: ' + Fore.GREEN + str(carrot_grow) + ' --> ' + str(carrot_grow_upgrade) + ' per click.'
            + Fore.LIGHTGREEN_EX + ' Upgrade cost: ' + str(carrot_grow_cost))

            print(Fore.LIGHTGREEN_EX + '>>> ' + Fore.GREEN + '3.' + Fore.LIGHTGREEN_EX + ' Rebirth.' + Fore.GREEN + ' You has: ' + str(bp_multi) + ' rebirths.' + Fore.LIGHTGREEN_EX + ' After rebirth: ' + Fore.GREEN + str(carrot_name) + ' (x' + str(bp_multi) + ')' + ' --> ' + str(cnn) + ' (x' + str(bp_multi_up) + ') per sell.' + Fore.LIGHTGREEN_EX + ' Upgrade cost: ' + str(carrot_name_cost))

            print(Fore.LIGHTGREEN_EX + '>>> ' + Fore.GREEN + '4.' + Fore.LIGHTGREEN_EX + ' Auto farmer' + Fore.GREEN + ' You has: ' + str(farmer) + ' per second.' + Fore.LIGHTGREEN_EX + ' After upgrade: ' + Fore.GREEN + str(farmer) + ' --> ' + str(farmer_up) + ' per second.' + Fore.LIGHTGREEN_EX + ' Upgrade cost: ' + str(farmer_cost))

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

            if ver_info_settings == True:
                ver_info_settings = False
                ver_info = 'On'
            elif ver_info_settings == False:
                ver_info_settings = True
                ver_info = 'Off'

            # print(Fore.LIGHTGREEN_EX + '1. ' + Fore.GREEN + 'Version info: ' + Fore.LIGHTCYAN_EX + str(ver_info))

        elif selected_option == '5':
            if farmer_lvl >= 1:
                print('')
                farmer_select = input(Fore.GREEN + 'You want to use farmer? (yes or no) ')
                if farmer_select == 'yes':
                    farmer_counter_loop = input(Fore.BLUE + 'Earning for (10s / 30s / 60s): ')
                    farmer_counter = 0
                    
                    if farmer_counter_loop == '10s':
                        while farmer_counter != 10:
                            cash = cash + farmer
                            print('')
                            print(Fore.LIGHTBLUE_EX + 'You earn ' + str(farmer) + ' cash !' + Fore.CYAN + ' You has: ' + str(cash) + ' cash')
                            farmer_counter = farmer_counter + 1
                            time.sleep(1)

                    elif farmer_counter_loop == '30s':
                        while farmer_counter != 30:
                            cash = cash + farmer
                            print(cash)
                            farmer_counter = farmer_counter + 1
                            time.sleep(1)

                    elif farmer_counter_loop == '60s':
                        while farmer_counter != 60:
                            cash = cash + farmer
                            print(cash)
                            farmer_counter = farmer_counter + 1
                            time.sleep(1)

                    else:
                        print('')
                        print(Fore.RED + '>>> Incorrect number! Automatically selected 10s!')
                        print('')
                        while farmer_counter != 10:
                            cash = cash + farmer
                            print(cash)
                            farmer_counter = farmer_counter + 1
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