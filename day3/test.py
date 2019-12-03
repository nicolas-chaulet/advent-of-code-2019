import unittest
from main import parse_path, segment, Wire

class TestWire(unittest.TestCase):
    def test_parse_path(self):
        path, _ = parse_path('R1,U1,L1,D1')
        self.assertEqual(path[0].A, [0,0])
        self.assertEqual(path[0].B, [1,0])
        self.assertEqual(path[-1].B, [0,1])
        self.assertEqual(path[-1].A, [0,0])
        self.assertEqual(len(path),4)


    def test_segment_intersection(self):
        sg1 = segment([0,0], [2,0])
        sg2 = segment([1,0], [1,2])
        self.assertEqual(sg1.intersect(sg2), (1,0))
        self.assertEqual(sg2.intersect(sg1), (1,0))

        sg3 = segment((10,0),(20,0))
        self.assertIsNone(sg1.intersect(sg3))

        sg1 = segment((0,0),(8,0))
        sg2 = segment((6,3),(6,7))
        self.assertIsNone(sg1.intersect(sg2))
        self.assertIsNone(sg2.intersect(sg1))

        sg1 = segment((0,0),(-8,0))
        sg2 = segment((-2,1),(-2,-7))
        self.assertEqual(sg1.intersect(sg2), (-2,0))
        self.assertEqual(sg2.intersect(sg1), (-2,0))

    def test_segment_contains(self):
        sg1 = segment((0,0),(-8,0))
        self.assertTrue(sg1.contains((-2,0)))
        self.assertFalse(sg1.contains((-2,1)))

        sg1 = segment((0,0),(0,10))
        self.assertFalse(sg1.contains((0,-20)))
        self.assertTrue(sg1.contains((0,1)))

    def test_wire_intersection(self):
        wire1 = Wire("R8,U5,L5,D3")
        wire2 = Wire("U7,R6,D4,L4")
        self.assertEqual(wire1.intersect(wire2)[0], [(0,0),(6,5),(3,3)])

    def test_solution(self):
        wire1 = Wire("R8,U5,L5,D3")
        wire2 = Wire("U7,R6,D4,L4")
        self.assertEqual(wire1.get_closest_intersection_distance(wire2), 6)

        wire1 = Wire("R75,D30,R83,U83,L12,D49,R71,U7,L72")
        wire2 = Wire("U62,R66,U55,R34,D71,R55,D58,R83")
        b = Board(wire1, wire2)
        self.assertEqual(wire1.get_closest_intersection_distance(wire2),159)

        wire1 = Wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
        wire2 = Wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
        self.assertEqual(wire1.get_closest_intersection_distance(wire2),135)

    def test_wire_distance_to_point(self):
        wire1 = Wire("R8,U5,L5,D3")
        self.assertEqual(wire1.distance_to_point((2,0)),2)
        self.assertEqual(wire1.distance_to_point((6,5)),15)

    def test_distance_to_point(self):
        wire1 = Wire("R8,U5,L5,D3")
        wire2 = Wire("U7,R6,D4,L4")
        intersections = wire1.intersect(wire2)

        lengths = []
        for intersection in intersections[1:]:
            lengths.append(wire1.distance_to_point(intersection) + wire2.distance_to_point(intersection))

        self.assertEqual(min(lengths),30)

        wire1 = Wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
        wire2 = Wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")

        intersections = wire1.intersect(wire2)

        lengths = []
        for intersection in intersections[1:]:
            lengths.append(wire1.distance_to_point(intersection) + wire2.distance_to_point(intersection))

        self.assertEqual(min(lengths),410)
        

if __name__ == "__main__":
    unittest.main()