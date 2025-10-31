import os
import tempfile
import shutil
import pytest

from pathlib import Path

@pytest.fixture()
def temp_config_dir(tmp_path):
    d = tmp_path / "config"
    d.mkdir()
    old = os.environ.get("TASKMASTER_CONFIG_DIR")
    os.environ["TASKMASTER_CONFIG_DIR"] = str(d)
    yield d
    # teardown
    if old is None:
        os.environ.pop("TASKMASTER_CONFIG_DIR", None)
    else:
        os.environ["TASKMASTER_CONFIG_DIR"] = old
