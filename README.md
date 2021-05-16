# Watermaker

This is a simple utility to watermark your images with custom text.
You can choose font, color, angle of text and distance between watermarks.

## Install

You can install utility using `pip3`:

```console
pip3 install --user watermarker-Darkclainer
```

## Usage

You can see all options by supplying `-h` flag:

```console
$ watermarker -h
usage: watermarker [-h] -i INPUT [-o OUTPUT] -t TEXT [--font FONT] [--font-size FONT_SIZE] [-c COLOR] [-a ANGLE] [--xmargin XMARGIN] [--ymargin YMARGIN] [-p]

watermark your image

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input image (default: None)
  -o OUTPUT, --output OUTPUT
                        output image (default: )
  -t TEXT, --text TEXT  watermark text (default: None)
  --font FONT           font name (default: LiberationMono-Regular.ttf)
  --font-size FONT_SIZE
                        font size (default: 24)
  -c COLOR, --color COLOR
                        color of text (default: #ff0000a0)
  -a ANGLE, --angle ANGLE
                        angle of text rotation (default: 45)
  --xmargin XMARGIN     horizontal margin (default: 0)
  --ymargin YMARGIN     vertical margin (default: 0)
  -p, --preview         preview image instead of saving it (default: False)
```

For example you have image:

![lenna original](./imgs/lenna.png)

To add watermarks you can use next command:

```console
watermarker --input lenna.png \
    --output lenna_watermarked.png \
    --text 'watermakred.omg' \
    --angle 30 \
    --color '#00ff00a0' \
    --font-size 15
```

The resulting image will be:

![lenna watermakred](./imgs/lenna_watermarked.png)
