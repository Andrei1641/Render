from bitmap_create.interface.pixel import Pixel
from tools.tools import Translator


class Pixel24Bit(Pixel):
    __padding: int = 0

    @classmethod
    def get_color_depth(cls) -> int:
        return 24

    def __init__(self, red: int, green: int, blue: int):
        self.__red = red
        self.__green = green
        self.__blue = blue
        Pixel24Bit.__padding += 1

    def get_padding(self) -> int:
        return Pixel24Bit.__padding

    def to_bytes(self) -> list[int]:
        pixel_in_bin: list[int] = []
        pixel_in_bin += Translator.from_int_to_bytes(self.__blue)
        pixel_in_bin += Translator.from_int_to_bytes(self.__green)
        pixel_in_bin += Translator.from_int_to_bytes(self.__red)
        return pixel_in_bin