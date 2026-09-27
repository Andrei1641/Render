from abc import ABC, abstractmethod


class Pixel(ABC):
    @classmethod
    @abstractmethod
    def get_color_depth(cls) -> int:
        ...
    @abstractmethod
    def to_bytes(self) -> list[int]:
        ...
    @abstractmethod
    def get_padding(self) -> int:
        ...