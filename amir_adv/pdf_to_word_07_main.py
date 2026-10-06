import subprocess
from pathlib import Path

from docx import Document

from amir_adv.utils_pdf import UtilsPdf
from amir_adv.utils_word import utilsWord



def main():


    pdf_path = Path(__file__).parent / "adv_docs" / "2977-105.pdf"
    word_path = Path(__file__).parent / "adv_docs" / "demo_2.docx"
    doc = Document(word_path)
    utils_word = utilsWord()
    utils_pdf = UtilsPdf()

    data = utils_pdf.get_pdf_text(pdf_path)
    pdf_data = utils_pdf.get_data_from_pdf(data)

    tables = utils_pdf.get_pdf_table_data_by_page(pdf_path)
    buyers_ids, buyers_names = utils_pdf.get_buyers_from_pdf(tables)
    area = utils_pdf.get_area_from_pdf(tables)
    seller_name, seller_id = utils_pdf.get_sellers_from_pdf(tables)
    print("Analyze PDF completed")
    utils_word.close_open_word_file()
    output_filename = "demo_4_updated.docx"

    seller_data = [
        [seller_name, ".ח.פ", seller_id]
    ]

    buyers_data = [
        [buyers_names[0],".ת.ז",  str(buyers_ids[0])[::-1],  f"1/{len(buyers_names)}"],
        [buyers_names[1],  ".ת.ז",  str(buyers_ids[1])[::-1],  f"1/{len(buyers_names)}"]
    ]

    utils_word.set_table_data_by_keyword(doc, "סוג זיהוי*", seller_data)
    # utils_word.set_table_data_by_keyword(doc, "החלק בזכות", buyers_data)

    utils_word.save_word_file(doc,output_filename)


if __name__ == "__main__":
    main()