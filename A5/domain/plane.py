class Plane:
    def __init__(self, planeID:str, airline_company:str, number_of_seats:int, destination:str):
        """
        Function that initializes a plane object

        Args:
            planeID (str: The plane's ID
            airline_company (str): The airline company that owns the plane
            number_of_seats (int): The number of seats on the plane
            destination (str): The plane's destination
        
        """
    
        self.__planeID = planeID
        self.__airline_company = airline_company
        self.__number_of_seats = number_of_seats
        self.__destination = destination

    # Getters   
    def get_planeID(self)->str|int:
        """
        Function that returns the plane ID

        Returns:
            str|int: The plane's ID
        """
        return self.__planeID
    
    def get_airline_company(self)->str:
        """
        Function that returns the airline company that owns the plane

        Returns:
            str: The airline company that owns the plane
        """
        return self.__airline_company
    
    def get_number_of_seats(self)->int:
        return self.__number_of_seats
    
    def get_destination(self)->str:
        return self.__destination
    
    # Setters
    def set_planeID(self, planeID:str|int)->str|int:
        self.__planeID = planeID
        return planeID
    
    def set_airline_company(self, airline_company:str)->str:
        self.__airline_company = airline_company
        return airline_company
    
    def set_number_of_seats(self, number_of_seats:int)->int:
        self.__number_of_seats = number_of_seats
        return number_of_seats
    
    def set_destination(self, destination:str)->str:
        self.__destination = destination
        return destination
    
    def __str__(self)->str:
        return f"{self.__planeID} {self.__airline_company} {self.__number_of_seats} {self.__destination}"
    
    def __repr__(self)->str:
        return f"{self.__planeID} {self.__airline_company} {self.__number_of_seats} {self.__destination}"
    
    def __eq__(self, other_plane)->bool:
        if self.__planeID == other_plane.get_planeID() and self.__airline_company == other_plane.get_airline_company() and self.__number_of_seats == other_plane.get_number_of_seats() and self.__destination == other_plane.get_destination():
            return True
        return False
    


