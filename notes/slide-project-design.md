# Slide Project Design Notes

## 方案 A：建立新 skill `slide-project`

**狀態：** 未實作（筆記用途）
**日期：** 2026-01-08
**決策：** 先採用方案 B（更新現有 skills），此方案保留供未來參考

---

## 設計概念

建立一個專門的 skill 負責定義和管理簡報專案的結構規範。

### 三層架構

```
┌─────────────────────────────────────┐
│   marpit-markdown (內容層)          │
│   - 撰寫 Marpit Markdown           │
│   - 參考 assets 路徑               │
│   - 產生簡報內容                   │
└─────────────────────────────────────┘
              ↓ 使用規範
┌─────────────────────────────────────┐
│   slide-svg-illustrator (資產層)    │
│   - 產生 SVG 插圖                  │
│   - 儲存到正確位置                 │
│   - 提供 embedding 程式碼          │
└─────────────────────────────────────┘
              ↓ 使用規範
┌─────────────────────────────────────┐
│   slide-project (基礎層)            │
│   - 定義專案結構                   │
│   - 提供命名規範                   │
│   - 按需建立目錄                   │
│   - 協助路徑解析                   │
└─────────────────────────────────────┘
```

---

## 專案結構規範

### 標準目錄結構

```
my-presentation/
├── slides.md          # 主簡報檔案
└── assets/
    ├── diagrams/      # 流程圖、架構圖
    ├── icons/         # 圖標集
    ├── charts/        # 數據圖表
    ├── backgrounds/   # 背景圖
    └── images/        # 其他圖片
```

### 命名規範

- **簡報檔案**: `slides.md` 或 `{topic}-slides.md`
- **Assets**: kebab-case，描述性命名
  - ✅ `marketplace-architecture.svg`
  - ✅ `python-workflow-diagram.svg`
  - ❌ `diagram1.svg`, `img.svg`

### 分類邏輯

| 類型 | 目錄 | 說明 |
|------|------|------|
| 流程圖、架構圖 | `assets/diagrams/` | 技術圖表、系統架構 |
| 圖標、徽章 | `assets/icons/` | 小型圖示元件 |
| 數據圖表 | `assets/charts/` | 統計圖、數據視覺化 |
| 背景圖 | `assets/backgrounds/` | 全頁背景 SVG |
| 其他圖片 | `assets/images/` | 照片、截圖等 |

---

## slide-project 職責

### 1. 提供規範文件

定義清楚的目錄結構和命名規範，作為其他 skills 的參考。

### 2. 協助其他 skills 判斷

當其他 skills 需要儲存檔案時，提供：
- 檔案應該放在哪個目錄？
- 檔案該如何命名？
- 相對路徑怎麼寫？

### 3. 按需建立 (On-Demand Creation)

**不預先建立**目錄結構，而是在需要時才建立：

```
slide-svg-illustrator 產生 diagram:
  1. 根據 slide-project 規範：diagram 應放在 assets/diagrams/
  2. 檢查目錄是否存在
  3. 不存在 → 使用 Bash mkdir -p 建立 assets/diagrams/
  4. 使用 Write 工具儲存 SVG
  5. 回傳相對路徑：assets/diagrams/marketplace-architecture.svg
```

### 4. 可選功能（未來擴展）

- 掃描現有專案結構
- 列出所有 assets
- 檢查 slides.md 中的引用是否存在
- 清理未使用的檔案
- 重命名/移動檔案時更新引用
- 產生專案摘要報告

---

## 與其他 Skills 的協同

### slide-svg-illustrator 依賴 slide-project

**讀取：**
- 專案結構規範
- 命名慣例
- 分類邏輯

**執行：**
1. 根據 SVG 類型（diagram/icon/chart/background）決定目錄
2. 檢查並按需建立目錄
3. 使用 Write 工具儲存 SVG
4. 回傳正確的相對路徑給使用者

**範例：**
```
User: "建立一個市場架構圖"
→ slide-svg-illustrator:
  - 判斷類型：diagram
  - 目錄：assets/diagrams/
  - 建立：mkdir -p assets/diagrams/
  - 儲存：assets/diagrams/marketplace-architecture.svg
  - 回傳：![w:1200](assets/diagrams/marketplace-architecture.svg)
```

