import pytest
from mock import patch

from app.solder_factory import SolderFactory


def test_create():
    sol = SolderFactory.create()
    assert sol.__class__.__name__ == 'Solder'
    assert sol._health == 100