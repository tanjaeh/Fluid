import numpy as np
from mayavi import mlab
import xlrd
import os

# from Sphere import plot_sphere, test_points3d

@mlab.animate(delay = 50)
def updateAnimation(flight, sheet):
    f = mlab.gcf()
    line = 1024


    while True:
        print("Line: " + str(line))

        x_data = sheet.cell_value(line, 0)
        y_data = sheet.cell_value(line, 1)
        z_data = sheet.cell_value(line, 2)

        print(str(x_data) + " " + str(y_data) + " " + str(z_data))

        # flight.mlab_source.set(x=0, y=0, z=line)
        flight.mlab_source.set(x=x_data, y=y_data, z=z_data)

        if line == 26:
            break

        line -= 1
        yield

# Exel file
loc = (r"C:\dev\DTE3600_Fluid\data\simData.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# mlab.plot3d(x, y, z, tube_radius=4, tube_sides=20)


ball = mlab.points3d(1.0, 0.0, 0.0, scale_factor=20.0)

updateAnimation(ball, sheet)
mlab.show()