from typing import Tuple

from src.character.digits import create_digit, Digit


class Board:
    def __init__(self, length: int, height: int, y_down_direction: bool = False):
        self._length = length
        self._height = height
        self._y_down_direction = y_down_direction

    @property
    def length(self) -> int:
        return self._length

    @property
    def height(self) -> int:
        return self._height

    @property
    def y_down_direction(self):
        return self._y_down_direction

    def _layout(self, size: int) -> [Tuple[Tuple[int, int], int, int]]:
        frame = self.length / size
        offset = 4 if frame / 5 <= 4 else frame / 5
        length = frame - offset
        height = length * 2 if length * 2 <= self.height else self.height

        print(f'length={length}', f'offset = {offset}', f'height={height}')

        return [((idx * frame, 0), length, (height / 2) * 1 if self.y_down_direction else -1) for idx in range(0, size)]

    def digitalize(self, num: int) -> [Digit]:
        chars = [c for c in str(num)]
        layouts = self._layout(len(chars))
        return [create_digit(key, *paras) for key, paras in zip(chars, layouts)]
