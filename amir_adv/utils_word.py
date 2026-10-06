from pathlib import Path
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from docx import Document
from docx.oxml.ns import qn
import os
import subprocess
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL


class utilsWord():


    def __init__(self):
        pass



    def close_open_word_file(self):

        try:
            subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            print("בוצע ניסיון לסגירת תהליכי Word פתוחים לשחרור הנעילה.")
        except Exception as e:
            print(f"לא ניתן היה לסגור את Word אוטומטית: {e}")

    def find_table_by_cell_content(self, doc, cell_text_to_find):
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    clean_cell_text = " ".join(cell.text.split())
                    if cell_text_to_find in clean_cell_text:
                        return table

        return None


    def set_cell_content_centered(self, cell, text):

        for p in cell.paragraphs:
            p.text = ""

        p = cell.paragraphs[0] if cell.paragraphs else cell.add_paragraph()
        p.text = str(text)

        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

    def save_word_file(self,doc,output_filename):
        try:
            doc.save(output_filename)
            print(f"המסמך עודכן ונשמר בהצלחה בשם: {output_filename}")
        except PermissionError:
            print(f"שגיאה: הקובץ '{output_filename}' עדיין נעול ע\"י תהליך אחר.")
        except Exception as e:
            print(f"שגיאה בשמירת הקובץ: {e}")


    def set_table_data(self,table,table_data,offset = 1):
        for i, data in enumerate(table_data):
            target_row_idx = offset + i

            if target_row_idx < len(table.rows):
                row_cells = table.rows[target_row_idx].cells

                self.set_cell_content_centered(row_cells[0], data[0])
                self.set_cell_content_centered(row_cells[1], data[1])
                self.set_cell_content_centered(row_cells[2], data[2])
                # self.set_cell_content_centered(row_cells[3], data[3])


    def set_table_data_by_keyword(self,doc,keyword,table_data):
        table = self.find_table_by_cell_content(doc, keyword)
        if table:
            self.set_table_data(table, table_data)