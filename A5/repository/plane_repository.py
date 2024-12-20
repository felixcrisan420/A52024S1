from domain.plane import Plane
from utils.utilities import FileHandler
from constants.const import Constants as const
import os

class PlaneRepository:
    def __init__(self):
        self.__plane_list = []
    
    # CRUD Operations for Plane
    # Create
    def add_plane(self, plane:Plane)->Plane:
        self.__plane_list.append(plane)
        return plane

    # Read
    def get_plane_list(self)->list[Plane]:
        return self.__plane_list
    
    def get_plane_by_index(self, index:int)->Plane:
        return self.__plane_list[index]
    
    def get_index_by_plane(self, search_plane:Plane)->int:
        index=0
        for plane in self.__plane_list:
            index += 1
            if plane==search_plane:
                return index
        if index == 0 or index == len(self.__plane_list):
            return -1
        
    def get_index_by_planeID(self, planeID:str)->int:
        index=0
        for plane in self.__plane_list:
            index += 1
            if plane.get_planeID() == planeID:
                return index
        if index == 0 or index == len(self.__plane_list):
            return -1
        
    def get_plane_by_planeID(self, planeID:str)->Plane:
        for plane in self.__plane_list:
            if plane.get_planeID() == planeID:
                return plane
        return Plane(0, "Does not exist", 0, "Does not exist")
    
    def get_passenger_list(self, planeID:str)->list:
        temp_list = []
        for plane in self.__plane_list:
            if plane.get_planeID() == planeID:
                temp_list.append(plane)
        return temp_list
        
    # Update
    def update_plane(self, index:int, plane:Plane)->Plane:
        self.__plane_list[index].set_planeID(plane.get_planeID())
        self.__plane_list[index].set_airline_company(plane.get_airline_company())
        self.__plane_list[index].set_number_of_seats(plane.get_number_of_seats())
        self.__plane_list[index].set_destination(plane.get_destination())
        return self.__plane_list[index]

    # Delete
    def delete_plane_by_index(self, index:int)->Plane:
        plane = self.__plane_list[index]
        del self.__plane_list[index]
        return plane
    
    def delete_plane_by_object(self, plane:Plane)->Plane:
        self.__plane_list.remove(plane)
        return plane
    
    def delete_plane(self, plane:Plane)->Plane:
        self.__plane_list.remove(plane)
        return plane
    
    def show_remaining_seats(self, planeID:str)->int:
        for plane in self.__plane_list:
            if plane.get_planeID() == planeID:
                return plane.get_number_of_seats() - len(self.get_passenger_list(planeID))
        return
    
    def read_from_file(self):
        for plane in FileHandler.read_from_file(const.FILE_NAME_PLANE, Plane):
            self.__plane_list.append(plane)
        return self.__plane_list
    
    def write_to_file(self):
        FileHandler.write_to_file(const.FILE_NAME_PLANE, self.__plane_list)
        return self.__plane_list
