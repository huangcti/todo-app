# CLI Contracts: TaskMaster

Location: `specs/001-taskmaster-cli/contracts/cli-commands.md`

## Commands

### 新增命令
- CLI: `TaskMaster 新增 "<task>"`
- Input: task (string)
- Output (stdout human): "已新增任務 <id>: <task>"
- Output (JSON mode): `{ "id": <id>, "text": "<task>", "status": "pending", "created_at": "ISO8601" }`
- Exit codes: 0 success, 2 invalid args, 3 IO error

### 清單命令
- CLI: `TaskMaster 清單 [--json]`
- Input: optional `--json`
- Output (human): table with columns [ID, Task, Status]
- Output (json): `{ "tasks": [ {id, text, status, created_at}, ... ] }`
- Exit codes: 0 success, 3 IO error

### 完成命令
- CLI: `TaskMaster 完成 <id>`
- Input: id (integer)
- Output (human): "任務 <id> 標記為已完成"
- Output (json): `{ "id": <id>, "status": "done" }`
- Error if id not found → Exit code 4, prints friendly error

### 刪除命令
- CLI: `TaskMaster 刪除 <id>`
- Input: id (integer)
- Output (human): "任務 <id> 已刪除"
- Output (json): `{ "id": <id>, "deleted": true }`
- Exit codes: 0 success, 4 not found, 3 IO error

## JSON Schemas (outputs)

- Task object schema (partial):

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "text", "status", "created_at"],
  "properties": {
    "id": { "type": "integer" },
    "text": { "type": "string" },
    "status": { "type": "string", "enum": ["pending","done"] },
    "created_at": { "type": "string", "format": "date-time" }
  }
}
```

Notes:
- CLI contract ensures machine-readable outputs are stable for consumers and tests.
