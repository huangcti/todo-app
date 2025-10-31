# Tasks: TaskMaster CLI

> 注意：此處產出的任務項目與相關說明應以中文編寫，保持與專案憲法一致。

**Input**: specs/001-taskmaster-cli/spec.md
**Prerequisites**: plan.md (required), data-model.md, contracts/cli-commands.md, quickstart.md

## Phase 1: Setup (Shared Infrastructure)

- [x] T001 初始化專案結構，建立 `src/taskmaster/`、`tests/`、`specs/001-taskmaster-cli/`（若尚未存在）
- [ ] T002 在專案 root 建立 Python 虛擬環境與開發依賴安裝檔（`pyproject.toml` 或 `requirements.txt`）並記錄安裝步驟於 `README.md`（路徑: `pyproject.toml` 或 `requirements.txt`、`README.md`）
- [ ] T003 安裝並設定 lint 與格式化工具（例如 `ruff`、`black`），在 `pyproject.toml` 或 `tox.ini` 中加入設定（路徑: `pyproject.toml` / `tox.ini`）
- [ ] T004 初始化 CI 工作流程草案，執行測試與 lint（檔案: `.github/workflows/ci.yml`）
- [ ] T005 在 `specs/001-taskmaster-cli/` 新增 `tasks.md`（本檔）並提交到分支（路徑: `specs/001-taskmaster-cli/tasks.md`）

## Phase 2: Foundational (Blocking Prerequisites)

- [x] T006 [P] 建立資料儲存模組 `src/taskmaster/storage.py`（包含路徑解析：Windows `%APPDATA%/TaskMaster`、Unix `~/.config/taskmaster`，與原子寫入 helper）
- [x] T007 [P] 建立資料模型 `src/taskmaster/models.py`（使用 Pydantic 定義 `Task`）
- [x] T008 [P] 建立核心 CLI 入口 `src/taskmaster/main.py` 框架（使用 Click）並加入基本命令骨架（`新增`、`清單`、`完成`、`刪除`）
- [x] T009 [P] 建立測試輔助工具 `tests/conftest.py`（提供臨時配置目錄 fixture，確保測試使用隔離的 JSON 檔案）

## Phase 3: User Story 1 - 新增任務 (Priority: P1) 🎯 MVP

**Goal**: 使用者可以以 `TaskMaster 新增 "<task>"` 新增任務並取得新任務 ID

**Independent Test**: 在隔離配置目錄執行 `TaskMaster 新增 "買牛奶"` 後，讀取該 JSON 檔案確認包含新任務且狀態為 `pending`。

- [x] T010 [US1] 寫測試 `tests/test_add_task.py`：驗證 `TaskMaster 新增 "買牛奶"` 在空資料檔時能新增任務並回傳 ID（路徑: `tests/test_add_task.py`）
- [x] T011 [US1] 實作 `新增` 命令在 `src/taskmaster/main.py`（路徑: `src/taskmaster/main.py`）與儲存呼叫到 `storage.py`
- [x] T012 [US1] 在 `src/taskmaster/storage.py` 中實作 `add_task(text: str) -> Task`，確保原子寫入與 `next_id` 管理（路徑: `src/taskmaster/storage.py`）
- [x] T013 [US1] 在 CLI `--help` 中加入 `新增` 範例與示範（更新 `src/taskmaster/main.py` 的 help 節）

## Phase 4: User Story 2 - 顯示清單 (Priority: P1)

**Goal**: 顯示包含 `ID`、`Task`、`Status` 的美觀表格，並支援 `--json` 切換

**Independent Test**: 在有多筆任務的資料檔下執行 `TaskMaster 清單 --json`，輸出為有效 JSON 且包含 `tasks` 陣列

