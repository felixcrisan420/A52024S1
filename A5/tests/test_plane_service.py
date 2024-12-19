import unittest
from unittest.mock import MagicMock
from domain.plane import Plane
from service.plane_service import PlaneService
from repository.plane_repository import PlaneRepository


class TestPlaneService(unittest.TestCase):
    def setUp(self):
        self.mock_repository = MagicMock(spec=PlaneRepository)
        self.service = PlaneService(self.mock_repository)

    def test_add_plane(self):
        plane = Plane("P001", "AirlineX", 150, "DestinationA")
        self.mock_repository.add_plane.return_value = plane
        result = self.service.add_plane("P001", "AirlineX", 150, "DestinationA")
        self.assertEqual(result, plane)
        self.mock_repository.add_plane.assert_called_once()
        self.assertEqual(result.get_destination(), "DestinationA")

    def test_get_plane_list(self):
        plane_list = [Plane("P001", "AirlineX", 150, "DestinationA")]
        self.mock_repository.get_plane_list.return_value = plane_list
        result = self.service.get_plane_list()
        self.assertEqual(result, plane_list)
        self.mock_repository.get_plane_list.assert_called_once()
        self.assertEqual(len(result), 1)

    def test_get_plane_by_index(self):
        plane = Plane("P001", "AirlineX", 150, "DestinationA")
        self.mock_repository.get_plane_list.return_value = [plane]
        self.mock_repository.get_plane_by_index.return_value = plane
        result = self.service.get_plane_by_index(0)
        self.assertEqual(result, plane)
        self.mock_repository.get_plane_by_index.assert_called_with(0)
        self.assertEqual(result.get_airline_company(), "AirlineX")

    def test_get_index_by_plane(self):
        plane = Plane("P001", "AirlineX", 150, "DestinationA")
        self.mock_repository.get_index_by_plane.return_value = 0
        result = self.service.get_index_by_plane("P001", "AirlineX", 150, "DestinationA")
        self.assertEqual(result, 0)
        self.mock_repository.get_index_by_plane.assert_called_once()
        self.assertIsInstance(result, int)

    def test_get_index_by_planeID(self):
        self.mock_repository.get_index_by_planeID.return_value = 0
        result = self.service.get_index_by_planeID("P001")
        self.assertEqual(result, 0)
        self.mock_repository.get_index_by_planeID.assert_called_with("P001")
        self.assertIsInstance(result, int)

    def test_get_plane_by_planeID(self):
        plane = Plane("P001", "AirlineX", 150, "DestinationA")
        self.mock_repository.get_plane_by_planeID.return_value = plane
        result = self.service.get_plane_by_planeID("P001")
        self.assertEqual(result, plane)
        self.mock_repository.get_plane_by_planeID.assert_called_with("P001")
        self.assertEqual(result.get_number_of_seats(), 150)

    def test_update_plane(self):
        plane = Plane("P001", "AirlineX", 150, "DestinationA")
        self.mock_repository.get_plane_list.return_value = [plane]
        self.mock_repository.update_plane.return_value = plane
        result = self.service.update_plane(0, "P001", "AirlineY", 200, "DestinationB")
        self.assertEqual(result, plane)
        self.mock_repository.update_plane.assert_called_once()
        self.assertEqual(result.get_airline_company(), "AirlineX")

    def test_delete_plane_by_index(self):
        plane = Plane("P001", "AirlineX", 150, "DestinationA")
        self.mock_repository.get_plane_list.return_value = [plane]
        self.mock_repository.delete_plane_by_index.return_value = True

        result = self.service.delete_plane_by_index(0)

        self.assertTrue(result)
        self.mock_repository.delete_plane_by_index.assert_called_with(0)
        self.mock_repository.get_plane_list.assert_called_once()


    def test_delete_plane_by_object(self):
        # Arrange: Create a mock plane and set up the mock repository behavior
        plane = Plane("P001", "AirlineX", 150, "DestinationA")
        self.mock_repository.delete_plane.return_value = True

        # Act: Call delete_plane_by_object
        result = self.service.delete_plane_by_object("P001", "AirlineX", 150, "DestinationA")

        # Assert: Validate the result
        self.assertTrue(result)
        self.mock_repository.delete_plane.assert_called_once_with(plane)


    def test_show_remaining_seats(self):
        self.mock_repository.show_remaining_seats.return_value = 50
        result = self.service.show_remaining_seats("P001")
        self.assertEqual(result, 50)
        self.mock_repository.show_remaining_seats.assert_called_with("P001")
        self.assertGreaterEqual(result, 0)

    def test_read_from_file(self):
        self.mock_repository.read_from_file.return_value = True
        result = self.service.read_from_file()
        self.assertTrue(result)
        self.mock_repository.read_from_file.assert_called_once()
        self.assertIsInstance(result, bool)

    def test_write_to_file(self):
        self.mock_repository.write_to_file.return_value = True
        result = self.service.write_to_file()
        self.assertTrue(result)
        self.mock_repository.write_to_file.assert_called_once()
        self.assertIsInstance(result, bool)


if __name__ == "__main__":
    unittest.main()
