from domain.passenger import Passenger
from repository.passenger_repository import PassengerRepository
from utils.utilities import Utilities as utils

FILE_NAME = "passenger_data.txt"

class PassengerService:
    def __init__(self, passenger_repository:PassengerRepository):
        self.__passenger_repository = passenger_repository

    # CRUD Operations for Passenger
    # Create
    def add_passenger(self, first_name, last_name, passportID, planeID):
        utils.validate_inputs({
            "First name": (first_name, str),
            "Last name": (last_name, str),
            "Passport ID": (passportID, str),
            "Plane ID": (planeID, str)
        })
        return self.__passenger_repository.add_passenger(
            Passenger(first_name, last_name, passportID, planeID)
        )
    
    # Read
    def get_passenger_list(self)->list:
        return self.__passenger_repository.get_passenger_list()
    
    def get_passenger_by_index(self, index)->list:
        utils.validate_inputs({
            "Index": (index, "index")
        })
        return self.__passenger_repository.get_passenger_by_index(int(index))
    
    def get_index_by_passenger(self, first_name, last_name, passportID, planeID)->int:
        utils.validate_inputs({
            "First name": (first_name, str),
            "Last name": (last_name, str),
            "Passport ID": (passportID, str),
            "Plane ID": (planeID, str)
        })
        
        return self.__passenger_repository.get_index_by_passenger(Passenger(first_name, last_name, passportID, planeID))
    
    def get_passengers_by_planeID(self, planeID)->list:
        utils.validate_inputs({
            "Plane ID": (planeID, str)
        })
        
        return self.__passenger_repository.get_passengers_by_planeID(planeID)
    
    def get_passengers_by_first_and_last_name(self, first_name, last_name)->list:
        utils.validate_inputs({
            "First Name": (first_name, str),
            "Last Name": (last_name, str)
        })
        
        return self.__passenger_repository.get_passengers_by_first_and_last_name(first_name, last_name)
    
    # Update
    def update_passenger(self, index, first_name, last_name, passportID, planeID):
        utils.validate_inputs({
            "Index": (index, "index")
        })
            
        if first_name == "":
            first_name = self.__passenger_repository.get_passenger_by_index(index).get_first_name()
        if last_name == "":
            last_name = self.__passenger_repository.get_passenger_by_index(index).get_last_name()
        if passportID == "":
            passportID = self.__passenger_repository.get_passenger_by_index(index).get_passportID()
        if planeID == "":
            planeID = self.__passenger_repository.get_passenger_by_index(index).get_planeID()
        
        utils.validate_inputs({
            "First name": (first_name, str),
            "Last name": (last_name, str),
            "Passport ID": (passportID, str),
            "Plane ID": (planeID, str)
        })
        
        return self.__passenger_repository.update_passenger(index, Passenger(first_name, last_name, passportID, planeID))

    # Delete
    def delete_passenger(self, first_name, last_name, passportID, planeID):
        utils.validate_inputs({
            "First name": (first_name, str),
            "Last name": (last_name, str),
            "Passport ID": (passportID, str),
            "Plane ID": (planeID, str)
        })
        
        return self.__passenger_repository.delete_passenger(Passenger(first_name, last_name, passportID, planeID))

    def delete_passenger_by_index(self, index):
        utils.validate_inputs({
            "Index": (index, "index")
        })
            
        return self.__passenger_repository.delete_passenger_by_index(int(index))
    
    # Read from file passenger
    def read_from_file_passenger(self):
        return utils.read_from_file(FILE_NAME)
    
    # Write to file passenger
    def write_to_file_passenger(self):
        return utils.write_to_file(FILE_NAME)
    