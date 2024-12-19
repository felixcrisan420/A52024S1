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
    
    def update_passenger(self, index:int, new_passenger:Passenger)->Passenger:
        return self.__passenger_repo.update_passenger(index, new_passenger)
    
    def delete_passenger(self, passenger:Passenger)->Passenger:
        return self.__passenger_repo.delete_passenger(passenger)
    
    def delete_passenger_by_index(self, index:int)->Passenger:
        return self.__passenger_repo.remove_passenger_by_index(index)
    
    def write_to_file_passenger(self) -> bool:
        """
        Writes all vectors to a file.

        Args:
            file_path (str): The path of the file to write to.

        Returns:
            bool: True if the vectors were successfully written to the file.
        """
        import os
        local_file = "output/passenger_data.txt"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, local_file)
        with open(file_path, 'w') as file:
            for passenger in self.__passenger_repo.get_passenger_list():
                file.write(str(passenger) + "\n")
        return True
    
    def read_from_file_passenger(self) -> bool:
        """
        Reads all vectors from a file.

        Args:
            file_path (str): The path of the file to read from.

        Returns:
            bool: True if the vectors were successfully read from the file.
        """
        self.__passenger_repo.read_from_file()
    
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
    
    def write_to_file_plane(self) -> bool:
        """
        Writes all vectors to a file.

        Args:
            file_path (str): The path of the file to write to.

        Returns:
            bool: True if the vectors were successfully written to the file.
        """
        import os
        local_file = "output/plane_data.txt"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, local_file)
        with open(file_path, 'w') as file:
            for plane in self.__plane_repo.get_plane_list():
                file.write(str(plane) + "\n")
        return True
    
    def read_from_file_plane(self) -> bool:
        """
        Reads all vectors from a file.

        Args:
            file_path (str): The path of the file to read from.

        Returns:
            bool: True if the vectors were successfully read from the file.
        """
        self.__plane_repo.read_from_file()
    
    # Show remaining seats
    def show_remaining_seats(self, planeID:str)->int:
        plane = self.get_plane_by_planeID(planeID)
        passengers = self.get_passengers_by_planeID(planeID)
        return plane.get_number_of_seats() - len(passengers)

    # Methods for Passenger
    # 3 Sort Passengers by last name
    def sort_passengers_in_plane_by_last_name(self, planeID:str)->list[Passenger]:
        passenger_list = self.get_passengers_by_planeID(planeID)
        passenger_list.sort(key=lambda passenger: passenger.get_last_name())

        return passenger_list
    
    # Methods for Plane
    # 4 Sort planes according to the nimber of passenger
    def sort_planes_by_number_of_passengers(self)->list[Plane]:
        plane_list = self.get_plane_list()
        plane_list.sort(key=lambda plane: len(self.get_passengers_by_planeID(plane.get_planeID())))
        return plane_list
    
    # 5 Sort planes accordubg to the number of passengers witht the first name with given substring
    def sort_planes_by_number_of_passengers_and_first_name_given_substring(self, substring: str) -> list[Plane]:
        plane_list = self.get_plane_list()

        if len(plane_list) != 0:
            plane_list.sort(key=lambda plane: len(self.get_passengers_by_planeID(plane.get_planeID())))
            plane_list.sort(key=lambda plane: (
                len(self.get_passengers_by_planeID(plane.get_planeID())) > 0 and
                substring in self.get_passengers_by_planeID(plane.get_planeID())[0].get_first_name()
            ), reverse=True)

        return plane_list

    
    # 6 Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
    def sort_planes_by_number_of_passengers_and_destination(self)->list[Plane]:
        plane_list = self.get_plane_list()
        list_to_sort = []
        index = 0
        for plane in plane_list:
            string = str(len(self.get_passengers_by_planeID(plane.get_planeID()))) + plane.get_destination()
            list_to_sort.append((index, f"{string}"))

        list_to_sort.sort(key=lambda x: x[1])
        sorted_list = []
        for index, _ in list_to_sort:
            sorted_list.append(plane_list[index])

        return sorted_list
    
    # 7 Identify planes that have passengers with passport numbers starting with the same 3 letters
    def get_planes_with_passengers_with_passport_starting_with_same_3_letters(self)->list[Plane]:
        plane_list = self.get_plane_list()
        plane_list_with_passengers = []
        for plane in plane_list:
            passengers = self.get_passengers_by_planeID(plane.get_planeID())
            for passenger in passengers:
                if passenger.get_passportID()[:3] == passengers[0].get_passportID()[:3]:
                    plane_list_with_passengers.append(plane)
                    break

        return plane_list_with_passengers
    
    # 8 Identify passengers from a given plane for which the first name or last name contatin a string given as parameter
    def passenger_from_plane_having_first_or_last_name_like_string(self, planeID:str, string:str)->list[Passenger]:
        passenger_list = self.get_passengers_by_planeID(planeID)
        final_list = []
        for passenger in passenger_list:
            if passenger.get_first_name() == string or passenger.get_last_name() == string:
                final_list.append(passenger)

        return final_list
    
    # 9 Identify plane(s) where there is a passenger with a given name
    def get_planes_with_passenger_name(self, first_name:str, last_name:str)->list[Plane]:
        passenger_list = self.get_passenger_list()
        identified_plane_list = []
        for passenger in passenger_list:
            if passenger.get_first_name() == first_name and passenger.get_last_name() == last_name:
                identified_plane_list.append(self.get_plane_by_planeID(passenger.get_planeID()))

        return identified_plane_list
    
    #10 Form groups of [k] passengers from the same plane but with different last names
    def groups_of_passengers_from_same_plane(self, planeID: str, k: int) -> list:
        passenger_list = self.get_passengers_by_planeID(planeID)
        group_list = []
        
        # Backtracking on the solutions
        def backtrack(group, index):
            if len(group) == k:
                group_list.append(group.copy())
                return
            
            for i in range(index, len(passenger_list)):
                if len(group) == 0 or passenger_list[i].get_last_name() not in [p.get_last_name() for p in group]:
                    group.append(passenger_list[i])
                    backtrack(group, i + 1)
                    group.pop()

        backtrack([], 0)
        return group_list

    
    # 11  Form groups of [k] planes with the same destination but belonging to different airline companies
    def groups_of_planes_with_same_destination_different_airline(self, k: int) -> list:
        plane_list = self.get_plane_list()
        group_list = []

        # Backtracking on the solutions 
        def backtrack(group, index):
            # If we have found a group of k planes, add it to the result
            if len(group) == k:
                group_list.append(group.copy())  # Use group.copy() to avoid references
                return

            # Try adding planes starting from index
            for i in range(index, len(plane_list)):
                if len(group) == 0 or (plane_list[i].get_destination() == group[0].get_destination() and
                                        plane_list[i].get_airline_company() not in [p.get_airline_company() for p in group]):
                    group.append(plane_list[i])
                    backtrack(group, i + 1)
                    group.pop()

        backtrack([], 0)
        return group_list

    

    

        

        



    

    

