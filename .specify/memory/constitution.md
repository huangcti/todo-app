<!--
Sync Impact Report

- Version change: unknown → 0.1.0
- Modified principles:
  - 新增: 簡潔程式碼 → "簡潔程式碼"
  - 新增: 全面測試 → "全面的測試"
  - 新增: 美觀的富用戶介面 → "美觀的富用戶介面"
  - 新增: 持久化 JSON 儲存 → "持久化的 JSON 儲存"
  - 新增: 直覺的命令 → "直覺的命令"
- Added sections: 無（在既有模板中填充原則與治理條款）
- Removed sections: 無
- Templates requiring updates:
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/tasks-template.md
  - ⚠ .specify/templates/checklist-template.md (手動檢查建議)
  - ⚠ .specify/templates/agent-file-template.md (手動檢查建議)
- Follow-up TODOs:
  - TODO(RATIFICATION_DATE): 原始核准日期未知，請維護者補上。

-->

# Todo 應用程式憲法（中文）

## 核心原則

### I. 簡潔程式碼（Concise Code）
1. 原則：程式碼必須清晰、易讀且最小化複雜度。優先可讀性與明確性，避免聰明但難以維護的技巧。
2. 規則（不可協商）：
	- 函數/模組應遵循單一職責（SRP）。
	- 無用或重複代碼必須移除；不得保留未被測試的實驗性程式。
	- 命名必須描述意圖，註解僅補充為何（not how）。
	- 所有公共 API 應有簡短范例與使用說明。
3. 理由：CLI 工具應輕量且可靠；簡潔的程式碼降低錯誤率並提高演進速度。

### II. 全面測試（Comprehensive Testing）
1. 原則：所有公開行為必須被自動化測試覆蓋，包含單元、整合與 CLI 合約測試。
2. 規則（不可協商）：
	- 每一個功能需求在實作前應至少有一個失敗的測試（鼓勵 TDD）。
	- CI 必須在 PR 合併前執行測試套件並通過。任何回歸都必須由測試捕捉。
	- 對於資料持久性與升級（schema migration）需要有專門的回歸測試。
3. 理由：測試保證穩定性，使重構與新增功能可安全進行。

### III. 美觀的富用戶介面（Beautiful, Rich UI）
1. 原則：即使是 CLI，使用者介面也應美觀、可讀且有良好可用性（色彩、表格、提示）。
2. 規則：
	- CLI 必須提供清晰的 help、示例與互動式回饋（如進度、表格、分級錯誤）。
	- 提供機器可解析的輸出（JSON）與人類友好的視覺輸出（表格、色彩）；兩者應能切換。
	- 錯誤訊息應友善且具可行的修復建議。
3. 理由：良好的 UX 提升採用率並降低使用者錯誤與支援成本。

### IV. 持久化的 JSON 儲存（Persistent JSON Storage）
1. 原則：使用 JSON 格式做為預設本地持久化，儲存在 OS 推薦的用戶配置目錄中（例如 Windows 的 %APPDATA% / Unix 的 ~/.config）。
2. 規則：
	- 寫入操作必須原子性（寫入暫存檔後改名替換或相等手法）。
	- JSON schema 需版本化；任何 schema 變更必須伴隨遷移代碼與測試。
	- 敏感資料需明確標注；預設不加密，但應提供說明與選項以供使用者自行保護資料。
3. 理由：簡單、可審閱且跨平台的儲存方式最適合 CLI 與使用者資料移植性。

### V. 直覺的命令（Intuitive Commands）
1. 原則：命令與參數設計必須直觀、可記憶且一致。
2. 規則：
	- 使用一致的動詞式命令（如 add/list/remove/complete）與短別名（如 a/l/r/c）。
	- 提供 discoverability：`--help`、`man` 範例、以及自動完成補全提示檔案（可選）。
	- CLI 命令應盡量無副作用或提供 `--yes` 類參數以確認破壞性操作。
3. 理由：直覺性降低學習成本並提升日常使用效率。

## 額外約束（Additional Constraints）

- 語言：本專案所有規格、計畫與憑證文件（包括 `.specify` 產出）必須以中文撰寫。
- 技術偏好（建議）：
  - 主體為 Python CLI（建議使用 `rich`/`typer`/`pytest`），但不得將語言作為強制限制；任何選擇需遵循本憲法原則。
  - 儲存格式為 JSON，儲存路徑遵循平台慣例。

## 開發工作流程（Development Workflow）

- 代碼審查：所有變更需透過 Pull Request，至少一名審查者批准，並且必須通過 CI 測試與 lint 規則。
- 品質閘道：PR 必須包含對應的測試與文件更新；若為 schema 變更，必須包含遷移計畫與回滾步驟。
- 版本化：程式碼倉庫與公開 API 採用語義化版本；憲法本身採獨立語義版本管理（見下）。

## 治理（Governance）

1. 憲法優先：本憲法優先於非正式慣例與單一開發者決策，任何與憲法衝突的變更需通過修憲程序。
2. 修憲程序：
	- 提案：任何團隊成員可提出修正案（在議題中說明變更理由與後向相容性評估）。
	- 審議：至少兩名核心維護者審閱並在討論串中記錄反饋與影響評估。
	- 決議：若獲得 2/3 核心維護者贊成，則採納並更新憲法文件與同步影響報告。
3. 版本策略（憲法文件）：
	- MAJOR：對原則進行不相容性重定義或移除時增大 MAJOR。
	- MINOR：新增原則或重要章節時增大 MINOR。
	- PATCH：文字修正、格式或明確性改善時增大 PATCH。
4. 合規檢查：所有重要 PR 應包含「憲法合規檢查」的清單條目，審查者需確認必要原則被遵守或在 PR 中提出偏離理由與補救計畫。

**Version**: 0.1.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2025-10-31

