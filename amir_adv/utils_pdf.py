from bidi.algorithm import get_display
import pdfplumber
import pandas as pd


class UtilsPdf:
    def get_pdf_table_data_by_page(self, path, page_number=1):

        with pdfplumber.open(path) as pdf:
            page_index = page_number - 1

            if page_index < 0 or page_index >= len(pdf.pages):
                print(f"Error: Page {page_number} not found. PDF has {len(pdf.pages)} pages")
                return []

            page = pdf.pages[page_index]
            tables = page.extract_tables()

            all_tables = []

            if tables:
                for table_num, table in enumerate(tables):
                    df = pd.DataFrame(table)
                    df_rtl = df.map(lambda x: x[::-1] if isinstance(x, str) else x)

                    df_rtl = df_rtl.iloc[:, ::-1]
                    print(f"found at PDF -Page {page_number}, Table {table_num + 1}:")

                    all_tables.append(df_rtl)
            else:
                print(f"No tables found on page {page_number}")

            return all_tables

    def get_pdf_all_table_data(self, path):

        with pdfplumber.open(path) as pdf:
            all_tables = []

            for page_num, page in enumerate(pdf.pages):
                tables = page.extract_tables()

                if tables:
                    print(f"Page {page_num + 1}: Found {len(tables)} table(s)")

                    for table_num, table in enumerate(tables):
                        df = pd.DataFrame(table)
                        df_rtl = df.map(lambda x: x[::-1] if isinstance(x, str) else x)

                        df_rtl = df_rtl.iloc[:, ::-1]
                        all_tables.append({
                            'page': page_num + 1,
                            'table_num': table_num + 1,
                            'data': df_rtl
                        })

            print(f"\nTotal tables found: {len(all_tables)}")
            return all_tables

    def get_pdf_text(self, pdf_path):

        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if text:
                    correct_text = get_display(text)
                    print(f"--- עמוד {page_num} ---")
                    return correct_text

    def get_data_from_pdf(self, text):
        pdf_data = {}
        lines = text.split('\n')

        for line in lines:
            if "לשכת רישום מקרקעין" in line:
                parts = line.split(":", 1)
                if len(parts) > 1:
                    pdf_data['district'] = parts[1].strip()
                    print(f"district: {pdf_data['district']}")

            if "גוש:" in line:
                index_1 = line.index("גוש:")
                index_2 = line.index("חלקה")
                gush = line[index_1 + 4:index_2].strip()
                helka = line[index_2 + 5:].strip()
                pdf_data['gush'] = gush
                pdf_data['helka'] = helka
                print(f"gush: {gush}, helka: {helka}")

            if "כתובת" in line:
                parts = line.split(":", 1)
                if len(parts) > 1:
                    city = line.split(";")[0].split(",")[1].strip()
                    pdf_data['city'] = city
                    print(f"city: {city}")
            if "תת חלקה" in line:

                    subplot = line.replace("תת חלקה", "").strip()
                    pdf_data['subplot'] = subplot
                    print(f"subplot: {subplot}")
        return pdf_data


    def get_buyers_from_pdf(self, tables, table_id =9):
        ids= tables[table_id].iloc[:, 4].dropna().tolist()
        names = tables[table_id].iloc[:, 2].dropna().tolist()
        print (f"found {len(names)} buyers at page ")
        return ids, names


    def get_sellers_from_pdf(self, tables, table_id =5):
        seller_name = tables[table_id].iloc[:, 2].dropna().to_list()[0]
        seller_id = tables[table_id].iloc[:, 4].dropna().to_list()[0]

        return seller_name, seller_id

    def get_area_from_pdf(self,tables,table_id =2 ):
        table = tables[table_id]
        area_as_list= table.iloc[0: 4].iloc[:, 2].dropna().tolist()
        area=area_as_list[1]
        area = area[::-1]
        return area


