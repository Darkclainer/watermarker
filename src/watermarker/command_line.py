import argparse

import PIL  # type: ignore
import PIL.Image  # type: ignore
import PIL.ImageFont  # type: ignore
import PIL.ImageDraw  # type: ignore

import watermarker


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='watermark your image',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='input image',
    )
    parser.add_argument(
        '-o', '--output',
        default='',
        help='output image',
    )
    parser.add_argument(
        '-t', '--text',
        required=True,
        help='watermark text',
    )
    parser.add_argument(
        '--font',
        default='LiberationMono-Regular.ttf',
        help='font name',
    )
    parser.add_argument(
        '--font-size',
        type=int,
        default=24,
        help='font size',
    )
    parser.add_argument(
        '-c', '--color',
        default='#ff0000a0',
        help='color of text',
    )
    parser.add_argument(
        '-a', '--angle',
        type=int,
        default=45,
        help='angle of text rotation',
    )
    parser.add_argument(
        '--xmargin',
        type=int,
        default=0,
        help='horizontal margin',
    )
    parser.add_argument(
        '--ymargin',
        type=int,
        default=0,
        help='vertical margin',
    )
    parser.add_argument(
        '-p', '--preview',
        action='store_const',
        const=True,
        default=False,
        help='preview image instead of saving it',
    )
    namespace = parser.parse_args()
    if namespace.output == '':
        namespace.output = generate_output_name(namespace.input)
    return namespace


def generate_output_name(name: str) -> str:
    return 'watermarked.png'


def load_font(
    *,
    name: str,
    size: int,
) -> PIL.ImageFont.ImageFont:
    font = PIL.ImageFont.truetype(name, size=size)
    return font


def main():
    args = parse_args()

    font = load_font(
        name=args.font,
        size=args.font_size,
    )

    watermark = watermarker.create_tile(
        font=font,
        text=args.text,
        color=args.color,
        angle=args.angle,
    )

    with PIL.Image.open(args.input) as img:
        watermarked = watermarker.tile(
            img,
            watermark,
            xmargin=args.xmargin,
            ymargin=args.ymargin,
        )

    if args.preview:
        watermarked.show()
        return

    watermarked.save(args.output)


if __name__ == "__main__":
    main()
