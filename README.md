# Rea_Vix_Zead｜雷貝斯杰德

深紫霓虹風的直播個人網站。純 HTML、CSS、JavaScript，適用 GitHub Pages，無需安裝套件。

- `index.html`：直播首頁。
- `about.html`：個人介紹與互動小約定。
- `community.html`：主要 Discord、直播朋友共用社群、投稿入口與社群連結。
- `support.html`：第三方支持方式與合作聯絡。
- `social.html`：Facebook 公開動態與標示日期的 X、Instagram、Threads 固定貼文。
- `schedule.html`：Google 日曆；手機顯示行程列表，電腦顯示月曆。
- `watch.html`：Twitch 直播、YouTube 精華播放清單及 Shorts 入口。

公開網站：https://rea-vix-zead.github.io/ReaVixZead-Live/

## 更新內容

編輯 `templates/` 內對應的 HTML，執行 `python build.py`，將模板與產生的七個根目錄 HTML 一起提交。請勿只改根目錄的產生檔，以免下次建置覆蓋。
首頁與播放器共用 `assets/highlights.js` 的精華播放清單 ID；新片加入該 YouTube 清單後，兩頁會跟著清單更新，排序也以清單為準，不需再設定單支影片 ID。這不會自動上傳影片或把新片加入清單。觀看入口位於首頁與播放器模板。背景音樂僅由訪客點擊播放，每次換頁保持靜音。
樣式位於 `assets/site.css`，選單與複製信箱功能位於 `assets/site.js`。

預覽：`python -m http.server 8767 --bind 127.0.0.1`。
GitHub Pages 使用 `main` 分支的根目錄。`.nojekyll` 保留靜態原始檔。

## 素材與狀態

角色主視覺採用使用者確認的黑髮紅眼形象，來源為使用者的 LINKGOODS 公開頭像。
圖像權利歸原權利人所有，不授予圖像重新散布、再製或商用授權。本站未加入 Live2D、3D 模型原始檔或本機素材目錄。

網站不宣稱即時開台狀態或固定直播時段；直播安排以 Twitch 為準。
投稿目前導向 LINKGOODS 原有表單入口，本站不收集投稿資料。
主要 Discord：https://discord.gg/UBVjfp7vX5 。首頁的 Discord 入口統一指向此處。
直播朋友共用社群：https://discord.gg/FZmGSzxWY2 ，可以和其他直播朋友聊天、交流與一起玩。

## 社群預覽更新方式

Facebook 使用官方 Page Plugin timeline，內容更新、顯示順序與延遲由 Facebook 控制。X、Instagram、Threads 為固定貼文，需在 `templates/social.html` 同步修改連結與貼文日期後重新建置；不會自動換成最新貼文。Meta 預覽延後到接近可視範圍時載入。
