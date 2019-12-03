
def parse_path(path_string):
    vertices = [[0,0]]
    segments = []
    steps = path_string.split(',')
    for step in steps:
        delta = int(step[1:])
        x,y = vertices[-1]
        if step[0] == 'U':
            vertices.append([x,y+delta])
        if step[0] == 'D':
            vertices.append([x,y-delta])
        if step[0] == 'R':
            vertices.append([x+delta,y])
        if step[0] == 'L':
            vertices.append([x-delta,y])
        segments.append(segment(vertices[-2],vertices[-1]))
    return segments, vertices

class segment:
    HORIZONTAL = 'H'
    VERTICAL = 'V'

    def __init__(self,A,B):
        self._start = A
        if A > B:
            tmp = A
            A = B
            B = tmp
        self.A = A
        self.B = B
    
    def direction(self):
        if self.A[1] == self.B[1]:
            return segment.HORIZONTAL
        else:
            return segment.VERTICAL
    
    def intersect(self,other_segment):
        if other_segment.direction() == self.direction():
            if other_segment.direction() == self.VERTICAL and other_segment.A[0] == self.A[0]:
                print("WARNING")
                print(other_segment)
            if other_segment.direction() == self.HORIZONTAL and other_segment.A[1] == self.A[1]:
                print("WARNING")
                print(other_segment.A)
            return None
        if self.direction() == self.HORIZONTAL:
            if not (other_segment.A[0] >= self.A[0] and other_segment.A[0] <= self.B[0]):
                return None
            elif other_segment.A[1] <= self.A[1] and other_segment.B[1] >= self.A[1]:
                return (other_segment.A[0], self.A[1])
            else:
                return None
        else:
            return other_segment.intersect(self)

    def contains(self,point):
        inx = self.A[0] <= point[0] and point[0] <= self.B[0]
        if self.direction() == self.HORIZONTAL:
            return inx and self.A[1] == point[1]
        
        iny = self.A[1] <= point[1] and point[1] <= self.B[1]
        return iny and self.A[0] == point[0]
        
    def length(self):
        if self.direction() == self.HORIZONTAL:
            return self.B[0] - self.A[0]
        else:
            return self.B[1] - self.A[1]

    def distance_to(self, point):
        if self.direction() == self.HORIZONTAL:
            return abs(point[0] - self._start[0])
        return abs(point[1] - self._start[1])


class Wire:
    def __init__(self,path):
        self.segments, self.vertices = parse_path(path)

    def intersect(self,other_wire):
        intersection_points = []
        for segment in self.segments:
            for other_segment in other_wire.segments:
                intersection = other_segment.intersect(segment)
                if intersection:
                    intersection_points.append(intersection)

        return intersection_points  

    def get_closest_intersection_distance(self,other_wire):
        distances = []
        intersections = self.intersect(other_wire)
        for i in range(1, len(intersections)):
            distances.append(abs(intersections[i][0]) + abs(intersections[i][1]))
        return min(distances)

    def distance_to_point(self, point):
        distance = 0
        for seg in self.segments:
            if not seg.contains(point):
                distance += seg.length()
            else:
                distance += seg.distance_to(point)
                return distance
        return distance


if __name__ == "__main__":
    with open('input.txt','r') as f:
        wire1 = Wire(f.readline())
        wire2 = Wire(f.readline())
    intersections = wire1.intersect(wire2)
    print(intersections)
    lengths = []
    for intersection in intersections:
        lengths.append(wire1.distance_to_point(intersection) + wire2.distance_to_point(intersection))
    print(min(lengths))