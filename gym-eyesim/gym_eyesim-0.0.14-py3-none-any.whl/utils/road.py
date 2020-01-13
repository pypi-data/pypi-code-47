import cv2
import numpy as np

from pathlib import Path
from scipy.interpolate import splprep, splev
from sklearn.cluster import DBSCAN

from .geometry import dist_between_points, dist_to_line, side_of_line, angle_between_vectors
from .coordinates import img_to_world


def binarize_img(img, thresh=127):
    """Create binary image from grayscale image.

    Args:
        img (array): grayscale image.
        thresh (int, optional): threshold for binarization.

    Returns:
        A binary image.
    """

    binary_img = np.zeros_like(img)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            value = img[y, x]
            if value > thresh:
                binary_img[y, x] = 255
    return binary_img


class RoadMark():
    def __init__(self, points):
        """Road mark

        Can be constructed from single point or list of points.

        Args:
            points (list or array): Point(s) belonging to this road mark
        """

        if points.ndim == 1:
            self.size = 1
            self.center = points
        else:
            self.size = len(points)
            self.center = np.mean(np.array(points), axis=0)


def detect_center_line(img):
    """Detect center line marks from binary image.

    Use DBSCAN to cluster points belonging to center line marks.

    Args:
        img (array): binary image of center line mark/non-center line mark points.

    Returns:
        A list of RoadMark objects.
    """

    # Find points belonding to center line marks
    road_mark_points = []
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            value = img[y, x]
            if value > 0:
                road_mark_points.append([y, x])

    # Convert to numpy array
    road_mark_points = np.array(road_mark_points)

    # Cluster points belonging to center line marks
    dbscan = DBSCAN(eps=4).fit(road_mark_points)
    labels = dbscan.labels_
    unique_labels = set(labels)
    core_samples_mask = np.zeros_like(labels, dtype=bool)
    core_samples_mask[dbscan.core_sample_indices_] = True

    # Accumulate center line marks
    center_line = []
    for label in unique_labels:
        if label == -1:
            continue
        class_member_mask = (label == labels)
        points = road_mark_points[class_member_mask & core_samples_mask]
        center_line.append(RoadMark(points))

    return center_line


def filter_center_line(center_line):
    """Filter center line marks by the number of points they contain to find road
    marks that form the center line.

    Args:
        center_line (list): list of center line marks.

    Returns:
        A list of filtered center line marks.
    """

    filtered_center_line = []
    for road_mark in center_line:
        if road_mark.size > 70 or road_mark.size < 30:
            continue

        filtered_center_line.append(road_mark)

    return filtered_center_line


def sort_center_line(center_line):
    """Sort center line marks

    Starting at the first center line mark find the closest one to it. If no center line mark
    is found in a small region check a larger region with angle constraint.

    Args:
        center_line (list): list of center line marks forming the center line.

    Returns:
        A list of sorted center line marks.
    """

    sorted_center_line = [center_line[0]]
    unused_center_line = center_line[1:]
    done = False

    while not done:
        index = None
        shortest_dist = 50
        for i, road_mark in enumerate(unused_center_line):
            dist = dist_between_points(
                sorted_center_line[-1].center,
                road_mark.center,
            )
            if dist < shortest_dist:
                shortest_dist = dist
                index = i

        if index is None:
            shortest_dist = 150
            max_angle = 25 / 180 * np.pi
            for i, road_mark in enumerate(unused_center_line):
                dist = dist_between_points(
                    sorted_center_line[-1].center,
                    road_mark.center,
                )
                v1 = sorted_center_line[-1].center - sorted_center_line[
                    -2].center
                v2 = road_mark.center - sorted_center_line[-1].center
                angle = abs(angle_between_vectors(v1, v2))
                if angle < max_angle:
                    if dist < shortest_dist:
                        shortest_dist = dist
                        index = i

        if index is not None:
            sorted_center_line.append(unused_center_line[index])
            del unused_center_line[index]
            # print(
            #     f"{sorted_center_line[-2].center} -> {sorted_center_line[-1].center}, {shortest_dist}"
            # )
        else:
            print(f"Remaining center line marks: {len(unused_center_line)}")
            break

        done = len(unused_center_line) == 0

    return sorted_center_line


def transform_center_line(center_line):
    for road_mark in center_line:
        road_mark.center = img_to_world(road_mark.center)

    return center_line


