from __future__ import annotations
import click
from . import storage
from .models import Task
from rich.console import Console
from rich.table import Table
import json

console = Console()

@click.group()
def cli():
    """TaskMaster - 簡潔的命令列待辦事項應用

    範例：
      TaskMaster 新增 "買牛奶"
      TaskMaster 清單
    """
    pass


@cli.command(name="新增")
@click.argument("text", nargs=-1)
def add(text):
    """新增任務：TaskMaster 新增 "買牛奶""" 
    txt = " ".join(text).strip()
    if not txt:
        console.print("[red]錯誤：任務內容不可為空[/red]")
        raise click.Abort()
    task = storage.add_task(txt)
    console.print(f"已新增任務 {task.id}: {task.text}")


@cli.command(name="清單")
@click.option("--json", "as_json", is_flag=True, help="輸出為 JSON 格式")
def list_cmd(as_json: bool):
    tasks = storage.list_tasks()
    if as_json:
        out = {"tasks": [t.model_dump() if hasattr(t, 'model_dump') else t.dict() for t in tasks]}
        console.print(json.dumps(out, ensure_ascii=False))
        return
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Task")
    table.add_column("Status", justify="center")
    for t in tasks:
        status = "✅ 已完成" if t.status == "done" else "○ 未完成"
        table.add_row(str(t.id), t.text, status)
    console.print(table)


@cli.command(name="完成")
@click.argument("task_id", type=int)
def complete(task_id: int):
    t = storage.complete_task(task_id)
    if not t:
        console.print(f"[red]錯誤：找不到 ID={task_id} 的任務[/red]")
        raise click.Abort()
    console.print(f"任務 {t.id} 標記為已完成")


@cli.command(name="刪除")
@click.argument("task_id", type=int)
@click.option("--yes", is_flag=True, help="不詢問直接刪除")
def delete(task_id: int, yes: bool):
    if not yes:
        confirm = click.confirm(f"確認要刪除任務 {task_id} 嗎？")
        if not confirm:
            console.print("取消刪除")
            return
    ok = storage.delete_task(task_id)
    if not ok:
        console.print(f"[red]錯誤：找不到 ID={task_id} 的任務[/red]")
        raise click.Abort()
    console.print(f"任務 {task_id} 已刪除")


if __name__ == "__main__":
    cli()
