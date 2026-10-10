from bitmap_calculate.objects.figures import Point, Line, Figure
from bitmap_calculate.objects.pixel import PixelXXBit, PixelAdapter
from bitmap_create.interface.pixel import Pixel


class Frame:
    def __init__(self, width: int, height: int):
        self.__pixels: list[list[PixelXXBit]] = [] #y x    size is 1X1
        for i in range(height):
            self.__pixels.append(PixelXXBit(0,0,0) * width)


    def get_render_pixels(self) -> list[Pixel]:
        adapter: PixelAdapter = PixelAdapter(self.__pixels)
        render_pixels: list[list[Pixel]] = adapter.translate_calculate_to_render_pixels()
        normalized_render_pixels: list[Pixel] = adapter.normalize_pixels(render_pixels)
        return normalized_render_pixels

    def draw_point(self, point: Point, color: tuple[int,int,int]):
        selected_pixel: PixelXXBit = self.__pixels[round(point.y)][round(point.x)]
        selected_pixel.red = color[0]
        selected_pixel.green = color[1]
        selected_pixel.blue = color[2]


    def draw_line(self, line: Line, color: tuple[int,int,int]):
        ...

    def draw_rectangle(self, position: Point, width: int, height: int, color: tuple[int,int,int]):
        ...

    def draw_circle(self, center: Point, radius: int, color: tuple[int,int,int]):
        ...

    def find_next_pixel(self, point: Point, figure: Figure) -> PixelXXBit:
        ...
