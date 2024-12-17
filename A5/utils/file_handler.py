import os
from domain.passenger import Passenger
from domain.plane import Plane

class FileHandler:
    @staticmethod
    def read_from_file(file_name: str, obj_type: type):
        """
        Reads data from a file and dynamically creates objects of the specified type.
        
        :param file_name: Name of the file to read from.
        :param obj_type: Class type to construct (e.g., Passenger or Plane).
        :return: List of objects of the specified type.
        """
        final_list = []
        file_path = os.path.join(os.getcwd(), "A5", "repository", "output", file_name)

        try:
            with open(file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue  # Skip empty lines
                    
                    line_data = line.split(" ")

                    # Dynamically create an instance of obj_type
                    if obj_type == Passenger and len(line_data) == 4:
                        obj = obj_type(line_data[0], line_data[1], line_data[2], line_data[3])
                    elif obj_type == Plane and len(line_data) == 4:
                        obj = obj_type(line_data[0], line_data[1], int(line_data[2]), line_data[3])
                    else:
                        raise ValueError(f"Invalid line format: {line}")
                    
                    final_list.append(obj)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error while reading file: {e}")

        return final_list
    
    @staticmethod
    def write_to_file(list_to_write, file_name):
        import os
        cwd = os.getcwd()
        # Clear the file by opening it in write mode ('w')
        with open(f"{cwd}/A5/repository/output/{file_name}", "w") as file:
            pass  # Simply open and close the file to clear its contents
        
        # Open the file in write mode ('w') to overwrite it completely
        with open(f"{cwd}/A5/repository/output/{file_name}.txt", "w") as file:
            for element in list_to_write:
                file.write(f"{element.__str__()}\n")
