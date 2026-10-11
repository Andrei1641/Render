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
        selected_pixel.set_color(color)


    def draw_line(self, line: Line, color: tuple[int,int,int]):
        tmp_point: Point = Point(line.x_borders[0], line.y_borders[0])
        bigger_borders: tuple[float, float] = line.x_borders if line.x_borders[1] - line.x_borders[0] > line.y_borders[1] - line.y_borders[0] else line.y_borders
        for i in range(round(bigger_borders[0]), round(bigger_borders[1])):
            tmp_pixel: PixelXXBit = self.__pixels[round(tmp_point.y)][round(tmp_point.x)]
            tmp_pixel.set_color(color)
            tmp_point = self.find_next_point(tmp_point, line)


    def draw_rectangle(self, position: Point, width: int, height: int, color: tuple[int,int,int]):
        ...

    def draw_circle(self, center: Point, radius: int, color: tuple[int,int,int]):
        ...

    @staticmethod
    def find_next_point(point: Point, figure: Figure) -> Point:
        """search next pixel from left to right(from bottom to top)"""
        point_side = figure.calculate_point_side(point)
        slope = figure.get_slope(point.x)
        if not slope:
            return Point(point.x, point.y + 1)
        elif slope < 0 and point_side == -1:
            return Point(point.x + 1, point.y)
        elif slope < 0 and point_side == 1:
            return Point(point.x, point.y - 1)
        elif slope > 0 and point_side == -1:
            return Point(point.x + 1, point.y)
        elif slope > 0 and point_side == 1:
            return Point(point.x, point.y + 1)
        elif slope == 0:
            return Point(point.x + 1, point.y)
        else:
            return Point(point.x, point.y + 1)