# Feature Specification: TaskMaster CLI

> 注意：本專案所有規格文件（spec、plan、tasks 等）必須以中文撰寫。

**Feature Branch**: `001-taskmaster-cli`
**Created**: 2025-10-31
**Status**: Draft
**Input**: 建立一個名為「TaskMaster」的命令列待辦事項應用程式。功能包括：
1. 新增「買牛奶」 - 新增任務
2. TaskMaster 清單 - 顯示包含 ID、任務和狀態的美觀表格
3. TaskMaster 完成 1 - 將任務標記為已完成
4. TaskMaster 刪除 2 - 刪除任務
5. JSON 持久性存儲
6. 帶有顏色和表格的豐富終端介面
7. 帶有範例的幫助命令

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.
  
  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - 新增任務 (Priority: P1)

使用者可以透過命令列新增一個任務，範例：

- 指令：`TaskMaster 新增 "買牛奶"`
- 獨立測試：在乾淨的資料檔案中執行指令後，讀取 JSON 檔案，確認新增的任務存在且狀態為未完成。

**Why this priority**: 新增任務是最基本且最頻繁的操作，必須先實作此功能才能繼續其他功能開發。

**Acceptance Scenarios**:

1. **Given** 空的任務清單，**When** 執行 `TaskMaster 新增 "買牛奶"`，**Then** 清單中出現一條新任務，內容為「買牛奶」，並分配一個唯一 ID，狀態為未完成。

---

### User Story 2 - 顯示清單 (Priority: P1)

使用者可以查看美觀表格格式的任務列表，包含 ID、任務與狀態；支援 `--json` 切換為機器可解析的輸出。

**Why this priority**: 查看任務列表是基礎功能，與新增任務同等重要，必須同時實作以確保使用者體驗完整。

**Independent Test**: 執行 `TaskMaster 清單`，解析輸出以確認至少包含 ID、task、status 欄位；當使用 `--json` 時，輸出為有效 JSON 並包含相同欄位。

**Acceptance Scenarios**:

1. **Given** 已有多筆任務，**When** 執行 `TaskMaster 清單`，**Then** 以表格列出每筆任務，列頭包含 `ID`、`Task`、`Status`。
2. **Given** 已有多筆任務，**When** 執行 `TaskMaster 清單 --json`，**Then** 輸出為有效 JSON 格式，包含相同資料。

---

### User Story 3 - 標記完成 (Priority: P2)

使用者可以以 ID 標記任務為完成，範例：`TaskMaster 完成 1`。

**Why this priority**: 標記完成是任務管理的核心功能，但可在基礎的新增/列表功能之後實作。

**Independent Test**: 在 JSON 檔案中設定一筆未完成任務，執行 `TaskMaster 完成 1`，確認該任務狀態變更為已完成且被持久化。

**Acceptance Scenarios**:

1. **Given** 任務 ID 1 為未完成，**When** 執行 `TaskMaster 完成 1`，**Then** 任務狀態變更為已完成，且 `TaskMaster 清單` 顯示為已完成。
2. **Given** 任務 ID 1 不存在，**When** 執行 `TaskMaster 完成 1`，**Then** 顯示友善的錯誤訊息。

### User Story 4 - 刪除任務 (Priority: P2)

使用者可以刪除指定 ID 的任務，範例：`TaskMaster 刪除 2`。

**Why this priority**: 刪除功能是基本的資料管理需求，但可在核心功能之後實作。

**Independent Test**: 在 JSON 檔案中設定至少兩筆任務，執行 `TaskMaster 刪除 2`，確認 ID=2 的任務被移除，且資料檔案已更新。

**Acceptance Scenarios**:

1. **Given** 任務 ID 2 存在，**When** 執行 `TaskMaster 刪除 2`，**Then** 該任務從資料中移除。
2. **Given** 任務 ID 2 不存在，**When** 執行 `TaskMaster 刪除 2`，**Then** 顯示友善的錯誤訊息。

### Edge Cases

- 任務內容超長（>1000字元）時的顯示處理
- JSON 檔案損壞時的錯誤處理與自動備份
- 同時執行多個指令時的檔案鎖定機制
- 非預期的指令格式（缺參數、錯誤的ID格式等）
- 中文字元與特殊符號的處理

## Requirements *(mandatory)*

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right functional requirements.
-->

### Functional Requirements

- **FR-001**: 系統 MUST 能以 `TaskMaster 新增 "<task>"` 新增任務並回傳新任務 ID。
- **FR-002**: 系統 MUST 能以 `TaskMaster 清單 [--json]` 顯示目前任務列表（預設表格、人類友好）。
- **FR-003**: 系統 MUST 能以 `TaskMaster 完成 <id>` 將指定任務標記為已完成並持久化。
- **FR-004**: 系統 MUST 能以 `TaskMaster 刪除 <id>` 刪除指定任務並持久化變更。
- **FR-005**: 系統 MUST 使用 JSON 格式於平台建議的位置儲存資料，並且寫入為原子性操作。
- **FR-006**: 系統 MUST 提供 `--help` 範例，展示常用語法與示例輸入。
- **FR-007**: 系統 MUST 支援中文輸入與顯示。
- **FR-008**: 系統 MUST 提供人性化的錯誤訊息，包含問題描述與修正建議。

### Key Entities

- **Task**: 代表一個待辦事項
  - id: 唯一識別號（整數）
  - text: 任務內容（文字）
  - status: 狀態（"pending" | "done"）
  - created_at: 建立時間（ISO8601 格式）

## Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable success criteria.
  These must be technology-agnostic and measurable.
-->

### Measurable Outcomes

- **SC-001**: 使用者能在 30 秒內由零開始完成第一個任務新增並顯示（包含安裝與首次使用說明）。
- **SC-002**: `TaskMaster 清單 --json` 輸出為有效 JSON（由標準解析器可解析），且包含所有 Task 欄位。
- **SC-003**: 所有核心功能的自動化測試覆蓋率至少達到 90%（單元 + 基本整合）。
- **SC-004**: 任何錯誤訊息都包含具體的修正建議，並有至少 80% 的使用者能依建議自行解決問題。

## Assumptions

1. 使用者環境假設：
   - 使用者在支援的作業系統上執行 CLI
   - 使用者具有寫入使用者配置目錄的權限
   - 終端機支援 UTF-8 與 ANSI 色彩

2. 功能範圍假設：
   - 初版僅支援單一使用者本地儲存（無同步或多人併發需求）
   - 不需要支援任務分類或標籤功能
   - 不需要支援任務截止日期或提醒功能

3. 使用者體驗假設：
   - 使用者偏好簡潔的命令語法
   - 使用者接受英文命令配合中文內容
   - 錯誤訊息應以中文呈現
