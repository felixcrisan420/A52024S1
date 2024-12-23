from domain.plane import Plane
from repository.plane_repository import PlaneRepository
from utils.utilities import Utilities



class PlaneService:
    
    def __init__(self, repository:PlaneRepository):
        """Constructor for PlaneService class

        Args:
            repository (PlaneRepository): The repository for the PlaneService
        """
        self.__plane_repository = repository

    # CRUD Operations for Plane
    # Create
    def add_plane(self, planeID, airline_company, number_of_seats, destination)->Plane:
        """Add a plane to the plane repository

        Args:
            planeID (str): The plane ID
            airline_company (str): The airline company
            number_of_seats (int): The number of seats
            destination (str): The destination

        Returns:
            Plane: The plane object that was added to the plane repository
        """
        Utilities.validate_inputs({
            "Plane ID": (planeID, str),
            "Airline Company": (airline_company, str)
        })
        airline_company = airline_company.replace(" ", "_")
        Utilities.validate_inputs({
            "Number of seats": (number_of_seats, int),
            "Destination": (destination, str)
        })
        return self.__plane_repository.add_plane(
            Plane(planeID, airline_company, int(number_of_seats), destination)
        )
    
    # Read
    def get_plane_list(self)->list[Plane]:
        """Get the list of planes from the plane repository

        Returns:
            list[Plane]: The list of planes from the plane repository
        """
        return self.__plane_repository.get_plane_list()
    
    def get_plane_by_index(self, index)->Plane:
        """Get a plane by index

        Args:
            index (int): The index of the plane

        Returns:
            Plane: The plane object at the specified index
        """
        # add the list of data to validate inputs
        Utilities.validate_inputs({
            "Index": (index, "index")
            },
            self.__plane_repository.get_plane_list()
        )
        return self.__plane_repository.get_plane_by_index(int(index))
    
    def get_index_by_plane(self, planeID, airline_company, number_of_seats, destination)->int:
        Utilities.validate_inputs({
            "Plane ID": (planeID, str),
            "Airline Company": (airline_company, str),
            "Number of seats": (number_of_seats, int),
            "Destination": (destination, str)
        })
        return self.__plane_repository.get_index_by_plane(Plane(planeID, airline_company, int(number_of_seats), destination))
    
    def get_index_by_planeID(self, planeID)->int:
        """Get the index of a plane by plane ID

        Args:
            planeID (str): The plane ID

        Returns:
            int: The index of the plane in the plane repository
        """
        Utilities.validate_inputs({
            "Plane ID": (planeID, str)
        })
        return self.__plane_repository.get_index_by_planeID(planeID)
    
    def get_plane_by_planeID(self, planeID)->Plane:
        """Get a plane by plane ID
        
        Args:
            planeID (str): The plane ID
            
        Returns:
            Plane: The plane object with the specified plane
        """
        Utilities.validate_inputs({
            "Plane ID": (planeID, str)
        })
        return self.__plane_repository.get_plane_by_planeID(planeID)
    
    # Update
    def update_plane(self, index, planeID, airline_company, number_of_seats, destination)->Plane:
        """Update a plane in the plane repository

        Args:
            planeID (str): The plane ID
            airline_company (str): The airline company
            number_of_seats (int): The number of seats
            destination (str): The destination

        Returns:
            Plane: The plane object that was updated in the plane repository
        """
        Utilities.validate_inputs({
            "Index": (index, "index")
            },
            self.__plane_repository.get_plane_list()
        ) 
        if planeID == "":
            planeID = self.__plane_repository.get_plane_by_index(index).get_planeID()
        if airline_company == "":
            airline_company = self.__plane_repository.get_plane_by_index(index).get_airline_company()
        if number_of_seats == None:
            number_of_seats = self.__plane_repository.get_plane_by_index(index).get_number_of_seats()
        if destination == "":
            destination = self.__plane_repository.get_plane_by_index(index).get_destination()
        
        Utilities.validate_inputs({
            "Plane ID": (planeID, str),
            "Airline Company": (airline_company, str),
            "Number of seats": (number_of_seats, int),
            "Destination": (destination, str)
        })

        return self.__plane_repository.update_plane(int(index), Plane(planeID, airline_company, int(number_of_seats), destination))
    
    # Delete
    def delete_plane_by_index(self, index)->Plane:
        """Delete a plane by index

        Args:
            index (int): The index of the plane

        Returns:
            Plane: The plane object that was deleted
        """
        Utilities.validate_inputs({
            "Index": (index, "index")
            },
            self.__plane_repository.get_plane_list()
        )
        return self.__plane_repository.delete_plane_by_index(int(index))
    
    def delete_plane_by_object(self, planeID, airline_company, number_of_seats, destination)->Plane:
        """Delete a plane by object
        
        Args:
            planeID (str): The plane ID
            airline_company (str): The airline company
            number_of_seats (int): The number of seats
            destination (str): The destination
            
        Returns:
            Plane: The plane object that was deleted
        """ 
        Utilities.validate_inputs({
            "Plane ID": (planeID, str),
            "Airline Company": (airline_company, str),
            "Number of seats": (number_of_seats, int),
            "Destination": (destination, str)
        })

        return self.__plane_repository.delete_plane(Plane(planeID, airline_company, int(number_of_seats), destination))
    
    # Show remaining seats
    def show_remaining_seats(self, planeID)->int:
        """Show the remaining seats on a plane
        
        Args:
            planeID (str): The plane ID
        
        Returns:
            int: The number of remaining seats on the plane
        """
        Utilities.validate_inputs({
            "PlaneID": (planeID, str)
        })
        return self.__plane_repository.show_remaining_seats(planeID)
    
    def read_from_file(self)->list[Plane]:
        """Read the list of planes from the file

        Returns:
            list[Plane]: The list of planes from the file
        """
        return self.__plane_repository.read_from_file()
    
    def write_to_file(self)->list[Plane]:
        """Write the list of planes to the file

        Returns:
            list[Plane]: The list of planes that was written to the file
        """
        return self.__plane_repository.write_to_file()
    
    