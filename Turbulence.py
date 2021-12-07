from mayavi import mlab
from DataCollection import Excel

def getTubulenceArray(excel):
    i_building = []

    for data_line in range(26, 1025):
        TI_building = excel.get_turbulence_intensity_with_building(data_line)

        i_building.append(TI_building)

    return i_building

