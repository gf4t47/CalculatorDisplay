from enum import Enum
from typing import Tuple


class Position(Enum):
    TOP_X = 1
    MEDIAN_X = 2
    BOTTOM_X = 3
    LEFT_UP_Y = 4
    LEFT_DOWN_Y = 5
    RIGHT_UP_Y = 6
    RIGHT_DOWN_Y = 7


position_map = {
    Position.TOP_X: lambda frame: (frame.left_top, frame.right_top),
    Position.MEDIAN_X: lambda frame: (frame.left_median, frame.right_median),
    Position.BOTTOM_X: lambda frame: (frame.left_bottom, frame.right_bottom),
    Position.LEFT_UP_Y: lambda frame: (frame.left_top, frame.left_median),
    Position.LEFT_DOWN_Y: lambda frame: (frame.left_median, frame.left_bottom),
    Position.RIGHT_UP_Y: lambda frame: (frame.right_top, frame.right_median),
    Position.RIGHT_DOWN_Y: lambda frame: (frame.right_median, frame.right_bottom),
}


class VirtualFrame:
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        """
        :param left_top: frame coordinate
        :param length: length in x axle
        :param half_height: half of height in y axle
        """
        x, y = left_top
        self._left_top = (x, y)
        self._left_median = (x, y + half_height)
        self._left_bottom = (x, y + half_height * 2)
        self._right_top = (x + length, y)
        self._right_median = (x + length, y + half_height)
        self._right_bottom = (x + length, y + half_height * 2)

    @property
    def left_top(self)->Tuple[int, int]:
        return self._left_top

    @property
    def left_median(self)->Tuple[int, int]:
        return self._left_median

    @property
    def left_bottom(self)->Tuple[int, int]:
        return self._left_bottom

    @property
    def right_top(self)->Tuple[int, int]:
        return self._right_top

    @property
    def right_median(self)->Tuple[int, int]:
        return self._right_median

    @property
    def right_bottom(self)->Tuple[int, int]:
        return self._left_bottom

    def create_line(self, position: Position)->Tuple[Tuple[int, int], Tuple[int, int]]:
        return position_map[position](self)
