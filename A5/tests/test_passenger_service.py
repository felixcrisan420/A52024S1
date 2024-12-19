import unittest
from unittest.mock import MagicMock
from domain.passenger import Passenger
from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository
from service.passenger_service import PassengerService


class TestPassengerService(unittest.TestCase):
    def setUp(self):
        self.mock_passenger_repo = MagicMock(spec=PassengerRepository)
        self.mock_plane_repo = MagicMock(spec=PlaneRepository)
        self.service = PassengerService(self.mock_passenger_repo, self.mock_plane_repo)

    def test_add_passenger(self):
        passenger = Passenger("John", "Doe", "P12345", "Plane001")
        self.mock_plane_repo.get_index_by_planeID.return_value = 0
        self.mock_passenger_repo.add_passenger.return_value = passenger

        result = self.service.add_passenger("John", "Doe", "P12345", "Plane001")

        self.assertEqual(result, passenger)
        self.mock_plane_repo.get_index_by_planeID.assert_called_with("Plane001")
        self.mock_passenger_repo.add_passenger.assert_called_once()

    def test_get_passenger_list(self):
        passengers = [Passenger("John", "Doe", "P12345", "Plane001")]
        self.mock_passenger_repo.get_passenger_list.return_value = passengers

        result = self.service.get_passenger_list()

        self.assertEqual(result, passengers)
        self.assertEqual(len(result), 1)
        self.mock_passenger_repo.get_passenger_list.assert_called_once()

    def test_get_passenger_by_index(self):
        passenger = Passenger("John", "Doe", "P12345", "Plane001")
        self.mock_passenger_repo.get_passenger_list.return_value = [passenger]
        self.mock_passenger_repo.get_passenger_by_index.return_value = passenger

        result = self.service.get_passenger_by_index(0)

        self.assertEqual(result, passenger)
        self.assertEqual(result.get_last_name(), "Doe")
        self.mock_passenger_repo.get_passenger_by_index.assert_called_once_with(0)

    def test_get_index_by_passenger(self):
        passenger = Passenger("John", "Doe", "P12345", "Plane001")
        self.mock_plane_repo.get_index_by_planeID.return_value = 0
        self.mock_passenger_repo.get_index_by_passenger.return_value = 0

        result = self.service.get_index_by_passenger("John", "Doe", "P12345", "Plane001")

        self.assertEqual(result, 0)
        self.mock_plane_repo.get_index_by_planeID.assert_called_with("Plane001")
        self.mock_passenger_repo.get_index_by_passenger.assert_called_once()

    def test_get_passengers_by_planeID(self):
        passengers = [Passenger("John", "Doe", "P12345", "Plane001")]
        self.mock_plane_repo.get_index_by_planeID.return_value = 0
        self.mock_passenger_repo.get_passengers_by_planeID.return_value = passengers

        result = self.service.get_passengers_by_planeID("Plane001")

        self.assertEqual(result, passengers)
        self.assertEqual(len(result), 1)
        self.mock_passenger_repo.get_passengers_by_planeID.assert_called_with("Plane001")

    def test_update_passenger(self):
        passenger = Passenger("John", "Doe", "P12345", "Plane001")
        self.mock_passenger_repo.get_passenger_list.return_value = [passenger]
        self.mock_passenger_repo.get_passenger_by_index.return_value = passenger
        self.mock_plane_repo.get_index_by_planeID.return_value = 0
        self.mock_passenger_repo.update_passenger.return_value = passenger

        result = self.service.update_passenger(0, "John", "Doe", "P12345", "Plane001")

        self.assertEqual(result, passenger)
        self.mock_passenger_repo.update_passenger.assert_called_once()
        self.mock_plane_repo.get_index_by_planeID.assert_called_with("Plane001")

    def test_delete_passenger_by_object(self):
        passenger = Passenger("John", "Doe", "P12345", "Plane001")
        self.mock_plane_repo.get_index_by_planeID.return_value = 0
        self.mock_passenger_repo.delete_passenger.return_value = True

        result = self.service.delete_passenger_by_object("John", "Doe", "P12345", "Plane001")

        self.assertTrue(result)
        self.mock_passenger_repo.delete_passenger.assert_called_once_with(passenger)
        self.mock_plane_repo.get_index_by_planeID.assert_called_with("Plane001")

    def test_delete_passenger_by_index(self):
        self.mock_passenger_repo.get_passenger_list.return_value = [Passenger("John", "Doe", "P12345", "Plane001")]
        self.mock_passenger_repo.delete_passenger_by_index.return_value = True

        result = self.service.delete_passenger_by_index(0)

        self.assertTrue(result)
        self.mock_passenger_repo.delete_passenger_by_index.assert_called_once_with(0)

    def test_read_from_file(self):
        self.mock_passenger_repo.read_from_file.return_value = True

        result = self.service.read_from_file()

        self.assertTrue(result)
        self.mock_passenger_repo.read_from_file.assert_called_once()

    def test_write_to_file(self):
        self.mock_passenger_repo.write_to_file.return_value = True

        result = self.service.write_to_file()

        self.assertTrue(result)
        self.mock_passenger_repo.write_to_file.assert_called_once()


if __name__ == "__main__":
    unittest.main()
