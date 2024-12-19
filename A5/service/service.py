from domain.plane import Plane
from domain.passenger import Passenger
from repository.repository import Repository

class Service:
    def __init__(self, repository:Repository):
        self.__repository = repository

    # CRUD Operations for Passenger
    # Create
    def add_passenger(self, first_name, last_name, passportID, planeID):
        if isinstance(first_name, str) == False:
            raise TypeError("First name must be a string")
        if isinstance(last_name, str) == False:
            raise TypeError("Last name must be a string")
        if isinstance(passportID, str) == False:
            raise TypeError("Passport ID must be a string")
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string or integer")
        return self.__repository.add_passenger(Passenger(first_name, last_name, passportID, planeID))
    
    # Read
    def get_passenger_list(self)->list:
        return self.__repository.get_passenger_list()
    
    def get_passenger_by_index(self, index)->list:
        if isinstance(index, int) == False:
            try:
                index = int(index)
            except:
                raise TypeError("Index must be an integer")
            index = int(index)
            if index < 0 or index > len(self.__repository.get_plane_list()):
                raise ValueError("Index must be an integer and within the list's range")
            
        return self.__repository.get_passenger_by_index(int(index))
    
    def get_index_by_passenger(self, first_name, last_name, passportID, planeID)->int:
        if isinstance(first_name, str) == False:
            raise TypeError("First name must be a string")
        if isinstance(last_name, str) == False:
            raise TypeError("Last name must be a string")
        if isinstance(passportID, str) == False:
            raise TypeError("Passport ID must be a string")
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string or integer")
        
        return self.__repository.get_index_by_passenger(Passenger(first_name, last_name, passportID, planeID))
    
    def get_passengers_by_planeID(self, planeID)->list:
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string")
        
        return self.__repository.get_passengers_by_planeID(planeID)
    
    # Update
    def update_passenger(self, index, first_name, last_name, passportID, planeID):
        if isinstance(index, int) == False:
            try:
                index = int(index)
            except:
                raise TypeError("Index must be an integer")
            if index < 0 or index > len(self.__repository.get_plane_list()):
                raise ValueError("Index must be an integer and within the list's range")
            
        if first_name == "":
            first_name = self.__repository.get_passenger_by_index(index).get_first_name()
        if last_name == "":
            last_name = self.__repository.get_passenger_by_index(index).get_last_name()
        if passportID == "":
            passportID = self.__repository.get_passenger_by_index(index).get_passportID()
        if planeID == "":
            planeID = self.__repository.get_passenger_by_index(index).get_planeID()
        if isinstance(first_name, str) == False:
            raise TypeError("First name must be a string")
        if isinstance(last_name, str) == False:
            raise TypeError("Last name must be a string")
        if isinstance(passportID, str) == False:
            raise TypeError("Passport ID must be a string")
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string or integer")
        
        return self.__repository.update_passenger(index, Passenger(first_name, last_name, passportID, planeID))

    # Delete
    def delete_passenger(self, first_name, last_name, passportID, planeID):
        if isinstance(first_name, str) == False:
            raise TypeError("First name must be a string")
        if isinstance(last_name, str) == False:
            raise TypeError("Last name must be a string")
        if isinstance(passportID, str) == False:
            raise TypeError("Passport ID must be a string")
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string or integer")
        
        return self.__repository.delete_passenger(Passenger(first_name, last_name, passportID, planeID))

    def delete_passenger_by_index(self, index):
        if isinstance(index, int) == False:
            try:
                index = int(index)
            except:
                raise TypeError("Index must be an integer")
            index = int(index)
            if index < 0 or index > len(self.__repository.get_plane_list()):
                raise ValueError("Index must be an integer and within the list's range")
            
        return self.__repository.delete_passenger_by_index(int(index))
    
    # Read from file passenger
    def read_from_file_passenger(self):
        return self.__repository.read_from_file_passenger()
    
    # Write to file passenger
    def write_to_file_passenger(self):
        return self.__repository.write_to_file_passenger()
    
    # CRUD Operations for Plane
    # Create
    def add_plane(self, planeID, airline_company, number_of_seats, destination):
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string or integer")
        if isinstance(airline_company, str) == False:
            raise TypeError("Airline company must be a string")
        if isinstance(number_of_seats, int) == False:
            try:
                number_of_seats = int(number_of_seats)
            except:
                raise TypeError("Number of seats must be an integer")
        if isinstance(destination, str) == False:
            raise TypeError("Destination must be a string")
        
        airline_company = airline_company.replace(" ", "_")
        
        
        return self.__repository.add_plane(Plane(planeID, airline_company, int(number_of_seats), destination))
    
    # Read
    def get_plane_list(self)->list:
        return self.__repository.get_plane_list()
    
    def get_plane_by_index(self, index)->Plane:
        if isinstance(index, int) == False:
            try:
                index = int(index)
            except:
                raise TypeError("Index must be an integer")
            index = int(index)
            if index < 0 or index > len(self.__repository.get_plane_list()):
                raise ValueError("Index must be an integer and within the list's range")
            
        return self.__repository.get_plane_by_index(int(index))
    
    def get_index_by_plane(self, planeID, airline_company, number_of_seats, destination)->int:
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string or integer")
        if isinstance(airline_company, str) == False:
            raise TypeError("Airline company must be a string")
        if isinstance(number_of_seats, int) == False:
            try:
                number_of_seats = int(number_of_seats)
            except:
                raise TypeError("Number of seats must be an integer")
        if isinstance(destination, str) == False:
            raise TypeError("Destination must be a string")
        return self.__repository.get_index_by_plane(Plane(planeID, airline_company, int(number_of_seats), destination))
    
    def get_index_by_planeID(self, planeID)->int:
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string")
        return self.__repository.get_index_by_planeID(planeID)
    
    def get_plane_by_planeID(self, planeID):
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string")
        return self.__repository.get_plane_by_planeID(planeID)
    
    # Update
    def update_plane(self, index, planeID, airline_company, number_of_seats, destination):
        if isinstance(index, int) == False:
            try:
                index = int(index)
            except:
                raise TypeError("Index must be an integer")
            index = int(index)
            if index < 0 or index > len(self.__repository.get_plane_list()):
                raise ValueError("Index must be an integer and within the list's range")
            
        if planeID == "":
            planeID = self.__repository.get_plane_by_index(index).get_planeID()
        if airline_company == "":
            airline_company = self.__repository.get_plane_by_index(index).get_airline_company()
        if number_of_seats == "":
            number_of_seats = self.__repository.get_plane_by_index(index).get_number_of_seats()
        if destination == "":
            destination = self.__repository.get_plane_by_index(index).get_destination()
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string or integer")
        if isinstance(airline_company, str) == False:
            raise TypeError("Airline company must be a string")
        if isinstance(number_of_seats, int) == False:
            try:
                number_of_seats = int(number_of_seats)
            except:
                raise TypeError("Number of seats must be an integer")
        if isinstance(destination, str) == False:
            raise TypeError("Destination must be a string")
        
        return self.__repository.update_plane(int(index), Plane(planeID, airline_company, int(number_of_seats), destination))
    
    # Delete
    def delete_plane_by_index(self, index):
        if isinstance(index, int) == False:
            try:
                index = int(index)
            except:
                raise TypeError("Index must be an integer")
            index = int(index)
            if index < 0 or index > len(self.__repository.get_plane_list()):
                raise ValueError("Index must be an integer and within the list's range")
        return self.__repository.delete_plane_by_index(int(index))
    
    def delete_plane(self, planeID, airline_company, number_of_seats, destination): 
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string or integer")
        if isinstance(airline_company, str) == False:
            raise TypeError("Airline company must be a string")
        if isinstance(number_of_seats, int) == False:
            try:
                number_of_seats = int(number_of_seats)
            except:
                raise TypeError("Number of seats must be an integer")
        if isinstance(destination, str) == False:
            raise TypeError("Destination must be a string")
        return self.__repository.delete_plane(Plane(planeID, airline_company, int(number_of_seats), destination))
    
     # Read from file passenger
    def read_from_file_plane(self):
        return self.__repository.read_from_file_plane()
    
    # Write to file passenger
    def write_to_file_plane(self):
        return self.__repository.write_to_file_plane()
    
    # Read from file passenger
    def read_from_file_plane(self):
        return self.__repository.read_from_file_plane()
    
    # Write to file passenger
    def write_to_file_passenger(self):
        return self.__repository.write_to_file_plane()
    
    # Show remaining seats
    def show_remaining_seats(self, planeID):
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string")
        return self.__repository.show_remaining_seats(planeID)
    
    # 3 Sort Passengers by last name
    def sort_passengers_in_plane_by_last_name(self, planeID):
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string")
        return self.__repository.sort_passengers_in_plane_by_last_name(planeID)
    
    # 4 Sort planes according to the number of passengers
    def sort_planes_by_number_of_passengers(self):
        return self.__repository.sort_planes_by_number_of_passengers()
    
    # 5 Sort planes accordubg to the number of passengers witht he first name with given substring
    def sort_planes_by_number_of_passengers_and_first_name_given_substring(self, substring):
        if isinstance(substring, str) == False:
            raise TypeError("Substring must be a string")
        return self.__repository.sort_planes_by_number_of_passengers_and_first_name_given_substring(substring)
    
    # 6 Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
    def sort_planes_by_number_of_passengers_and_destination(self):
        return self.__repository.sort_planes_by_number_of_passengers_and_destination()
    
    # 7 Identify planes that have passengers with passport numbers starting with the same 3 letters
    def get_planes_with_passengers_with_passport_starting_with_same_3_letters(self):
        return self.__repository.get_planes_with_passengers_with_passport_starting_with_same_3_letters()
    
    # 8 Identify passengers from a given plane for which the first name or last name contatin a string given as parameter
    def passenger_from_plane_having_first_or_last_name_like_string(self, planeID, substring):
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string")
        if isinstance(substring, str) == False:
            raise TypeError("Substring must be a string")
        return self.__repository.passenger_from_plane_having_first_or_last_name_like_string(planeID, substring)
    
    # 9 Identify plane(s) where there is a passenger with a given name
    def get_planes_with_passenger_name(self, first_name, last_name):
        if isinstance(first_name, str) == False:
            raise TypeError("First name must be a string")
        if isinstance(last_name, str) == False:
            raise TypeError("Last name must be a string")
        return self.__repository.get_planes_with_passenger_name(first_name, last_name)
    
    # 10 Form groups of [k] passengers from the same plane but with different last names
    def groups_of_passengers_from_same_plane(self, planeID, k):
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string")
        if isinstance(k, int) == False:
            try:
                k = int(k)
            except:
                raise TypeError("Number of elements in the group must be an integer")
        return self.__repository.groups_of_passengers_from_same_plane(planeID, int(k))
    
    # 11 Form groups of [k] planes with the same destination but belonging to different airline companies
    def groups_of_planes_with_same_destination_different_airline(self, k):
        if isinstance(k, int) == False:
            try:
                k = int(k)
            except:
                raise TypeError("Number of elements in the group must be an integer")
        return self.__repository.groups_of_planes_with_same_destination_different_airline(int(k))
    
    
    
    
    
    
        

