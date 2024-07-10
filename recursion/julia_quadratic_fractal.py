# First variant
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#
# def julia_quadratic(zx, zy, cx, cy, threshold):
#     """Calculates whether the number z[0] = zx + i*zy with a constant c = x + i*y
#     belongs to the Julia set. In order to belong, the sequence
#     z[i + 1] = z[i]**2 + c, must not diverge after 'threshold' number of steps.
#     The sequence diverges if the absolute value of z[i+1] is greater than 4.
#
#     :param float zx: the x component of z[0]
#     :param float zy: the y component of z[0]
#     :param float cx: the x component of the constant c
#     :param float cy: the y component of the constant c
#     :param int threshold: the number of iterations to considered it converged
#     """
#     # initial conditions
#     z = complex(zx, zy)
#     c = complex(cx, cy)
#
#     for i in range(threshold):
#         z = z ** 2 + c
#         if abs(z) > 4.:  # it diverged
#             return i
#
#     return threshold - 1  # it didn't diverge
#
#
# x_start, y_start = -2, -2  # an interesting region starts here
# width, height = 4, 4  # for 4 units up and right
# density_per_unit = 200  # how many pixles per unit
#
# # real and imaginary axis
# re = np.linspace(x_start, x_start + width, width * density_per_unit)
# im = np.linspace(y_start, y_start + height, height * density_per_unit)
#
# threshold = 20  # max allowed iterations
# frames = 100  # number of frames in the animation
#
# # we represent c as c = r*cos(a) + i*r*sin(a) = r*e^{i*a}
# r = 0.7885
# a = np.linspace(0, 2 * np.pi, frames)
#
# fig = plt.figure(figsize=(10, 10))  # instantiate a figure to draw
# ax = plt.axes()  # create an axes object
#
#
# def animate(i):
#     ax.clear()  # clear axes object
#     ax.set_xticks([], [])  # clear x-axis ticks
#     ax.set_yticks([], [])  # clear y-axis ticks
#
#     X = np.empty((len(re), len(im)))  # the initial array-like image
#     cx, cy = r * np.cos(a[i]), r * np.sin(a[i])  # the initial c number
#
#     # iterations for the given threshold
#     for i in range(len(re)):
#         for j in range(len(im)):
#             X[i, j] = julia_quadratic(re[i], im[j], cx, cy, threshold)
#
#     img = ax.imshow(X.T, interpolation="bicubic", cmap='magma')
#     return [img]
#
#
# anim = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)
# anim.save('julia_set.gif', writer='imagemagick')


# Second variant
import argparse
import numpy as np
#pip install opencv-python
import cv2
from tqdm import tqdm


def generate_colors(n):
    palette = [(0, 0, 0)]
    img = np.zeros([1, 1, 3], dtype=np.uint8)
    for i in range(n):
        img[:] = ((i/n) * 255, 255 * 0.85, 255)
        rgb = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        palette.append((rgb[0,0][0], rgb[0,0][1], rgb[0,0][2]))

    return palette


def interpolate(c1, c2, steps):
    delta1 = (c2[0] - c1[0]) / steps
    delta2 = (c2[1] - c1[1]) / steps
    res = []
    cc1 = c1[0]
    cc2 = c1[1]
    for i in range(steps):
        res.append((cc1, cc2))
        cc1 += delta1
        cc2 += delta2

    return res


def process_julia(max_iter, c, palette, width, height):
    w, h, zoom = width, height, 0.7
    move_x = 0.0
    move_y = 0.0
    img = np.zeros([h, w, 3], dtype=np.uint8)

    c_x = c[0]
    c_y = c[1]
    for x in range(w):
        for y in range(h):
            zx = 1.5 * (x - w / 2) / (0.5 * zoom * w) + move_x
            zy = 1.0 * (y - h / 2) / (0.5 * zoom * h) + move_y
            i = max_iter
            while zx * zx + zy * zy < 20 and i > 1:
                tmp = zx * zx - zy * zy + c_x
                zy, zx = 2.0 * zx * zy + c_y, tmp
                i -= 1

            index = (i * len(palette)) // max_iter
            img[y, x] = (palette[index][0], palette[index][1], palette[index][2])

    cv2.imshow('', img)
    cv2.waitKey(1)

    return img


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default='interpolate_Julia.mp4', type=str, help='resulting video')
    parser.add_argument('-i', '--iterations', default=100, type=int, help='number of iterations')
    args = parser.parse_args()
    print(args)

    width = 800
    height = 600

    interps = []
    num_iter = args.iterations

    interps.append(interpolate((-0.16, 1.0405), (-0.722, 0.246), num_iter))
    interps.append(interpolate((-0.722, 0.246), (-0.235125, 0.827215), num_iter))
    interps.append(interpolate((-0.235125, 0.827215),(-1.25066, 0.02012), num_iter))
    interps.append(interpolate((-1.25066, 0.02012), (-0.748, 0.1), num_iter))
    interps.append(interpolate((-0.748, 0.1), (-0.16, 1.0405), num_iter))
    pbar = tqdm(total=(num_iter * len(interps)))
    palette = generate_colors(2000)
    fourcc = cv2.VideoWriter_fourcc('F', 'M', 'P', '4')
    out_cutter_name = args.output
    fps = 24
    out = cv2.VideoWriter(out_cutter_name, fourcc, fps, (width, height))

    for interp in interps:
        for p in interp:
            r = process_julia(num_iter, p, palette, width, height)
            out.write(r)
            pbar.update(1)

    out.release()