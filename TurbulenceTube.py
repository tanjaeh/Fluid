from mayavi import mlab
from DataCollection import Excel

def create_line(excel):
    x_array = []
    y_array = []
    z_array = []

    i_building = []

    for data_line in range(26, 1025):
        x, y, z = excel.get_position(data_line)
        x_array.append(x)
        y_array.append(y)
        z_array.append(z)

        TI_building = excel.get_turbulence_intensity_with_building(data_line)

        i_building.append(TI_building)

    mlab.plot3d(x_array, y_array, z_array, i_building, tube_radius=10, tube_sides=30, opacity=0.50)


excel = Excel()
create_line(excel)