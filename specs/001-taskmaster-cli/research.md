# Research: TaskMaster CLI

**Decision Date:** 2025-10-31

## Decisions

1. 語言與執行環境
   - Decision: 使用 Python 3.12 作為開發與執行環境。
   - Rationale: Python 3.12 提供最新語法與效能改善，且開發者生態與 CLI 工具支援良好。
   - Alternatives considered: 3.11（較成熟，但已確認可向後相容）

2. 套件管理
   - Decision: 以使用者的要求採用 `uv` 作為套件管理工具（假設 `uv` 已安裝於環境）。
   - Rationale: 需求明確指定 `uv`，若目標環境沒有 `uv`，備選方案為使用 `pip` / `venv`。
   - Alternatives considered: `pip` + `venv`（最通用）、`pipx`（適合可執行工具）
   - Notes: 若 `uv` 不可用，安裝與 CI 指令將以 `python -m pip` 為替代。

3. 核心庫
   - Decision: 使用 `rich`（終端 UI/表格）、`click`（CLI 解析）、`pydantic`（資料驗證）作為核心庫。
   - Rationale: 這三個套件相互搭配可快速建立美觀且可驗證輸入的 CLI 應用。

4. 檔案儲存與原子性
   - Decision: JSON 儲存在使用者慣用配置目錄（Windows: `%APPDATA%/TaskMaster`，Unix: `~/.config/taskmaster`）。寫入採原子性流程：先寫入臨時檔，再以原子性改名（rename/replace）。
   - Rationale: 簡單跨平台且易於檢視。原子寫入減少資料損壞風險。

5. CLI 行為與輸出
   - Decision: 預設輸出為易讀表格（rich），提供 `--json` 切換到機器可解析的 JSON。`--help` 必須包含使用範例。
   - Rationale: 同時滿足人類與程式解析需要。

6. 測試策略
   - Decision: 使用 `pytest` 撰寫單元與整合測試；重點測試資料持久性、CLI 合約（輸出格式）與指令錯誤處理。
   - Rationale: 測試能在 CI 中自動執行並符合憲法「全面測試」原則。

## Open Questions / NEEDS CLARIFICATION

- Q1: `uv` 的安裝與使用細節（CI 中是否可用？）  — 假設可用；若不可用則改為 `pip`。

## Actionable Research Tasks

- Task: 驗證 CI 執行環境是否安裝 `uv`（或決定以 `pip` 為主）。
- Task: 範例 JSON schema 與小型遷移策略草案（見 data-model.md）。
