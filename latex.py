import sys
import argparse
import base64
from io import BytesIO

from matplotlib import mathtext
from matplotlib.font_manager import FontProperties


parser = argparse.ArgumentParser()

parser.add_argument('--input',       required=True)
parser.add_argument('--family',      default='serif')
parser.add_argument('--mathfamily',  default='dejavuserif')
parser.add_argument('--style',       default='italic')
parser.add_argument('--size',        default=16, type=int)
args = parser.parse_args()

font = FontProperties(family=args.family,
                        math_fontfamily=args.mathfamily,
                        style=args.style,
                        size=args.size)

buffer = BytesIO()
mathtext.math_to_image(r'{}'.format(args.input), buffer,
                                prop=font, format='svg')

buffer.seek(0)

encoded = 'data:image/svg+xml;;base64,{}'.format(
                        base64.b64encode(buffer.read()).decode('utf-8'))


print(encoded, end='')
