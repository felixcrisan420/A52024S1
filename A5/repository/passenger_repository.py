from domain.passenger import Passenger
import os

class PassengerRepository:
    def __init__(self):
        self.__passenger_list = []

    # CRUD OPERATIONS for Passenger

    # Create
    def add_passenger(self, passenger:Passenger)->Passenger:
        self.__passenger_list.append(passenger)
        return passenger
    
    # Read
    def get_passenger_list(self)->list:
        return self.__passenger_list
    
    def get_passenger_by_index(self, index:int)->Passenger:
        return self.__passenger_list[index]
    
    def get_index_by_passenger(self, search_passenger: Passenger) -> int:
        for index, passenger in enumerate(self.__passenger_list):
            if passenger == search_passenger:
                return index
        return -1
        
    def get_passengers_by_planeID(self, planeID:str)->list[Passenger]:
        passenger_list = []
        for passenger in self.__passenger_list:
            if passenger.get_planeID() == planeID:
                passenger_list.append(passenger)
        return passenger_list
    
    def get_passengers_by_first_and_last_name(self, first_name:str, last_name:str)->list[Passenger]:
        passenger_list = []
        for passenger in self.__passenger_list:
            if passenger.get_first_name() == first_name and passenger.get_last_name() == last_name:
                passenger_list.append(passenger)
        return passenger_list
    
    # Update
    def update_passenger(self, index:int, new_passenger:Passenger)->Passenger:
        self.__passenger_list[index].set_first_name(new_passenger.get_first_name())
        self.__passenger_list[index].set_last_name(new_passenger.get_last_name())
        self.__passenger_list[index].set_passportID(new_passenger.get_passportID())
        self.__passenger_list[index].set_planeID(new_passenger.get_planeID())
        return self.__passenger_list[index]
    
    # Delete
    def delete_passenger(self, passenger:Passenger)->Passenger:
        self.__passenger_list.remove(passenger)
        return passenger

    def remove_passenger_by_index(self, index)->Passenger:
        passenger = self.__passenger_list[index]
        del self.__passenger_list[index]
        return passenger
    
    
    # Write to file
    def write_to_file(self):
        cwd = os.getcwd()
        # Clear the file by opening it in write mode ('w')
        with open(f"{cwd}/A5/repository/output/passenger_data.txt", "w") as file:
            pass  # Simply open and close the file to clear its contents
        
        # Open the file in write mode ('w') to overwrite it completely
        with open(f"{cwd}/A5/repository/output/passenger_data.txt", "w") as file:
            for passenger in self.__passenger_list:
                file.write(f"{passenger.__str__()}\n")
       
    # Read from file
    def read_from_file(self):
        cwd = os.getcwd()
        with open(f"{cwd}/A5/repository/output/passenger_data.txt", "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(" ")
                passenger = Passenger(line[0], line[1], line[2], line[3])
                self.__passenger_list.append(passenger)
