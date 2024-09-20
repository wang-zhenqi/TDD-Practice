from datetime import datetime

import pytest
from database_repository import RelationalDataBaseManager
from utils import read_yaml_file


@pytest.fixture(scope="module")
def db():
    config = read_yaml_file("../database_connection.yaml")
    return RelationalDataBaseManager(**config)


@pytest.fixture(scope="module")
def today():
    return datetime.today()
