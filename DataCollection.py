import xlrd

class Excel:
    def __init__(self):
        location = (r"C:\dev\DTE3600_Fluid\data\simData.xlsx")
        wb = xlrd.open_workbook(location)
        self.sheet = wb.sheet_by_index(0)

    def get_position(self, line):
        x_data = self.sheet.cell_value(line, 0)
        y_data = self.sheet.cell_value(line, 1)
        z_data = self.sheet.cell_value(line, 2)

        return x_data, y_data, z_data

    def get_turbulence_intensity_no_building(self, line):
        return self.sheet.cell_value(line, 4)

    def get_turbulence_intensity_with_building(self, line):
        return self.sheet.cell_value(line, 16)

    def get_turbulence_difference(self, line):
        return self.get_turbulence_intensity_with_building(line) - self.get_turbulence_intensity_no_building(line)

