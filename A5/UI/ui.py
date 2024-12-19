import os
from time import sleep
from tabulate import tabulate
from service.passenger_service import PassengerService
from service.plane_service import PlaneService
from controller.controller import Controller
from utils.utilities import Utilities as utils


class CLI:
    def __init__(self, passenger_service:PassengerService, plane_service:PlaneService, controller: Controller):
        self.__plane_service = plane_service
        self.__passenger_service = passenger_service
        self.__controller = controller
        
    @staticmethod
    def __get_input():
        try:
            option = input("Option: ")
            while not option.isdigit():
                print("Please enter a valid number.")
                option = input("Option: ")
            return int(option)
        except ValueError:
            print("Please enter a valid number.")
            return None


    @staticmethod 
    def __print_main_menu():
        print("""
              Welcome to the management console!
              
              Options:
                0. Exit
                1. Enter the Plane Management Menu
                2. Enter the Passenger Management Menu
                3. Enter the General Management Menu
                
              """)

    @staticmethod 
    def __print_plane_menu():
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
    def __print_passenger_menu():
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
    def __print_general_menu():
        print("""
              General Management Menu:
                
              Options:
                0. Return to the main menu
                1. Sort passengers by last name
                2. Sort planes according to the number of passengers
                3. Sort planes according to the number of passengers with the first name with given substring
                4. Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
                5. Identify planes that have passengers with passport numbers starting with the same 3 letters
                6. Identify passengers from a given plane for which the first name or last name contatin a string given as parameter
                7. Identify plane(s) where there is a passenger with a given name
                8. Form groups of [k] passengers from the same plane but with different last names
                9. Form groups of [k] planes with the same destination but belonging to different airline companies
                """)

    @staticmethod
    def __clear_menu():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def __print_exit():
        print("Exiting program")
        
    def __print_planes(self, plane_list):
        headers = ["Index", "Plane ID", "Airline Company", "Number of Seats", "Destination"]
        table = []
        for index, plane in enumerate(plane_list):
            table.append([index, plane.get_planeID(), plane.get_airline_company(), plane.get_number_of_seats(), plane.get_destination()])
        print(tabulate(table, headers=headers, tablefmt="grid"))
        
    def __print_passengers(self, passenger_list, option):
        headers = ["Index", "First Name", "Last Name", "Passport ID", f"Plane ID\n{option}"]
        table = []
        for index, passenger in enumerate(passenger_list):
            table.append([index, passenger.get_first_name(), passenger.get_last_name(), passenger.get_passportID(), passenger.get_planeID()])
        print(tabulate(table, headers=headers, tablefmt="grid"))
        
    def __print_remaining_seats(self, plane_list):
        headers = ["Index", "Plane ID", "Remaining Seats"]
        table = []
        for index, plane in enumerate(plane_list):
            table.append([index, plane.get_planeID(), self.__plane_service.show_remaining_seats(plane.get_planeID())])
        print(tabulate(table, headers=headers, tablefmt="grid"))

    def __print_backtracking_solutions(self, groups, print_func):
        """
        Generalized method to print backtracking solutions.

        Args:
            groups (list): List of groups to be printed.
            print_func (callable): A function that takes a group and prints its details.
        """
        for index, group in enumerate(groups):
            print(f"Group {index + 1}:")
            print_func(group)
            print()  # Add a newline after each group
        
    def __plane_menu(self):
        while True:
            CLI.__clear_menu()
            CLI.__print_plane_menu()
            user_input = CLI. __get_input()
            if user_input == 0:
                self.__main_menu()
            elif user_input == 1:
                # add plane
                planeID = input("Enter planeID: ")
                airline_company = input("Enter airline company: ")
                number_of_seats = input("Enter number of seats: ")
                destination = input("Enter destination: ")
                if utils.check_integer(number_of_seats) == False:
                    sleep(1.5)
                    continue
                try:
                    self.__plane_service.add_plane(planeID, airline_company, int(number_of_seats), destination)
                    print("Plane added successfully")
                    sleep(1.5)
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 2:
                # view all planes
                plane_list = self.__plane_service.get_plane_list()
                self.__print_planes(plane_list)
                input("Press ENTER to continue")
            elif user_input == 3:
                # view plane by ID
                planeID = input("Enter planeID: ")
                try:
                    plane = self.__plane_service.get_plane_by_planeID(planeID)
                    self.__print_planes([plane])
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 4:
                # view plane at Repository index
                index = input("Enter index: ")
                if utils.check_integer(index) == False:
                    sleep(1.5)
                    continue
                try:
                    plane = self.__plane_service.get_plane_by_index(int(index))
                    self.__print_planes([plane])
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 5:
                # update a plane
                index = input("Enter index: ")
                print("Leave empty if you don't want to update the field (ENTER)")
                planeID = input("Enter planeID: ")
                airline_company = input("Enter airline company: ")
                number_of_seats = input("Enter number of seats: ")
                destination = input("Enter destination: ")
                if utils.check_integer(index) == False or utils.check_integer(number_of_seats) == False:
                    sleep(1.5)
                    continue
                try:
                    self.__plane_service.update_plane(int(index), planeID, airline_company, int(number_of_seats), destination)
                    print("Plane updated successfully")
                    sleep(1.5)
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 6:
                # delete a plane
                index = input("Enter index: ")
                if utils.check_integer(index) == False:
                    sleep(1.5)
                    continue
                try:
                    self.__plane_service.delete_plane_by_index(int(index))
                    print("Plane deleted successfully")
                    sleep(1.5)
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 8:
                # Show remaining seats in each plane
                plane_list = self.__plane_service.get_plane_list()
                self.__print_remaining_seats(plane_list)
                input("Press ENTER to continue")
            else:
                print("Invalid input")
                sleep(1.5)
                
    def __passenger_menu(self):
        while True:
            CLI.__clear_menu()
            CLI.__print_passenger_menu()
            user_input = CLI.__get_input()
            if user_input == 0:
                self.__main_menu()
            elif user_input == 1:
                # add passenger
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                passportID = input("Enter passportID: ")
                planeID = input("Enter planeID: ")
                try:
                    self.__passenger_service.add_passenger(first_name, last_name, passportID, planeID)
                    print("Passenger added successfully")
                    sleep(1.5)
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 2:
                # view all passengers
                passenger_list = self.__passenger_service.get_passenger_list()
                self.__print_passengers(passenger_list, "All")
                input("Press ENTER to continue")
            elif user_input == 3:
                # view passenger in a plane by planeID
                planeID = input("Enter planeID: ")
                try:
                    passenger_list = self.__passenger_service.get_passengers_by_planeID(planeID)
                    self.__print_passengers(passenger_list, planeID)
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 4:
                # search passenger with passportID
                passportID = input("Enter passportID: ")
                try:
                    passenger = self.__passenger_service.get_passenger_by_passportID(passportID)
                    self.__print_passengers([passenger], "")
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 5:
                # view all passengers with the same name
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                try:
                    passenger_list = self.__passenger_service.get_passengers_by_first_and_last_name(first_name, last_name)
                    self.__print_passengers(passenger_list, "All")
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 6:
                # view all planes
                plane_list = self.__plane_service.get_plane_list()
                self.__print_planes(plane_list)
                input("Press ENTER to continue")
            elif user_input == 7:
                # update a passenger
                index = input("Enter index: ")
                if utils.check_integer(index) == False:
                    sleep(1.5)
                    continue
                
                print("Leave empty if you don't want to update the field (ENTER)")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                passportID = input("Enter passportID: ")
                planeID = input("Enter planeID: ")
                try:
                    self.__passenger_service.update_passenger(int(index), first_name, last_name, passportID, planeID)
                    print("Passenger updated successfully")
                    sleep(1.5)
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 8:
                # delete a passenger
                index = input("Enter index: ")
                if utils.check_integer(index) == False:
                    sleep(1.5)
                    continue
                try:
                    self.__passenger_service.delete_passenger_by_index(int(index))
                    print("Passenger deleted successfully")
                    sleep(1.5)
                except Exception as e:
                    print(e)
                    sleep(1.5)
            else:
                print("Invalid input")
                sleep(1.5)
    
    def __general_menu(self):
        while(True):
            CLI.__clear_menu()
            CLI.__print_general_menu()
            user_input = CLI.__get_input()
            if user_input == 0:
                self.__main_menu()
            elif user_input == 1:
                # Sort passengers by last name
                try:
                    planeID = input("Enter planeID: ")
                    self.__print_passengers(self.__controller.sort_passengers_in_plane_by_last_name(planeID), planeID)
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 2:
                # Sort planes according to the number of passengers
                self.__print_planes(self.__controller.sort_planes_by_number_of_passengers())
                input("Press ENTER to continue")
            elif user_input == 3:
                # Sort planes accordubg to the number of passengers witht he first name with given substring
                try:
                    substring = input("Enter substring: ")
                    self.__print_planes(self.__controller.sort_planes_by_number_of_passengers_and_first_name_given_substring(substring))
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 4:
                # Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
                self.__print_planes(self.__controller.sort_planes_by_number_of_passengers_and_destination())
                input("Press ENTER to continue")
            elif user_input == 5:
                # Identify planes that have passengers with passport numbers starting with the same 3 letters
                self.__print_planes(self.__controller.get_planes_with_passengers_with_passport_starting_with_same_3_letters())
                input("Press ENTER to continue")
            elif user_input == 6:
                # Identify passengers from a given plane for which the first name or last name contatin a string given as parameter
                planeID = input("Enter planeID: ")
                string = input("First or last name: ")
                try:
                    self.__print_passengers(self.__controller.passenger_from_plane_having_first_or_last_name_like_string(planeID, string), planeID)
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 7:
                # Identify plane(s) where there is a passenger with a given name
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                try:
                    plane_list = self.__controller.get_planes_with_passenger_name(first_name, last_name)
                    self.__print_planes(plane_list)
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 8:
                # Form groups of [k] passengers from the same plane but with different last names
                planeID = input("Enter planeID: ")
                k = input("Enter the number of elements in the group: ")
                if utils.check_integer(k) == False:
                    sleep(1.5)
                    continue
                try:
                    groups = self.__controller.groups_of_passengers_from_same_plane(planeID, int(k))
                    self.__print_backtracking_solutions(
                        groups, 
                        lambda group: self.__print_passengers(group, planeID)
                    )
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1.5)
            elif user_input == 9:
                # Form groups of [k] planes with the same destination but belonging to different airline companies
                k = input("Enter the number of elements in the group: ")
                if utils.check_integer(k) == False:
                    sleep(1.5)
                    continue
                try:
                    groups = self.__controller.groups_of_planes_with_same_destination_different_airline(int(k))
                    self.__print_backtracking_solutions(
                        groups, 
                        self.__print_planes
                    )
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1.5)
            else:
                print("Invalid input")
                sleep(1.5)

    def __main_menu(self):
        CLI.__clear_menu()
        while True:
            CLI.__print_main_menu()
            user_input = CLI.__get_input()
            if user_input == 0:
                option = input("Save data to file? (y/n): ")
                while option != "y" and option != "n":
                    print("Invalid input")
                    option = input("Save data to file? (y/n): ")
                if option == "y":
                    self.__passenger_service.write_to_file()
                    self.__plane_service.write_to_file()
                CLI.__print_exit()
                exit()
            elif user_input == 1:
                self.__plane_menu()
            elif user_input == 2:
                self.__passenger_menu()
            elif user_input == 3:
                self.__general_menu()
            else:
                print("Invalid input")

    def run(self):
        self.__plane_service.read_from_file()
        self.__passenger_service.read_from_file()
        self.__main_menu()