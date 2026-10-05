from pathlib import Path

from amir_adv.utils_pdf import UtilsPdf
from amir_adv.utils_word import UtilsWord


pdf_path = Path(__file__).parent / "adv_docs" / "2977-105.pdf"
word_path = Path(__file__).parent / "adv_docs" / "forms_tabu-009.docx"
utils_pdf = UtilsPdf()
utils_word = UtilsWord(word_path)
data = utils_pdf.get_pdf_text(pdf_path)
pdf_data = utils_pdf.get_data_from_pdf(data)

tables = utils_pdf.get_pdf_table_data_by_page(pdf_path)
buyers_ids,buyers_names = utils_pdf.get_buyers_from_pdf(tables)
area = utils_pdf.get_area_from_pdf(tables)
sellers = utils_pdf.get_sellers_from_pdf(tables)
print ("Analyze PDF completed")
text = utils_word.get_word_data()
word_tables = utils_word.get_word_tables()
utils_word.set_word_buyers_data(1, buyers_ids, buyers_names)
utils_word.set_word_real_estate_data(2,pdf_data,area)
utils_word.set_word_signature_data(3,sellers[0],buyers_names)
print ("Analyze Word completed")









