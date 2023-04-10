#!/usr/bin/env python3
import os
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

# paste image without converting the colro and the size
def image(inky_display_img, img_path, x, y) -> Image:

    img_position = (x, y)
    img = Image.open(img_path)
    inky_display_img.paste(img, img_position)

    return inky_display_img

# paste image after converting the color (black, red, and white) and the size
def image_convert(inky_display_img, img_path, x, y) -> Image:

    img_position = (x, y)
    inky_img_path = os.path.splitext(os.path.basename(img_path))[0] + "_inky_rbw_resize.png"

    if os.path.isfile(inky_img_path):
        img = Image.open(inky_img_path)

    else:
        img_pre_convert = Image.open(img_path).convert("RGBA")
        background = Image.new("RGBA", img_pre_convert.size, (255,255,255))

        img = Image.alpha_composite(background, img_pre_convert)
        img = img.convert('P')

        palette = [255, 255, 255, # White
                   255, 0, 0,     # Red
                   0, 0, 0]       # Black

        img.putpalette(palette)

        max_size = (250, 122)
        img.thumbnail(max_size)

        img.save(inky_img_path)

        # for some reason I need to open the saved file here...
        img.close()
        img = Image.open(inky_img_path)

    inky_display_img.paste(img, img_position)

    return inky_display_img

# paste text
def text(inky_display_img, text, font_color, font_size, x, y) -> Image:

    draw = ImageDraw.Draw(inky_display_img)

    font = ImageFont.truetype(FredokaOne, font_size)
    draw.text((x, y), text, font_color, font)

    return inky_display_img
