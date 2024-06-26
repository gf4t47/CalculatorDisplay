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
    TOP_RIGHT_TO_BOTTOM_MEDIAN = 8


position_map = {
    Position.TOP_X: lambda frame: (frame.left_top, frame.right_top),
    Position.MEDIAN_X: lambda frame: (frame.left_median, frame.right_median),
    Position.BOTTOM_X: lambda frame: (frame.left_bottom, frame.right_bottom),
    Position.LEFT_UP_Y: lambda frame: (frame.left_top, frame.left_median),
    Position.LEFT_DOWN_Y: lambda frame: (frame.left_median, frame.left_bottom),
    Position.RIGHT_UP_Y: lambda frame: (frame.right_top, frame.right_median),
    Position.RIGHT_DOWN_Y: lambda frame: (frame.right_median, frame.right_bottom),
    Position.TOP_RIGHT_TO_BOTTOM_MEDIAN: lambda frame: (frame.right_top, ((frame.left_bottom[0] + frame.right_bottom[0]) // 2, frame.left_bottom[1]))
}


class VirtualFrame:
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        """
        :param origin: frame coordinate
        :param width: width in x axle
        :param half_height: half of height in y axle
        """
        x, y = origin
        self._left_top = (x, y)
        self._left_median = (x, y + half_height)
        self._left_bottom = (x, y + half_height * 2)
        self._right_top = (x + width, y)
        self._right_median = (x + width, y + half_height)
        self._right_bottom = (x + width, y + half_height * 2)

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
        return self._right_bottom

    def create_line(self, position: Position)->Tuple[Tuple[int, int], Tuple[int, int]]:
        return position_map[position](self)
