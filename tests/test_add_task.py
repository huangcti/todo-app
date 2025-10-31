from click.testing import CliRunner
from taskmaster.main import cli
import os


def test_add_task(temp_config_dir):
    runner = CliRunner()
    result = runner.invoke(cli, ["新增", "買牛奶"])
    assert result.exit_code == 0
    assert "已新增任務" in result.output
    # verify store
    p = os.path.join(os.environ["TASKMASTER_CONFIG_DIR"], "tasks.json")
    assert os.path.exists(p)
    import json
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["tasks"][0]["text"] == "買牛奶"
