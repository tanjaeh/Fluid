from mayavi import mlab
from DataCollection import Excel


@mlab.animate(delay=100)
def updateAnimation():
    line = 1024
    excel = Excel()

    ball = mlab.points3d(1.0, 0.0, 0.0, scale_factor=20)

    while True:
        # Data from excel:
        x_data, y_data, z_data = excel.get_position(line)

        # Move ball
        ball.mlab_source.set(x=x_data, y=y_data, z=z_data)

        if line > 25:
            line -= 1
        yield

updateAnimation()
mlab.show()
