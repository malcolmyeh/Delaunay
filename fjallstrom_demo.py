import matplotlib.pyplot as plt
from utils import *
from Fjallstrom import *
import cv2
import argparse

def generate_raster(n):
    # create 2d array of random values
    # todo: find method to generate "pseudorandom" data that resembles real world data
    return np.array([[randint(1, 1000) for _ in range(n)] for _ in range(n)])

parser = argparse.ArgumentParser()
parser.add_argument("-s", type=int, help="side length of raster to generate", default=15)
parser.add_argument("-p", type=str, help="path to input raster image")
parser.add_argument("-e", type=float, help="maximum error for Fjallstrom algorithm", default=0.5)
args = parser.parse_args()

if args.p is not None:
    image = cv2.imread(args.p)
    raster = np.array(image)
    raster = cv2.cvtColor(raster, cv2.COLOR_BGR2GRAY)
    n = len(raster)
else:
    n = args.s
    raster = generate_raster(n);

grid = raster_to_grid(raster)

plt.figure()
plt.title('initial')
plt.imshow(raster, cmap='Greys')

fjallstrom(grid, args.e)
conv_raster = grid_to_raster(grid)

plt.figure()
plt.title(f'Fjallstrom Error={args.e}')
plt.imshow(conv_raster, cmap='Greys')
# plt.savefig(f'./converted/{args.p[:-4]}_{args.e}.png')
plt.show()

