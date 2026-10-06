import os
import subprocess
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL


def close_open_word_file():

    try:
        subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        print("בוצע ניסיון לסגירת תהליכי Word פתוחים לשחרור הנעילה.")
    except Exception as e:
        print(f"לא ניתן היה לסגור את Word אוטומטית: {e}")




def set_cell_content_centered(cell, text):
    """
    מנקה את התא לחלוטין ומגדירה טקסט ממורכז (אופקית ואנכית).
    """
    for p in cell.paragraphs:
        p.text = ""

    p = cell.paragraphs[0] if cell.paragraphs else cell.add_paragraph()
    p.text = str(text)

    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER


def find_table_by_cell_content(doc, cell_text_to_find):
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                clean_cell_text = " ".join(cell.text.split())
                if cell_text_to_find in clean_cell_text:
                    return table
    return None


def main():
    # 1. סגירת קובצי Word פתוחים ממש בתחילת ההרצה
    close_open_word_file()

    file_path = "demo_2.docx"
    output_filename = "demo_2_updated.docx"

    # 2. טעינת המסמך
    try:
        doc = Document(file_path)
    except Exception as e:
        print(f"שגיאה בטעינת הקובץ '{file_path}': {e}")
        return

    # 3. איתור הטבלה לפי "החלק בזכות"
    cell_keyword = "החלק בזכות"
    table = find_table_by_cell_content(doc, cell_keyword)

    if not table:
        print(f"שגיאה: לא נמצאה טבלה המכילה את המלל '{cell_keyword}'.")
        return

    # 4. הנתונים להזנה
    buyers_data = [
        {"name": "גכגכגכגכגבדבדסדסראלי", "id_type": "ת.ז.", "id_num": "012345678", "share": "1/2"},
        {"name": "ישראלה ישראלי", "id_type": "ת.ז.", "id_num": "987654321", "share": "1/2"}
    ]

    # 5. זיהוי שורת כותרת העמודות
    header_row_idx = None
    for idx, row in enumerate(table.rows):
        row_text = " ".join([cell.text for cell in row.cells])
        if cell_keyword in row_text:
            header_row_idx = idx
            break

    start_row_idx = (header_row_idx + 1) if header_row_idx is not None else 1

    # 6. עדכון השורות הקיימות בלבד
    for i, data in enumerate(buyers_data):
        target_row_idx = start_row_idx + i

        if target_row_idx < len(table.rows):
            row_cells = table.rows[target_row_idx].cells

            set_cell_content_centered(row_cells[0], data["name"])
            set_cell_content_centered(row_cells[1], data["id_type"])
            set_cell_content_centered(row_cells[2], data["id_num"])
            set_cell_content_centered(row_cells[3], data["share"])

    # 7. שמירת המסמך
    try:
        doc.save(output_filename)
        print(f"המסמך עודכן ונשמר בהצלחה בשם: {output_filename}")
    except PermissionError:
        print(f"שגיאה: הקובץ '{output_filename}' עדיין נעול ע\"י תהליך אחר.")
    except Exception as e:
        print(f"שגיאה בשמירת הקובץ: {e}")


if __name__ == "__main__":
    main()