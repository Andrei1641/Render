from copy import deepcopy

from bitmap_calculate.objects.pixel import PixelXXBit
from bitmap_create.interface.body_and_head import *
from bitmap_create.objects.win_body_head import WinHeader, WinBody
from tools import Translator


class PictureCreator:
    @staticmethod
    def write_file(header: Header, body: Body, file_address: str):
        with open(file_address, 'wb') as f:
            f.write(bytes(header.get_header()))
            f.write(bytes(body.get_body()))

class PictureReader:
    @staticmethod
    def read_magic_number(address: str) -> bytes:
        with open(address, "rb") as f:
            content = f.read(8)
        return content

    @staticmethod
    def create_calculate_pixels(raw_body: bytes, header: Header) -> list[list[PixelXXBit]] | None:
        calculate_pixels = None
        if isinstance(header, WinHeader):
            pixel_depth: int = header.get_depth()
            row_width: int = header.get_width()
            bytes_per_pixel = pixel_depth // 8
            row_size = row_width * bytes_per_pixel
            padding = (4 - row_size % 4) % 4

            calculate_pixels: list[list[PixelXXBit]] = []
            pixel_counter: int = 0
            row_width_counter: int = 0
            tmp_calculate_pixel: PixelXXBit = PixelXXBit(0,0,0)
            tmp_row: list[PixelXXBit] = []
            for i in range(len(raw_body)):
                if pixel_counter == 0:
                    tmp_calculate_pixel.blue = int(raw_body[i])
                    pixel_counter += 1
                elif pixel_counter == 1:
                    tmp_calculate_pixel.green = int(raw_body[i])
                    pixel_counter += 1
                elif pixel_counter == 2:
                    tmp_calculate_pixel.red = int(raw_body[i])
                    pixel_counter = 0
                    row_width_counter += 1
                    tmp_row.append(deepcopy(tmp_calculate_pixel))

                if row_width_counter >= row_width:
                    calculate_pixels.append(tmp_row)
                    tmp_row = []
                    row_width_counter = 0
                    i += padding
        return calculate_pixels



    @staticmethod
    def read_raw_body(address: str) -> bytes|None:  #!!!
        header: Header|None = PictureReader.read_header(address)
        raw_body: bytes = b''
        if header:
            body_position: int = header.get_body_position()
            with open(address, 'rb') as f:
                f.seek(body_position)
                raw_body = f.read()
            return raw_body
        else:
            return None


    @staticmethod
    def read_header(address:str) -> Header|None:            #!!!
        header: Header|None = None
        magic_number: bytes = PictureReader.read_magic_number(address)
        if b'BM' in magic_number:
            header = PictureReader.read_win_header(address)
        return header


    @staticmethod
    def read_win_header(address: str) -> WinHeader:      #!!!
        with open(address, "rb") as f:
            bfType = f.read(2)
            bfSize = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))
            bfReserved = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))
            bfOffBits = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))
            biSize = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))
            biWidth = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))
            biHight = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))
            biPlanes = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(2))))
            biBitCount = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(2))))
            biCompression = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))
            biSizeImage = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))
            biXPelsPerMeter = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))
            biYPelsPerMeter = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))
            biClrUsed = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))
            biClrImportant = Translator.from_bytes_to_int(Translator.translate_endian(list(f.read(4))))

        win_header: WinHeader = WinHeader(bfSize, bfReserved, bfOffBits, biSize, biWidth, biHight, biPlanes,
                                          biBitCount, biCompression, biSizeImage, biXPelsPerMeter, biYPelsPerMeter,
                                          biClrUsed, biClrImportant)
        return win_header