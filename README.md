# App Store Creative（製作 App 商店圖的 AI Skill）

> 「App 開發與上架入門」課程附贈。作者：江承祐（阿班）· Threads @your.engineer.ben

讓 AI 代理（Claude Code、Codex 等）用**真實的 App 畫面**，做出一致、好讀、高轉換率的 App Store / Google Play 截圖、啟動畫面與 App Icon。

## 內容

- `SKILL.md`：完整工作流程（先拍真實畫面 → 定故事 → 先做第一張主視覺 → 鎖定風格 → 一張一張做 → 驗證輸出）
- `references/`：直式商店圖版型系統、截圖策略、生成提示詞範本、啟動畫面與 Icon 指南
- `assets/portrait-editorial-reference/`：範例商店圖（僅作版型與品質參考，請勿複製角色與文字）
- `scripts/validate_store_assets.py`：檢查輸出尺寸、張數、編號、透明度

## 安裝

- **Claude Code**：把整個資料夾放到 `~/.claude/skills/app-store-creative/`
- **Codex**：放到 `~/.codex/skills/app-store-creative/`

然後跟 AI 說：「用 app-store-creative 幫我做這個 App 的商店截圖」。

## 注意

- 生成點陣圖需要你的 AI 工具具備產圖能力（例如 Codex 內建的圖片生成）；沒有的話，仍可用這份流程與版型規則搭配其他產圖工具。
- 商店尺寸規定會變，skill 會要求 AI 先查 Apple / Google 官方最新規格。
- 截圖只能呈現 App 真的有的功能（App Review Guideline 2.3）。
