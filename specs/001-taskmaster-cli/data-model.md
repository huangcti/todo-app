# Data Model: TaskMaster CLI

## Entities

### Task
- Description: 代表一則待辦事項
- Fields:
  - id: integer (唯一識別，遞增或使用簡單整數池)
  - text: string (任務內容，最大長度建議 1000 字元)
  - status: string enum { "pending", "done" }
  - created_at: string (ISO8601 timestamp)
  - updated_at: string (ISO8601 timestamp, optional)

## Validation Rules
- `text` 不得為空。
- `status` 僅可為 `pending` 或 `done`。
- `id` 為正整數且唯一。

## Storage Schema (JSON)

示例單一檔案格式 (tasks.json):

{
  "version": 1,
  "next_id": 3,
  "tasks": [
    { "id": 1, "text": "買牛奶", "status": "pending", "created_at": "2025-10-31T14:00:00Z" },
    { "id": 2, "text": "寄信", "status": "done", "created_at": "2025-10-30T09:00:00Z" }
  ]
}

Notes:
- `version` 用於未來 schema 遷移。
- `next_id` 可以簡化 id 指派，但在檔案損毀或跨進程情況下要小心；若實作需考慮檔案鎖或樂觀重試。

## State Transitions
- pending -> done : 透過 `TaskMaster 完成 <id>` 觸發。
- delete : 從 tasks 陣列中移除該物件（不可逆，建議先執行備份或將刪除設為可回復的未來版本）。

## Migration Considerations
- 若 schema 升級（例如加入 `tags`）：
  - 讀取舊 schema 時自動填補欄位預設值
  - 提供 `migrate` 測試與回退策略
