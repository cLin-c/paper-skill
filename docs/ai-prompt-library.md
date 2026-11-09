# AI 提示词网页版

入口：https://clin-c.github.io/paper-skill/ai-prompts/

采用 st-oa.cn 在 2026-10-23 发布并下载核验的本地版本，不代表该网站当前在线版本。保留全部 116 条提示词、论文八步目录、原始样式、复制按钮，以及原服务器注入的搜索栏（关键词高亮、上一处、下一处、清空）。提示词原文未改写。

页面主体来自 `workflow-live-verified.html`，原文件 SHA-256：
`d622b11c81598ef2d1681a4c4bc91d40ea218ff7cf2d4c296eb8c11df351c0e4`。
搜索代码来自当时保存的 `server-search-assets.html`，插入页面结束标签前，替代原服务器的动态注入。

`site/ai-prompts/index.html` 为无外部资源依赖的静态页面，不需要腾讯云服务器、登录信息或后端接口。README 顶部提供网页导航。推送 `site/` 的修改到 main 后，由 `.github/workflows/pages.yml` 发布 GitHub Pages。

本地预览：`python -m http.server 8765 --directory site`，然后访问 http://localhost:8765/ai-prompts/。
