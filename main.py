from bitmap_calculate.frame import Frame
from bitmap_calculate.objects.figures import Point
from bitmap_create.interface.body_and_head import Header, Body
from bitmap_create.objects.pixel import *
from bitmap_create.objects.win_body_head import WinHeader, WinBody
from tools.file_writer import PictureCreator

#logic
WIDTH: int = 10
HEIGHT: int = 10

frame = Frame(WIDTH, HEIGHT)
frame.draw_point(Point(2, 2), (255, 0, 0))
frame.draw_point(Point(3, 3), (255, 0, 0))

#render
normalized_render_pixels: list[Pixel] = frame.get_render_pixels()

pixels: list[Pixel] = normalized_render_pixels
win_body: Body = WinBody(pixels, WIDTH, HEIGHT)

win_header: Header = WinHeader(
    54 + (len(pixels) * 3), 0, 54, 40, win_body.get_width(), win_body.get_height(), 1, win_body.get_color_deph(), 0,
    (len(pixels) * 3), 0, 0, 0, 0
)

PictureCreator.write_file(win_header, win_body)