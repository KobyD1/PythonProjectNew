from pathlib import Path

from amir_adv.utils_pdf import UtilsPdf

utils_pdf = UtilsPdf()
pdf_path = Path(__file__).parent / "adv_docs" / "2977-105.pdf"

data = utils_pdf.get_pdf_text(pdf_path)
utils_pdf.get_data_from_pdf(data)

tables = utils_pdf.get_pdf_table_data_by_page(pdf_path)
ids,names = utils_pdf.get_customers_from_pdf(tables)
area = utils_pdf.get_area_from_pdf(tables)
print ("Analyze PDF completed")





