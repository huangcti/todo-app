from click.testing import CliRunner
from taskmaster.main import cli
import os
import json


def test_list_tasks(temp_config_dir):
    runner = CliRunner()
    runner.invoke(cli, ["新增", "買牛奶"])
    runner.invoke(cli, ["新增", "寄信"])
    result = runner.invoke(cli, ["清單", "--json"])
    assert result.exit_code == 0
    out = json.loads(result.output)
    assert "tasks" in out
    assert len(out["tasks"]) >= 2
