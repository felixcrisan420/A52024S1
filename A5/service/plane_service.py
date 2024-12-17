from domain.plane import Plane
from repository.plane_repository import PlaneRepository
from utils.utilities import Utilities as utils



class PlaneService:
    FILE_NAME = "plane_data.txt"
    
    def __init__(self, repository:PlaneRepository):
        self.__plane_repository = repository

    # CRUD Operations for Plane
    # Create
    def add_plane(self, planeID, airline_company, number_of_seats, destination):
        utils.validate_inputs({
            "Plane ID": (planeID, str),
            "Airline Company": (airline_company, str)
        })
        airline_company = airline_company.replace(" ", "_")
        utils.validate_inputs({
            "Number of seats": (number_of_seats, int),
            "Destination": (destination, str)
        })
        return self.__plane_repository.add_plane(
            Plane(planeID, airline_company, int(number_of_seats), destination)
        )
    
    # Read
    def get_plane_list(self)->list:
        return self.__plane_repository.get_plane_list()
    
    def get_plane_by_index(self, index)->Plane:
        utils.validate_inputs({
            "Index": (index, "index")
        })
            
        return self.__plane_repository.get_plane_by_index(int(index))
    
    def get_index_by_plane(self, planeID, airline_company, number_of_seats, destination)->int:
        utils.validate_inputs({
            "Plane ID": (planeID, str),
            "Airline Company": (airline_company, str),
            "Number of seats": (number_of_seats, int),
            "Destination": (destination, str)
        })
        return self.__plane_repository.get_index_by_plane(Plane(planeID, airline_company, int(number_of_seats), destination))
    
    def get_index_by_planeID(self, planeID)->int:
        utils.validate_inputs({
            "Plane ID": (planeID, str)
        })
        return self.__plane_repository.get_index_by_planeID(planeID)
    
    def get_plane_by_planeID(self, planeID):
        utils.validate_inputs({
            "Plane ID": (planeID, str)
        })
        return self.__plane_repository.get_plane_by_planeID(planeID)
    
    # Update
    def update_plane(self, index, planeID, airline_company, number_of_seats, destination):
        utils.validate_inputs({
            "Index": (index, "index")
        })
            
        if planeID == "":
            planeID = self.__plane_repository.get_plane_by_index(index).get_planeID()
        if airline_company == "":
            airline_company = self.__plane_repository.get_plane_by_index(index).get_airline_company()
        if number_of_seats == "":
            number_of_seats = self.__plane_repository.get_plane_by_index(index).get_number_of_seats()
        if destination == "":
            destination = self.__plane_repository.get_plane_by_index(index).get_destination()
        
        utils.validate_inputs({
            "Plane ID": (planeID, str),
            "Airline Company": (airline_company, str),
            "Number of seats": (number_of_seats, int),
            "Destination": (destination, str)
        })

        return self.__plane_repository.update_plane(int(index), Plane(planeID, airline_company, int(number_of_seats), destination))
    
    # Delete
    def delete_plane_by_index(self, index):
        utils.validate_inputs({
            "Index": (index, "index")
        })
        return self.__plane_repository.delete_plane_by_index(int(index))
    
    def delete_plane(self, planeID, airline_company, number_of_seats, destination): 
        utils.validate_inputs({
            "Plane ID": (planeID, str),
            "Airline Company": (airline_company, str),
            "Number of seats": (number_of_seats, int),
            "Destination": (destination, str)
        })

        return self.__plane_repository.delete_plane(Plane(planeID, airline_company, int(number_of_seats), destination))
    
    # Show remaining seats
    def show_remaining_seats(self, planeID):
        utils.validate_inputs({
            "PlaneID": (planeID, str)
        })
        return self.__plane_repository.show_remaining_seats(planeID)
    