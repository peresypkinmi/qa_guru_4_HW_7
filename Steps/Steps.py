import os
import zipfile
from zipfile import ZipFile
import hashlib
import csv
from PyPDF2 import PdfFileReader
import PyPDF2
import pandas as pd
import io
from io import BytesIO


class Steps:

    def make_zip_files(self, zip_file, *args):
        with ZipFile(zip_file, 'w') as zip_:
            [zip_.write(i) for i in args]
            pass

    def get_byte_from_zip(self, name_file, zip_file):
        with ZipFile(zip_file, 'r') as myzip:
            file = myzip.read(name_file)
        return file

    def get_byte_from_file(self, file):
        with open(file, 'rb', encoding=None) as pdf:
            byte_str_raw_pdf_file = pdf.read()
            return byte_str_raw_pdf_file

    def get_hash_sum(self, bytes):
        return hashlib.md5(bytes).hexdigest()

    def get_path(self, *args):
        return os.path.abspath(os.path.join(*args))

    def get_values_csv_from_file(self, path_csv):
        csv_data = pd.read_csv(path_csv, delimiter=';')
        return csv_data.values.tolist()

    def get_values_csv_from_zip(self, zip_file, path_csv):
        zip_ = zipfile.ZipFile(zip_file)
        txt_data = zip_.read(path_csv[1:])
        asd = pd.read_csv(io.BytesIO(txt_data), delimiter=';')
        return asd.values.tolist()

    def get_pdf_pages_from_zip(self, zip_file, path_pdf, page=0):
        with zipfile.ZipFile(zip_file, 'r') as zip_:
            pdf_file = zip_.read(path_pdf[1:])
            text = PyPDF2.PdfReader(BytesIO(pdf_file))
            return text.pages[page].extract_text()

    def get_pdf_pages_from_file(self, path_pdf, page=0):
        with open(path_pdf, 'rb') as pdf_data:
            pdf_ = PyPDF2.PdfReader(pdf_data)
            return pdf_.pages[page].extract_text()

    def get_xls_data_from_zip(self, path_zip, path_xls, row=0):
        with zipfile.ZipFile(path_zip, 'r') as zip_:
            xls_file = zip_.read(path_xls[1:])
            text = pd.read_excel(xls_file)
            return str(text.values[row])

    def get_xls_data_from_file(self, path_xls, row=0):
        text = pd.read_excel(path_xls)
        return str(text.values[row])
