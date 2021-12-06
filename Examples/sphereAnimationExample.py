import numpy as np
from mayavi import mlab


def wantedMovement(sphere, y, t):
    if y:
        sphere.mlab_source.set(x=0, y=t, z=0)
    else:
        sphere.mlab_source.set(x=0, y=0, z=t)


@mlab.animate(delay = 100)
def updateAnimation():
    # list = []
    # direction = []
    #
    # list.append(ball)
    # direction.append(True)
    #
    # list.append(ball2)
    # direction.append(False)

    t = 0.0
    while True:
        # print(str(list.size()))
        print("HELLO")

        # for i in range(objList.size()):
        #     wantedMovement(objList[i], directionList[i], t)

        wantedMovement(ball, True, t)
        wantedMovement(ball2, False, t)
        t += 0.1
        yield



# ball = mlab.points3d(np.array(1.), np.array(0.), np.array(0.))
ball = mlab.points3d(1.0, 0.0, 0.0)
ball2 = mlab.points3d(1.0, 0.0, 0.0)

list = []
direction = []

list.append(ball)
direction.append(True)

list.append(ball2)
direction.append(False)



updateAnimation()
mlab.show()