# Implementation Plan: TaskMaster CLI

**Branch**: `001-taskmaster-cli` | **Date**: 2025-10-31 | **Spec**: specs/001-taskmaster-cli/spec.md

## Summary

建立一個單檔 Python CLI 應用 `src/taskmaster/main.py`，提供新增、列出、標記完成與刪除任務功能，使用 JSON 在使用者配置目錄中持久化資料。CLI 輸出會提供美觀表格（rich）並支援 `--json` 機器解析輸出。

## Technical Context

- Language/Version: Python 3.12
- Package manager: uv（需求指定）；fallback: pip + venv
- Primary Dependencies: `rich`, `click`, `pydantic`, `pytest`
- Storage: JSON file in OS-specific user config directory
- Testing: `pytest`
- Project Type: Single-file CLI app under `src/taskmaster/main.py`
- Performance Goals: 非高負載場景；啟動延遲應盡量低於 200ms
- Constraints: 單使用者本地儲存；檔案原子寫入

## Constitution Check

- 憲法中要求：簡潔程式碼、全面測試、美觀 UI、JSON 儲存、直覺命令 —— 本計畫符合所有原則。
- GATE: 必須在 PR 前包含測試與示例；若 schema 變更要有遷移測試（已列入 data-model.md）。

## Phase 0: Research (complete)
- Outputs: `research.md`（已建立）
- Resolved: Python 3.12、核心套件、JSON 儲存位置
- Open: `uv` 可用性需在 CI 中驗證；已在 research.md 列為待辦。

## Phase 1: Design & Contracts (outputs to generate)
1. `data-model.md` — 已建立: Task schema、validation
2. `contracts/cli-commands.md` — 已建立: CLI 合約與 JSON schema
3. `quickstart.md` — 已建立：安裝與使用示例
4. Agent context update: **TODO** run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType copilot` (若系統允許指令碼執行)

## Phase 2: Implementation (high level)

Phase 2 tasks (examples):

- T001 Create project structure and entry point: `src/taskmaster/main.py` (Click-based CLI)
- T002 Implement storage module `src/taskmaster/storage.py` (atomic write/read, path resolution)
- T003 Implement Task model using Pydantic `src/taskmaster/models.py`
- T004 Implement commands: `新增`, `清單`, `完成`, `刪除` with Click and produce rich output
- T005 Add tests in `tests/` for each FR (unit + basic integration using temporary config dir)
- T006 Add CLI examples to `--help` and quickstart

## Files to generate now
- `specs/001-taskmaster-cli/research.md` (done)
- `specs/001-taskmaster-cli/data-model.md` (done)
- `specs/001-taskmaster-cli/contracts/cli-commands.md` (done)
- `specs/001-taskmaster-cli/quickstart.md` (done)
- Update agent context script: TODO (see above)

## Gate Evaluation
- No blocking constitution violations detected. All gates satisfied assuming tests will be included in PR.

## Next Steps / Owner Actions
1. Developer: Implement `src/taskmaster/main.py` and modules following Phase 2 tasks.
2. DevOps/CI: Verify `uv` available in CI or configure fallback to pip.
3. Maintainer: Run agent-context updater script if desired.


