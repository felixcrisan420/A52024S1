import os

class UI:
    @staticmethod
    def get_input():
        try:
            return int(input("Option: "))
        except ValueError:
            print("Please enter a valid number.")
            return None

    @staticmethod 
    def print_main_menu():
        print("""
              Welcome to the management console!
              
              Options:
                0. Exit
                1. Enter the Plane Management Menu
                2. Enter the Passenger Management Menu
                3. Enter the General Management Menu
                
              """)

    @staticmethod 
    def print_plane_menu():
        print("""
              Plane Management Menu:
              
              Options:
                0. Return to the main menu
                --------------------------------
                Add:
                1. Add a plane
                --------------------------------
                View:
                2. View all planes
                3. View plane by ID
                4. View plane at Repository index
                --------------------------------
                Update:
                5. Update a plane
                --------------------------------
                Delete:
                6. Delete a plane
                --------------------------------
                Operations:
                8. Show remaining seats in each plane
                --------------------------------
              """)

    @staticmethod 
    def print_passenger_menu():
        print("""
              Passenger Management Menu:
              
              Options:
                0. Return to the main menu
                --------------------------------
                Add:
                1. Add a passenger
                --------------------------------
                View:
                2. View all passengers
                3. View passengers in a plane with plane ID
                4. Seach passenger with passport ID
                5. View all passengers with the same name
                6. View all planes
                --------------------------------
                Update:
                7. Update a passenger
                --------------------------------
                Delete:
                8. Delete a passenger
                --------------------------------

              """)

    @staticmethod
    def print_general_menu():
        print("""
              General Management Menu:
                
              Options:
                0. Return to the main menu
                1. Sort passengers by last name
                2. Sort planes according to the number of passengers
                3. Sort planes accordubg to the number of passengers witht he first name with given substring
                4. Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
                5. Identify planes that have passengers with passport numbers starting with the same 3 letters
                6. Identify passengers from a given plane for which the first name or last name contatin a string given as parameter
                7. Identify plane(s) where there is a passenger with a given name
                8. Form groups of [k] passengers from the same plane but with different last names
                9. Form groups of [k] planes with the same destination but belonging to different airline companies
                """)

    @staticmethod
    def clear_menu():
        os.system('cls' if os.name == 'nt' else 'clear')