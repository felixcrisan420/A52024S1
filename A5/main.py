from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository
from service.plane_service import PlaneService
from service.passenger_service import PassengerService
from UI.ui import CLI
from controller.controller import Controller

if __name__ == "__main__":
    plane_repository = PlaneRepository()
    passenger_repository = PassengerRepository()

    plane_service = PlaneService(plane_repository)
    passenger_service = PassengerService(passenger_repository, plane_repository)

    controller = Controller(plane_service, passenger_service)

    ui = CLI(passenger_service, plane_service, controller) 

    ui.run()
