from click.testing import CliRunner
from taskmaster.main import cli
import os
import json


def test_delete_task(temp_config_dir):
    runner = CliRunner()
    runner.invoke(cli, ["新增", "買牛奶"])
    runner.invoke(cli, ["新增", "寄信"])
    result = runner.invoke(cli, ["刪除", "2", "--yes"])
    assert result.exit_code == 0
    data = json.loads(open(os.path.join(os.environ["TASKMASTER_CONFIG_DIR"], "tasks.json"), encoding="utf-8").read())
    assert all(t["id"] != 2 for t in data["tasks"]) 
