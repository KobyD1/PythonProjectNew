from bidi.algorithm import get_display
import pdfplumber
import pandas as pd
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn


class UtilsWord:

    def __init__(self, path):
        self.path = Document(path)

    def get_word_data(self):



        doc = Document(self.path)

        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    print(cell.text)

    def get_word_tables(self):
        tables = []
        for child in self.doc._body._element:
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
        return tables
    def set_word_table_by_col(self, table_id, col_index, col_data, offset = 0 ):


        table = self.doc.tables[table_id]
        index = 1+offset
        for data  in col_data:

            table.cell(index, col_index).text = data
            index += 1

        self.doc.save("updated.docx")
    def set_word_table_by_row(self, table_id, row_index, row_data):

        table = self.doc.tables[table_id]
        col_index = 0
        for data  in row_data:

            table.cell(row_index, col_index).text = data
            col_index += 1

        self.doc.save("updated.docx")
    def set_word_buyers_data(self, table_id,ids,names):
        part = f"1/{len(ids)}"
        self.set_word_table_by_col(table_id, 2, ids)
        self.set_word_table_by_col(table_id, 0, names)
        self.set_word_table_by_col(table_id, 1, ["ת.ז", "ת.ז"])
        self.set_word_table_by_col(table_id, 3, [part, part])

    def set_word_real_estate_data(self, table_id,pdf_data,area):
        data = []
        plot = f"{pdf_data.get("helka")}.{pdf_data.get("subplot")}"
        data.append(pdf_data.get("gush"))
        data.append(plot)
        data.append(area)
        data.append("בשלמות")
        data.append("בשלמות")
        data.append("אין")

        self.set_word_table_by_row(table_id, 2, data)


    def set_word_signature_data(self,table_id,seller,buyer_names):


        self.set_word_table_by_row(table_id, 2, ["","","",seller])
        self.set_word_table_by_col(table_id, 0, buyer_names,1)