- [x] T014 [US2] 寫測試 `tests/test_list_tasks.py`：建立多筆任務後驗證 `TaskMaster 清單 --json` 輸出為有效 JSON（路徑: `tests/test_list_tasks.py`）
- [x] T015 [US2] 實作 `清單` 命令，使用 `rich` 顯示表格並在 `--json` 模式下輸出 JSON（路徑: `src/taskmaster/main.py`）
- [x] T016 [US2] 在 `src/taskmaster/storage.py` 中實作 `list_tasks() -> List[Task]`（路徑: `src/taskmaster/storage.py`）
- [ ] T017 [US2] 為長列表加入分頁或限制參數（可選，標註為 [P]）以支援大量任務情境（路徑: `src/taskmaster/main.py`）

## Phase 5: User Story 3 - 標記完成 (Priority: P2)

**Goal**: 使用者可執行 `TaskMaster 完成 <id>` 將任務標記為已完成並持久化

**Independent Test**: 已存在未完成任務時執行 `TaskMaster 完成 1`，JSON 檔案中該任務 `status` 變更為 `done`

- [x] T018 [US3] 寫測試 `tests/test_complete_task.py`：驗證 `完成` 命令可更新任務狀態（路徑: `tests/test_complete_task.py`）
- [x] T019 [US3] 在 `src/taskmaster/storage.py` 實作 `complete_task(id: int) -> Task`（路徑: `src/taskmaster/storage.py`）
- [x] T020 [US3] 在 `src/taskmaster/main.py` 中實作 `完成` 命令（路徑: `src/taskmaster/main.py`），並處理找不到 ID 的友善錯誤回報

## Phase 6: User Story 4 - 刪除任務 (Priority: P2)

**Goal**: 使用者可執行 `TaskMaster 刪除 <id>` 刪除任務並持久化

**Independent Test**: 多筆任務存在時執行 `TaskMaster 刪除 2`，確認 ID=2 的任務已移除

- [x] T021 [US4] 寫測試 `tests/test_delete_task.py`：驗證 `刪除` 命令移除指定任務（路徑: `tests/test_delete_task.py`）
- [x] T022 [US4] 在 `src/taskmaster/storage.py` 實作 `delete_task(id: int) -> bool`（路徑: `src/taskmaster/storage.py`）
- [x] T023 [US4] 在 `src/taskmaster/main.py` 中實作 `刪除` 命令並提供回收站或確認參數選項（`--yes`）以避免誤刪（路徑: `src/taskmaster/main.py`）

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: 文件、測試覆蓋、發行準備

- [ ] T024 更新 `quickstart.md` 以包含完整安裝與使用範例（路徑: `specs/001-taskmaster-cli/quickstart.md`）
- [ ] T025 新增 CLI 範例至 `README.md`（路徑: `README.md`）
- [ ] T026 實作自動完成支援（shell completion）與相關說明（路徑: `src/taskmaster/completion.py`、`README.md`）
- [ ] T027 在 CI 中加入 `pytest` 與 lint 檢查（檔案: `.github/workflows/ci.yml`）
- [ ] T028 撰寫基本整合測試（例如模擬檔案系統，路徑: `tests/test_integration_cli.py`）

## Dependencies & Execution Order

- Foundation (T006-T009) 必須先完成，否則 User Story 任務可能無法正確執行。
- MVP 建議範圍：US1 (T010-T013) 與 US2 (T014-T016) 優先完成並合併。

## Parallel Opportunities

- 可以並行執行的任務（不同檔案、無相依）：T006, T007, T009
- 測試編寫可與實作並行（例如 T010 與 T011 在不同文件可並行）

## Summary

- Total tasks: 28
- Tasks per story:
  - Setup/Foundation: 9
  - US1 (新增): 4
  - US2 (清單): 4
  - US3 (完成): 3
  - US4 (刪除): 3
  - Polish: 5
- Parallelizable tasks identified: T006, T007, T009, T011/T010 (partial), T014/T015 (partial)
- Suggested MVP: 完成 US1 + US2（T010-T016）以提供最基本的新增/查看功能

---

## Try it

To run the tests locally (PowerShell):

```powershell
# from repo root
python -m pytest -q
```

