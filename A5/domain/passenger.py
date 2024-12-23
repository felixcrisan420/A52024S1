class Passenger:
    def __init__(self, first_name:str, last_name:str, passportID:str, planeID:str):
        """
        Function that initializes a passenger object

        Args:
            first_name(str): The first name of the passenger
            last_name(str): The last name of the passenger
            passportID(str): The passenger's passport ID number
            planeID(str|int): The plane ID that the passenger
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__passportID = passportID
        self.__planeID = planeID


    # Getters
    def get_first_name(self)->str:
        """
        Getter for the first name of the passenger

        Returns:
            str: The first name of the passenger
        """
        return self.__first_name
    
    def get_last_name(self)->str:
        """
        Getter for the last name of the passenger

        Returns:
            str: The last name of the
        """
        return self.__last_name
    
    def get_passportID(self)->str:
        """
        Getter for the passport ID of the passenger

        Returns:
            str: The passport ID of the passenger
        """
        return self.__passportID
    
    def get_planeID(self)->str|int:
        """
        Getter for the plane ID of the passenger

        Returns:
            str|int: The plane ID of the passenger
        """
        return self.__planeID
    
    # Setters
    def set_first_name(self, first_name:str)->str:
        """
        Setter for the first name of the passenger

        Args:
            first_name(str): The first name of the passenger

        Returns:
            str: The first name of the passenger
        """
        self.__first_name=first_name
        return first_name
    
    def set_last_name(self, last_name:str)->str:
        """
        Setter for the last name of the passenger

        Args:
            last_name(str): The last name of the passenger

        Returns:
            str: The last name of the passenger
        """
        self.__last_name=last_name
        return last_name
    
    def set_passportID(self, passportID: str)->str:
        """
        Setter for the passport ID of the passenger 

        Args:
            passportID(str): The passport ID of the passenger

        Returns:
            str: The passport ID of the passenger
        """
        self.__passportID = passportID
        return passportID
    
    def set_planeID(self, planeID:str|int)->str|int:
        """
        Setter for the plane ID of the passenger

        Args:
            planeID(str|int): The plane ID of the passenger

        Returns:
            str|int: The plane ID of the passenger
        """
        self.__planeID = planeID
        return planeID
    

    def __str__(self)->str:
        """
        String representation of the passenger object

        Returns:
            str: The string representation of the passenger object
        """
        return f"{self.__first_name} {self.__last_name} {self.__passportID} {self.__planeID}"
    
    def __repr__(self)->str:
        """
        Srt representation of the passenger object

        Returns:
            str: The string representation of the passenger object
        """
        return f"{self.__first_name} {self.__last_name} {self.__passportID} {self.__planeID}"
    
    def __eq__(self, other_passenger:"Passenger")->bool:
        """
        Equality function for the passenger object

        Args:
            other_passenger(Passenger): The passenger object to compare with

        Returns:
            bool: True if the passengers are equal, False otherwise
        """
        if isinstance(other_passenger, Passenger) == True:
            if self.__first_name == other_passenger.get_first_name() and self.__last_name == other_passenger.get_last_name() and self.__passportID == other_passenger.get_passportID():
                return True
        return False
    
    





