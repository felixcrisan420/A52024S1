from service.service import Service
from domain.plane import Plane
from domain.passenger import Passenger
from utils.utilities import Utilities

class Controller:
    def __init__(self, service: Service, utils: Utilities):
        self.__service = service
        self.__utils = utils

    # Methods for Passenger
    # 3 Sort Passengers by last name
    def sort_passengers_in_plane_by_last_name(self, planeID: str) -> list[Passenger]:
        passenger_list = self.__service.get_passengers_by_planeID(planeID)
        return self.__utils.sort_data(
            data=passenger_list,
            sort_key=lambda p: p.get_last_name(),
            order_func=lambda a, b: a <= b  # Ascending order
        )

    # 4 Sort planes according to the number of passengers
    def sort_planes_by_number_of_passengers(self) -> list[Plane]:
        plane_list = self.__service.get_plane_list()
        return self.__utils.sort_data(
            data=plane_list,
            sort_key=lambda plane: len(self.__service.get_passengers_by_planeID(plane.get_planeID())),
            order_func=lambda a, b: a >= b  # Descending order
        )

    # 5 Sort planes by the number of passengers with the first name containing a given substring
    def sort_planes_by_number_of_passengers_and_first_name_given_substring(self, substring: str) -> list[Plane]:
        plane_list = self.__service.get_plane_list()
        filtered_planes = self.__utils.filter_data(
            data=plane_list,
            filter_func=lambda plane: any(
                substring in passenger.get_first_name()
                for passenger in self.__service.get_passengers_by_planeID(plane.get_planeID())
            )
        )
        return self.__utils.sort_data(
            data=filtered_planes,
            sort_key=lambda plane: len(self.__service.get_passengers_by_planeID(plane.get_planeID())),
            order_func=lambda a, b: a >= b  # Descending order
        )

    # 6 Sort planes by concatenation of the number of passengers and the destination
    def sort_planes_by_number_of_passengers_and_destination(self) -> list[Plane]:
        plane_list = self.__service.get_plane_list()
        return self.__utils.sort_data(
            data=plane_list,
            sort_key=lambda plane: f"{len(self.__service.get_passengers_by_planeID(plane.get_planeID()))}{plane.get_destination()}",
            order_func=lambda a, b: a <= b  # Ascending order
        )

    # 7 Identify planes with passengers having passport numbers starting with the same 3 letters
    def get_planes_with_passengers_with_passport_starting_with_same_3_letters(self) -> list[Plane]:
        plane_list = self.__service.get_plane_list()
        return self.__utils.filter_data(
            data=plane_list,
            filter_func=lambda plane: len(set(
                passenger.get_passportID()[:3]
                for passenger in self.__service.get_passengers_by_planeID(plane.get_planeID())
            )) == 1
        )

    # 8 Identify passengers from a plane whose first or last name contains a given string
    def passenger_from_plane_having_first_or_last_name_like_string(self, planeID: str, string: str) -> list[Passenger]:
        passenger_list = self.__service.get_passengers_by_planeID(planeID)
        return self.__utils.filter_data(
            data=passenger_list,
            filter_func=lambda passenger: string in passenger.get_first_name() or string in passenger.get_last_name()
        )

    # 9 Identify planes where there is a passenger with a given name
    def get_planes_with_passenger_name(self, first_name: str, last_name: str) -> list[Plane]:
        plane_list = self.__service.get_plane_list()
        return self.__utils.filter_data(
            data=plane_list,
            filter_func=lambda plane: any(
                passenger.get_first_name() == first_name and passenger.get_last_name() == last_name
                for passenger in self.__service.get_passengers_by_planeID(plane.get_planeID())
            )
        )

    # 10 Form groups of [k] passengers from the same plane but with different last names
    def groups_of_passengers_from_same_plane(self, planeID: str, k: int) -> list:
        passenger_list = self.__service.get_passengers_by_planeID(planeID)
        return self.__utils.generalized_backtracking(
            data = passenger_list,
            k=k,
            is_valid_group=lambda group, passenger: len(group) == 0 or passenger.get_last_name() not in [p.get_last_name() for p in group]
        )

    # 11 Form groups of [k] planes with the same destination but belonging to different airline companies
    def groups_of_planes_with_same_destination_different_airline(self, k: int) -> list:
        plane_list = self.__service.get_plane_list()
        
        return self.__utils.generalized_backtracking(
            data=plane_list,
            k=k,
            is_valid_group=lambda group, plane: len(group) == 0 or plane.get_airline_company() not in [p.get_airline_company() for p in group]
        )

        
                
            
    