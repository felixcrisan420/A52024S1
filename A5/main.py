from repository.repository import Repository
from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository
from service.service import Service
from UI.ui import UI
from controller.controller import Controller
import subprocess
import os

if __name__ == "__main__":
    plane_repo = PlaneRepository()
    passenger_repo = PassengerRepository()
    ui = UI()
    repo = Repository(passenger_repo, plane_repo)
    service = Service(repo)
    controller = Controller(service, ui)
    
    controller.run()