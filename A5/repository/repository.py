from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository
from domain.plane import Plane
from domain.passenger import Passenger

class Repository:
    def __init__(self, passenger_repo:PassengerRepository, plane_repo:PlaneRepository):
        self.__passenger_repo = passenger_repo
        self.__plane_repo = plane_repo

    # CRUD Passenger
    def add_passenger(self, passenger:Passenger)->Passenger:
        self.__passenger_repo.add_passenger(passenger)
        return passenger
    
    def get_passenger_list(self)->list[Passenger]:
        return self.__passenger_repo.get_passenger_list()
    
    def get_passenger_by_index(self, index:int)->Passenger:
        return self.__passenger_repo.get_passenger_by_index(index)
    
    def get_index_by_passenger(self, search_passenger:Passenger)->int:
        return self.__passenger_repo.get_index_by_passenger(search_passenger)
    
    def get_passengers_by_planeID(self, planeID:str)->list[Passenger]:
        return self.__passenger_repo.get_passengers_by_planeID(planeID)
    
    def get_passengers_by_first_and_last_name(self, first_name:str, last_name:str)->list[Passenger]:
        return self.__passenger_repo.get_passengers_by_first_and_last_name(first_name, last_name)

    def update_passenger(self, index:int, new_passenger:Passenger)->Passenger:
        return self.__passenger_repo.update_passenger(index, new_passenger)
    
    def delete_passenger(self, passenger:Passenger)->Passenger:
        return self.__passenger_repo.delete_passenger(passenger)
    
    def delete_passenger_by_index(self, index:int)->Passenger:
        return self.__passenger_repo.remove_passenger_by_index(index)
    
    
    # CRUD Plane
    def add_plane(self, plane:Plane)->Plane:
        self.__plane_repo.add_plane(plane)
        return plane
    
    def get_plane_list(self)->list[Plane]:
        return self.__plane_repo.get_plane_list()
    
    def get_plane_by_index(self, index:int)->Plane:
        return self.__plane_repo.get_plane_by_index(index)
 
    def get_index_by_plane(self, search_plane:Plane)->int:
        return self.__plane_repo.get_index_by_plane(search_plane)
    
    def get_index_by_planeID(self, planeID:str)->int:
        return self.__plane_repo.get_index_by_planeID(planeID)
    
    def get_plane_by_planeID(self, planeID:str)->Plane:
        return self.__plane_repo.get_plane_by_planeID(planeID)
    
    def update_plane(self, index:int, plane:Plane)->Plane:
        return self.__plane_repo.update_plane(index, plane)
    
    def delete_plane_by_index(self, index:int)->Plane:
        return self.__plane_repo.delete_plane_by_index(index)
    
    def delete_plane(self, plane:Plane)->Plane:
        return self.__plane_repo.delete_plane(plane)
    
    # Show remaining seats
    def show_remaining_seats(self, planeID:str)->int:
        plane = self.get_plane_by_planeID(planeID)
        passengers = self.get_passengers_by_planeID(planeID)
        return plane.get_number_of_seats() - len(passengers)
    

    def read_from_file(self, option):
        if option == "Passenger":
            self.__passenger_repo.read_from_file()
        elif option == "Plane":
            self.__plane_repo.read_from_file()
        
    def write_to_file(self, option):
        if option == "Passenger":
            self.__passenger_repo.write_to_file()
        elif option == "Plane":
            self.__plane_repo.write_to_file()

    

    

        

        



    

    

