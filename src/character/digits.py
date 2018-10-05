from typing import List, Tuple

from src.character.frame import VirtualFrame, Position


class Digit(VirtualFrame):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._width = width
        self._height = half_height * 2
        self._lines = []

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def lines(self) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        return self._lines


class Zero(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int, decorated: bool):
        super().__init__(origin, width, half_height)
        raw_lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.LEFT_DOWN_Y),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]
        self._lines = self.decorate(raw_lines) if decorated else raw_lines

    def decorate(self, lines: List[Tuple[Tuple[int, int], Tuple[int, int]]])-> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        width = (self.width - self.width // 24) // 2
        height = self.height // 24
        lines.append(((self.left_median[0] + width, self.left_median[1] - height), (self.right_median[0] - width, self.right_median[1] + height)))
        return lines


class One(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int, decorated: bool):
        super().__init__(origin, width, half_height)
        raw_lines = [
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.LEFT_DOWN_Y),
        ]
        self._lines = self.decorate(raw_lines) if decorated else raw_lines

    def decorate(self, lines: List[Tuple[Tuple[int, int], Tuple[int, int]]])-> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        centered = [((start_x + self.width // 2, start_y), (end_x + self.width // 2, end_y)) for (start_x, start_y), (end_x, end_y) in lines]
        origin_x, origin_y = self.left_top
        centered.append(((origin_x, origin_y + (self.height // 8)), (origin_x + self.width // 2, origin_y)))  # head decoration
        centered.append(self.create_line(Position.BOTTOM_X))  # bottom decoration
        return centered


class Two(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.LEFT_DOWN_Y),
            self.create_line(Position.BOTTOM_X),
        ]


class Three(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class Four(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._lines = [
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.RIGHT_DOWN_Y)
        ]


class Five(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class Six(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.LEFT_DOWN_Y),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class Seven(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int, decorated: bool):
        super().__init__(origin, width, half_height)
        raw_lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.TOP_RIGHT_TO_BOTTOM_MEDIAN)
        ]
        self._lines = self.decorate(raw_lines) if decorated else raw_lines

    def decorate(self, lines: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        offset = self.width // 4
        width = self.width // 24
        height = self.height // 24
        lines.append(((self.right_median[0] - offset - width, self.right_median[1] - height), (self.right_median[0] - offset + width, self.right_median[1] + height)))
        return lines


class Eight(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.LEFT_DOWN_Y),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class Nine(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


digit_map = {
    '0': lambda coord, l, h: Zero(coord, l, h, True),
    '1': lambda coord, l, h: One(coord, l, h, True),
    '2': lambda coord, l, h: Two(coord, l, h),
    '3': lambda coord, l, h: Three(coord, l, h),
    '4': lambda coord, l, h: Four(coord, l, h),
    '5': lambda coord, l, h: Five(coord, l, h),
    '6': lambda coord, l, h: Six(coord, l, h),
    '7': lambda coord, l, h: Seven(coord, l, h, True),
    '8': lambda coord, l, h: Eight(coord, l, h),
    '9': lambda coord, l, h: Nine(coord, l, h),
}


def create_digit(digit: str, origin: Tuple[int, int], width: int, half_height: int)->Digit:
    # print(f'origin={origin}', f'width={width}', f'height/2={half_height}')
    if digit in digit_map:
        return digit_map[digit](origin, width, half_height)

    raise ValueError(f'Unknown digit {digit}')
