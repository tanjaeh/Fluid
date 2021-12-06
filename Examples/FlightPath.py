from mayavi import mlab
import numpy as np

def create_line():
    data = np.genfromtxt('../data/csv/case_279.csv', delimiter=';')
    data = np.transpose(data)
    x, y, z, d, i, u, v, w, delta_u, delta_v, U_prime = data

    return mlab.plot3d(x, y, z, i, tube_radius=9, tube_sides=30, opacity=0.10), y, i

line, i_y, intensity = create_line()

dt = .016
delay = int(dt * 1000)

def get_intensity(index, d):
    current_intensity = intensity[index]

    factor = 70
    right = .01 * np.sin(d * 2) * current_intensity * 0.01 * factor
    up = -current_intensity * 0.01 * factor
    up += 4.86 * 0.01 * factor  # To stay at center of tube (avoid sudden drop when tube is entered)

    distance_to_next = np.sqrt(np.square(i_y[index - 1] - i_y[len(i_y) - 1]))
    if distance_to_next <= d:
        index -= 1

    return right, up, index

@mlab.animate(delay=delay)
def anim():
    line_start = (322.5, 482, 59.1)
    line_flatten = (322.5, -302.7, 18.0)
    line_end = (322.5, -518.0, 18.0)
    cam_start = (322.5, 1000, line_start[2] + np.tan(np.deg2rad(3)) * (1000 - line_start[1]))
    mlab.view(azimuth=90, elevation=87, distance=.1, focalpoint=cam_start)

    current_fig = mlab.gcf()
    scene = current_fig.scene
    cam = current_fig.scene.camera

    v = 44  # 160 km/p - Approx. landing speed of DHC-8 300
    v_dt = v * dt
    t = 0
    d = 0
    index = len(intensity) - 1
    prev_i_move = (0, 0)

    pitch_start = line_flatten[1] - 10
    pitch_end = line_flatten[1] + 10
    pitch_delta = 3. / ((pitch_end - pitch_start) / (v * dt))

    while True:
        if t > 3.:
            if cam.position[1] <= line_start[1]:
                mlab.move(right=-prev_i_move[0], up=-prev_i_move[1])
                mlab.move(v_dt)
                right, up, index = get_intensity(index, d)
                mlab.move(right=right, up=up)
                prev_i_move = (right, up)
                d += v_dt
            else:
                mlab.move(v_dt)

            if pitch_start < cam.position[1] < pitch_end:
                cam.pitch(pitch_delta)

            if cam.position[1] <= line_end[1]:
                print(d)
                break

        scene.render()
        t += dt
        # print("t: " + str(t))
        yield


anim()
mlab.show()