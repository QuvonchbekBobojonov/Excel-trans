import pandas as pd
from Excel_Trans.transliterate import to_cyrillic, to_latin
from deep_translator import GoogleTranslator


def cyrillic_excel(file, save_file):
    x = pd.DataFrame()
    xlsx = pd.read_excel(file, None)
    SHEETS = list(xlsx)
    x.to_excel(save_file, sheet_name=to_cyrillic(SHEETS[0]))
    for sheet in SHEETS:
        TITLES = list(xlsx[sheet])
        TRANS_DATA = {}
        for title in TITLES:
            DATA = list(xlsx[sheet][title])
            if title[0:7] == 'Unnamed':
                TRANS_TITLE = ' '
            else:
                TRANS_TITLE = str(to_cyrillic(title))
            DataList = []
            for data in DATA:
                if str(data) == 'nan':
                    DataList.append(" ")
                else:
                    Data = str(to_cyrillic(str(data)))
                    DataList.append(Data)
            TRANS_DATA[TRANS_TITLE] = DataList
        save_xlsx = pd.DataFrame(TRANS_DATA)
        with pd.ExcelWriter(save_file, mode='a', if_sheet_exists="replace") as writer:
            save_xlsx.to_excel(writer, sheet_name=f'{to_cyrillic(sheet)}', index=False)


def latin_excel(file, save_file):
    x = pd.DataFrame()
    xlsx = pd.read_excel(file, None)
    SHEETS = list(xlsx)
    x.to_excel(save_file, sheet_name=to_latin(SHEETS[0]))
    for sheet in SHEETS:
        TITLES = list(xlsx[sheet])
        TRANS_DATA = {}
        for title in TITLES:
            DATA = list(xlsx[sheet][title])
            if title[0:7] == 'Unnamed':
                TRANS_TITLE = ' '
            else:
                TRANS_TITLE = str(to_latin(title))
            DataList = []
            for data in DATA:
                if str(data) == 'nan':
                    DataList.append(" ")
                else:
                    Data = str(to_latin(str(data)))
                    DataList.append(Data)
            TRANS_DATA[TRANS_TITLE] = DataList
        save_xlsx = pd.DataFrame(TRANS_DATA)
        with pd.ExcelWriter(save_file, mode='a', if_sheet_exists="replace") as writer:
            save_xlsx.to_excel(writer, sheet_name=f'{to_latin(sheet)}', index=False)


class Translator:



    def UzbekTranslate(self, file, to_variant, save_file):
        if to_variant == 'cyrillic':
            cyrillic_excel(file=file, save_file=save_file)
        elif to_variant == 'latin':
            latin_excel(file=file, save_file=save_file)
        else:
            err = {
                'variants': ['latin', 'cyrillic']
            }
            print(err)


    def variant(self):
         errs = {
                'variants': ['latin', 'cyrillic']
            }
         return errs


    def GlobalTranslate(self, file, target, save_file):
        x = pd.DataFrame()
        xlsx = pd.read_excel(file, None)
        SHEETS = list(xlsx)
        x.to_excel(save_file, sheet_name=GoogleTranslator(source='auto', target=target).translate(SHEETS[0]))
        for sheet in SHEETS:
            TITLES = list(xlsx[sheet])
            TRANS_DATA = {}
            for title in TITLES:
                DATA = list(xlsx[sheet][title])
                if title[0:7] == 'Unnamed':
                    TRANS_TITLE = ' '
                else:
                    TRANS_TITLE = GoogleTranslator(source='auto', target=target).translate(title)
                DataList = []
                for data in DATA:
                    if str(data) == 'nan':
                        DataList.append(" ")
                    else:
                        Data = GoogleTranslator(source='auto', target=target).translate(str(data))
                        DataList.append(Data)
                TRANS_DATA[TRANS_TITLE] = DataList
            save_xlsx = pd.DataFrame(TRANS_DATA)
            with pd.ExcelWriter(save_file, mode='a', if_sheet_exists="replace") as writer:
                save_xlsx.to_excel(writer, sheet_name=GoogleTranslator(source='auto', target=target).translate(sheet), index=False)

    def get_supported_languages(self, as_dict):
        if as_dict == True:
            langs_list = GoogleTranslator().get_supported_languages(as_dict=True)
        else:
            langs_list = GoogleTranslator().get_supported_languages()

        return langs_list
