from mayavi import mlab
import numpy as np
import math

placement = np.linspace(0, 10, 100)

ys = np.sin(placement)
zs = np.zeros_like(placement)
xs = np.zeros_like(placement)

mlab.points3d(0, 0, 0)
plt = mlab.points3d(xs[:1], ys[:1], zs[:1])


@mlab.animate(delay=60)
def anim_loc():
    f = mlab.gcf()
    while True:
        for (x, y, z) in zip(xs, ys, zs):
            # print('Updating scene...')
            plt.mlab_source.set(x=x, y=y, z=z)
            yield


anim_loc()
mlab.show()
