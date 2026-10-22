import openpyxl
from openpyxl.styles import Alignment


class UtilsExcel:
    def __init__(self, template_path,result_temp_path):
        self.template_path = template_path
        self.result_temp_path = result_temp_path+"ecxel_1.xlsx"

    def convert_to_number(self, value):
        if value is None:
            return value

        if isinstance(value, (int, float)):
            return value

        if isinstance(value, str):
            v = value.strip().replace(",", ".")

            try:
                num = float(v)
                if num.is_integer():
                    return int(num)
                return num
            except:
                return value

        return value

    def add_gush_helka_to_excel(self, data, start_row, length):

        wb = openpyxl.load_workbook(self.template_path)
        ws = wb.active

        center_align = Alignment(horizontal="center", vertical="center")

        gush_value = data["gush"]
        helka_value = data["helka"]



        gush_value = self.convert_to_number(gush_value)
        helka_value = self.convert_to_number(helka_value)

        for i in range(length):
            row = start_row + i

            cell_gush = ws.cell(row=row, column=1, value=gush_value)
            cell_gush.alignment = center_align
            cell_gush.number_format = "0"
            ws.column_dimensions[cell_gush.column_letter].width = 8

            cell_helka = ws.cell(row=row, column=2, value=helka_value)
            cell_helka.alignment = center_align

        print("גוש וחלקה נכתבו והומרו למספרים בהצלחה לכל השורות!")
        return wb

    def add_row_to_excel(self,wb, data_list, column, start_row=1, prefix= ""):

        ws = wb.active

        center_align = Alignment(horizontal="center", vertical="center")

        for index, value in enumerate(data_list):
            current_row = start_row + index

            value = self.convert_to_number(value)

            if isinstance(column, str):
                cell = ws[f"{column}{current_row}"]
                cell.value = value
                cell.alignment = center_align
            else:
                cell = ws.cell(row=current_row, column=column, value=value)
                cell.alignment = center_align

        return wb


    def save_excel(self,wb):
        wb.save(self.result_temp_path)


