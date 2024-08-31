import os
import sys
import argparse
from PIL import Image

def resize(args):
    """Resize image"""
    image, width, height, output = args.image, args.width, args.height, args.output
    if not os.path.exists(image):
        sys.stderr.write(f'Error: {image} not found\n')
        return

    with Image.open(image) as img:
        if height == 0:
            height = int(img.height * (width / img.width))
        resized_img = img.resize((width, height))

        if output:
            resized_img_name = f'{output}{os.path.splitext(image)[1]}'
        else:
            name, ext = os.path.splitext(image)
            resized_img_name = f'{name}_resized{ext}'

        resized_img.save(resized_img_name)
        print(f'Image saved as {resized_img_name}')


if __name__ == '__main__':
    def msg():
        """Custom usage message"""
        return "resize [-h] -w WIDTH [-H HEIGHT] [-o OUTPUT] image"

    parser = argparse.ArgumentParser(usage=msg())

    parser.add_argument('image', type=str, help='Image to resize')
    parser.add_argument('-w', '--width', dest='width', type=int, help='Width of the resized image', required=True)
    parser.add_argument('-H', '--height', dest='height', type=int, help='Height of the resized image. If not specify, program will calculate the new height base on the aspect ratio of the original image.', default=0)
    parser.add_argument('-o', '--output', dest='output', type=str, help='Output file name', default='')

    resize_args = parser.parse_args()
    resize(resize_args)
