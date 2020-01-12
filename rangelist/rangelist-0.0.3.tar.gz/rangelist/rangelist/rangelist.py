from __future__ import absolute_import, unicode_literals

from .point import Point, NEG_INF, INF
from .rangeitem import RangeItem


class RangeList(object):
    _items = []

    def __init__(self, items=None):
        if items is None:
            self._items = []
        else:
            for range_item in items or dict():
                assert isinstance(range_item, RangeItem)
                self.insert(range_item)

    def items(self):
        return self._items

    def __eq__(self, other):
        return frozenset(self.items()) == frozenset(other.items())

    def __len__(self):
        return len(self._items)

    def _find_ranges_with_point(self, point, ignore_excluded_bounds=False):
        for range_item in self._items:
            if ignore_excluded_bounds and range_item.left_bound > point:
                break
            if not ignore_excluded_bounds:
                if range_item.left_excluded and range_item.left_bound >= point:
                    break
                if not range_item.left_excluded and range_item.left_bound > point:
                    break
            if ignore_excluded_bounds:
                if range_item.left_bound <= point <= range_item.right_bound:
                    yield range_item
            elif point in range_item:
                yield range_item
            continue

    def _insert_point(self, point):
        assert point not in [INF, NEG_INF]
        existing_ranges = sorted(
            list(self._find_ranges_with_point(point, ignore_excluded_bounds=True)))
        if len(existing_ranges) == 2:
            # combine the two range_items
            left_range, right_range = existing_ranges
            left_range.right_bound = right_range.right_bound
            left_range.right_excluded = right_range.right_excluded
            self._items.remove(right_range)
        elif len(existing_ranges) == 1:
            range_item = existing_ranges[0]
            if range_item.left_bound == point and range_item.left_excluded:
                range_item.left_excluded = False
                # check situation if there's adjacent left-bound range
            elif range_item.right_bound == point and range_item.right_excluded:
                range_item.right_excluded = False
        else:
            self.insert(RangeItem(point, point))

    def _insert_item(self, item_to_insert):
        if not self._items:
            self._items.append(item_to_insert)
            return

        new_ranges = []

        for pos, current_item in enumerate(self._items):
            # item_to_insert is left to current item
            if item_to_insert < current_item:
                if current_item.left_bound == item_to_insert.right_bound:
                    # we need to make sure that if 2 items are adjacent, and one
                    # has excluded boundary - other's boundary should be excluded too
                    if current_item.left_excluded:
                        item_to_insert.right_excluded = True
                    if item_to_insert.right_excluded:
                        current_item.left_excluded = True
                new_ranges.append(item_to_insert)
                new_ranges.append(current_item)
                break

            # item_to_insert is right to current item
            if item_to_insert > current_item:
                # if it's the last item - just insert it to the right
                if pos == len(self._items) - 1:
                    if current_item.right_bound == item_to_insert.left_bound:
                        # we need to make sure that if 2 items are adjacent, and one
                        # has excluded boundary - other's boundary should be excluded too
                        if current_item.right_excluded:
                            item_to_insert.left_excluded = True
                        if item_to_insert.left_excluded:
                            current_item.right_excluded = True
                    new_ranges.append(current_item)
                    new_ranges.append(item_to_insert)
                    break
                # it's not the last item, so skip it and check the next one
                new_ranges.append(current_item)
                continue

            # item is identical to the one we already have; nothing to do here
            if item_to_insert == current_item:
                new_ranges.append(current_item)
                break

            # item_to_insert is inside current item
            if item_to_insert in current_item:
                points_to_split = []
                if item_to_insert.left_excluded:
                    points_to_split.append(item_to_insert.left_bound)
                if item_to_insert.right_excluded:
                    points_to_split.append(item_to_insert.right_bound)
                for item_to_insert in current_item.split_with_points(points_to_split):
                    new_ranges.append(item_to_insert)
                break

            # item_to_insert contains current item
            if current_item in item_to_insert:
                points_to_split = []
                if current_item.left_excluded:
                    points_to_split.append(current_item.left_bound)
                if current_item.right_excluded:
                    points_to_split.append(current_item.right_bound)
                items_to_insert = item_to_insert.split_with_points(points_to_split)
                for item in items_to_insert[0:-1]:
                    new_ranges.append(item)
                item_to_insert = items_to_insert[-1]

                # it it was the last item in list - then insert item,
                # otherwise continue to the end of the list
                if pos == len(self._items) - 1:
                    new_ranges.append(item_to_insert)
                    break
                continue

            if item_to_insert.intersects_with(current_item):
                points_to_split = []
                if item_to_insert.left_bound < current_item.left_bound:
                    # we already know, that current item is not IN item_to_insert
                    # hence, it's right bound is less
                    if item_to_insert.right_excluded:
                        points_to_split.append(item_to_insert.right_bound)
                    if current_item.left_excluded:
                        points_to_split.append(current_item.left_bound)
                    item_to_insert.right_bound = current_item.right_bound
                    item_to_insert.right_excluded = current_item.right_excluded
                else:
                    # the range we're inserting intersects and continues to the right
                    # after the current range. There's a possibility that it spans over other items,
                    # too
                    if item_to_insert.left_excluded:
                        points_to_split.append(item_to_insert.left_bound)
                    if current_item.right_excluded:
                        points_to_split.append(current_item.right_bound)
                    item_to_insert.left_bound = current_item.left_bound
                    item_to_insert.left_excluded = current_item.left_excluded
                items_to_insert = sorted(item_to_insert.split_with_points(points_to_split))
                if len(items_to_insert) > 1:
                    for item_to_insert in items_to_insert[0:-1]:
                        new_ranges.append(item_to_insert)
                item_to_insert = items_to_insert[-1]
                if pos == len(self._items) - 1:
                    new_ranges.append(item_to_insert)
                else:
                    continue
                break

        if pos + 1 <= len(self._items) - 1:
            new_ranges.extend(self._items[pos + 1:])

        self._items = new_ranges

    def insert(self, range_item_or_point):
        if not isinstance(range_item_or_point, RangeItem):
            range_item_or_point = Point(range_item_or_point)
        if isinstance(range_item_or_point, RangeItem):
            self._insert_item(range_item_or_point)
        else:
            self._insert_point(range_item_or_point)

    def extend(self, other):
        assert isinstance(other, RangeList)
        for range_item in other:
            self.insert(range_item)

    def __repr__(self):
        return str([range_item.__repr__() for range_item in self._items])

    def __contains__(self, item):
        if not isinstance(item, (RangeItem, Point)):
            item = Point(item)
        if not self._items:
            return False
        if isinstance(item, Point):
            # item is point
            ranges = self._find_ranges_with_point(item)
            for a in ranges:
                return True
            return False

        # item is range
        for current_range in self._items:
            if item > current_range:
                continue
            if item == current_range or item in current_range:
                return True
            if item > current_range:
                return False
        return False
