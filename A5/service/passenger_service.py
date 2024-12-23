from domain.passenger import Passenger
from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository
from utils.utilities import Utilities


class PassengerService:
    def __init__(self, passenger_repository:PassengerRepository, plane_repository: PlaneRepository):
        """Constructor for PassengerService class

        Args:
            passenger_repository (PassengerRepository): The passenger repository
            plane_repository (PlaneRepository): The plane repository
        """
        self.__passenger_repository = passenger_repository
        self.__plane_repository = plane_repository


    def __check_plane_existance(self, planeID:str)->None:
        """Check if the plane exists in the plane repository

        Args:
            planeID (str): The plane ID to check

        Raises:
            ValueError: If the plane ID does not exist in the plane repository
        """
        if self.__plane_repository.get_index_by_planeID(planeID) == -1:
            raise ValueError("Plane ID does not exist")
    # CRUD Operations for Passenger
    # Create
    def add_passenger(self, first_name:str, last_name:str, passportID:str, planeID:str)->Passenger:
        """Add a passenger to the passenger repository

        Args:
            first_name (str): The first name of the passenger
            last_name (str): The last name of the passenger
            passportID (str): The passport ID of the passenger
            planeID (str): The plane ID of the passenger

        Returns
            Passenger:  The passenger object that was added to the passenger repository
        """
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
    def get_passenger_list(self)->list[Passenger]:
        """Get the list of passengers from the passenger repository

        Returns:
            list: The list of passengers from the passenger repository
        """
        return self.__passenger_repository.get_passenger_list()
    
    def get_passenger_by_index(self, index)->list[Passenger]:
        """Get the passenger by index from the passenger repository

        Args:
            index (int): The index of the passenger to get

        Returns:
            list[Passnger]: The passenger object from the passenger repository
        """
        Utilities.validate_inputs({
            "Index": (index, "index")
            },
            self.__passenger_repository.get_passenger_list()
        )
        return self.__passenger_repository.get_passenger_by_index(int(index))
    
    def get_index_by_passenger(self, first_name:str, last_name:str, passportID:str, planeID:str)->int:
        """Get the index of the passenger from the passenger repository

        Args:
            first_name (str): The first name of the passenger
            last_name (str): The last name of the passenger
            passportID (str): The passport ID of the passenger
            planeID (str): The plane ID of the passenger

        Returns:
            int: The index of the passenger from the passenger repository
        """
        Utilities.validate_inputs({
            "First name": (first_name, str),
            "Last name": (last_name, str),
            "Passport ID": (passportID, str),
            "Plane ID": (planeID, str)
        })
        self.__check_plane_existance(planeID)
        return self.__passenger_repository.get_index_by_passenger(Passenger(first_name, last_name, passportID, planeID))
    
    def get_passengers_by_planeID(self, planeID)->list[Passenger]:
        """Get the list of passengers by plane ID from the passenger repository

        Args:
            planeID (str): The plane ID to get the passengers by

        Returns:
            list[Passenger]: The list of passengers by plane ID from the passenger repository
        """
        Utilities.validate_inputs({
            "Plane ID": (planeID, str)
        })
        self.__check_plane_existance(planeID)
        return self.__passenger_repository.get_passengers_by_planeID(planeID)
    
    def get_passengers_by_first_and_last_name(self, first_name:str, last_name:str)->list[Passenger]:
        """Get the list of passengers by first and last name from the passenger repository

        Args:
            first_name (str): The first name of the passenger
            last_name (str): The last name of the passenger

        Returns:
            list[Passenger]: The list of passengers by first and last name from the passenger repository
        """
        Utilities.validate_inputs({
            "First Name": (first_name, str),
            "Last Name": (last_name, str)
        })
        
        return self.__passenger_repository.get_passengers_by_first_and_last_name(first_name, last_name)
    
    def get_passenger_by_passportID(self, passportID:str)->Passenger:
        """Get the passenger by passport ID from the passenger repository

        Args:
            passportID (str): The passport ID of the passenger

        Returns:
            Passenger: The passenger object by passport ID from the passenger repository
        """
        Utilities.validate_inputs({
            "Passport ID": (passportID, str)
        })
        
        return self.__passenger_repository.get_passenger_by_passportID(passportID)
    
    # Update
    def update_passenger(self, index:int, first_name:str, last_name:str, passportID:str, planeID:str)->Passenger:
        """Update the passenger by index from the passenger repository

        Args:
            index (int): The index of the passenger to update
            first_name (str): The first name of the passenger
            last_name (str): The last name of the passenger
            passportID (str): The passport ID of the passenger
            planeID (str): The plane ID of the passenger

        Returns:
            Passenger: The passenger object that was updated in the passenger repository
        """
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
    def delete_passenger_by_object(self, first_name:str, last_name:str, passportID:str, planeID:str)->Passenger:
        """Delete the passenger by object from the passenger repository

        Args:
            first_name (str): The first name of the passenger
            last_name (str): The last name of the passenger
            passportID (str): The passport ID of the passenger
            planeID (str): The plane ID of the passenger

        Returns:
            Passenger: The passenger object that was deleted from the passenger repository
        """
        Utilities.validate_inputs({
            "First name": (first_name, str),
            "Last name": (last_name, str),
            "Passport ID": (passportID, str),
            "Plane ID": (planeID, str)
        })
        self.__check_plane_existance(planeID)
        return self.__passenger_repository.delete_passenger(Passenger(first_name, last_name, passportID, planeID))

    def delete_passenger_by_index(self, index:int)->Passenger:
        """Delete the passenger by index from the passenger repository

        Args:
            index (int): The index of the passenger to delete

        Returns:
            Passenger: The passenger object that was deleted from the passenger repository
        """
        Utilities.validate_inputs({
            "Index": (index, "index")
            },
            self.__passenger_repository.get_passenger_list()
        )
            
        return self.__passenger_repository.delete_passenger_by_index(int(index))
    
    # Read from file passenger
    def read_from_file(self)->list[Passenger]:
        """Read from file.

        Returns:
            list[Passenger]: The list of passengers.
        """
        return self.__passenger_repository.read_from_file()
    
    # Write to file passenger
    def write_to_file(self)->list[Passenger]:
        """Write to file.
        
        Returns:
            list[Passenger]: The list of passengers.
        """
        return self.__passenger_repository.write_to_file()
    