from typing import Tuple

from src.character.digits import create_digit, Digit


class Board:
    def __init__(self, size: Tuple[int, int], y_down_direction: bool = False):
        self._width, self._height = size
        self._y_down_direction = y_down_direction

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def y_down_direction(self):
        return self._y_down_direction

    def _layout(self, size: int) -> [Tuple[Tuple[int, int], int, int]]:
        frame = self.width // size
        offset = 4 if frame // 5 <= 4 else frame // 5
        width = frame - offset
        height = width * 2 if (width * 2) <= self.height else self.height

        print(f'width={width}', f'offset={offset}', f'height={height}')
        return [((idx * frame, 0), width, (height / 2) * (1 if self.y_down_direction else -1)) for idx in range(0, size)]

    def digitalize(self, num: int) -> [Digit]:
        chars = [c for c in str(num)]
        layouts = self._layout(len(chars))
        return [create_digit(key, *paras) for key, paras in zip(chars, layouts)]
