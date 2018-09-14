from typing import List, Tuple

from src.model.frame import VirtualFrame, Position


class Digit(VirtualFrame):
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        super().__init__(left_top, length, half_height)
        self._lines = []

    @property
    def lines(self) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        return self._lines


class Zero(Digit):
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        super().__init__(left_top, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.LEFT_DOWN_Y),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class One(Digit):
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        super().__init__(left_top, length, half_height)
        self._lines = [
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.LEFT_DOWN_Y),
        ]


class Two(Digit):
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        super().__init__(left_top, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.LEFT_DOWN_Y),
            self.create_line(Position.BOTTOM_X),
        ]


class Three(Digit):
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        super().__init__(left_top, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class Four(Digit):
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        super().__init__(left_top, length, half_height)
        self._lines = [
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.RIGHT_DOWN_Y)
        ]


class Five(Digit):
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        super().__init__(left_top, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class Six(Digit):
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        super().__init__(left_top, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.LEFT_DOWN_Y),
            self.create_line(Position.RIGHT_DOWN_Y),
            self.create_line(Position.BOTTOM_X)
        ]


class Seven(Digit):
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        super().__init__(left_top, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.RIGHT_DOWN_Y)
        ]


class Eight(Digit):
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        super().__init__(left_top, length, half_height)
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
    def __init__(self, left_top: Tuple[int, int], length: int, half_height: int):
        super().__init__(left_top, length, half_height)
        self._lines = [
            self.create_line(Position.TOP_X),
            self.create_line(Position.LEFT_UP_Y),
            self.create_line(Position.RIGHT_UP_Y),
            self.create_line(Position.MEDIAN_X),
            self.create_line(Position.RIGHT_DOWN_Y)
        ]
