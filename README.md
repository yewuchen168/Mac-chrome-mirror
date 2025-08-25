# 🍏 Mac Chrome Mirror

[![Daily Update](https://github.com/你的用户名/Mac-chrome-mirror/actions/workflows/mac_dual_latest.yml/badge.svg)](https://github.com/你的用户名/Mac-chrome-mirror/actions/workflows/mac_dual_latest.yml)
[![GitHub release](https://img.shields.io/github/v/release/你的用户名/Mac-chrome-mirror?include_prereleases&label=Latest%20Release)](https://github.com/你的用户名/Mac-chrome-mirror/releases)
[![Releases](https://img.shields.io/github/downloads/你的用户名/Mac-chrome-mirror/total?label=Downloads)](https://github.com/你的用户名/Mac-chrome-mirror/releases)

> 自动归档 **macOS 版 Google Chrome 安装包 (.dmg)**  
> 支持区分 **Intel (x86_64)** 与 **Apple Silicon (arm64/M 系列)**

---

## ✨ 功能

- 每天自动检查最新版 Chrome（Stable 渠道）。  
- 按芯片架构区分：  
  - `v<版本号>-intel` → Intel 芯片  
  - `v<版本号>-arm64` → Apple 芯片  
- 每次运行：  
  - 下载并发布 `.dmg` 到 **GitHub Releases**  
  - 额外保存为 **Artifact**（双保险）。  
- 长期运行后，你的仓库将形成 **历史版本归档**。

---

## 📥 下载方式

1. 打开 [Releases 页面](https://github.com/你的用户名/Mac-chrome-mirror/releases)。  
2. 选择对应芯片：  
   - **Intel 芯片 Mac** → 下载 `googlechrome-intel.dmg`  
   - **Apple 芯片 Mac (M1/M2/M3…)** → 下载 `googlechrome-arm64.dmg`  
3. 双击 `.dmg` → 将 `Google Chrome.app` 拖入应用程序文件夹即可。

---

## ⚙️ 工作流说明

- Actions 定时任务：每天 **北京时间 10:00** 自动运行。  
- 版本号来源： [VersionHistory API](https://versionhistory.googleapis.com/)  
- 安装包下载源：Google 官方 CDN (`dl.google.com`)  
- 历史版本：每日自动归档，Google 官方 **不提供旧 DMG 下载**。

---

## 🙏 致谢

- [Google Chrome](https://www.google.com/chrome/)  
- [VersionHistory API](https://versionhistory.googleapis.com/)  
- [GitHub Actions](https://docs.github.com/actions) 自动化服务  

---

💡 **提示**：如果你想要 **Windows / Linux** 版本归档，可以建立独立仓库，用类似的工作流实现。