### marpit-markdown 依賴 slide-project

**讀取：**
- 簡報檔案命名規範
- Assets 相對路徑格式

**執行：**
1. 在正確位置建立/編輯 `slides.md`
2. 引用 assets 時使用規範的相對路徑
3. 如果簡報檔案不存在，建立新檔案並加入基本 frontmatter

**範例：**
```markdown
---
marp: true
theme: default
paginate: true
---

# Slide Title

![w:1200](assets/diagrams/marketplace-architecture.svg)
```

---

## 工作流程範例

### 完整流程

```bash
# 使用者無需初始化，直接開始工作

# 1. 產生第一個 SVG
User: "建立一個市場架構圖"
→ slide-svg-illustrator:
  - 檢查 assets/diagrams/ → 不存在
  - 建立 assets/diagrams/
  - 儲存 SVG
  - 回傳路徑

# 2. 撰寫簡報
User: "寫三張投影片介紹這個專案"
→ marpit-markdown:
  - 檢查 slides.md → 不存在
  - 建立 slides.md
  - 插入 SVG 引用
  - 產生內容

# 3. 產生更多 assets
User: "建立 6 個圖標"
→ slide-svg-illustrator:
  - 檢查 assets/icons/ → 不存在
  - 建立 assets/icons/
  - 儲存 6 個 SVG
  - 回傳路徑列表
```

---

## SKILL.md 架構草稿

### skills/slide-project/SKILL.md

```markdown
# Slide Project Structure

## Intent

Define and maintain a standardized directory structure and naming conventions
for Marp/Marpit presentation projects. Enable consistent asset organization
and cross-skill collaboration.

---

## Core Principle: On-Demand Creation

**DO NOT pre-create directories.** Create them only when needed (when saving
the first file to that location).

---

## Standard Directory Structure

[詳細結構定義]

---

## Naming Conventions

[命名規範]

---

## Asset Classification

[分類邏輯和決策樹]

---

## Path Resolution

[相對路徑計算方法]

---

## Integration with Other Skills

### For slide-svg-illustrator
[如何使用此規範]

### For marpit-markdown
[如何使用此規範]

---

## Utility Functions (Conceptual)

[提供給其他 skills 的邏輯函數描述]

---

## Examples

[實際使用範例]
```

---

## 實作考量

### 優點

- ✅ 關注點分離 - 專案結構是獨立的關注點
- ✅ 單一權威來源 - 規範定義在一個地方
- ✅ 易於維護 - 要改規範只需改一處
- ✅ 可擴展 - 未來可加入驗證、掃描、清理等功能
- ✅ 示範最佳實踐 - 展示如何組織多個協同的 skills

### 挑戰

- ❌ 多一個 skill 要維護
- ❌ 使用者需要理解三個 skills 的關係
- ❌ 可能過度設計（如果規範很簡單）

### 何時考慮實作

當出現以下情況時，應該重新考慮方案 A：

1. **規範變複雜** - 目錄結構或命名規則變得更複雜
2. **不同步問題** - 兩個 skills 的規範定義開始不一致
3. **需要新功能** - 想加入掃描、驗證、清理等專案管理功能
4. **使用者反饋** - 使用者希望有更明確的專案組織工具
5. **維護困難** - 在兩個 skills 中同步更新規範變得繁瑣

---

## 遷移路徑（從方案 B 到方案 A）

如果未來決定實作：

1. **建立 slide-project skill**
2. **從現有 skills 中提取規範章節** → 移到 slide-project
3. **更新現有 skills** → 引用 slide-project 的規範
4. **更新 marketplace.json** → 將 slide-project 加入 slides-skills plugin
5. **測試協同** → 確保三個 skills 正確協作
6. **更新文檔** → README.md, CLAUDE.md, GUIDE.md

---

## 參考資料

- [方案 B 實作]: skills/slide-svg-illustrator/SKILL.md
- [方案 B 實作]: skills/marpit-markdown/SKILL.md
- [討論記錄]: 2026-01-08 與使用者討論

---

**結論：** 方案 A 架構清晰、易於維護，適合作為長期解決方案。目前採用方案 B
是為了快速驗證可行性，待規範穩定後可考慮重構為方案 A。
