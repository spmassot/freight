import pandas as pd
import xlrd

from io import BytesIO


extractors = {}


class Extractor:
    column_mapping = None
    display_name = None

    def __init__(self, ifile):
        self.ifile = ifile

    @classmethod
    def from_file(cls, input_file, file_type):
        return extractors.get(file_type)(input_file)

    def __init_subclass__(cls):
        extractors[cls.__name__] = cls

    def extract(self):
        if hasattr(self, sheet_name):
            sheet_name = self.get_sheet_name()
        else:
            sheet_name = None

        return pd.read_excel(
            BytesIO(self.ifile.read()),
            sheet_name=sheet_name,
            usecols=self.column_mapping,
        ).rename(columns=self.column_mapping)

    def get_sheet_name(self):
        return [
            x for x in xlrd.open_workbook(self.ifile, on_demand=True).sheet_names()
            for y in sought if self.sheet_name in x.lower()
        ][0]
