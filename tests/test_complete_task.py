from click.testing import CliRunner
from taskmaster.main import cli
import os
import json


def test_complete_task(temp_config_dir):
    runner = CliRunner()
    runner.invoke(cli, ["新增", "買牛奶"])
    result = runner.invoke(cli, ["完成", "1"])
    assert result.exit_code == 0
    data = json.loads(open(os.path.join(os.environ["TASKMASTER_CONFIG_DIR"], "tasks.json"), encoding="utf-8").read())
    assert data["tasks"][0]["status"] == "done"
