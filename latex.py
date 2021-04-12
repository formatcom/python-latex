import sys
import argparse
import base64
from io import BytesIO

from matplotlib import mathtext
from matplotlib.font_manager import FontProperties


parser = argparse.ArgumentParser()

parser.add_argument('--input',       required=True)
parser.add_argument('--output',      default='latex.svg')
parser.add_argument('--name',        default='latex')
parser.add_argument('--family',      default='serif')
parser.add_argument('--mathfamily',  default='dejavuserif')
parser.add_argument('--style',       default='italic')
parser.add_argument('--size',        default=16, type=int)
parser.add_argument('--base64',      action='store_true')
parser.add_argument('--markdown',    action='store_true')
args = parser.parse_args()

font = FontProperties(family=args.family,
                        math_fontfamily=args.mathfamily,
                        style=args.style,
                        size=args.size)

buffer = BytesIO()
mathtext.math_to_image(r'{}'.format(args.input), buffer,
                                prop=font, format='svg')

buffer.seek(0)

if args.base64:
    encoded = 'data:image/svg+xml;base64,{}'.format(
                            base64.b64encode(buffer.read()).decode('utf-8'))

    if args.markdown:
        print('base64 and markdown no support', file=sys.stderr)
    else:
        print(encoded, end='')

else:

    f = open(args.output, 'wb')
    f.write(buffer.read())
    f.close()

    if args.markdown:
        print('![{name}]({output})'.format(name=args.name, output=args.output), end='')

