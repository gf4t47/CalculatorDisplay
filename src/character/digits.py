from typing import List, Tuple

from src.character.frame import VirtualFrame, Position


class Digit(VirtualFrame):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._length = width
        self._height = half_height * 2
        self._lines = []

    @property
    def length(self):
        return self._length

    @property
    def height(self):
        return self._height

    @property
    def origin(self):
        return self.left_top

    @property
    def lines(self) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        return self._lines


class Zero(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.LEFT_DOWN_Y),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class One(Digit):
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._lines = self.decorate([
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.LEFT_DOWN_Y),
        ])

    def decorate(self, lines: List[Tuple[Tuple[int, int], Tuple[int, int]]])-> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        centered = [((start_x + self.length // 2, start_y), (end_x + self.length // 2, end_y)) for (start_x, start_y), (end_x, end_y) in lines]
        centered.append(self.create_line(Position.BOTTOM_X))  # bottom decoration
        centered.append(((self.origin[0], self.origin[1] + (self.height // 8)), (self.origin[0] + self.length // 2, self.origin[1])))  # head decoration
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
    def __init__(self, origin: Tuple[int, int], width: int, half_height: int):
        super().__init__(origin, width, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.RIGHT_DOWN_Y)
        ]


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
            self.create_line(Position.RIGHT_DOWN_Y)
        ]


digit_map = {
    '0': lambda coord, l, h: Zero(coord, l, h),
    '1': lambda coord, l, h: One(coord, l, h),
    '2': lambda coord, l, h: Two(coord, l, h),
    '3': lambda coord, l, h: Three(coord, l, h),
    '4': lambda coord, l, h: Four(coord, l, h),
    '5': lambda coord, l, h: Five(coord, l, h),
    '6': lambda coord, l, h: Six(coord, l, h),
    '7': lambda coord, l, h: Seven(coord, l, h),
    '8': lambda coord, l, h: Eight(coord, l, h),
    '9': lambda coord, l, h: Nine(coord, l, h),
}


def create_digit(digit: str, origin: Tuple[int, int], width: int, half_height: int)->Digit:
    # print(f'origin={origin}', f'width={width}', f'height/2={half_height}')
    if digit in digit_map:
        return digit_map[digit](origin, width, half_height)

    raise ValueError(f'Unknown digit {digit}')
