from domain.plane import Plane
from domain.passenger import Passenger
import os
import time

class Utilities:
    def __init__(self):
        pass

    @staticmethod
    def filter_data(data, filter_func=None):
        """
        Filter data based on a provided filter function.

        Args:
            data (list): The list of objects to be filtered.
            filter_func (callable, optional): A function to filter elements in the list.

        Returns:
            list: A filtered list of objects.
        """
        if filter_func:
            return [item for item in data if filter_func(item)]
        return data


    @staticmethod
    def sort_data(data, sort_key=None, order_func=None):
        """
        Sort data based on a provided sort key and a comparison function.

        Args:
            data (list): The list of objects to be sorted.
            sort_key (callable, optional): A function to extract a comparison key for sorting.
            order_func (callable, optional): A function that takes two arguments and returns True
                                            if the first argument should come before the second.

        Returns:
            list: A sorted list of objects.
        """
        if not sort_key or not order_func:
            return data

        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if not order_func(sort_key(data[j]), sort_key(data[j + 1])):
                    data[j], data[j + 1] = data[j + 1], data[j]

        return data
    
    @staticmethod 
    def generalized_backtracking(data, k, is_valid_group):
        """
        Generalized backtracking function to form groups based on constraints.

        Args:
            data (list): The list of items to group.
            k (int): The size of each group.
            is_valid_group (callable): A function that takes the current group and a new item
                                    and returns True if the item can be added to the group.

        Returns:
            list: A list of valid groups.
        """
        group_list = []

        def backtrack(group, index):
            if len(group) == k:
                group_list.append(group.copy())
                return

            for i in range(index, len(data)):
                if is_valid_group(group, data[i]):
                    group.append(data[i])
                    backtrack(group, i + 1)
                    group.pop()

        backtrack([], 0)
        return group_list
    
    @staticmethod
    def validate_inputs(data: dict, list_of_data=None):
        """Validate the input data based on the expected types and constraints.

        Args:
            data (dict): A dictionary of key-value pairs where the key is the name of the data
            list_of_data (list, optional): The list of data to validate against. Defaults to None.

        Raises:
            ValueError: Validation error due to constraints.
            TypeError: Validation error due to data type mismatch.
            IndexError: Validation error due to index out of range.
            TypeError: The key must be of type str
            ValueError: The key cannot be empty
        """
        for key, (value, expected_type) in data.items():
            if expected_type == "index":
                if list_of_data is None:
                    raise ValueError(f"{key} cannot be validated as an index because list_of_data is not provided")
                if not isinstance(value, int):
                    raise TypeError(f"{key} must be an integer for index validation")
                if value < 0 or value >= len(list_of_data):
                    raise IndexError(f"{key} is out of range")
            if isinstance(value, int):
                if value < 0:
                    raise ValueError(f"{key} cannot be negative")
            else:
                if not isinstance(value, expected_type):
                    raise TypeError(f"{key} must be of type {expected_type.__name__}")
                if expected_type == str and not value.strip():
                    raise ValueError(f"{key} cannot be empty")

          
    @staticmethod  
    def check_integer(integer:str)->bool:
        """Check if the input is an integer

        Args:
            integer (str): Input to check

        Returns:
            bool: True if the input is an integer, False otherwise
        """ 
        try:
            int(integer)
            return True
        except:
            print(f"{integer} must be int.")
            return False
        
    @staticmethod
    def check_existance(data:str, list_of_data:list)->bool:
        """Check if the data exists in the list of data

        Args:
            data (str): Data to check
            list_of_data (list): List of data to check against

        Returns:
            bool: True if the data exists in the list of data, False otherwise
        """
        if data not in list_of_data:
            print(f"{data} does not exist.")
            return False
        return True

class FileHandler:
    @staticmethod
    def read_from_file(file_name: str, obj_type: type):
        """
        Reads data from a file and dynamically creates objects of the specified type.
        
        Args:
            file_name (str): The name of the file to read from.
            obj_type (type): The type of object to create.
            
        Returns:
            list: A list of objects created from the file.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            Exception: If an error occurs while reading the file.
        """
        final_list = []
        # if I am in A5, just do not add it
        if os.getcwd().endswith("A5"):
            file_path = os.path.join(os.getcwd(), "repository", "output", file_name)
        else:
            file_path = os.path.join(os.getcwd(), "A5", "repository", "output", file_name)
        print(f"Read from {file_path}")
        time.sleep(1)
        try:
            with open(file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue  # Skip empty lines
                    
                    line_data = line.split(" ")

                    # Dynamically create an instance of obj_type
                    if obj_type == Passenger and len(line_data) == 4:
                        obj = Passenger(line_data[0], line_data[1], line_data[2], line_data[3])
                    elif obj_type == Plane and len(line_data) == 4:
                        obj = Plane(line_data[0], line_data[1], int(line_data[2]), line_data[3])
                    else:
                        raise ValueError(f"Invalid line format: {line}")
                    final_list.append(obj)
        
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error while reading file: {e}")

        return final_list
    
    @staticmethod
    def write_to_file(file_name, list_to_write:list):
        """Write data to a file.

        Args:
            file_name (str): The name of the file to write to.
            list_to_write (list): The list of objects to write to the file.
            
        Raises:
            Exception: If an error occurs while writing to the file.
        """
        import os
        cwd = os.getcwd()
        if os.getcwd().endswith("A5"):
            file_path = os.path.join(os.getcwd(), "repository", "output", file_name)
        else:
            file_path = os.path.join(os.getcwd(), "A5", "repository", "output", file_name)
        with open(file_path, "w") as file:
            pass  
        
        with open(file_path, "w") as file:
            for element in list_to_write:
                file.write(f"{element.__str__()}\n")
                
        print(f"Wrote to {file_path}")