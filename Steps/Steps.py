import os
from zipfile import ZipFile
import hashlib


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
