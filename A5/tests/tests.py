import unittest
from service.service import Service
from domain.passenger import Passenger
from domain.plane import Plane
from repository.repository import Repository
from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository

class TestService(unittest.TestCase):
    def setUp(self):
        self.passenger_repo = PassengerRepository()
        self.plane_repo = PlaneRepository()
        self.repository = Repository(self.passenger_repo, self.plane_repo)
        self.service = Service(self.repository)

    def test_add_passenger(self):
        passenger = self.service.add_passenger("John", "Doe", "P123", "PL1")
        self.assertEqual(len(self.repository.get_passenger_list()), 1)
        self.assertEqual(self.repository.get_passenger_list()[0].get_first_name(), "John")
        self.assertEqual(self.repository.get_passenger_list()[0].get_last_name(), "Doe")

    def test_get_passenger_list(self):
        self.service.add_passenger("John", "Doe", "P123", "PL1")
        self.service.add_passenger("Jane", "Smith", "P124", "PL1")
        passengers = self.service.get_passenger_list()
        self.assertEqual(len(passengers), 2)
        self.assertEqual(passengers[0].get_passportID(), "P123")
        self.assertEqual(passengers[1].get_passportID(), "P124")

    def test_get_passenger_by_index(self):
        self.service.add_passenger("John", "Doe", "P123", "PL1")
        passenger = self.service.get_passenger_by_index(0)
        self.assertEqual(passenger.get_first_name(), "John")
        self.assertEqual(passenger.get_last_name(), "Doe")
        self.assertEqual(passenger.get_passportID(), "P123")

    def test_add_plane(self):
        plane = self.service.add_plane("PL1", "Delta", 150, "New York")
        self.assertEqual(len(self.repository.get_plane_list()), 1)
        self.assertEqual(self.repository.get_plane_list()[0].get_planeID(), "PL1")
        self.assertEqual(self.repository.get_plane_list()[0].get_airline_company(), "Delta")

    def test_get_plane_list(self):
        self.service.add_plane("PL1", "Delta", 150, "New York")
        self.service.add_plane("PL2", "United", 200, "Chicago")
        planes = self.service.get_plane_list()
        self.assertEqual(len(planes), 2)
        self.assertEqual(planes[0].get_destination(), "New York")
        self.assertEqual(planes[1].get_destination(), "Chicago")

    def test_delete_passenger_by_index(self):
        self.service.add_passenger("John", "Doe", "P123", "PL1")
        self.service.add_passenger("Jane", "Smith", "P124", "PL1")
        self.service.delete_passenger_by_index(0)
        self.assertEqual(len(self.repository.get_passenger_list()), 1)
        self.assertEqual(self.repository.get_passenger_list()[0].get_passportID(), "P124")

    def test_delete_plane_by_index(self):
        self.service.add_plane("PL1", "Delta", 150, "New York")
        self.service.add_plane("PL2", "United", 200, "Chicago")
        self.service.delete_plane_by_index(0)
        self.assertEqual(len(self.repository.get_plane_list()), 1)
        self.assertEqual(self.repository.get_plane_list()[0].get_planeID(), "PL2")

    def test_show_remaining_seats(self):
        self.service.add_plane("PL1", "Delta", 150, "New York")
        seats = self.service.show_remaining_seats("PL1")
        self.assertEqual(seats, 150)

    def test_sort_passengers_in_plane_by_last_name(self):
        self.service.add_passenger("John", "Doe", "P123", "PL1")
        self.service.add_passenger("Jane", "Smith", "P124", "PL1")
        sorted_passengers = self.service.sort_passengers_in_plane_by_last_name("PL1")
        self.assertEqual(sorted_passengers[0].get_last_name(), "Doe")
        self.assertEqual(sorted_passengers[1].get_last_name(), "Smith")
        self.assertEqual(len(sorted_passengers), 2)

    def test_sort_planes_by_number_of_passengers(self):
        self.service.add_plane("PL1", "Delta", 150, "New York")
        self.service.add_plane("PL2", "United", 200, "Chicago")
        self.service.add_passenger("John", "Doe", "P123", "PL1")
        self.service.add_passenger("Jane", "Smith", "P124", "PL1")
        sorted_planes = self.service.sort_planes_by_number_of_passengers()
        self.assertEqual(sorted_planes[0].get_planeID(), "PL2")
        self.assertEqual(sorted_planes[1].get_planeID(), "PL1")
        self.assertEqual(len(sorted_planes), 2)

    def test_sort_planes_by_number_of_passengers_and_first_name_given_substring(self):
        self.service.add_plane("PL1", "Delta", 150, "New York")
        self.service.add_plane("PL2", "United", 200, "Chicago")
        self.service.add_passenger("John", "Doe", "P123", "PL1")
        self.service.add_passenger("Jake", "Smith", "P124", "PL1")
        sorted_planes = self.service.sort_planes_by_number_of_passengers_and_first_name_given_substring("Jake")
        self.assertEqual(sorted_planes[0].get_planeID(), "PL2")
        self.assertEqual(len(sorted_planes), 2)
        self.assertNotEqual(sorted_planes[0].get_airline_company(), "Delta")

    def test_sort_planes_by_number_of_passengers_and_destination(self):
        self.service.add_plane("PL1", "Delta", 150, "New York")
        self.service.add_plane("PL2", "United", 200, "Chicago")
        self.service.add_passenger("John", "Doe", "P123", "PL1")
        sorted_planes = self.service.sort_planes_by_number_of_passengers_and_destination()
        self.assertEqual(sorted_planes[0].get_destination(), "New York")
        self.assertEqual(len(sorted_planes), 2)

    def test_groups_of_passengers_from_same_plane(self):
        self.service.add_passenger("John", "Doe", "P123", "PL1")
        self.service.add_passenger("Jane", "Smith", "P124", "PL1")
        groups = self.service.groups_of_passengers_from_same_plane("PL1", 1)
        self.assertEqual(len(groups), 2)
        self.assertEqual(groups[0][0].get_first_name(), "John")
        self.assertEqual(groups[1][0].get_first_name(), "Jane")

    def test_groups_of_planes_with_same_destination_different_airline(self):
        self.service.add_plane("PL1", "Delta", 150, "New York")
        self.service.add_plane("PL2", "United", 200, "New York")
        groups = self.service.groups_of_planes_with_same_destination_different_airline(1)
        self.assertEqual(len(groups), 2)
        self.assertEqual(groups[0][0].get_planeID(), "PL1")
        self.assertEqual(groups[1][0].get_planeID(), "PL2")

if __name__ == "__main__":
    unittest.main()
