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

                    all_tables.append(df_rtl)
            else:
                print(f"No tables found on page {page_number}")

            return all_tables

    def remove_table_by_content(self, tables, target_text):
        i = 0
        while i < len(tables):
            table = tables[i]
            found = False
            for index, row in table.iterrows():
                row_text = ' '.join(row.dropna().astype(str).tolist())
                if target_text in row_text:
                    print(f'נמצאה התאמה בטבלה אינדקס {i}, שורה {index}. הטבלה הוסרה.')
                    tables.pop(i)
                    found = True
                    break

            if found:
                break

            i += 1

        return tables

    def filter_tables_by_row_and_content(self, pdf_path, target_row_index, target_text, offset=0):
        print(f"analyze all tables for {target_text}")
        tables_filtered = []
        all_tables_with_metadata = []

        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                tables = page.extract_tables()
                if not tables:
                    continue

                for t_idx, table in enumerate(tables):
                    all_tables_with_metadata.append({
                        "page": page_num,
                        "table_index": t_idx + 1,
                        "table_data": table
                    })

        for entry in all_tables_with_metadata:
            page_num = entry["page"]
            t_idx = entry["table_index"]
            table = entry["table_data"]

            if len(table) > target_row_index + offset:
                row = table[target_row_index + offset]
                if row:
                    row = [item[::-1] if item is not None else "" for item in row[::-1]]

                non_empty_cells = [str(c).replace('\n', ' ') for c in row if c and c.strip()]
                if not non_empty_cells:
                    continue

                row_text = " ".join(non_empty_cells)
                reversed_row_text = row_text[::-1]

                text_matches = any(
                    (t in row_text) or (t in reversed_row_text) for t in target_text
                )
                if text_matches:
                    tables_filtered.append({
                        "page": page_num,
                        "table_index": t_idx,
                        "row_index": target_row_index + 1,
                        "row_data": row
                    })

        return tables_filtered

    def split_by_subplot(self, pdf_path):

        from bidi.algorithm import get_display
        import pdfplumber

        lines = []

        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    visual = get_display(text)
                    lines.extend(visual.splitlines())

        sections = []
        current_section = None

        for line in lines:

            if "תת חלקה" in line:

                if current_section:
                    sections.append("\n".join(current_section))

                current_section = [line]

            elif current_section:
                current_section.append(line)

        if current_section:
            sections.append("\n".join(current_section))

        return sections

    def get_buyyers_amount (self,section_text):

        count = section_text.split(" ").count("ת.ז")

        match count:
            case amount if amount > 2:
                print ("More than 2 buyers found")
                return 2
            case amount if amount > 0:
                return amount
            case 0:
                match True:
                    case _ if section_text.count("מכר") > 0:
                        return section_text.count("מכר")
                    case _ if section_text.count("רישום בית משותף") > 0:
                        return section_text.count("רישום בית משותף")
                    case _:
                        return 0

    def get_data_from_sections(self, sections):
        buyyer_data = []

        for section in sections:
            buyyer = {}
            buyyer["id_1"] = ""
            buyyer["name_1"] = ""
            amount = self.get_buyyers_amount(section)
            buyyer["amount"] = amount


            rows = section.split("\n")
            plot = rows[0].split(" ")[2]
            buyyer["plot"] = plot
            counter = 0
            next_row_empty = False

            for row in rows:

                if counter >2 :break

                if ("רישום בית משותף" in row) and( "מדינת ישראל"in row):
                    buyyer[f"name_1"] = "מדינת ישראל"
                    buyyer["id_1"] = ""
                    break


                if ("רישום בית משותף" in row) and( "ת.ז" in row):
                    counter += 1

                    index_1 = row.index("ת.ז")
                    index_2 = row.index("רישום בית משותף")
                    buyyer[f"name_{counter}"] = row[index_2 + 15:index_1].strip()
                    id_temp = row[index_1:].strip()
                    id = id_temp.split(" ")[1]
                    buyyer[f"id_{counter}"] = id

                if "צוואה" in row:
                    counter += 1

                    index_1 = row.index("ת.ז")
                    index_2 = row.index("צוואה")
                    buyyer[f"name_{counter}"] = row[index_2 + 6:index_1].strip()
                    id_temp = row[index_1:].strip()
                    id = id_temp.split(" ")[1]
                    buyyer[f"id_{counter}"] = id
                    continue



                if "מכר ללא תמורה" in row:
                    counter += 1

                    index_1 = row.index("ת.ז")
                    index_2 = row.index("תמורה")
                    buyyer[f"name_{counter}"] = row[index_2 + 6:index_1].strip()
                    id_temp = row[index_1:].strip()
                    id = id_temp.split(" ")[1]
                    buyyer[f"id_{counter}"] = id
                    continue



                elif   ("מכר" in row) and ("חברה"  not in row )  :
                    counter += 1

                    index_1 = row.index("ת.ז") if "ת.ז" in row else None
                    index_2 = row.index("מכר") if "מכר" in row else None

                    buyyer[f"name_{counter}"] = row[index_2 + 4:index_1].strip()
                    id_temp = row[index_1:].strip()
                    id = id_temp.split(" ")[1]
                    buyyer[f"id_{counter}"] = id
                    next_row_empty = True
                    continue



                if "סעיף 126" in row:
                    counter += 1

                    index_1 = row.index("ת.ז") if "ת.ז" in row else None
                    index_2 = row.index("126") if "126" in row else None

                    buyyer[f"name_{counter}"] = row[index_2 + 4:index_1].strip()
                    id_temp = row[index_1:].strip()
                    id = id_temp.split(" ")[1]
                    buyyer[f"id_{counter}"] = id
                    next_row_empty = True
                    continue


                if ( "הערת אזהרה" in row) and ( "הערת אזהרה לרישום משכנתה" not in row ) and( "סעיף 126" not in row):
                    counter += 1
                    index_1 = row.index("ת.ז")
                    index_2 = row.index("הערת אזהרה")

                    buyyer[f"name_{counter}"] = row[index_2 + len("הערת אזהרה"):index_1].strip()
                    id_temp = row[index_1:].strip()
                    id = id_temp.split(" ")[1]
                    buyyer[f"id_{counter}"] = id
                    next_row_empty = True
                    continue




                if ( "ת.ז" in row) and next_row_empty :
                    counter += 1

                    index_1 = row.index("ת.ז")


                    buyyer[f"name_{counter}"] = row[ :index_1].strip()
                    id = row[index_1+3:].strip()
                    buyyer["amount"] = 2

                    buyyer[f"id_{counter}"] = id




            buyyer_data.append(buyyer)

        return buyyer_data
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

        hebrew_text = []

        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    logical = text

                    visual = get_display(logical)

                    hebrew_text.append(visual)
        return hebrew_text

    def get_data_from_pdf(self, text, page=0):
        pdf_data = {}
        page_data = text[page]
        lines = page_data.split('\n')
        counter = 0

        for line in lines:
            if "לשכת רישום מקרקעין" in line:
                parts = line.split(":", 1)
                if len(parts) > 1:
                    pdf_data['district'] = parts[1].strip()
                    print(f"district found")

            if "גוש" in line and "חלקה" in line:
                # if "גוש" in line and "חלקות" not in line:

                print(line)
                index_1 = line.index("גוש")
                index_2 = line.index("חלקה")
                gush = line[index_1 + 4:index_2].strip()
                helka = line[index_2 + 5:].strip()
                pdf_data['gush'] = gush
                pdf_data['helka'] = helka
                print(f"gush helka found")
                counter += 1

            if "כתובת" in line:
                parts = line.split(":", 1)
                if len(parts) > 1:
                    city = line.split(";")[0].split(",")[1].strip()
                    pdf_data['city'] = city
                    print(f"city found")
            if "תת חלקה" in line:
                subplot = line.replace("תת חלקה", "").strip()
                pdf_data['subplot'] = subplot
                print(f"subplot found")
        return pdf_data

    def get_buyers_from_pdf(self, tables, table_id=9):
        ids = tables[table_id].iloc[:, 4].dropna().tolist()
        names = tables[table_id].iloc[:, 2].dropna().tolist()
        print(f"found {len(names)} buyers at page ")
        return ids, names

    def get_plots_from_tables(self, tables):
        plots = []
        for table in tables:
            data = table["row_data"]
            for text in data:
                if 'תת חלקה' in text:
                    plot = text.split(" ")[2][::-1]
                    plots.append(plot)
        return plots

    def get_area_from_tables(self, tables):
        area_data = []
        for table in tables:
            area_data.append(str(table["table_data"][3][5]))
        return area_data

    def get_areas_from_pdf(self, text):
        area_data = []
        pages = []

        for page in text:
            pages.append(page)

        for page in pages:
            rows = page.split("\n")
            for i, row in enumerate(rows):
                if "תיאור קומה" in row:
                    row_text = rows[i + 1]
                    data = row_text.split(" ")
                    area = data[0]
                    if area ==  "עמוד":area = "not found"
                    area_data.append(area)
        return area_data

    def get_first_buyers_from_pdf(self, text):
        buyer_data = []
        pages = []

        for page in text:
            pages.append(page)

        for page in pages:
            rows = page.split("\n")
            for i, row in enumerate(rows):
                if "בעלויות" in row:
                    row_text = rows[i + 1]
                    data = row_text.split(" ")
                    buyer = data[1]
                    buyer_data.append(buyer)
        return buyer_data

    def arrange_buyer_data(self, buyer_data):
        index_to_remove = []
        i = 0

        while i < len(buyer_data) - 1:
            current = buyer_data[i]
            name1_current = current.get('name_1', '').split(" ")[0]
            next = buyer_data[i + 1]
            name1_next = next.get('name_1', '').split(" ")[0]
            if name1_current == name1_next and name1_current != "מדינת":
                print(f"**** Dupliceted names found name = {name1_current} ****")
                current['amount'] = '2'
                current['id_2'] = next.get('id_1', '')
                current['name_2'] = next.get('name_1', '')
                print(f"**** Dupliceted names complited ****")
                index_to_remove.append(i + 1)
            i += 1
        for index in index_to_remove:
            del buyer_data[index]
        return buyer_data

    def get_buyer_from_tables(self, array1, array2):
        lookup_dict = {}
        for item2 in array2:
            key = (item2['page'], item2['table_index'])
            lookup_dict[key] = item2

        final_result = []
        index = 0
        last_name = ""

        for item1 in array1:
            key = (item1['page'], item1['table_index'])

            name1 = item1['row_data'][2] if len(item1['row_data']) > 2 else ''
            id1 = item1['row_data'][4] if len(item1['row_data']) > 4 else ''
            last_name = name1.split(" ")[0]

            combined_entry = {
                'page': item1['page'],
                'table_index': item1['table_index'],
                'name_1': name1,
                'id_1': id1[::-1],
                'amount': "1"
            }

            if key in lookup_dict:
                item2 = lookup_dict[key]
                name2 = item2['row_data'][2] if len(item2['row_data']) > 2 else ''
                id2 = item2['row_data'][4] if len(item2['row_data']) > 4 else ''

                combined_entry['name_2'] = name2
                combined_entry['id_2'] = id2[::-1]
                combined_entry['amount'] = "2"

            final_result.append(combined_entry)
        index += 1

        return final_result

    def get_sellers_from_pdf(self, tables, table_id=5):
        seller_name = tables[table_id].iloc[:, 2].dropna().to_list()[0]
        seller_id = tables[table_id].iloc[:, 4].dropna().to_list()[0]
        print(f"seller_name found {seller_name}")

        return seller_name, seller_id

    def get_area_from_pdf(self, tables, table_id=2):
        table = tables[table_id]
        area_as_list = table.iloc[0: 4].iloc[:, 2].dropna().tolist()
        area = area_as_list[1]
        area = area[::-1]
        return area
