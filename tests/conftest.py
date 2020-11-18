import pathlib

import pytest

HERE = pathlib.Path(__file__).parent


@pytest.fixture
def fixtures_dir():
    return HERE / 'fixtures'
