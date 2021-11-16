import numpy as np
from mayavi import mlab
import xlrd

@mlab.animate(delay = 100)
def updateAnimation(flight):
    line = 26

    # Exel file
    # C:\dev\DTE3600_Fluid\
    # loc = ("data\Sim DataTurbanalyse Innflygningslinje   17.07.20.xlsx")
    # wb = xlrd.open_workbook(loc)
    # sheet = wb.sheet_by_index(0)


    while True:
        # x_data = sheet.cell_value(line, 0)
        # y_data = sheet.cell_value(line, 1)
        # z_data = sheet.cell_value(line, 2)

        print("HELLO")
        # print(str(x_data) + str(y_data) + str(z_data))
        #
        # flight.mlab_source.set(x=x_data, y=y_data, z=z_data)
        flight.mlab_source.set(x=0, y=line, z=0)

        if line == 1024:
            break

        line += 1
        yield

ball = mlab.points3d(1.0, 0.0, 0.0)
updateAnimation(ball)
mlab.show()