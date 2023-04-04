import xlsxwriter
import csv
from datetime import datetime

class ExportCar:
    """Class for exporting car details"""

    def __init__(self, output, file_type):
        from .serializers import CarSerializer
        self.fields= CarSerializer.Meta.fields
        self.formatted_fields = {
            'brand': 'Brand',
            'model_name': 'Model Name',
            'year': 'Year',
            'color' : 'Color',
            'price' : 'Price',
            'description': 'Description'
        }
        self.non_required_fields = ['image']
        self.workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        # self.bold_format = self.workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter'})
        # self.centered_format = self.workbook.add_format({'valign': 'vcenter'})

    def create_worksheet_header_for_car(self, sheet_name):
        """
        Creating Header for sheet with all fields in Car
        """
        worksheet = self.workbook.add_worksheet(sheet_name)
        bold = self.workbook.add_format({'bold': True})
        col = 0
        non_required_fields = []
        for field in self.fields:
            if field in self.non_required_fields: #Skip for non required fields
                continue
            worksheet.write(0, col, self.formatted_fields.get(field, field), bold)
            col += 1
        return self.workbook, worksheet
    

    def create_worksheet(self, car_data, worksheet_name):
        """
        Values for each fields of Car
        """
        worksheet_name = worksheet_name
        self.workbook, worksheet = self.create_worksheet_header_for_car(worksheet_name)
        row = 1
        for data in car_data:
            column = 0
            for field in self.fields:
                if field in self.non_required_fields: #Skip for non required fields
                    continue
                value = str(data.get(field)) if type(data.get(field)) in [datetime, str , list, dict] else data.get(field)
                worksheet.write(row, column, value)
                column += 1
            row += 1
        return self.workbook

    def export_sheet_car(self, car_data):
        self.workbook = self.create_worksheet(car_data, "Car")
        self.workbook.close()
        return self.workbook
