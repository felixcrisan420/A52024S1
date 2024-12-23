from domain.passenger import Passenger
from utils.utilities import FileHandler
from constants.const import Constants as const

class PassengerRepository:
    def __init__(self):
        """
        Constructor for PassengerRepository class.

        Args:
            None

        Returns:
            None
        """
        self.__passenger_list = []

    # CRUD OPERATIONS for Passenger

    # Create
    def add_passenger(self, passenger:Passenger)->Passenger:
        """
        Add a passenger to the passenger list. 

        Args:
            passenger (Passenger): The passenger to be added to the list.

        Returns:
            Passenger: The passenger that was added to the list.
        """
        self.__passenger_list.append(passenger)
        return passenger
    
    # Read
    def get_passenger_list(self)->list:
        """
        Get the list of passengers.

        Args:
            None

        Returns:    
            list: The list of passengers.
        """
        return self.__passenger_list
    
    def get_passenger_by_index(self, index:int)->Passenger:
        """
        Get a passenger by index.

        Args:
            index (int): The index of the passenger in the list.

        Returns:
            Passenger: The passenger at the specified index.
        """
        return self.__passenger_list[index]
    
    def get_index_by_passenger(self, search_passenger: Passenger) -> int:
        """
        Get the index of a passenger in the list.

        Args:
            search_passenger (Passenger): The passenger to search for in the list.

        Returns:
            int: The index of the passenger in the list.
        """
        for index, passenger in enumerate(self.__passenger_list):
            if passenger == search_passenger:
                return index
        return -1
        
    def get_passengers_by_planeID(self, planeID:str)->list[Passenger]:
        """
        Get a list of passengers by plane ID.

        Args:
            planeID (str): The plane ID to search for.

        Returns:
            list: A list of passengers with the specified plane ID.
        """
        passenger_list = []
        for passenger in self.__passenger_list:
            if passenger.get_planeID() == planeID:
                passenger_list.append(passenger)
        return passenger_list
    
    def get_passengers_by_first_and_last_name(self, first_name:str, last_name:str)->list[Passenger]:
        """
        Get a list of passengers by first and last name.

        Args:
            first_name (str): The first name of the passenger.
            last_name (str): The last name of the passenger.

        Returns:
            list: A list of passengers with the specified first and last name.
        """
        passenger_list = []
        for passenger in self.__passenger_list:
            if passenger.get_first_name() == first_name and passenger.get_last_name() == last_name:
                passenger_list.append(passenger)
        return passenger_list
    
    def get_passenger_by_passportID(self, passportID:str)->Passenger:
        """
        Get a passenger by passport ID.

        Args:
            passportID (str): The passport ID of the passenger.

        Returns:
            Passenger: The passenger with the specified passport ID.
        """
        for passenger in self.__passenger_list:
            if passenger.get_passportID() == passportID:
                return passenger
        return Passenger("Does not exist", "Does not exist", "Does not exist", "Does not exist")
    
    # Update
    def update_passenger(self, index:int, new_passenger:Passenger)->Passenger:
        """
        Update a passenger in the list.

        Args:
            index (int): The index of the passenger in the list.
            new_passenger (Passenger): The updated passenger object.

        Returns:
            Passenger: The updated passenger object.
        """
        self.__passenger_list[index].set_first_name(new_passenger.get_first_name())
        self.__passenger_list[index].set_last_name(new_passenger.get_last_name())
        self.__passenger_list[index].set_passportID(new_passenger.get_passportID())
        self.__passenger_list[index].set_planeID(new_passenger.get_planeID())
        return self.__passenger_list[index]
    
    # Delete
    def delete_passenger_by_object(self, passenger:Passenger)->Passenger:
        """
        Delete a passenger from the list.   

        Args:
            passenger (Passenger): The passenger to be deleted.

        Returns:
            Passenger: The passenger that was deleted.
        """
        self.__passenger_list.remove(passenger)
        return passenger

    def delete(self, passenger:Passenger)->Passenger:
        """ 
        Delete a passenger from the list

        Args:
            passenger (Passenger): The passenger to be deleted. 

        Returns:
            Passenger: The passenger that was deleted
        """
        self.__passenger_list.remove(passenger)
        return passenger
    
    def delete_passenger(self, passenger:Passenger)->Passenger:
        """
        Delete a passenger from the list.

        Args:
            passenger (Passenger): The passenger to be deleted.

        Returns:
            Passenger: The passenger that was deleted.
        """
        self.__passenger_list.remove(passenger)
        return passenger

    def delete_passenger_by_index(self, index)->Passenger:
        """
        Delete a passenger from the list by index.

        Args:
            index (int): The index of the passenger to be deleted.

        Returns:
            Passenger: The passenger that was deleted.
        """
        passenger = self.__passenger_list[index]
        del self.__passenger_list[index]
        return passenger
    
    def read_from_file(self)->list[Passenger]:
        """
        Read from file and return the passenger list.

        Args:
            None

        Returns:
            list[Passenger]: The list of passengers.
        """
        for passenger in FileHandler.read_from_file(const.FILE_NAME_PASSENGER, Passenger):
            self.__passenger_list.append(passenger)
        return self.__passenger_list

    def write_to_file(self)->list[Passenger]:
        """
        Write to file and return the passenger list.

        Args:
            None

        Returns:
            list[Passenger]: The list of passengers.
        """
        FileHandler.write_to_file(const.FILE_NAME_PASSENGER, self.__passenger_list)
        return self.__passenger_list
    
    
    
