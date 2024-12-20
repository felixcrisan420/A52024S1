from domain.passenger import Passenger
from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository
from utils.utilities import Utilities


class PassengerService:
    def __init__(self, passenger_repository:PassengerRepository, plane_repository: PlaneRepository):
        self.__passenger_repository = passenger_repository
        self.__plane_repository = plane_repository


    def __check_plane_existance(self, planeID):
        if self.__plane_repository.get_index_by_planeID(planeID) == -1:
            raise ValueError("Plane ID does not exist")
    # CRUD Operations for Passenger
    # Create
    def add_passenger(self, first_name, last_name, passportID, planeID):
        Utilities.validate_inputs({
            "First name": (first_name, str),
            "Last name": (last_name, str),
            "Passport ID": (passportID, str),
            "Plane ID": (planeID, str)
        })
        self.__check_plane_existance(planeID)
        return self.__passenger_repository.add_passenger(
            Passenger(first_name, last_name, passportID, planeID)
        )
    
    # Read
    def get_passenger_list(self)->list:
        return self.__passenger_repository.get_passenger_list()
    
    def get_passenger_by_index(self, index)->list:
        Utilities.validate_inputs({
            "Index": (index, "index")
            },
            self.__passenger_repository.get_passenger_list()
        )
        return self.__passenger_repository.get_passenger_by_index(int(index))
    
    def get_index_by_passenger(self, first_name, last_name, passportID, planeID)->int:
        Utilities.validate_inputs({
            "First name": (first_name, str),
            "Last name": (last_name, str),
            "Passport ID": (passportID, str),
            "Plane ID": (planeID, str)
        })
        self.__check_plane_existance(planeID)
        return self.__passenger_repository.get_index_by_passenger(Passenger(first_name, last_name, passportID, planeID))
    
    def get_passengers_by_planeID(self, planeID)->list:
        Utilities.validate_inputs({
            "Plane ID": (planeID, str)
        })
        self.__check_plane_existance(planeID)
        return self.__passenger_repository.get_passengers_by_planeID(planeID)
    
    def get_passengers_by_first_and_last_name(self, first_name, last_name)->list:
        Utilities.validate_inputs({
            "First Name": (first_name, str),
            "Last Name": (last_name, str)
        })
        
        return self.__passenger_repository.get_passengers_by_first_and_last_name(first_name, last_name)
    
    def get_passenger_by_passportID(self, passportID):
        Utilities.validate_inputs({
            "Passport ID": (passportID, str)
        })
        
        return self.__passenger_repository.get_passenger_by_passportID(passportID)
    
    # Update
    def update_passenger(self, index, first_name, last_name, passportID, planeID):
        Utilities.validate_inputs({
            "Index": (index, "index")
            },
            self.__passenger_repository.get_passenger_list()
        )
            
        if first_name == "":
            first_name = self.__passenger_repository.get_passenger_by_index(index).get_first_name()
        if last_name == "":
            last_name = self.__passenger_repository.get_passenger_by_index(index).get_last_name()
        if passportID == "":
            passportID = self.__passenger_repository.get_passenger_by_index(index).get_passportID()
        if planeID == "":
            planeID = self.__passenger_repository.get_passenger_by_index(index).get_planeID()
        
        Utilities.validate_inputs({
            "First name": (first_name, str),
            "Last name": (last_name, str),
            "Passport ID": (passportID, str),
            "Plane ID": (planeID, str)
        })
        self.__check_plane_existance(planeID)
        return self.__passenger_repository.update_passenger(index, Passenger(first_name, last_name, passportID, planeID))

    # Delete
    def delete_passenger_by_object(self, first_name, last_name, passportID, planeID):
        Utilities.validate_inputs({
            "First name": (first_name, str),
            "Last name": (last_name, str),
            "Passport ID": (passportID, str),
            "Plane ID": (planeID, str)
        })
        self.__check_plane_existance(planeID)
        return self.__passenger_repository.delete_passenger(Passenger(first_name, last_name, passportID, planeID))

    def delete_passenger_by_index(self, index):
        Utilities.validate_inputs({
            "Index": (index, "index")
            },
            self.__passenger_repository.get_passenger_list()
        )
            
        return self.__passenger_repository.delete_passenger_by_index(int(index))
    
    # Read from file passenger
    def read_from_file(self):
        return self.__passenger_repository.read_from_file()
    
    # Write to file passenger
    def write_to_file(self):
        return self.__passenger_repository.write_to_file()
    