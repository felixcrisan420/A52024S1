# A5 - UBB AI, 1011, Felix Crisan, cfai0070

## Description
This project is part of the coursework for AI at UBB. It focuses on the development of a system for managing passengers and planes, with functionality for CRUD operations, sorting, and advanced queries.

The project demonstrates key concepts in Python programming, including object-oriented design, modularity, and testing.

## Project Structure
```
A5 - UBB AI
├── domain/
│   ├── __init__.py
│   ├── passenger.py
│   ├── plane.py
├── repository/
│   ├── __init__.py
│   ├── repository.py
│   ├── passenger_repository.py
│   ├── plane_repository.py
├── service/
│   ├── __init__.py
│   ├── service.py
├── tests/
│   ├── __init__.py
│   ├── test_service.py
├── main.py
├── pyproject.toml
├── README.md
```

### **Modules**
- `domain/`: Contains classes for the core objects (`Passenger`, `Plane`).
- `repository/`: Handles data persistence and CRUD operations for passengers and planes.
- `service/`: Provides business logic and higher-level operations.
- `tests/`: Contains test cases for validating the functionality of the project.

## Features
- **CRUD Operations**: 
  - Add, update, delete passengers and planes.
- **Sorting**:
  - Sort planes by number of passengers.
  - Sort passengers by last name.
- **Advanced Queries**:
  - Find planes with passengers matching specific conditions.
  - Group passengers or planes by various criteria.
- **Testing**:
  - Comprehensive test suite using `unittest`.

## Requirements
- Python 3.10+
- Required dependencies are listed in `pyproject.toml`:
  - `pytest`
  - `unittest`
  - `numpy`
  - `pandas`
  - `setuptools`
  - `wheel`

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd A5-UBB-AI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the `PYTHONPATH` is set to the project root.
   ```bash
   export PYTHONPATH=.
   ```

## Running the Project
1. To execute the main script:
   ```bash
   python main.py
   ```
2. To run tests:
   ```bash
   python -m unittest discover
   ```
   Or, if using `pytest`:
   ```bash
   pytest tests/
   ```

## Author
Felix Crisan  
Email: [felix.crisan1@stud.ubbcluj.ro](mailto:felix.crisan1@stud.ubbcluj.ro)

## License
This project is licensed under the MIT License.

