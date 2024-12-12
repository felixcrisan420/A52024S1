from domain.plane import Plane
from domain.passenger import Passenger
from repository.repository import Repository
from utils.utilities import Utilities 

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
    
    def get_passengers_by_first_and_last_name(self, first_name, last_name)->list:
        if isinstance(first_name, str) == False:
            raise TypeError("First name must be a string")
        if isinstance(last_name, str) == False:
            raise TypeError("Last name must be a string")
        
        return self.__repository.get_passengers_by_first_and_last_name(first_name, last_name)
    
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
        return self.__repository.read_from_file("Passenger")
    
    # Write to file passenger
    def write_to_file_passenger(self):
        return self.__repository.write_to_file("Passenger")
    
    # CRUD Operations for Plane
    # Create
    def add_plane(self, planeID, airline_company, number_of_seats, destination):
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string or integer")
        if isinstance(airline_company, str) == False:
            raise TypeError("Airline company must be a string")
        airline_company = airline_company.replace(" ", "_")
        if isinstance(number_of_seats, int) == False:
            try:
                number_of_seats = int(number_of_seats)
            except:
                raise TypeError("Number of seats must be an integer")
        if isinstance(destination, str) == False:
            raise TypeError("Destination must be a string")
        
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
    
    # Show remaining seats
    def show_remaining_seats(self, planeID):
        if isinstance(planeID, str) == False:
            raise TypeError("Plane ID must be a string")
        return self.__repository.show_remaining_seats(planeID)
    
    def write_to_file_plane(self):
        return self.__repository.write_to_file("Plane")
    
    def read_from_file_plane(self):
        return self.__repository.read_from_file("Plane")
    
    
    
    
    
    
        

