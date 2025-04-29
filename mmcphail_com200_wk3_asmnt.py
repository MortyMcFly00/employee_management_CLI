# Dictionary data structure that assigns unique numeric IDs to employees as keys.
employees = {}

# Starting value for the employee IDs.
employee_id: int = 1000

# Global variable counter to track the amount of employees input into the system.
employee_counter = 0

# Variables containing different menu states within the system.
employee_db = True
main_menu = True
view_employees_menu = False
add_employee_menu = False
employee_data_menu = False

# Variable to store the ID of the current employee being viewed.
selected_employee_id = None

# Function displaying the main menu, navigation options, and the current employee count.
def main():
    print(f'-------------------------------Employee Database Log-------------------------------\n')
    print(f' \n')
    print(f'         Directory Navigation: \n')
    print(f'                               1: View Employees \n')
    print(f'                               2: Add Employee \n')
    print(f' \n')
    print(f'         There are ({employee_counter}) employees in the system. \n')
    print(f' \n')
    print(f'                  Press 1 to View | Press 2 to Add | Press q to quit\n')

# Function that displays the menu where the user can add a new employee and store their data in an employee ID container
def add_employee():

    # Global variables being called into the function to be utilized.
    global employee_id
    global employee_counter

    # Collects employee data for all required fields.
    print(f'-------------------------------Add Employee Data-------------------------------\n')
    print(f' \n')
    employee_name = input(f'         Enter Employee Name: ')
    employee_ssn = input(f'         Enter Employee SSN: ')
    employee_phone = input(f'         Enter Employee Phone: ')
    employee_email = input(f'         Enter Employee Email: ')
    employee_salary = input(f'         Enter Employee Salary: ')
    print(f' \n')
    print(f'                           Press m to return to main menu\n')

    # Adds the employee data into the dictionary and assigns the employee_name an employee_id number to be referenced in the key.
    employees[employee_id] = [employee_name, employee_ssn, employee_phone, employee_email, employee_salary]
    print(f'\n         Employee {employee_name} added with ID {employee_id}.\n')
    # Increases both the employee_id number and the employee_counter number for every employee input.
    employee_id += 1
    employee_counter += 1

# Function that displays the contents of the dictionary, listing out all employees stored in the system.
def view_employees():
    print(f'-------------------------------Employee List-------------------------------\n')
    print(f'\n')

    # If no employees are stored, inform the user.
    if not employees:
        print(f'         No employees have been added yet. \n')

    # Otherwise, print each employee beginning with ID# and then name. Ordered by ID#.
    else:
        for current_employee_id in employees:
            print(f'         ID {current_employee_id}: {employees[current_employee_id][0]}\n')

        print(f'      Press ID# to View | Press d to Delete | Press m to return to main menu\n')

# Function that displays the details of the specified employee.
def employee_data(selected_id):
    print(f'-------------------------------Employee Data-------------------------------\n')
    print(f' \n')

    # Checks if the specified employee ID# is present in the system.
    if selected_id in employees:
        print(f'         Name: {employees[selected_id][0]} \n')

        # String splicing to format both the SSN and phone number for readability.
        print(f'         SSN: {employees[selected_id][1][:3]}-{employees[selected_id][1][3:5]}-{employees[selected_id][1][5:]} \n')
        print(f'         Phone: ({employees[selected_id][2][:3]}) {employees[selected_id][2][3:6]}-{employees[selected_id][2][6:]} \n')
        print(f'         Email: {employees[selected_id][3]} \n')
        print(f'         Salary: ${employees[selected_id][4]} \n')

    # Prints employee not found if the specified ID# is not stored in the system.
    else:
        print(f'         Employee not found. \n')
    print(f' \n')
    print(f'                     Press b to Go Back | Press m to Return to Main Menu\n')

# Running Script

# Main loop for navigating menus based on user input.
while employee_db:

    # If statement that displays the main menu and allows the user to begin inputting navigational keystrokes.
    if main_menu:
        main()
        menu_input = input('')

        # If user presses the '1' key they are ported to the view employee menu where all employees and their IDs are displayed.
        if menu_input == '1':
            main_menu = False
            view_employees_menu = True

        # If the user presses '2' they are ported the add employee menu where they can input a new employees data into the system.
        elif menu_input == '2':
            main_menu = False
            add_employee_menu = True

        # If the user presses 'q' they are ported out of the main menu and the program terminates.
        elif menu_input == 'q':
            employee_db = False
            print(f'\n         Goodbye!')

        # If the user inputs anything else the program responds with 'Invalid Input'.
        else:
            print(f'         Invalid Input')

    # If statement that initializes the employee add menu, connected to the '2' keystroke.
    elif add_employee_menu:
        add_employee()
        add_employee_menu = False
        main_menu = True

    # If statement that initializes the view employee menu, connected to the '1' keystroke.
    elif view_employees_menu:
        view_employees()

        # If statement stating that if there are no employees stored then the terminal will inform the user and then 'continue' back to the main menu.
        if not employees:
            view_employees_menu = False
            main_menu = True
            continue

        menu_input = input('')

        # If statement that allows the user to remove an employee from the database by inputting their ID# once initialized with the 'd' keystroke.
        if menu_input == 'd':
            delete_employee_id = int(input(f'         Enter Employee ID to Delete: '))

            # Checks to see if the employee ID exists in the system before performing delete. Then informs the user deletion was successful.
            if delete_employee_id in employees:
                del employees[delete_employee_id]
                employee_counter -= 1
                print(f'\n         Employee deleted successfully. ')

            # If ID is not found the user is informed.
            else:
                print(f'\n         Employee ID not found. ')

        # If statement that allows the user to return to the main menu with the 'm' keystroke.
        elif menu_input == 'm':
            view_employees_menu = False
            main_menu = True

        # Alters the selected employee global variable value to match the specified ID# and converts it from a string to an integer.
        else:
            selected_employee_id = int(menu_input)

            # Checks if the specified employee ID exists in the system and if so ports the user to that employees personal data menu.
            if selected_employee_id in employees:
                view_employees_menu = False
                employee_data_menu = True

            # If statement that informs the user if the specified user ID was not found.
            else:
                print(f'\n         Employee not found. ')

    # If statement that initializes the employees personal data menu.
    elif employee_data_menu:
        employee_data(selected_employee_id)
        menu_input = input('')

        # If statement that allows the user to return to the previous menu with the 'b' keystroke.
        if menu_input == 'b':
            employee_data_menu = False
            view_employees_menu = True

        # If statement that allows the user to return to the main menu with the 'm' keystroke.
        elif menu_input == 'm':
            employee_data_menu = False
            main_menu = True

        # If the user inputs anything else the program responds with 'Invalid Input'.
        else:
            print('\n         Invalid input. ')

