from typing import List, Tuple

from src.character.frame import VirtualFrame, Position


class Digit(VirtualFrame):
    def __init__(self, origin: Tuple[int, int], length: int, half_height: int):
        super().__init__(origin, length, half_height)
        self._lines = []

    @property
    def lines(self) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        return self._lines


class Zero(Digit):
    def __init__(self, origin: Tuple[int, int], length: int, half_height: int):
        super().__init__(origin, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.LEFT_DOWN_Y),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class One(Digit):
    def __init__(self, origin: Tuple[int, int], length: int, half_height: int):
        super().__init__(origin, length, half_height)
        self._lines = [
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.LEFT_DOWN_Y),
        ]


class Two(Digit):
    def __init__(self, origin: Tuple[int, int], length: int, half_height: int):
        super().__init__(origin, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.LEFT_DOWN_Y),
            self.create_line(Position.BOTTOM_X),
        ]


class Three(Digit):
    def __init__(self, origin: Tuple[int, int], length: int, half_height: int):
        super().__init__(origin, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class Four(Digit):
    def __init__(self, origin: Tuple[int, int], length: int, half_height: int):
        super().__init__(origin, length, half_height)
        self._lines = [
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.RIGHT_DOWN_Y)
        ]


class Five(Digit):
    def __init__(self, origin: Tuple[int, int], length: int, half_height: int):
        super().__init__(origin, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class Six(Digit):
    def __init__(self, origin: Tuple[int, int], length: int, half_height: int):
        super().__init__(origin, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.LEFT_DOWN_Y),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class Seven(Digit):
    def __init__(self, origin: Tuple[int, int], length: int, half_height: int):
        super().__init__(origin, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.RIGHT_DOWN_Y)
        ]


class Eight(Digit):
    def __init__(self, origin: Tuple[int, int], length: int, half_height: int):
        super().__init__(origin, length, half_height)
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
    def __init__(self, origin: Tuple[int, int], length: int, half_height: int):
        super().__init__(origin, length, half_height)
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


def create_digit(digit: str, origin: Tuple[int, int], length: int, half_height: int)->Digit:
    if digit in digit_map:
        return digit_map[digit](origin, length, half_height)

    raise ValueError(f'Unknown digit {digit}')
