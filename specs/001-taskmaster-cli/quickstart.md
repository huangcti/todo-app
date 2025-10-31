# Quickstart: TaskMaster CLI (Draft)

## 前置條件
- Python 3.12 已安裝
- 建議已安裝 `uv` 套件管理（若未安裝，使用 `pip` 作為替代）

## 安裝

Windows PowerShell 範例：

```powershell
# 建議在虛擬環境中執行
python -m venv .venv; .\.venv\Scripts\Activate.ps1
# 使用 uv 安裝依賴（若 uv 可用）
uv install
# 或使用 pip
python -m pip install -r requirements.txt
```

## 使用範例

1. 新增任務：

```powershell
TaskMaster 新增 "買牛奶"
# -> 已新增任務 1: 買牛奶
```

2. 顯示清單：

```powershell
TaskMaster 清單
# -> 顯示表格：ID | Task | Status
```

3. 標記完成：

```powershell
TaskMaster 完成 1
# -> 任務 1 標記為已完成
```

4. 刪除任務：

```powershell
TaskMaster 刪除 2
# -> 任務 2 已刪除
```

## 資料檔案位置
- Windows: `%APPDATA%\TaskMaster\tasks.json`
- Unix: `~/.config/taskmaster/tasks.json`

## 測試

```powershell
# 在專案 root
python -m pytest -q
```

