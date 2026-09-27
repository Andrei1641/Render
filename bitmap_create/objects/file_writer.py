from bitmap_create.interface.body_and_head import *


class PictureCreator:
    @staticmethod
    def write_file(header: Header, body: Body):
        with open('file.bmp', 'wb') as f:
            f.write(bytes(header.get_header()))
            f.write(bytes(body.get_body()))