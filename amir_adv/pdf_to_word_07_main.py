from datetime import datetime

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from amir_adv.globals import PDF_PATH, WORD_07_PATH, OUTPUT_FILE
from amir_adv.utils_pdf import UtilsPdf
from amir_adv.utils_word import utilsWord


def main():


    utils_word = utilsWord()
    utils_pdf = UtilsPdf()

    folder = PDF_PATH
    files_list = [str(file) for file in folder.iterdir() if file.is_file()]
    for file in files_list:
        data = utils_pdf.get_pdf_text(file)
        pdf_data = utils_pdf.get_data_from_pdf(data)

        plot_tables = utils_pdf.filter_tables_by_row_and_content(file,0,"תת חלקה")
        buyers_tables = utils_pdf.filter_tables_by_row_and_content(file,0,"ת.ז")
        buyers_tables_1 = utils_pdf.filter_tables_by_row_and_content(file,1,"ת.ז")

        area_tables = utils_pdf.filter_tables_by_row_and_content(file,3,"קומה",0)
        first_page_tables = utils_pdf.get_pdf_table_data_by_page(file,1)

        plots_data = utils_pdf.get_plots_from_tables(plot_tables)
        buyer_data = utils_pdf.get_buyer_from_tables(buyers_tables, buyers_tables_1)
        area_data = utils_pdf.get_area_from_tables(area_tables)

        seller_name, seller_id = utils_pdf.get_sellers_from_pdf(first_page_tables,5)
        print("Analyze PDF completed")
        output_file_prefix = OUTPUT_FILE

        time_stamp = datetime.now().strftime("%M%S")
        folder_word = f'{OUTPUT_FILE}//{pdf_data["gush"]}_{pdf_data["helka"]}'

        utils_word.recreate_folder(folder_word)


        for i in range (len(plots_data)):
            doc = Document(WORD_07_PATH)
            table_title = utils_word.find_table_by_cell_content(doc, "לשכת")
            utils_word.close_open_word_file()
            buyers_names=[]

            utils_word.set_cell_data(table_title, 0,1,  pdf_data['district'] )

            seller_data = [
                [seller_name, ".ח.פ", str(seller_id[::-1])]
            ]
            buyyer_to_analyze = buyer_data[i]
            buyers_1 = [ [buyyer_to_analyze["name_1"], ".ת.ז", buyyer_to_analyze["id_1"], f"1/{buyyer_to_analyze["amount"]}"]]
            utils_word.set_table_data_by_keyword(doc, "החלק בזכות", buyers_1)
            signature_data_1 = utils_word.get_signature_data(seller_name, buyers_1)
            utils_word.set_table_data_by_keyword(doc, "השם", signature_data_1, 2, 0)


            if buyyer_to_analyze["amount"] == "2":

                buyer_2 = [[buyyer_to_analyze["name_2"], ".ת.ז", buyyer_to_analyze["id_2"], f"1/{buyyer_to_analyze["amount"]}"]]
                utils_word.set_table_data_by_keyword(doc, "החלק בזכות", buyer_2,2)

                signature_data_2 = utils_word.get_signature_data("", buyer_2)
                utils_word.set_table_data_by_keyword(doc, "השם", signature_data_2, 3, 0)

            utils_word.set_table_data_by_keyword(doc, "סוג זיהוי*", seller_data)

            table_city = utils_word.find_table_by_cell_content(doc, "הישוב")
            utils_word.set_cell_data(table_city, 1, 1, pdf_data['city'])

            plot = f"{pdf_data.get("helka")}/{plots_data[i]}"
            estate_data = [
                ["", "", "", pdf_data['gush'],plot , "", area_data[i], "בשלמות", "בשלמות ", "אין     "]
            ]
            utils_word.set_table_data_by_keyword(doc, "החלקים", estate_data,5,WD_ALIGN_PARAGRAPH.CENTER)

            table_estate = utils_word.find_table_by_cell_content(doc, "החלקים")
            utils_word.set_cell_data(table_estate, 5, 2, pdf_data['gush'],WD_ALIGN_PARAGRAPH.CENTER)

            signature_data = utils_word.get_signature_data(seller_name,buyers_1)
            utils_word.set_table_data_by_keyword(doc, "השם",signature_data,2,0)

            today_str = datetime.today().strftime("%d/%m/%Y")
            for i in range(5):

                table_time = utils_word.find_table_by_cell_content(doc, "תאריך",i)
                utils_word.set_cell_data(table_time, 0, 0, today_str)


            utils_word.replace_text(doc, "כי בתאריך _________", f"כי בתאריך __{today_str}__")
            folder_name = f"{pdf_data['gush']}_{pdf_data['helka']}"
            utils_word.save_word_file(doc,output_file_prefix,buyers_1,folder_name,time_stamp)
            buyers_names.clear()
            estate_data.clear()


    print ("#"*56)
    print (f"#"*8,f"   Process Complted for {len(files_list)} PDF files   ","#"*8)
    print ("#"*56)



if __name__ == "__main__":
    main()