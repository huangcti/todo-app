from __future__ import annotations
from pathlib import Path
import os
import json
from typing import List
from .models import Task
from datetime import datetime, UTC

ENV_VAR = "TASKMASTER_CONFIG_DIR"
DEFAULT_FILENAME = "tasks.json"


def get_config_dir() -> Path:
    env = os.getenv(ENV_VAR)
    if env:
        return Path(env)
    # platform-specific defaults
    if os.name == "nt":
        base = os.getenv("APPDATA", Path.home() / "AppData" / "Roaming")
        return Path(base) / "TaskMaster"
    else:
        return Path(os.getenv("XDG_CONFIG_HOME", Path.home() / ".config")) / "taskmaster"


def ensure_config_dir():
    d = get_config_dir()
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_tasks_file() -> Path:
    d = ensure_config_dir()
    return d / DEFAULT_FILENAME


def read_store() -> dict:
    p = get_tasks_file()
    if not p.exists():
        return {"version": 1, "next_id": 1, "tasks": []}
    try:
        with p.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        # If JSON corrupted, back up and return empty store
        bak = p.with_suffix(".bak")
        try:
            p.replace(bak)
        except Exception:
            pass
        return {"version": 1, "next_id": 1, "tasks": []}


def write_store(store: dict):
    p = get_tasks_file()
    tmp = p.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=2)
        f.flush()
        os.fsync(f.fileno())
    # atomic replace
    tmp.replace(p)


def list_tasks() -> List[Task]:
    store = read_store()
    return [Task(**t) for t in store.get("tasks", [])]


def add_task(text: str) -> Task:
    store = read_store()
    nid = store.get("next_id", 1)
    now = datetime.now(UTC).isoformat()
    task = {"id": nid, "text": text, "status": "pending", "created_at": now}
    store.setdefault("tasks", []).append(task)
    store["next_id"] = nid + 1
    write_store(store)
    return Task(**task)


def complete_task(task_id: int) -> Task | None:
    store = read_store()
    for t in store.get("tasks", []):
        if t.get("id") == task_id:
            t["status"] = "done"
            t["updated_at"] = datetime.now(UTC).isoformat()
            write_store(store)
            return Task(**t)
    return None


def delete_task(task_id: int) -> bool:
    store = read_store()
    before = len(store.get("tasks", []))
    store["tasks"] = [t for t in store.get("tasks", []) if t.get("id") != task_id]
    after = len(store.get("tasks", []))
    if after < before:
        write_store(store)
        return True
    return False
