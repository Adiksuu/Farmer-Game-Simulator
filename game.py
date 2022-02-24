# ------------------ ( COLORAMA IMPORT - MODULES ) -----------------

import colorama
from colorama import Fore
colorama.init

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

ver_info_settings = True

game_start = True
game_menu = True

free_money = False
free_bag = False

# ------------------ (     GAME START - WHILE    ) -----------------

while game_start == True:
    print('')
    print(Fore.LIGHTGREEN_EX + '---=( ' + Fore.GREEN + 'FARMER GAME v1.3 ' + Fore.LIGHTGREEN_EX + ')=---')
    print(Fore.LIGHTGREEN_EX + '  ---=( ' + Fore.GREEN + 'DEMO EDITION ' + Fore.LIGHTGREEN_EX + ')=---')
    print(Fore.LIGHTGREEN_EX + '---=( ' + Fore.GREEN + 'FARMER GAME v1.3 ' + Fore.LIGHTGREEN_EX + ')=---')
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
            cnn = 'MAX UPGRADE LEVEL'
            bp_multi = 5
            bp_multi_up = bp_multi + 1

            if bp_multi_up == 6:
                bp_multi_up = 5

            carrot_name_cost = 'MAX UPGRADE LEVEL'

        print('')
        print(Fore.BLUE + '---=( ' + Fore.LIGHTBLUE_EX + 'SELECT OPTION ' + Fore.BLUE + ')=---')
        print('')
        print(Fore.CYAN + '1. ' + Fore.LIGHTCYAN_EX + 'Make a ' + str(carrot_name))
        print(Fore.CYAN + '2. ' + Fore.LIGHTCYAN_EX + 'Sell a ' + str(carrot_name))
        print(Fore.CYAN + '3. ' + Fore.LIGHTCYAN_EX + 'Upgrades')
        print(Fore.CYAN + '4. ' + Fore.LIGHTCYAN_EX + 'Settings')
        print(Fore.CYAN + '5. ' + Fore.LIGHTCYAN_EX + 'Quit game')
        print(Fore.CYAN + '6. ' + Fore.LIGHTCYAN_EX + 'Enter Code')
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

            print(Fore.LIGHTGREEN_EX + '>>> ' + Fore.GREEN + '3.' + Fore.LIGHTGREEN_EX + ' Upgrade a ' + str(carrot_name) + ' name.' + Fore.GREEN + ' Name now: ' + str(carrot_name) + ' (x' + str(bp_multi) + ') per sell.' +
                  '.' + Fore.LIGHTGREEN_EX + ' After upgrade: ' + Fore.GREEN + str(carrot_name) + ' --> ' + str(cnn) + ' (x' + str(bp_multi_up) + ') per sell.' + Fore.LIGHTGREEN_EX + ' Upgrade cost: ' + str(carrot_name_cost))

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
                if carrot_name != 'pumpkins':
                    if cash >= carrot_name_cost:
                        carrot_name_level = carrot_name_level + 1
                        carrot_name_cost = carrot_name_cost * 5
                        cash = cash - carrot_name_cost
                    else:
                        print('')
                        print(Fore.RED + "You don't have " + str(carrot_name_cost) + ' cash!' + Fore.LIGHTRED_EX + ' You have: ' + str(cash) + ' / ' + str(carrot_name_cost) + ' cash')

                else:
                    print('')
                    print(Fore.RED + '>>> You have a max level of this item name!')

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
            print('')
            print(Fore.MAGENTA + 'Leaving...' + Fore.WHITE)
            print('')
            game_start = False
            game_menu = False

        elif selected_option == '6':
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

            if typed_code == 'Bag4free':
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
            print('')
            print(Fore.LIGHTRED_EX + '---=(' + Fore.RED + ' ERROR - INCORRECT OPTION! ' + Fore.LIGHTRED_EX + ')=---')