import pytest

from asphalt.core import util


@pytest.fixture(autouse=True)
def set_global_event_loop(event_loop):
    util.event_loop = event_loop