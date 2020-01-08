import unittest
from helpers import haversine_distance


class TestCalculateHaversineDistance(unittest.TestCase):

    def test_all_files_in_directory(self):
        from_latitude = [47.6062]
        from_longitude = [122.3321]
        to_latitude = [47.5301]
        to_longitude = [122.0326]

        distance = haversine_distance.calculate_haversine_distance(from_latitude,
                                                                   from_longitude,
                                                                   to_latitude,
                                                                   to_longitude)
        self.assertEqual(17.5, round(distance[0], 1))


if __name__ == '__main__':
    unittest.main()
