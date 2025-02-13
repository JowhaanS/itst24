import menu_functions
input_for_scan = 'input.txt'

def switch_case_menu(value):
    match value:    
        case "1":
           menu_functions.read_input_file(input_for_scan)
        case "2":
            ip = input('What IP do you wish to add?\n')
            if menu_functions.is_valid_ip(ip):
                menu_functions.append_input_file(input_for_scan, ip)
            else:
                print('Not a valid ip adress')
        case "3":
            ip = input('What IP do you wish to remove?\n')
            if menu_functions.is_valid_ip(ip):
                menu_functions.search_file(input_for_scan, ip)
            else:
                print('Not a valid ip adress')
        case "4":
            choice = input('Do you want to scan a saved IP y/n?\n').lower()
            if choice == 'n':
                ip = input('What adress do you wish to scan?\n')
                print('Nmap validating...')
                if menu_functions.is_valid_ip(ip):
                    print(f'Scanning {ip}\n')
                    result = menu_functions.scan_from_input(ip)
                    menu_functions.print_current_scan(result)
                    menu_functions.ask_to_save(result)
                else:
                    print('Not a valid IP adress..')
            elif choice == 'y':
                print('Nmap scan validating...')
                menu_functions.extract_from_input(input_for_scan)
            else:
                print('Not a valid option')
        case "5":
            menu_functions.show_result_files()
        case "6":
            menu_functions.read_result_file(input('Which file do you want to see?\n'))
        case "h":
            display_menu()
        case _:
            print()
    return 

def display_menu():
    print(
        "Welcome to this nmap thingie program\n"
        "What do you wish to do?\n\n"
        "1. Check what IP's to scan\n"
        "2. Add IP to scan\n"
        "3. Remove IP to scan\n"
        "4. SCAN\n"
        "5. View list of results\n"
        "6. Select and read individual result\n"
        "h. See menu again"
    )
display_menu()
while True:
    value = input()
    
    if value.lower() == 'q': 
        print("Exiting the program...")
        break

    if value not in ['1', '2', '3', '4', '5', '6', 'h']:
        print("Invalid option selected. Please choose between 1 and 6.")
    
    switch_case_menu(value)