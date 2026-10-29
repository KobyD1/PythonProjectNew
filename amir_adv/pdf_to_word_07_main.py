from datetime import datetime
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from amir_adv.globals import PDF_PATH, WORD_TEMPLATE_PATH_1, OUTPUT_FOLDER_1, EXCEL_TEMPLATE_PATH_1, OUTPUT_FOLDER_TEMP, \
    API_KEY, BASE_ID, TABLE_NAME, IS_EXCEL_ONLY
from amir_adv.utils_atable_api import AirTableApi
from amir_adv.utils_excel import UtilsExcel
from amir_adv.utils_pdf import UtilsPdf
from amir_adv.utils_word import utilsWord


def main():
    utils_word = utilsWord()
    utils_pdf = UtilsPdf()
    utils_excel = UtilsExcel(EXCEL_TEMPLATE_PATH_1)



    utils_atable = AirTableApi(API_KEY, BASE_ID, TABLE_NAME)

    folder = PDF_PATH
    files_list = [str(file) for file in folder.iterdir() if file.is_file()]
    if utils_atable.verify_or_register_license():
        for file in files_list:
            print(f"#" * 12, f"   Start Process for  PDF file   ", "#" * 12)

            data = utils_pdf.get_pdf_text(file)
            sections = utils_pdf.split_by_subplot(file)
            sections_data =utils_pdf.get_data_from_sections(sections)

            pdf_data = utils_pdf.get_data_from_pdf(data)


            plot_tables = utils_pdf.filter_tables_by_row_and_content(file, 0, ["תת חלקה"])
            area_data = utils_pdf.get_areas_from_pdf(data)

            first_page_tables = utils_pdf.get_pdf_table_data_by_page(file, 1)
            first_page_tables = utils_pdf.remove_table_by_content(first_page_tables, 'הגוש הגיע בתאריך')
            plots_data = utils_pdf.get_plots_from_tables(plot_tables)

            seller_name, seller_id = utils_pdf.get_sellers_from_pdf(first_page_tables, 5)
            print("Analyze PDF completed")
            wb = utils_excel.add_gush_helka_to_excel(pdf_data, 2, len(area_data))
            wb = utils_excel.add_row_to_excel(wb, plots_data, 3, 2, pdf_data["helka"] + "/")

            wb = utils_excel.add_row_to_excel(wb, area_data, 4, 2)
            wb = utils_excel.add_section_data_to_excel(wb, sections_data, 2, 10)
            excel_file = f"{pdf_data.get("gush")}_{pdf_data.get("helka")}.xlsx"

            utils_excel.save_excel(wb, OUTPUT_FOLDER_TEMP + excel_file)
            print("Analyze Excel completed")
            if not IS_EXCEL_ONLY:
                output_file_prefix = OUTPUT_FOLDER_1

                time_stamp = datetime.now().strftime("%M%S")
                folder_word = f'{OUTPUT_FOLDER_1}//{pdf_data["gush"]}_{pdf_data["helka"]}'

                utils_word.recreate_folder(folder_word)

                for i in range(len(plots_data)):
                    doc = Document(WORD_TEMPLATE_PATH_1)
                    table_title = utils_word.find_table_by_cell_content(doc, "לשכת")
                    utils_word.close_open_word_file()
                    buyers_names = []

                    utils_word.set_cell_data(table_title, 0, 1, pdf_data['district'])

                    seller_data = [
                        [seller_name, ".ח.פ", str(seller_id[::-1])]
                    ]
                    buyyer_to_analyze = sections_data[i]
                    buyers_1 = [
                        [buyyer_to_analyze["name_1"], ".ת.ז", buyyer_to_analyze["id_1"], f"1/{buyyer_to_analyze["amount"]}"]]
                    utils_word.set_table_data_by_keyword(doc, "החלק בזכות", buyers_1)
                    signature_data_1 = utils_word.get_signature_data(seller_name, buyers_1)
                    utils_word.set_table_data_by_keyword(doc, "השם", signature_data_1, 2, 0)

                    if buyyer_to_analyze["amount"] == 2:
                        buyer_2 = [[buyyer_to_analyze["name_2"], ".ת.ז", buyyer_to_analyze["id_2"],
                                    f"1/{buyyer_to_analyze["amount"]}"]]
                        utils_word.set_table_data_by_keyword(doc, "החלק בזכות", buyer_2, 2)

                        signature_data_2 = utils_word.get_signature_data("", buyer_2)
                        utils_word.set_table_data_by_keyword(doc, "השם", signature_data_2, 3, 0)

                    utils_word.set_table_data_by_keyword(doc, "סוג זיהוי*", seller_data)

                    table_city = utils_word.find_table_by_cell_content(doc, "הישוב")
                    utils_word.set_cell_data(table_city, 1, 1, pdf_data['city'])

                    plot = f"{pdf_data.get("helka")}/{plots_data[i]}"
                    estate_data = [
                        ["", "", "", pdf_data['gush'], plot, "", area_data[i], "בשלמות", "בשלמות ", "אין     "]
                    ]
                    utils_word.set_table_data_by_keyword(doc, "החלקים", estate_data, 5, WD_ALIGN_PARAGRAPH.CENTER)

                    table_estate = utils_word.find_table_by_cell_content(doc, "החלקים")
                    utils_word.set_cell_data(table_estate, 5, 2, pdf_data['gush'], WD_ALIGN_PARAGRAPH.CENTER)

                    signature_data = utils_word.get_signature_data(seller_name, buyers_1)
                    utils_word.set_table_data_by_keyword(doc, "השם", signature_data, 2, 0)

                    today_str = datetime.today().strftime("%d/%m/%Y")
                    for i in range(5):
                        table_time = utils_word.find_table_by_cell_content(doc, "תאריך", i)
                        utils_word.set_cell_data(table_time, 0, 0, today_str)

                    utils_word.replace_text(doc, "כי בתאריך _________", f"כי בתאריך __{today_str}__")
                    folder_name = f"{pdf_data['gush']}_{pdf_data['helka']}"
                    utils_word.save_word_file(doc, output_file_prefix, buyers_1, folder_name, time_stamp)
                    buyers_names.clear()
                    estate_data.clear()

                excel_file = f"{pdf_data.get("gush")}_{pdf_data.get("helka")}.xlsx"
                utils_excel.save_excel(wb, folder_word + "\\" + excel_file)

        print("#" * 56)
        print(f"#" * 8, f"   Process Complted for {len(files_list)} PDF files   ", "#" * 8)
        print("#" * 56)


if __name__ == "__main__":
    main()
