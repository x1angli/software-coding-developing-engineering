__author__ = 'x1ang.li'

import os

from PIL import Image, ImageDraw, ImageFont


def main(str):
    canvas_edge = 100
    canvas_rect = (canvas_edge, canvas_edge)
    template = Image.new('RGB', canvas_rect, 'white')
    font = ImageFont.truetype('msyhbd.ttf', 90) # MicroSoft Ya Hei Bold

    i = 0
    for char in str:
        i = i + 1
        cur_img = template.copy()
        font_box = font.getsize(char)
        point = ((canvas_rect[0] - font_box[0]) / 2, (canvas_rect[1] - font_box[1]) / 2)
        point_adjusted = (point[0], point[1] - 8) # this line should be removed.
        draw =  ImageDraw.Draw(cur_img)
        draw.text(point_adjusted, char, font=font, fill='red')
        filename = '{0:02d}_{1}.jpg'.format(i, char)
        cur_img.save(filename)
        print("The image has been saved as: {}".format(os.path.abspath(filename)))

if __name__ == '__main__':
    main('Hello world')

