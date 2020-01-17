import pytest

from .core import FakeProcess


from .core import FakeProcess
@pytest.fixture
def fake_process() -> FakeProcess:
    with FakeProcess() as process:
        yield process
