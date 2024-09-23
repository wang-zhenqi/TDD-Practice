from datetime import datetime

import pytest
from orms.relational_database import RelationalDatabase
from utils import read_yaml_file


@pytest.fixture(scope="module")
def db():
    config = read_yaml_file("../database_connection.yaml")
    return RelationalDatabase(**config)


@pytest.fixture(scope="module")
def today():
    return datetime.today()
