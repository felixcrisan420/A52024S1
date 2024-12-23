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
        Getter for the plane ID

        Returns:
            str|int: The plane's ID
        """
        return self.__planeID
    
    def get_airline_company(self)->str:
        """
        Getter for the airline company that owns the plane

        Returns:
            str: The airline company that owns the plane
        """
        return self.__airline_company
    
    def get_number_of_seats(self)->int:
        """
        Getter for the number of seats on the plane

        Returns:
            int: The number of seats on the plane
        """
        return self.__number_of_seats
    
    def get_destination(self)->str:
        """
        Getter for the plane's destination

        Returns:
            str: The plane's destination
        """
        return self.__destination
    
    # Setters
    def set_planeID(self, planeID:str|int)->str|int:
        """
        Setter for the plane ID

        Args:
            planeID (str|int): The plane's ID
        
        Returns:
            str|int: The plane's ID
        """
        self.__planeID = planeID
        return planeID
    
    def set_airline_company(self, airline_company:str)->str:
        """
        Setter for the airline company that owns the plane

        Args:
            airline_company (str): The airline company that owns the plane

        Returns:
            str: The airline company that owns the plane
        """
        self.__airline_company = airline_company
        return airline_company
    
    def set_number_of_seats(self, number_of_seats:int)->int:
        """
        Setter for the number of seats on the plane

        Args:
            number_of_seats (int): The number of seats on the plane

        Returns:
            int: The number of seats on the plane
        """
        self.__number_of_seats = number_of_seats
        return number_of_seats
    
    def set_destination(self, destination:str)->str:
        """
        Setter for the plane's destination

        Args:
            destination (str): The plane's destination

        Returns:
            str: The plane's destination
        """
        self.__destination = destination
        return destination
    
    def __str__(self)->str:
        """
        String representation of the plane object

        Returns:
            str: The plane's ID, airline company, number of seats, and destination
        """
        return f"{self.__planeID} {self.__airline_company} {self.__number_of_seats} {self.__destination}"
    
    def __repr__(self)->str:
        """
        String representation of the plane object

        Returns:
            str: The plane's ID, airline company, number of seats, and destination
        """
        return f"{self.__planeID} {self.__airline_company} {self.__number_of_seats} {self.__destination}"
    
    def __eq__(self, other_plane:"Plane")->bool:
        """
        Equality function for the plane object

        Args:
            other_plane (Plane): The plane object to compare

        Returns:
            bool: True if the planes are equal, False otherwise
        """
        if isinstance(other_plane, Plane) == True:
            if self.__planeID == other_plane.get_planeID() and self.__airline_company == other_plane.get_airline_company() and self.__number_of_seats == other_plane.get_number_of_seats() and self.__destination == other_plane.get_destination():
                return True
        return False
    


