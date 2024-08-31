import os
import sys
import argparse
from PIL import Image

def convert_png_to_jpg(image, out):
    """Convert PNG image to JPEG image"""
    with Image.open(image) as img:
        img = img.convert('RGB')
        img.save(out, 'JPEG')

def convert_jpeg_to_png(image, out):
    """Convert JPEG image to PNG image"""
    with Image.open(image) as img:
        img.save(out, 'PNG')

def convert_heic_to_all(image, out):
    """Convert HEIC image to PNG/JPEG image and vice versa"""
    os.execv('/opt/homebrew/bin/magick', ['magick', image, out])

def convert(args):
    """Convert image to another format"""
    image, new_fmt = args.image, args.format
    if not os.path.exists(image):
        sys.stderr.write(f'Error: {image} not found\n')
        return

    name, ori_fmt = os.path.splitext(image)
    ori_fmt = ori_fmt.strip('.').lower()
    converted_image = f'{name}.{new_fmt}'
    if new_fmt == 'jpg':
        new_fmt = 'jpeg'
    if ori_fmt == new_fmt:
        sys.stderr.write(f'Error: {image} is already in {new_fmt} format\n')
        return

    if ori_fmt == "png" and new_fmt == "jpeg":
        convert_png_to_jpg(image, converted_image)
    elif ori_fmt == "jpeg" and new_fmt == "png":
        convert_jpeg_to_png(image, converted_image)
    elif (ori_fmt == "heic" and new_fmt in ("png", "jpeg")) or (ori_fmt in ("png","jpeg") and new_fmt == "heic"):
        convert_heic_to_all(image, converted_image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image', type=str, help='Image to convert')
    parser.add_argument('format', type=str, choices=["png", "jpeg", "jpg", "heic"], help='Format of output image')

    convert_args = parser.parse_args()
    convert(convert_args)
