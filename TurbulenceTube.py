from mayavi import mlab
from DataCollection import Excel

def create_line(excel):
    x_array = []
    y_array = []
    z_array = []

    i_building = []
    i_no_building = []
    i_difference = []

    for data_line in range(26, 1025):
        x, y, z = excel.get_position(data_line)
        x_array.append(x)
        y_array.append(y)
        z_array.append(z)

        TI_building = excel.get_turbulence_intensity_with_building(data_line)
        # TI_no_building = excel.get_turbulence_intensity_no_building(data_line)
        # color = abs(excel.get_turbulence_difference(data_line)) * 5.0

        i_building.append(TI_building)
        # i_no_building.append(TI_no_building)
        # i_difference.append(color)

    mlab.plot3d(x_array, y_array, z_array, i_building, tube_radius=10, tube_sides=30, opacity=0.50)


excel = Excel()
create_line(excel)