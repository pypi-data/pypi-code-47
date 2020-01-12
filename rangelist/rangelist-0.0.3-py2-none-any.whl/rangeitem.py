from __future__ import absolute_import, unicode_literals

from copy import copy
from .point import Point, NEG_INF, INF


class RangeItem(object):
    def __init__(self, left_bound, right_bound, left_excluded=False, right_excluded=False):
        if not isinstance(left_bound, Point):
            left_bound = Point(left_bound)
        if not isinstance(right_bound, Point):
            right_bound = Point(right_bound)
        assert isinstance(left_bound, Point)
        assert isinstance(right_bound, Point)
        assert left_bound < right_bound or left_bound == right_bound
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.left_excluded = left_excluded if left_bound != NEG_INF else False
        self.right_excluded = right_excluded if right_bound != INF else False

    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        return (
            other.left_bound == self.left_bound and
            other.right_bound == self.right_bound and
            other.left_excluded == self.left_excluded and
            other.right_excluded == self.right_excluded
        )

    def __lt__(self, other):
        if not isinstance(other, (Point, RangeItem)):
            other = Point(other)
        assert isinstance(other, (Point, RangeItem))
        if self.right_bound == INF:
            return False
        if isinstance(other, RangeItem) and other.left_bound == NEG_INF:
            return False
        if isinstance(other, RangeItem):
            if other.left_excluded or self.right_excluded:
                return self.right_bound <= other.left_bound
            return self.right_bound < other.left_bound
        return (
            other > self.right_bound and not self.right_excluded or
            other >= self.right_bound and self.right_excluded
        )

    def __le__(self, other):
        if not isinstance(other, Point):
            other = Point(other)
        return self < other or other in self

    def __ge__(self, other):
        if not isinstance(other, Point):
            other = Point(other)
        return self > other or other in self

    def __gt__(self, other):
        if not isinstance(other, (Point, RangeItem)):
            other = Point(other)
        assert isinstance(other, (Point, RangeItem))
        if self.left_bound == NEG_INF:
            return False
        if isinstance(other, RangeItem):
            if other.right_excluded or self.left_excluded:
                return self.left_bound >= other.right_bound
            return self.left_bound > other.right_bound
        return (
            other < self.left_bound and not self.left_excluded or
            other <= self.left_bound and self.left_excluded
        )

    def __contains__(self, item):
        if not isinstance(item, (Point, RangeItem)):
            item = Point(item)
        assert isinstance(item, (Point, RangeItem))
        if isinstance(item, RangeItem):
            is_greater_than_left_bound = (
                self.left_bound == NEG_INF or
                item.left_bound != NEG_INF and (
                    self.left_excluded and (
                        item.left_bound > self.left_bound or
                        item.left_excluded and item.left_bound >= self.left_bound
                    ) or not self.left_excluded and (
                        item.left_bound >= self.left_bound or
                        item.left_excluded and item.left_bound >= self.left_bound
                    )
                )
            )
            is_less_than_right_bound = (
                self.right_bound == INF or
                item.right_bound != INF and (
                    self.right_excluded and item.right_bound < self.right_bound or
                    (self.right_excluded and item.right_excluded and
                     item.right_bound <= self.right_bound) or
                    not self.right_excluded and item.right_bound <= self.right_bound or
                    (not self.right_excluded and item.right_excluded and
                     item.right_bound <= self.right_bound)
                )
            )
        else:
            if item in (INF, NEG_INF, ):
                return item in (self.left_bound, self.right_bound, )
            is_greater_than_left_bound = (
                self.left_bound == NEG_INF or
                self.left_excluded and item > self.left_bound or
                not self.left_excluded and item >= self.left_bound
            )
            is_less_than_right_bound = (
                self.right_bound == INF or
                self.right_excluded and item < self.right_bound or
                not self.right_excluded and item <= self.right_bound
            )
        return is_greater_than_left_bound and is_less_than_right_bound

    def __copy__(self):
        return RangeItem(
            left_bound=self.left_bound, right_bound=self.right_bound,
            left_excluded=self.left_excluded, right_excluded=self.right_excluded
        )

    def __repr__(self):
        left_bound_bracket = '(' if self.left_excluded else '['
        right_bound_bracket = ')' if self.right_excluded else ']'
        return '{0}{1}, {2}{3}'.format(
            left_bound_bracket, self.left_bound, self.right_bound, right_bound_bracket)

    def __add__(self, other):
        if other in self:
            return self
        if self in other:
            return copy(other)
        assert (
            self.right_bound in other or self.left_bound in other
        ), 'Intervals must have an intersection to be added'
        if self.left_bound in other:
            return RangeItem(
               other.left_bound, self.right_bound, left_excluded=other.left_excluded,
               right_excluded=self.right_excluded
            )
        return RangeItem(
            self.left_bound, other.right_bound, left_excluded=self.left_excluded,
            right_excluded=other.right_excluded
        )

    def intersects_with(self, other):
        if other in self or self in other:
            return True
        if not other.left_excluded and other.left_bound in self:
            return True
        if not other.right_excluded and other.right_bound in self:
            return True
        if (other.left_excluded or self.right_excluded) and other.left_bound == self.right_bound:
            return False
        if (other.right_excluded or self.left_excluded) and other.right_bound == self.left_bound:
            return False
        return other.left_bound in self or other.right_bound in self

    def split_with_points(self, points_list=None):
        if points_list is None:
            return [self, ]
        points_list = sorted(points_list)
        new_items = []
        unsplit = self
        for point in points_list:
            if point == unsplit.left_bound:
                unsplit.left_excluded = True
                continue
            if point == unsplit.right_bound:
                unsplit.right_excluded = True
                continue
            if point in [NEG_INF, INF]:
                continue
            left_side, right_side = unsplit.split_with_point(point, True)
            new_items.append(left_side)
            unsplit = right_side
        new_items.append(unsplit)
        return new_items

    def split_with_point(self, point, point_excluded=False):
        if not isinstance(point, Point):
            point = Point(point)
        assert point in self
        assert self.left_bound == NEG_INF or self.left_bound != point
        assert self.right_bound == INF or self.right_bound != point
        return (
            RangeItem(
                left_bound=self.left_bound, right_bound=point,
                left_excluded=self.left_excluded, right_excluded=point_excluded),
            RangeItem(
                left_bound=point, right_bound=self.right_bound,
                left_excluded=point_excluded, right_excluded=self.right_excluded)
        )
