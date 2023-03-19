import os
import pytest


@pytest.fixture
def clear_file_before_test():
    if os.path.exists(os.path.abspath(os.path.join('resources', 'myzip.zip'))):
        os.remove(os.path.abspath(os.path.join('resources', 'myzip.zip')))
