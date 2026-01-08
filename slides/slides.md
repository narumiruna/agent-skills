---
marp: true
theme: default
paginate: true
backgroundColor: #1e3a5f
color: #e8d7b0
---

<!-- _class: lead -->
<!-- _backgroundColor: #0a1520 -->

# 🔌 Narumi's Claude Marketplace

**Claude Code 插件市場**
開發工具 + 完整文檔範例

---

<!-- _class: lead -->

## 這個 Repository 的雙重目的

**1. Working Marketplace**
安裝即用的開發工具插件

**2. Documentation & Examples**
學習創建自己的插件市場

---

<style scoped>
table {
  background-color: #0d2438;
  color: #e8d7b0;
}
table th {
  background-color: #0a1520;
  color: #e8d7b0;
}
table td {
  background-color: #0d2438;
}
</style>

## 🎯 核心價值

| ⚡ **即時可用** | 📚 **學習範本** | 🔧 **可擴展** |
|:---:|:---:|:---:|
| 三大實用插件 | 完整實作範例 | 自訂插件市場 |
| Python + 簡報創作 | Hooks + Skills 示範 | 遵循最佳實踐 |

---

<!-- _class: lead -->
<!-- _backgroundColor: #0a1520 -->

# 三大可用插件

**Code Quality + Development Skills + Slide Creation**

---

## 🛡️ python-code-quality

**自動化程式碼品質檢查**

在 Edit/Write 操作前自動執行：
- `uv run ruff format` - 自動格式化
- `uv run ruff check --fix` - Lint 與自動修復
- `uv run ty check` - 型別檢查

**插件類型**: Hooks Plugin (PreToolUse)

**特點**: 零配置，安裝即可使用

---

## 🎓 python-skills

**綜合 Python 開發工具包**

結合專案工作流程標準與 ORM 模式

**插件類型**: Skill Plugin（提供 Claude Python 開發專業知識）

---

## 🎓 python-skills (1/2)

**Python Project Workflow** (`python-project` skill)

- 現代工具鏈: uv, ruff, pytest, ty, typer, loguru
- 專案設定與依賴管理
- 測試、型別檢查、Lint 模式
- CLI 開發最佳實踐

---

## 🎓 python-skills (2/2)

**Peewee ORM Patterns** (`python-peewee` skill)

- DatabaseProxy 設定模式
- 連線上下文與原子交易範例
- SQLite 測試模式

---

## 🎨 slide-skills (1/2)

**完整 Marp/Marpit 簡報工具包**

統一工作流程：從色彩設計到帶圖表的最終簡報

**Color Design 模組**
- 設計簡報色彩系統（背景、文字、強調色）
- 三種策略：深色技術風、淺色專業風、強調色驅動
- 10 種即用調色盤

**Marpit Authoring 模組**
- 撰寫有效的 Marpit/Marp Markdown 簡報
- 主題支援（default/gaia/uncover）
- 簡報模式（標題、內容、雙欄、程式碼）

---

## 🎨 slide-skills (2/2)

**SVG Illustration 模組**
- 創建簡報就緒的 SVG 圖表與插圖
- 智慧尺寸邏輯，針對 Marp HTML 匯出最佳化
- 模式範例（流程圖、時間軸、架構圖）

**架構特色**
- 漸進式揭露設計
- 根據任務複雜度載入所需模組
- 端到端簡報創作支援

**插件類型**: Skill Plugin

---

<!-- _class: lead -->
<!-- _backgroundColor: #0a1520 -->

# 快速安裝

**三個簡單步驟**

---

## 步驟 1: 加入市場

**從 GitHub 加入**

```bash
/plugin marketplace add narumi/claude-marketplace
```

**本地測試**

```bash
/plugin marketplace add ./path/to/claude-marketplace
```

---

## 步驟 2: 安裝插件

選擇需要的插件：

```bash
# 程式碼品質鉤子
/plugin install python-code-quality@narumi

# Python 開發技能（包含專案工作流程 + Peewee ORM）
/plugin install python-skills@narumi

# 簡報創作技能
/plugin install slide-skills@narumi
```

---

## 步驟 3: 開始使用

插件安裝後立即啟用

**Python 開發自動化**
- 編輯 Python 檔案時自動格式化
- 自動 Lint 與修復問題
- 即時型別檢查回饋

---

## 步驟 3: 開始使用（續）

**簡報創作指引**
- 色彩系統設計建議
- Marpit 語法最佳實踐
- SVG 圖表創建協助

**Claude 獲得專業知識**
- Python 專案工作流程標準
- Peewee ORM 模式與範例
- 端到端簡報創作工作流程

---

<!-- _class: lead -->
<!-- _backgroundColor: #0a1520 -->

# 學習與擴展

**這個市場展示了什麼**

---

## 📚 實作範例

這個 marketplace 展示：

**Hooks 插件**
- `python-code-quality` 展示 PreToolUse hooks
- 自動攔截檔案操作並執行工具

**Multi-skill 插件**
- `python-skills` 整合多個相關技能
- `slide-skills` 漸進式模組載入
- 使用 `strict: false` 進行內聯插件定義

**目錄組織**
- 插件在 `plugins/` 目錄
- 共享技能在 `skills/` 目錄
- 每個插件獨立配置

---

## 🧪 測試與驗證

**確保 marketplace 結構正確**

```bash
/plugin validate .
```

**發布前本地測試**

```bash
# 1. 加入本地市場
/plugin marketplace add .

# 2. 列出可用插件
/plugin list

# 3. 測試安裝
/plugin install python-skills@narumi
```

---

## 📂 Marketplace 結構

**標準目錄組織**

```
claude-marketplace/
├── plugins/
│   ├── python-code-quality/
│   ├── python-skills/
│   └── slide-skills/
└── skills/
    ├── python-project/
    ├── python-peewee/
    └── slide-creation/
```

---

## 📖 完整文檔

**學習如何建立自己的市場**

**核心文檔**
- **[GUIDE.md](GUIDE.md)** - 創建與發布 Claude Code 插件市場的完整指南
- **[CLAUDE.md](CLAUDE.md)** - 開發者指引
- **[README.md](README.md)** - 快速入門與安裝說明

**實作展示**
- Hooks 插件實作（PreToolUse）
- Multi-skill 插件組織策略
- Marketplace 驗證與測試流程
- 漸進式技能載入架構

---

<!-- _class: lead -->
<!-- _backgroundColor: #0a1520 -->

# 開始使用

**Working Marketplace + Learning Resource**

🔗 **github.com/narumiruna/claude-marketplace**

安裝實用插件 | 學習建立自己的市場
