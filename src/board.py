class Board:
    def __init__(self, length: int, height: int):
        self._length = length
        self._height = height

    @property
    def length(self)->int:
        return self._length

    @property
    def height(self)->int:
        return self._height

    def display(self, num: int)->None:
        chars = [c for c in str(num)]
