from datetime import datetime

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from amir_adv.globals import PDF_PATH, WORD_07_PATH, OUTPUT_FILE
from amir_adv.utils_pdf import UtilsPdf
from amir_adv.utils_word import utilsWord


def main():


    doc = Document(WORD_07_PATH)
    utils_word = utilsWord()
    utils_pdf = UtilsPdf()

    folder = PDF_PATH
    files_list = [str(file) for file in folder.iterdir() if file.is_file()]
    for file in files_list:
        data = utils_pdf.get_pdf_text(file)
        pdf_data = utils_pdf.get_data_from_pdf(data)

        tables = utils_pdf.get_pdf_table_data_by_page(file)
        buyers_ids, buyers_names = utils_pdf.get_buyers_from_pdf(tables)
        area = utils_pdf.get_area_from_pdf(tables)
        seller_name, seller_id = utils_pdf.get_sellers_from_pdf(tables)
        print("Analyze PDF completed")
        utils_word.close_open_word_file()

        output_file_prefix = OUTPUT_FILE

        table_title = utils_word.find_table_by_cell_content(doc, "לשכת")
        utils_word.set_cell_data(table_title, 0,1,  pdf_data['district'] )


        seller_data = [
            [seller_name, ".ח.פ", str(seller_id[::-1])]
        ]
        buyers_data = [
            [buyers_names[0], ".ת.ז", str(buyers_ids[0])[::-1], f"1/{len(buyers_names)}"],
            [buyers_names[1], ".ת.ז", str(buyers_ids[1])[::-1], f"1/{len(buyers_names)}"]
        ]
        utils_word.set_table_data_by_keyword(doc, "סוג זיהוי*", seller_data)
        utils_word.set_table_data_by_keyword(doc, "החלק בזכות", buyers_data)


        table_city = utils_word.find_table_by_cell_content(doc, "הישוב")
        utils_word.set_cell_data(table_city, 1, 1, pdf_data['city'])

        plot = f"{pdf_data.get("helka")}/{pdf_data.get("subplot")}"
        estate_data = [
            ["", "", "", pdf_data['gush'], plot, "", area, "בשלמות", "בשלמות ", "אין     "]
        ]
        utils_word.set_table_data_by_keyword(doc, "החלקים", estate_data,5,WD_ALIGN_PARAGRAPH.CENTER)

        table_estate = utils_word.find_table_by_cell_content(doc, "החלקים")
        utils_word.set_cell_data(table_estate, 5, 2, pdf_data['gush'],WD_ALIGN_PARAGRAPH.CENTER)

        signature_data = utils_word.get_signature_data(seller_name,buyers_names)
        utils_word.set_table_data_by_keyword(doc, "השם",signature_data,2,0)

        today_str = datetime.today().strftime("%d/%m/%Y")
        for i in range(5):

            table_time = utils_word.find_table_by_cell_content(doc, "תאריך",i)
            utils_word.set_cell_data(table_time, 0, 0, today_str)


        utils_word.replace_text(doc, "כי בתאריך _________", f"כי בתאריך __{today_str}__")

        utils_word.save_word_file(doc,output_file_prefix,utils_word.get_full_name_data(buyers_names))
    l= len(files_list)
    print ("#"*52)
    print (f"#"*8,f"   Process Complted for {l} files   ","#"*8)
    print ("#"*52)



if __name__ == "__main__":
    main()