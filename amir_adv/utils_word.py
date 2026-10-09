from datetime import datetime

from docx.oxml.ns import qn
import subprocess
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL


class utilsWord():


    def __init__(self):
        pass

    def get_word_tables(self,doc):
        tables = []
        for child in doc._body._element:
            if child.tag == qn('w:tbl'):
                table = child
                table_data = []
                for row in table.iter(qn('w:tr')):
                    row_data = []
                    for cell in row.iter(qn('w:tc')):
                        texts = [t.text for t in cell.iter(qn('w:t'))]
                        row_data.append(" ".join(texts))
                    table_data.append(row_data)
                tables.append(table_data)
        print (f"found {len(tables)} tables")
        return tables

    def close_open_word_file(self):

        try:
            subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            print("Trying to close Word automatically...")
        except Exception as e:
            print(f"Can not closed Word automatic {e}")

    def find_table_by_cell_content(self, doc, cell_text_to_find, ignore_offset = 0 ):
        counter = 0
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    clean_cell_text = " ".join(cell.text.split())
                    if cell_text_to_find in clean_cell_text:
                        counter+=1
                        if counter > ignore_offset:
                            return table
        if table:
            print ("Table  found for keyword:", cell_text_to_find)
        else:
            print ("Table not found for keyword:", cell_text_to_find)

        return None


    def set_cell_content_centered(self, cell, text ,align = WD_ALIGN_PARAGRAPH.LEFT):

        for p in cell.paragraphs:
            p.text = ""

        p = cell.paragraphs[0] if cell.paragraphs else cell.add_paragraph()
        p.text = str(text)

        p.alignment = align
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

    def save_word_file(self,doc,prefix,suffix=""):
        time_stamp = datetime.now().strftime("%M%S")
        file_name=f"{prefix}_{suffix}_{time_stamp}.docx"
        if " " in file_name:
            file_name=file_name.replace(" ","_")
        try:
            doc.save(file_name)
            print(f"The document has been updated and saved successfully")
        except PermissionError:
            print(f"Error: The file is  locked by another process.")
        except Exception as e:
            print(f"Error saving the file: {e}")
    def set_cell_data(self,table,target_row_idx,col_idx,value ,align = WD_ALIGN_PARAGRAPH.LEFT):
        row_cells = table.rows[target_row_idx].cells
        self.set_cell_content_centered(row_cells[col_idx], value,align)


    def set_table_data(self,table,table_data,offset = 1,align=WD_ALIGN_PARAGRAPH.LEFT):
        for i, data in enumerate(table_data):
            target_row_idx = offset + i

            if target_row_idx < len(table.rows):
                row_cells = table.rows[target_row_idx].cells

                for col_idx, value in enumerate(data[:len(row_cells)]):
                    self.set_cell_content_centered(row_cells[col_idx], value , align)



    def set_table_data_by_keyword(self,doc,keyword,table_data,row_offset = 1, table_offset = 0 ,align = WD_ALIGN_PARAGRAPH.LEFT):
        table = self.find_table_by_cell_content(doc, keyword,table_offset)
        if table:
            print ("Table found for keyword ")
            self.set_table_data(table, table_data,row_offset)

    def get_signature_data(self,seller,names):
        if len(names) == 1:

            signature_data = [[seller, "", "", names[0]]]

        else:
            names_new =names[1:]
            signature_data = [["", "", "", name] for name in names_new]
            signature_data.insert(0, [seller, "", "", names[0]])

        return signature_data

    def get_full_name_data(self, names):
        if len(names) == 1:
            return names[0]
        else:
            first_name= names[1].split(" ")[1]
            buyer = names[0] + " ו" + first_name
            return buyer

    def replace_text(self, doc, old_text, new_text):
        for paragraph in doc.paragraphs:
            if old_text in paragraph.text:
                for run in paragraph.runs:
                    if old_text in run.text:
                        run.text = run.text.replace(old_text, new_text)
