from Steps.Steps import Steps


def test_pack_and_check_several_files(clear_file_before_test):
    step = Steps()
    path_zip = step.get_path('resources', 'myzip.zip')
    path_pdf_file = step.get_path('resources', 'file-sample_150kB.pdf')
    path_xls_file = step.get_path('resources', 'file_example_XLS_10.xls')
    path_csv_file = step.get_path('resources', 'username.csv')
    step.make_zip_files(path_zip, path_pdf_file, path_xls_file, path_csv_file)
    pdf_from_zip = step.get_byte_from_zip(path_pdf_file[1:], path_zip)
    pdf_from_file = step.get_byte_from_file(path_pdf_file)
    csv_from_zip = step.get_byte_from_zip(path_csv_file[1:], path_zip)
    csv_from_file = step.get_byte_from_file(path_csv_file)
    xls_from_zip = step.get_byte_from_zip(path_xls_file[1:], path_zip)
    xls_from_file = step.get_byte_from_file(path_xls_file)
    assert pdf_from_file == pdf_from_zip
    assert step.get_hash_sum(pdf_from_file) == step.get_hash_sum(pdf_from_zip)
    assert csv_from_file == csv_from_zip
    assert step.get_hash_sum(csv_from_file) == step.get_hash_sum(csv_from_zip)
    assert xls_from_file == xls_from_zip
    assert step.get_hash_sum(xls_from_file) == step.get_hash_sum(xls_from_zip)
