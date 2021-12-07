import random
import numpy as np

from mayavi import mlab
from DataCollection import Excel
from Turbulence import getTubulenceArray

def get_intensity(current_intensity):
    factor = 0.4
    x_right = 0
    z_up = 0
    turbulence_direction = random.randint(0, 3)
    if turbulence_direction == 0:
        x_right += current_intensity
    elif turbulence_direction == 1:
        z_up += current_intensity
    elif turbulence_direction == 2:
        x_right -= current_intensity
    elif turbulence_direction == 3:
        z_up -= current_intensity

    return x_right * factor, z_up * factor


@mlab.animate(delay=100)
def anim():
    line = 1024
    excel = Excel()
    x_start, y_start, z_start = excel.get_position(line)
    turbulence_array = getTubulenceArray(excel)

    # Camera setup
    cam_start = (x_start, y_start, z_start)
    mlab.view(azimuth=90, elevation=87, distance=.1, focalpoint=cam_start)

    current_fig = mlab.gcf()
    scene = current_fig.scene
    cam = current_fig.scene.camera

    prev_i_move = (0, 0)

    pitch_start = -302.7 - 10
    pitch_end = -302.7 + 10


    while True:
        # Data from excel:
        x_data, y_data, z_data = excel.get_position(line)

        next_line = line-2
        if line == 26:
            next_line = 26

        print(next_line)
        x_next, y_next, z_next = excel.get_position(next_line)
        v_dt = abs(y_next - y_data)

        if cam.position[1] <= y_start:
            mlab.move(right=-prev_i_move[0], up=-prev_i_move[1])
            mlab.move(v_dt)
            right, up = get_intensity(turbulence_array[line-26])
            mlab.move(right=right, up=up)
            prev_i_move = (right, up)
        else:
            mlab.move(v_dt)


        if pitch_start < cam.position[1] < pitch_end:
            pitch_delta = 3. / ((pitch_end - pitch_start) / (v_dt))
            cam.pitch(pitch_delta)


        if line > 27:
            line -= 2
        yield

anim()
mlab.show()

