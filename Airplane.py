import random

from mayavi import mlab
from DataCollection import Excel
from Turbulence import getTubulenceArray


@mlab.animate(delay=100)
def updateAnimation():
    line = 1024
    excel = Excel()

    ball = mlab.points3d(0.5, 0.0, 0.0, scale_factor=20, color=(1.0, 0.0, 1.0))

    turbulence_array = getTubulenceArray(excel)

    while True:
        # Data from excel:
        x_data, y_data, z_data = excel.get_position(line)

        # Apply turbulence intensity for position
        turbulence_intensity = turbulence_array[line-26]
        turbulence_direction = random.randint(0, 3)
        if turbulence_direction == 0:
            x_data += turbulence_intensity
        elif turbulence_direction == 1:
            z_data += turbulence_intensity
        elif turbulence_direction == 2:
            x_data -= turbulence_intensity
        elif turbulence_direction == 3:
            z_data -= turbulence_intensity

        # Move ball
        ball.mlab_source.set(x=x_data, y=y_data, z=z_data)

        if line > 26:
            line -= 1
        yield

updateAnimation()
mlab.show()
