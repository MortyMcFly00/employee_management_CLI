# Title value that is printed at the top of the CLUI.
employee_title = 'Employee Database Log'

# List containing the name elements for each employee.
employee_name = ['', '', '', '', '']

# List containing the information elements for each employee.
employee_list = [[], [], [], [], []]

# Employee 1 information.
employee_name[0] = input('Enter name for Employee 1: ')
ssn0 = input('Enter SSN for Employee 1: ')
phone0 = input('Enter phone for Employee 1: ')
email0 = input('Enter email for Employee 1: ')
salary0 = float(input('Enter salary for Employee 1: '))
employee_list[0] = [ssn0, phone0, email0, salary0]

# Employee 2 information.
employee_name[1] = input('Enter name for Employee 2: ')
ssn1 = input('Enter SSN for Employee 2: ')
phone1 = input('Enter phone for Employee 2: ')
email1 = input('Enter email for Employee 2: ')
salary1 = float(input('Enter salary for Employee 2: '))
employee_list[1] = [ssn1, phone1, email1, salary1]

# Employee 3 information.
employee_name[2] = input('Enter name for Employee 3: ')
ssn2 = input('Enter SSN for Employee 3: ')
phone2 = input('Enter phone for Employee 3: ')
email2 = input('Enter email for Employee 3: ')
salary2 = float(input('Enter salary for Employee 3: '))
employee_list[2] = [ssn2, phone2, email2, salary2]

# Employee 4 information.
employee_name[3] = input('Enter name for Employee 4: ')
ssn3 = input('Enter SSN for Employee 4: ')
phone3 = input('Enter phone for Employee 4: ')
email3 = input('Enter email for Employee 4: ')
salary3 = float(input('Enter salary for Employee 4: '))
employee_list[3] = [ssn3, phone3, email3, salary3]

# Employee 5 information.
employee_name[4] = input('Enter name for Employee 5: ')
ssn4 = input('Enter SSN for Employee 5: ')
phone4 = input('Enter phone for Employee 5: ')
email4 = input('Enter email for Employee 5: ')
salary4 = float(input('Enter salary for Employee 5: '))
employee_list[4] = [ssn4, phone4, email4, salary4]

# Assigns the boolean value True to employee_log_run.
employee_log_run = True
# Assigns the boolean value True to employee_log1.
employee_log1 = True
# Assigns the boolean value False to employee_log2.
employee_log2 = False
# Assigns the value 0 to selected.
selected = 0

# Initiates the while loop employee_log_run because the boolean value of employee_log_run is True.
while employee_log_run:

        # Initiates the while loop employee_log1 because the boolean value of employee_log1 is True.
        while employee_log1:

            # Prints the main CLUI, displaying the previously entered employee names.
            print(f'------------------{employee_title}------------------\n')
            print(f'\n')
            print(f'        1.{employee_name[0]}\n')
            print(f'        2.{employee_name[1]}\n')
            print(f'        3.{employee_name[2]}\n')
            print(f'        4.{employee_name[3]}\n')
            print(f'        5.{employee_name[4]}\n')
            print(f'\n')
            print(f'------------------Press q to quit------------------\n')

            # Assigns the object menu_input the value of input(), meaning its value is determined by the users terminal input.
            menu_input = input()

            # If expression stating that if menu_input corresponds with one of the numbers associated with its respective employee name,
            # initialize CLUI employee_log2.
            if menu_input == '1' or menu_input == '2' or menu_input == '3' or menu_input == '4' or menu_input == '5':
                # Switches the value of menu_input from a string to integer, then replaces the value in selected with the value in menu_input,
                # then subtract 1 to correspond with 0-4 index structure.
                selected = int(menu_input) - 1
                # Assigns the boolean value True to employee_log2, initializing the secondary CLUI.
                employee_log2 = True
                # Assigns the boolean value False to employee_log1, closing the primary CLUI.
                employee_log1 = False

            # secondary if expression stating that if the user input is equal to 'q' key all three while loops close, shutting down the program.
            elif menu_input == 'q':
                # Assigns the boolean value False to all three while loops.
                employee_log_run = False
                employee_log1 = False
                employee_log2 = False
                # Prints the 'Goodbye!' greeting before closing program.
                print('Goodbye!')

            # Secondary else expression stating that if any other keys are pressed the terminal will print 'Invalid Input'
            # and return to the beginning of the loop.
            else:
                print('Invalid Input')

        # Initiates the while loop employee_log2 if the boolean value that corresponds with this loops comes back True
        # and the boolean value for employee_log1 comes back False.
        while employee_log2:

            # If expression checking the specified list index element for employee_name if it is now empty.
            if employee_name[selected] == '':
                # If specified element in list employee_name is now empty then print the following.
                print('This employee slot is empty.\n Please re-enter information')
                # Requests the user to re-input the information in same format as beginning of script.
                employee_name[selected] = input('Enter name: ')
                ssn = input('Enter SSN: ')
                phone = input('Enter phone: ')
                email = input('Enter email: ')
                salary = float(input('Enter salary: '))
                # stores re-input information into the specified element in employee_list.
                employee_list[selected] = [ssn, phone, email, salary]
                # Assigns the boolean value True to employee_log1 re-initializing the primary CLUI.
                employee_log1 = True
                # Assigns the boolean value False to employee_log2 closing the secondary CLUI.
                employee_log2 = False

            # Else expression that initializes if there is data already stored in the specified list index location.
            else:
                # Prints secondary CLUI for employee_log2.
                print(f'------------------{employee_title}------------------\n')
                print(f'    {employee_name[selected]}\n')
                print(f'\n')
                print(f'        {employee_list[selected][0][:3]}-{employee_list[selected][0][3:5]}-{employee_list[selected][0][5:]}\n')
                print(f'        ({employee_list[selected][1][:3]}) {employee_list[selected][1][3:6]}-{employee_list[selected][1][6:]}\n')
                print(f'        {employee_list[selected][2]}\n')
                print(f'        ${employee_list[selected][3]:,.2f}\n')
                print(f'\n')
                print(f'-------press b for back-------Press d to delete-------\n')

                # Assigns the object menu_input the value of input(), meaning its value is determined by the users terminal input.
                menu_input = input()

                # Secondary if expression stating that if the user input is equal to 'b' key then return to primary CLUI employee_log1.
                if menu_input == 'b':
                    employee_log1 = True
                    employee_log2 = False

                # Secondary if expression stating that if the user input is equal to 'd' key then remove data stored in the specified element slot
                # for both employee_name and employee_list lists, then re-initialize primary CLUI employee_log1.
                elif menu_input == 'd':
                    employee_name[selected] = ''
                    employee_list[selected] = []
                    employee_log1 = True
                    employee_log2 = False

                # Secondary else expression stating that if any other keys are pressed the terminal will print 'Invalid Input'
                # and return to the beginning of the loop.
                else:
                    print('Invalid Input')