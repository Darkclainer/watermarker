import PIL  # type: ignore
import PIL.Image  # type: ignore
import PIL.ImageFont  # type: ignore
import PIL.ImageDraw  # type: ignore


def create_tile(
    font: PIL.ImageFont.ImageFont,
    text: str,
    color: str,
    angle: int,
) -> PIL.Image.Image:
    flat_size = font.getsize(text)
    im = PIL.Image.new("RGBA", flat_size)
    draw = PIL.ImageDraw.Draw(im)
    draw.text((0, 0), text, fill=color, font=font)
    im = im.rotate(angle, expand=True)
    return im


def tile(
    img: PIL.Image.Image,
    tile: PIL.Image.Image,
    xmargin: int,
    ymargin: int,
) -> PIL.Image.Image:
    img = img.convert(mode="RGBA")
    width, height = img.size
    tile_width, tile_height = tile.size
    for x in range(0, width, tile_width + xmargin):
        for y in range(0, height, tile_height + ymargin):
            img.paste(tile, (x, y), tile)
    return img