def fill_gaps(center_line, max_gap=300):
    """Fill gaps

    For each pair of center line marks insert additional center line marks in between if the
    distance between them is too large.

    Args:
        center_line (list): list of center line marks forming the center line.

    Returns:
        List of complete center line marks.
    """

    complete_center_line = []
    dist_to_next = np.linalg.norm(center_line[0].center -
                                  center_line[-1].center)

    # Fill gap
    n_missing = int(dist_to_next // max_gap)
    for n in range(n_missing):
        complete_center_line.append(
            RoadMark(center_line[-1].center +
                     (center_line[0].center - center_line[-1].center) *
                     (n + 1) / (n_missing + 1)))

    for i in range(len(center_line) - 1):
        dist_to_next = np.linalg.norm(center_line[i + 1].center -
                                      center_line[i].center)
        n_missing = int(dist_to_next // max_gap)
        complete_center_line.append(center_line[i])
        for n in range(n_missing):
            # print(
            #     center_line[i].center, center_line[i + 1].center,
            #     center_line[i].center +
            #     (center_line[i + 1].center - center_line[i].center) * (n + 1) /
            #     (n_missing + 1))
            complete_center_line.append(
                RoadMark(center_line[i].center +
                         (center_line[i + 1].center - center_line[i].center) *
                         (n + 1) / (n_missing + 1)))

    complete_center_line.append(center_line[-1])
    return complete_center_line


def smooth_center_line(center_line):
    """Interpolate splines to smooth road.

    Args:
        center_line (list): list of center line marks forming the center line.

    Returns:
        List of smoothed center line marks.
    """

    pts = np.array([road_mark.center for road_mark in center_line])
    tck, u = splprep(pts.T, u=None, s=0.0, per=1)
    u_new = np.linspace(u.min(), u.max(), 1000)
    x_new, y_new = splev(u_new, tck, der=0)
    return [RoadMark(np.array([x, y])) for x, y in zip(x_new, y_new)]


def determine_road_width(img, center_line):
    """Determine road width.

    Args:
        img (array): binary image of center line mark/non-center line mark points
        center_line (list): list of center line marks forming the center line.

    Returns:
        The average width of the road in pixel coordinates.
    """
    def _determine_road_witdh(p1, p2):
        """Nested function for road width.

        Calculates road width at the location of a pair of center line marks by going
        orthogonal to the direction until encountering a non-zero pixel.

        Args:
            p1 (array): center of first center line mark.
            p2 (array): center of second center line mark.

        Returns:
            The approximated road width at this point of the road.
        """

        average = (p1 + p2) / 2
        direction = (p2 - p1) / np.linalg.norm(p2 - p1)
        orthogonal = np.array([-direction[1], direction[0]])
        left_found = False
        right_found = False
        i = 1
        left_pixel = None
        right_pixel = None
        done = False
        while not done:
            if not left_found:
                left_pixel_pos = (np.rint(average +
                                          orthogonal * i)).astype(int)
                left_pixel = img[left_pixel_pos[0], left_pixel_pos[1]]
                if left_pixel > 0:
                    left_found = True

            if not right_found:
                right_pixel_pos = (np.rint(average -
                                           orthogonal * i)).astype(int)
                right_pixel = img[right_pixel_pos[0], right_pixel_pos[1]]
                if right_pixel > 0:
                    right_found = True

            done = left_found and right_found
            i += 1

        road_width = np.linalg.norm(left_pixel_pos - right_pixel_pos)
        return road_width

    road_widths = [
        _determine_road_witdh(
            center_line[-1].center,
            center_line[0].center,
        )
    ]

    for i in range(len(center_line) - 1):
        road_widths.append(
            _determine_road_witdh(
                center_line[i].center,
                center_line[i + 1].center,
            ))

    return sum(road_widths) / len(road_widths)


class Lane():
    def __init__(self, points):
        self.points = points

    def dist(self, point):
        """The distance of a point to the closest pair of neightboring lane marks of this lane.

        Args:
            point (array): point in world coordinates.

        Returns:
            The distance of a point to the closest pair of neightboring lane marks of this lane.
        """

        # Find closest lane mark
        index, _, _ = self.closest(point)

        # Compute distance to previous and next lane mark
        prev_index = (index - 1) % len(self.points)
        next_index = (index + 1) % len(self.points)
        shortest_dist = min(
            dist_to_line(
                self.points[prev_index].center,
                self.points[index].center,
                point,
            ),
            dist_to_line(
                self.points[index].center,
                self.points[next_index].center,
                point,
            ),
        )

        return shortest_dist

    def direction(self, point):
        # Find closest lane mark
        index, _, _ = self.closest(point)

        # Compute distance to previous and next lane mark
        prev_index = (index - 1) % len(self.points)
        next_index = (index + 1) % len(self.points)

        direction = self.points[next_index].center - self.points[
            prev_index].center
        return direction / np.linalg.norm(direction)

    def angle(self, point):
        direction = self.direction(point)
        return np.arctan2(direction[1], direction[0])

    def curvature(self, point):
        # Find closest lane mark
        first_index, _, _ = self.closest(point)

        # Sample two points ahead
        second_index = (first_index + 5) % len(self.points)
        third_index = (first_index + 10) % len(self.points)

        # Compute angle between edges connecting three points
        first_edge = self.points[
            second_index].center - self.points[first_index].center
        second_edge = self.points[
            third_index].center - self.points[second_index].center
        angle = angle_between_vectors(first_edge, second_edge)
        return angle

    def side(self, point):
        """Determine on which side of the road a point lies.

        Args:
            point (array): Point to check.

        Returns:
             A value larger than 0 if p3 is left of p1 and p2.
        """

        first_index, second_index = self.closest_pair(point)

        # Determine side of line
        return side_of_line(
            self.points[first_index].center,
            self.points[second_index].center,
            point,
        )

    def closest(self, point, granularity=20):
        """Find closest lane mark to given point.

        For performance reasons the search starts with low granularity to find
        an anchor and repeats with granularity 1 on the second run. Increased
        granularity may cause a wrong result.

        Args:
            point (array): Point to check.
            granularity (int): Granularity for first search iteration.

        Returns:
            Index, coordinate and distance of closest lane mark.
        """

        shortest_dist = None
        index = None
        for i in range(0, len(self.points), granularity):
            lane_point = self.points[i]
            dist = dist_between_points(lane_point.center, point)
            if index is None:
                shortest_dist = dist
                index = i
                continue

            if dist < shortest_dist:
                shortest_dist = dist
                index = i

        for i in range(index, index+granularity):
            lane_point = self.points[i]
            dist = dist_between_points(lane_point.center, point)
            if dist < shortest_dist:
                shortest_dist = dist
                index = i

        return index, self.points[i], shortest_dist

    def closest_pair(self, point):
        # Find closest lane mark
        first_index, _, _ = self.closest(point)

        # Find closest neighbor
        prev_index = (first_index - 1) % len(self.points)
        dist_to_prev = dist_between_points(
            self.points[prev_index].center,
            point,
        )
        next_index = (first_index + 1) % len(self.points)
        dist_to_next = dist_between_points(
            self.points[next_index].center,
            point,
        )
        second_index = prev_index if dist_to_prev < dist_to_next else next_index

        # Swap indices if second is smaller
        if second_index % len(self.points) < first_index % len(
                self.points):
            first_index, second_index = second_index, first_index

        return first_index, second_index

    def random_pose(self):
        """Generate a random pose on this lane.

        Returns:
            Tuple of position array and orientation.
        """

        first_index = np.random.randint(len(self.points))
        second_index = (first_index + 1) % len(self.points)
        first_position = self.points[first_index].center
        second_position = self.points[second_index].center
        scale = np.random.rand(1)
        direction = second_position - first_position
        position = first_position + scale * direction
        orientation = np.arctan2(direction[1], direction[0])
        return position, orientation


class Road():
    def __init__(self, width):
        """A road consists of two lanes.

        Args:
            width (float): Road width
        """

        self.width = width
        self.lanes = (Lane([]), Lane([]))

    def add_points_to_lanes(self, points):
        """Add tuple of points to lanes.

        Args:
            points (tuple): Two points to be added to lanes.
        """
        for i, lane in enumerate(self.lanes):
            lane.points.append(RoadMark(points[i]))


def create_lanes(center_line, road_width):
    """Create lanes from center line and road width

    Args:
        center_line (list): list of center line marks.
        road_width (float): width of road
    """
    def _create_lanes(p1, p2, p3):
        """Nested function for lane creation.

        Given three points compute the direction from previous to next.
        Add/subtract orthogonal lane shift to center points.

        Args:
            p1 (array): previous point
            p2 (array): current point
            p3 (array): next point

        Returns:
            Tuple of left and right lane point
        """

        direction = (p3 - p1) / np.linalg.norm(p3 - p1)
        orthogonal = np.array([-direction[1], direction[0]])
        lane_shift = road_width / 4 * orthogonal
        return p2 + lane_shift, p2 - lane_shift

    road = Road(road_width)
    for i in range(len(center_line)):
        lane_points = _create_lanes(
            center_line[(i - 1) % len(center_line)].center,
            center_line[i].center,
            center_line[(i + 1) % len(center_line)].center,
        )
        road.add_points_to_lanes(lane_points)

    # Invert lane 1
    road.lanes[1].points = road.lanes[1].points[::-1]

    return road


def detect_road(path_to_sim):
    path_to_floor_texture = Path(
        path_to_sim).parents[0] / "worlds" / "carolo.png"
    img = cv2.imread(str(path_to_floor_texture))

    # Convert to grayscale image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Rotate by 180 degree
    center = tuple(value / 2 for value in gray_img.shape)
    angle = 180
    scale = 1
    rot = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_img = cv2.warpAffine(gray_img, rot, gray_img.shape)

    # Create binary image (center line mark/non-center line mark)
    binary_img = binarize_img(rotated_img)

    # Detect center line marks
    center_line = detect_center_line(binary_img)

    # Filter center line marks
    filtered_center_line = filter_center_line(center_line)

    # Sort center line marks
    sorted_center_line = sort_center_line(filtered_center_line)

    # Determine road width
    road_width = determine_road_width(binary_img, sorted_center_line)
    road_width = img_to_world(road_width)

    # Transform to from image to world coordinates
    transformed_center_line = transform_center_line(sorted_center_line)

    # Fill gaps in road
    complete_center_line = fill_gaps(transformed_center_line)

    # Smooth road
    smoothed_center_line = smooth_center_line(complete_center_line)

    # Create lanes to form road
    road = create_lanes(smoothed_center_line, road_width)

    return road
